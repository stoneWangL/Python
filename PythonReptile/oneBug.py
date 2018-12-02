import requests
#第一个爬虫脚本：主要是将猫眼电影的一个页面的请求返回页面代码显示出来
def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()
