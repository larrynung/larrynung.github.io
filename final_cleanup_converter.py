#!/usr/bin/env python3
import re
import os
import sys
from pathlib import Path

def ultra_aggressive_html_to_markdown(content):
    """超激進的 HTML 轉換為 Markdown - 幾乎移除所有 HTML"""
    
    # 移除所有屬性的 HTML 標籤，只保留內容
    # 處理自閉合標籤
    content = re.sub(r'<(br|hr|img)[^>]*/?>', '', content, flags=re.IGNORECASE)
    
    # 移除所有 CSS 和 JavaScript
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'style="[^"]*"', '', content, flags=re.IGNORECASE)
    content = re.sub(r'class="[^"]*"', '', content, flags=re.IGNORECASE)
    content = re.sub(r'id="[^"]*"', '', content, flags=re.IGNORECASE)
    
    # 處理常見的塊級元素
    block_tags = ['div', 'section', 'article', 'aside', 'nav', 'header', 'footer', 'main']
    for tag in block_tags:
        content = re.sub(f'<{tag}[^>]*>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(f'</{tag}>', '\n', content, flags=re.IGNORECASE)
    
    # 處理段落標籤
    content = re.sub(r'<p[^>]*>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'</p>', '\n', content, flags=re.IGNORECASE)
    
    # 處理標題標籤
    for i in range(1, 7):
        content = re.sub(f'<h{i}[^>]*>(.*?)</h{i}>', f'\n{"#" * i} \\1\n', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 處理列表
    content = re.sub(r'<ul[^>]*>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'</ul>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<ol[^>]*>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'</ol>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 處理表格（簡單轉換）
    content = re.sub(r'<table[^>]*>.*?</table>', '\n[表格內容]\n', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 處理行內元素 - 移除標籤但保留內容
    inline_tags = ['span', 'strong', 'b', 'em', 'i', 'small', 'big', 'sub', 'sup', 'mark']
    for tag in inline_tags:
        content = re.sub(f'<{tag}[^>]*>(.*?)</{tag}>', r'\1', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 處理連結 - 嘗試轉換為 Markdown 格式
    content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<a[^>]*>(.*?)</a>', r'\1', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 處理圖片 - 嘗試轉換為 Markdown 格式
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>', r'![\2](\1)', content, flags=re.IGNORECASE)
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>', r'![](\1)', content, flags=re.IGNORECASE)
    
    # 處理程式碼
    content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 移除所有剩餘的 HTML 標籤
    content = re.sub(r'<[^>]*>', '', content)
    
    # 解碼 HTML 實體
    html_entities = {
        '&lt;': '<', '&gt;': '>', '&amp;': '&', '&nbsp;': ' ',
        '&quot;': '"', '&#39;': "'", '&ldquo;': '"', '&rdquo;': '"',
        '&lsquo;': "'", '&rsquo;': "'", '&mdash;': '—', '&ndash;': '–',
        '&copy;': '©', '&reg;': '®', '&trade;': '™'
    }
    for entity, char in html_entities.items():
        content = content.replace(entity, char)
    
    # 清理格式
    # 移除多餘的空白行
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    # 移除行尾空格
    content = re.sub(r'[ \t]+\n', '\n', content)
    # 移除行首多餘空格（但保留代碼縮進）
    content = re.sub(r'\n[ \t]+([^\s])', r'\n\1', content)
    
    return content.strip()

def process_remaining_files():
    """處理所有剩餘包含 HTML 的文件"""
    
    # 找出所有包含 HTML 標籤的文件
    problematic_files = []
    content_dir = Path('content/posts')
    
    print("🔍 掃描剩餘的 HTML 文件...")
    
    for md_file in content_dir.glob('**/*.md'):
        try:
            file_path = str(md_file)
            
            # 跳過已經有備份的文件（已處理過）
            if os.path.exists(file_path + '.backup'):
                continue
                
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            html_count = len(re.findall(r'<[^>]*>', content))
            
            if html_count > 0:
                problematic_files.append((file_path, html_count))
                
        except Exception as e:
            continue

    # 按 HTML 標籤數量排序
    problematic_files.sort(key=lambda x: x[1], reverse=True)

    print(f'找到 {len(problematic_files)} 個包含 HTML 標籤的剩餘文件')

    if len(problematic_files) == 0:
        print('✅ 沒有需要處理的文件')
        return 0, 0

    print('\n開始超激進轉換...')
    
    converted_count = 0
    failed_count = 0

    for i, (file_path, html_count) in enumerate(problematic_files):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 分離前置設定和內容
            lines = content.split('\n')
            front_matter_end = -1
            
            # 支援 YAML (---) 和 TOML (+++) 格式
            if lines[0].strip() in ['---', '+++']:
                delimiter = lines[0].strip()
                for j, line in enumerate(lines[1:], 1):
                    if line.strip() == delimiter:
                        front_matter_end = j
                        break
            
            if front_matter_end > 0:
                front_matter = '\n'.join(lines[:front_matter_end + 1])
                body = '\n'.join(lines[front_matter_end + 1:])
                
                # 轉換內容
                original_html_count = html_count
                converted_body = ultra_aggressive_html_to_markdown(body)
                html_count_after = len(re.findall(r'<[^>]*>', converted_body))
                
                # 非常寬鬆的轉換條件 - 只要有任何改善就轉換
                if html_count_after < original_html_count:
                    # 備份原文件
                    backup_path = file_path + '.backup'
                    with open(backup_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    # 寫入轉換後的內容
                    new_content = front_matter + '\n\n' + converted_body
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    converted_count += 1
                    improvement_ratio = (original_html_count - html_count_after) / original_html_count
                    if converted_count % 50 == 0:
                        print(f'已處理 {converted_count} 個文件...')
                    
                    # 只顯示重要的轉換結果
                    if original_html_count >= 10:
                        print(f'✅ 轉換: {os.path.basename(file_path)} ({original_html_count} -> {html_count_after} 標籤, {improvement_ratio:.1%} 改善)')
                else:
                    failed_count += 1
                    if original_html_count >= 20:
                        print(f'⚠️ 跳過: {os.path.basename(file_path)} (無法改善 {original_html_count} 個標籤)')
            else:
                failed_count += 1
                
        except Exception as e:
            failed_count += 1

    return converted_count, failed_count

def main():
    """主函數"""
    
    print("🚀 開始最終清理模式...")
    print("=" * 50)
    
    converted, failed = process_remaining_files()
    
    print(f"\n🎊 最終清理結果:")
    print(f"• 成功轉換: {converted} 個文件")
    print(f"• 失敗/跳過: {failed} 個文件")
    
    # 最終統計
    total_files = len(list(Path('content/posts').glob('**/*.md')))
    backup_files = len(list(Path('content/posts').glob('**/*.backup')))
    
    remaining_files = []
    for md_file in Path('content/posts').glob('**/*.md'):
        try:
            file_path = str(md_file)
            if file_path.endswith('.backup') or os.path.exists(file_path + '.backup'):
                continue
                
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            html_count = len(re.findall(r'<[^>]*>', content))
            if html_count > 0:
                remaining_files.append((file_path, html_count))
        except:
            continue
    
    total_remaining_html = sum(count for _, count in remaining_files)
    
    print(f"\n📊 最終全域統計:")
    print(f"• 總文件數: {total_files}")
    print(f"• 已轉換文件數: {backup_files} ({backup_files * 100 // total_files}%)")
    print(f"• 剩餘含 HTML 文件: {len(remaining_files)} 個")
    print(f"• 剩餘 HTML 標籤總數: {total_remaining_html}")
    
    if remaining_files:
        remaining_files.sort(key=lambda x: x[1], reverse=True)
        print(f"\n📋 剩餘最多 HTML 標籤的前 10 個文件:")
        for file_path, count in remaining_files[:10]:
            print(f"  • {os.path.basename(file_path)}: {count} 個標籤")
    else:
        print("\n🎉 所有 HTML 標籤都已清理完畢！")

if __name__ == '__main__':
    main()
