#!/usr/bin/env python3
import os
import re
import html
from pathlib import Path

def protect_code_blocks(text):
    """保護代碼塊，避免轉換其中的內容"""
    protected_blocks = []
    placeholder_template = "PROTECTED_BLOCK_{}"
    
    # 保護三個反引號的代碼塊
    def replace_code_block(match):
        block_id = len(protected_blocks)
        protected_blocks.append(match.group(0))
        return placeholder_template.format(block_id)
    
    # 保護```代碼塊
    text = re.sub(r'```[\s\S]*?```', replace_code_block, text)
    
    # 保護單個反引號的行內代碼
    text = re.sub(r'`[^`\n]*`', replace_code_block, text)
    
    return text, protected_blocks, placeholder_template

def restore_code_blocks(text, protected_blocks, placeholder_template):
    """恢復被保護的代碼塊"""
    for i, block in enumerate(protected_blocks):
        placeholder = placeholder_template.format(i)
        text = text.replace(placeholder, block)
    return text

def convert_html_to_markdown(text):
    """只轉換非代碼區域的HTML到Markdown"""
    # 保護代碼塊
    protected_text, protected_blocks, placeholder_template = protect_code_blocks(text)
    
    # 移除所有style屬性
    protected_text = re.sub(r'\s*style\s*=\s*["\'][^"\']*["\']', '', protected_text, flags=re.IGNORECASE | re.DOTALL)
    protected_text = re.sub(r'\s*style\s*=\s*[^>\s]*', '', protected_text, flags=re.IGNORECASE)
    
    # 處理標題
    for i in range(6, 0, -1):
        protected_text = re.sub(rf'<h{i}\s*[^>]*>(.*?)</h{i}>', rf'{"#" * i} \1', protected_text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理段落（但要小心不要破壞XML文檔註釋）
    # 只轉換明顯的HTML段落標籤
    protected_text = re.sub(r'<p\s*[^>]*>\s*(.*?)\s*</p>', r'\1\n', protected_text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理換行
    protected_text = re.sub(r'<br\s*/?>', '\n', protected_text, flags=re.IGNORECASE)
    
    # 處理強調（小心XML註釋）
    protected_text = re.sub(r'<(strong|b)\s*[^>]*>(.*?)</\1>', r'**\2**', protected_text, flags=re.IGNORECASE | re.DOTALL)
    protected_text = re.sub(r'<(em|i)\s*[^>]*>(.*?)</\1>', r'*\2*', protected_text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理連結
    protected_text = re.sub(r'<a\s+[^>]*href\s*=\s*["\']([^"\']+)["\'][^>]*>(.*?)</a>', r'[\2](\1)', protected_text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理圖片
    protected_text = re.sub(r'<img\s+[^>]*src\s*=\s*["\']([^"\']+)["\'][^>]*/?>', r'![](\1)', protected_text, flags=re.IGNORECASE)
    
    # 處理列表
    protected_text = re.sub(r'<ul\s*[^>]*>\s*', '', protected_text, flags=re.IGNORECASE)
    protected_text = re.sub(r'\s*</ul>', '', protected_text, flags=re.IGNORECASE)
    protected_text = re.sub(r'<ol\s*[^>]*>\s*', '', protected_text, flags=re.IGNORECASE)
    protected_text = re.sub(r'\s*</ol>', '', protected_text, flags=re.IGNORECASE)
    protected_text = re.sub(r'<li\s*[^>]*>(.*?)</li>', r'- \1', protected_text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理明確的div標籤（但保留可能是XML文檔註釋的內容）
    protected_text = re.sub(r'<div\s*[^>]*>\s*', '', protected_text, flags=re.IGNORECASE)
    protected_text = re.sub(r'\s*</div>', '', protected_text, flags=re.IGNORECASE)
    
    # 處理span標籤
    protected_text = re.sub(r'<span\s*[^>]*>(.*?)</span>', r'\1', protected_text, flags=re.IGNORECASE | re.DOTALL)
    
    # 處理其他常見標籤
    protected_text = re.sub(r'<hr\s*/?>', '---', protected_text, flags=re.IGNORECASE)
    protected_text = re.sub(r'<center\s*[^>]*>(.*?)</center>', r'\1', protected_text, flags=re.IGNORECASE | re.DOTALL)
    
    # 解碼HTML實體
    protected_text = html.unescape(protected_text)
    
    # 恢復代碼塊
    result = restore_code_blocks(protected_text, protected_blocks, placeholder_template)
    
    # 清理多餘的空行
    result = re.sub(r'\n\s*\n\s*\n', '\n\n', result)
    result = re.sub(r' +\n', '\n', result)  # 移除行尾空格
    
    return result.strip()

def should_convert_file(file_path):
    """判斷文件是否應該被轉換"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # 跳過有編碼問題的文件
        return False, 0
    
    # 統計HTML標籤
    html_tags = re.findall(r'<[^>]+>', content)
    
    if not html_tags:
        return False, 0
    
    # 保護代碼塊後再統計
    protected_text, protected_blocks, _ = protect_code_blocks(content)
    protected_html_tags = re.findall(r'<[^>]+>', protected_text)
    
    # 過濾掉XML文檔註釋標籤
    xml_doc_tags = ['summary', 'param', 'returns', 'value', 'see', 'exception', 'c', 'example', 'remarks']
    non_xml_tags = []
    
    for tag in protected_html_tags:
        is_xml_doc = False
        for xml_tag in xml_doc_tags:
            if f'<{xml_tag}' in tag.lower() or f'</{xml_tag}>' in tag.lower():
                is_xml_doc = True
                break
        if not is_xml_doc:
            non_xml_tags.append(tag)
    
    return len(non_xml_tags) > 0, len(non_xml_tags)

def convert_remaining_files():
    """轉換剩餘包含HTML標籤的文件"""
    posts_dir = Path('/Users/larrynung/Documents/github/larrynung.github.io/content/posts')
    
    # 找到所有包含HTML標籤的非備份markdown文件
    files_to_convert = []
    
    for md_file in posts_dir.glob('**/index.md'):
        if md_file.name.endswith('.backup'):
            continue
            
        should_convert, tag_count = should_convert_file(md_file)
        if should_convert:
            files_to_convert.append((md_file, tag_count))
    
    if not files_to_convert:
        print("沒有找到需要轉換的文件。")
        return
    
    # 按HTML標籤數量排序
    files_to_convert.sort(key=lambda x: x[1], reverse=True)
    
    print(f"找到 {len(files_to_convert)} 個需要轉換的文件")
    print("前10個文件的非XML HTML標籤數量：")
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
                
                # 檢查剩餘的非XML HTML標籤
                _, remaining_count = should_convert_file(file_path)
                print(f"✓ 轉換 {file_path.name}: {html_count} → {remaining_count} 個非XML HTML標籤")
                converted_count += 1
            else:
                print(f"⚠ 跳過 {file_path.name}: 無需轉換")
                skipped_count += 1
                
        except Exception as e:
            print(f"✗ 錯誤處理 {file_path}: {e}")
            skipped_count += 1
    
    print(f"\n轉換完成:")
    print(f"  轉換成功: {converted_count} 個文件")
    print(f"  跳過: {skipped_count} 個文件")

if __name__ == "__main__":
    convert_remaining_files()
