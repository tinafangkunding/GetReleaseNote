import requests
import re
import json

def request_doc(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    pattern = re.compile('<a class="reference internal".*?id="id.*?">(.*?)</a>',re.S)
    items = re.findall(pattern,html)
    #print('here is the content of the ', items)
    print(len(items))
    return items

def write_item_to_file(item,year,month):
    print('开始写入数据 ====> ' + str(item))
    with open('releasenote.txt', 'a', encoding='UTF-8') as f:
        f.write('ReleaseNote' + '-' + str(year) + '-' + str(month).zfill(2) + '\n')
        f.write(str(item) + '\n')
        f.close()

def main(year,month):
    url = 'https://docs.snowflake.com/en/release-notes/' + str(year) + '-' + str(month).zfill(2) + '.html'
    html = request_doc(url)
    items = parse_result(html)
    write_item_to_file(items,year,month)
    print(url)

if __name__ == "__main__":
    for y in range(2015,2016):#change the years if need
        for m in range(6,13):
            main(y,m) 
