#!/usr/bin/env python3
import os
import re
import html
import glob
from pathlib import Path

def convert_html_to_markdown(text):
    """更強力的HTML到Markdown轉換"""
    original_text = text
    
    # 移除所有style屬性（包括多行的）
    text = re.sub(r'\s*style\s*=\s*["\'][^"\']*["\']', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\s*style\s*=\s*[^>\s]*', '', text, flags=re.IGNORECASE)
    
    # 移除各種屬性
    attributes_to_remove = [
        'class', 'id', 'width', 'height', 'border', 'cellspacing', 'cellpadding',
        'align', 'valign', 'bgcolor', 'color', 'face', 'size', 'target', 'rel',
        'title', 'alt', 'name', 'onclick', 'onload', 'xmlns'
    ]
    for attr in attributes_to_remove:
        text = re.sub(rf'\s*{attr}\s*=\s*["\'][^"\']*["\']', '', text, flags=re.IGNORECASE)
        text = re.sub(rf'\s*{attr}\s*=\s*[^>\s]*', '', text, flags=re.IGNORECASE)
    
    # 移除註釋
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    
    # 處理代碼塊（更嚴格）
    text = re.sub(r'<pre\s*[^>]*>\s*<code\s*[^>]*>(.*?)</code>\s*</pre>', r'```\n\1\n```', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<pre\s*[^>]*>(.*?)</pre>', r'```\n\1\n```', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<code\s*[^>]*>(.*?)</code>', r'`\1`', text, flags=re.DOTALL | re.IGNORECASE)
    
    # 處理標題
    for i in range(6, 0, -1):
        text = re.sub(rf'<h{i}\s*[^>]*>(.*?)</h{i}>', rf'{"#" * i} \1', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理段落
    text = re.sub(r'<p\s*[^>]*>(.*?)</p>', r'\1\n', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理換行
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    
    # 處理強調
    text = re.sub(r'<(strong|b)\s*[^>]*>(.*?)</\1>', r'**\2**', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<(em|i)\s*[^>]*>(.*?)</\1>', r'*\2*', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理連結
    text = re.sub(r'<a\s+[^>]*href\s*=\s*["\']([^"\']+)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<a\s*[^>]*>(.*?)</a>', r'\1', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理圖片
    text = re.sub(r'<img\s+[^>]*src\s*=\s*["\']([^"\']+)["\'][^>]*/?>', r'![](\1)', text, flags=re.IGNORECASE)
    text = re.sub(r'<img\s*[^>]*/?>', '', text, flags=re.IGNORECASE)
    
    # 處理列表
    text = re.sub(r'<ul\s*[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</ul>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<ol\s*[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</ol>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<li\s*[^>]*>(.*?)</li>', r'- \1', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理表格
    text = re.sub(r'<table\s*[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</table>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<tr\s*[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</tr>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<td\s*[^>]*>(.*?)</td>', r'\1 | ', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<th\s*[^>]*>(.*?)</th>', r'**\1** | ', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<thead\s*[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</thead>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<tbody\s*[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</tbody>', '', text, flags=re.IGNORECASE)
    
    # 處理通用容器標籤（移除但保留內容）
    container_tags = ['div', 'span', 'section', 'article', 'header', 'footer', 'main', 'aside', 'nav', 
                     'blockquote', 'center', 'font', 'small', 'big', 'sup', 'sub', 'mark', 'del', 'ins']
    for tag in container_tags:
        text = re.sub(rf'<{tag}\s*[^>]*>', '', text, flags=re.IGNORECASE)
        text = re.sub(rf'</{tag}>', '', text, flags=re.IGNORECASE)
    
    # 處理其他常見標籤
    text = re.sub(r'<hr\s*/?>', '---', text, flags=re.IGNORECASE)
    text = re.sub(r'<wbr\s*/?>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<nobr\s*[^>]*>(.*?)</nobr>', r'\1', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 移除任何剩餘的HTML標籤
    text = re.sub(r'<[^>]+>', '', text, flags=re.DOTALL)
    
    # 解碼HTML實體
    text = html.unescape(text)
    
    # 清理多餘的空行和空白
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)  # 最多保留兩個連續換行
    text = re.sub(r'[ \t]+', ' ', text)  # 將多個空格或tab替換為單個空格
    text = re.sub(r' *\n', '\n', text)  # 移除行尾空格
    text = re.sub(r'\n +', '\n', text)  # 移除行首空格
    
    return text.strip()

def convert_files_with_html():
    """轉換包含HTML標籤的文件"""
    posts_dir = Path('/Users/larrynung/Documents/github/larrynung.github.io/content/posts')
    
    # 找到所有包含HTML標籤的非備份markdown文件
    files_to_convert = []
    
    for md_file in posts_dir.glob('**/index.md'):
        if md_file.name.endswith('.backup'):
            continue
            
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 檢查是否包含HTML標籤
            if re.search(r'<[^>]+>', content):
                html_count = len(re.findall(r'<[^>]+>', content))
                files_to_convert.append((md_file, html_count))
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
    
    if not files_to_convert:
        print("沒有找到包含HTML標籤的文件。")
        return
    
    # 按HTML標籤數量排序
    files_to_convert.sort(key=lambda x: x[1], reverse=True)
    
    print(f"找到 {len(files_to_convert)} 個包含HTML標籤的文件")
    print("前10個文件的HTML標籤數量：")
    for file_path, count in files_to_convert[:10]:
        print(f"  {file_path.name}: {count} 個標籤")
    
    converted_count = 0
    skipped_count = 0
    
    for file_path, html_count in files_to_convert:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 分離front matter和內容
            parts = content.split('---', 2) if content.startswith('---') else content.split('+++', 2) if content.startswith('+++') else [None, None, content]
            
            if len(parts) == 3:
                front_matter = f"{parts[0]}---{parts[1]}---"
                body = parts[2]
            else:
                front_matter = ""
                body = content
            
            # 轉換HTML到Markdown
            converted_body = convert_html_to_markdown(body)
            
            # 檢查是否有實際改變
            if converted_body != body:
                # 創建備份
                backup_path = file_path.with_suffix('.md.backup')
                if not backup_path.exists():
                    with open(backup_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                
                # 寫入轉換後的內容
                new_content = front_matter + converted_body if front_matter else converted_body
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                # 檢查剩餘HTML標籤
                remaining_html = len(re.findall(r'<[^>]+>', converted_body))
                print(f"✓ 轉換 {file_path.name}: {html_count} → {remaining_html} HTML標籤")
                converted_count += 1
            else:
                print(f"⚠ 跳過 {file_path.name}: 無法轉換")
                skipped_count += 1
                
        except Exception as e:
            print(f"✗ 錯誤處理 {file_path}: {e}")
            skipped_count += 1
    
    print(f"\n轉換完成:")
    print(f"  轉換成功: {converted_count} 個文件")
    print(f"  跳過: {skipped_count} 個文件")

if __name__ == "__main__":
    convert_files_with_html()
