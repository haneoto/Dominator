import requests
import os

# 要下载的文件链接
urls = [
    "https://ruleset.skk.moe/Clash/domainset/download.txt",
    "https://ruleset.skk.moe/Clash/non_ip/download.txt",
    "https://ruleset.skk.moe/Clash/domainset/cdn.txt",
    "https://ruleset.skk.moe/Clash/non_ip/cdn.txt"
]

# 设置 User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

def download_files():
    output_lines = {
        'DOMAIN': [],
        'DOMAIN-SUFFIX': [],
        'DOMAIN-KEYWORD': [],
        'DOMAIN-REGEX': []
    }

    for url in urls:
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()  # 检查请求是否成功

        # 检查响应内容类型
        if 'text/plain' not in response.headers.get('Content-Type', ''):
            print(f"警告: {url} 返回的不是文本内容，可能是 HTML 格式。")
            continue

        # 处理下载的内容
        for line in response.text.splitlines():
            line = line.strip()

            # 检查是否包含 # 或特定字符串
            if '#' in line or 'this_ruleset_is_made_by_sukkaw.ruleset.skk.moe' in line:
                continue

            # 处理行
            if line.startswith('+.'):
                line = 'DOMAIN-SUFFIX,' + line[2:]
                output_lines['DOMAIN-SUFFIX'].append(line)
            elif line.startswith('DOMAIN-KEYWORD'):
                output_lines['DOMAIN-KEYWORD'].append(line)
            elif line.startswith('DOMAIN-REGEX'):
                output_lines['DOMAIN-REGEX'].append(line)
            elif not line.startswith('DOMAIN'):
                line = 'DOMAIN,' + line
                output_lines['DOMAIN'].append(line)
            else:
                output_lines['DOMAIN'].append(line)

    # 按顺序合并所有行
    sorted_lines = (
        output_lines['DOMAIN'] +
        output_lines['DOMAIN-SUFFIX'] +
        output_lines['DOMAIN-KEYWORD'] +
        output_lines['DOMAIN-REGEX']   
    )

    # 检查 supplement.txt 是否存在并添加内容
    if os.path.exists('Supplement.txt'):
        with open('Supplement.txt', 'r', encoding='utf-8') as supplement_file:
            supplement_content = supplement_file.read().strip().splitlines()
            sorted_lines = supplement_content + sorted_lines  # 将 Supplement 内容放在最上方

    # 写入输出文件
    with open('Cluster_CDN.DL-Global.list', 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(sorted_lines) + '\n')

    print("处理完成，结果已保存到 Cluster_CDN.DL-Global")

if __name__ == '__main__':
    download_files()
