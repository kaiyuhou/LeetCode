# -*- coding: utf-8 -*-
import requests
import random
from time import sleep
from m3u_parser import M3uParser

m3_u8_folder = 'C:/Users/mikew/Desktop/m3u8/'

def check_url_ok(url):
    useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    try:
        result = requests.get(url, headers={"User-Agent": useragent}, timeout=10)
        return result.status_code == 200
    except requests.exceptions.ConnectionError as e:
        return False

def m3u_parse():
    m3u = M3uParser()
    for line in src_data:
        url = line[1]

        m3u.parse_m3u(url)
        print(f'**{url}')
        # print(m3u.get_list())
        m3u_list = map(lambda item: {"name": item.get("name", ""), "url": item.get("url", "")}, m3u.get_list())
        for m in m3u_list:
            sleep(1)
            print(f'**{m}')
            if not check_url_ok(m.get("url")):
                continue
            print("{name},{url}".format(name=m.get("name"), url=m.get("url", "")))


def generate_m3u8(src, output_file='temp'):
    output_file = f'{m3_u8_folder}{output_file}.m3u8'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('#EXTM3U\n')
        for line in src:
            f.write(f'#EXTINF:-1 ,{line[0]}\n')
            f.write(f'{line[1]}\n')


def read_txt(file = f'{m3_u8_folder}src_2021-12-22.txt'):
    with open(file, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or ',' not in line:
                continue
            src_data.append(line.split(','))


def read_m3u8(file=f'{m3_u8_folder}Global.m3u8'):
    name = None
    with open(file, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or '#EXTM3U' in line:
                continue
            if '#' in line:
                name = line.split(',')[1]
            else:
                src_data.append((name, line))


def remove_dump(src):
    ans = []
    dp = set()
    for line in src:
        if line[1] in dp:
            continue
        dp.add(line[1])
        ans.append(line)
    return ans



src_data = []
read_txt()

print(len(src_data))

ok_url = set()
ok_file = f'{m3_u8_folder}check.m3u8'

with open(ok_file, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        ok_url.add(line)

output_data = []
for line in src_data:
    if line[1] in ok_url:
        output_data.append(line)

src_data = output_data
read_m3u8()
src_data += src_data


output_data = []
for line in src_data:
    if 'cctv' in line[0] or 'CCTV' in line[0] or 'Cctv' in line[0]:
        output_data.append(line)

###################

print('len output ',len(output_data))

# print(output_data)

cctv_5 = []

for line in output_data:
    if '5' in line[0] or '体育' in line[0]:  #'新闻' in line[0]:
        if '15' in line[0]:
            continue
        if '5+' in line[0]:
            continue
        cctv_5.append(line)

cctv_5 = remove_dump(cctv_5)


print(f'final output {len(cctv_5)}')
generate_m3u8(cctv_5, 'cctv_5')






















