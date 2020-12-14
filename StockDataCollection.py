import requests
from lxml import etree
import time
import re
import json

if __name__ == '__main__':

    stockList = ['sz002555', 'sh600519', 'sz300033', 'sh601012', 'sh603288']
    for stock in stockList:
    # with open(f"StockDataset/stockdata/{stock}.json") as f:
    #     json = json.load(f)
        URL = 'https://androidinvest.com'
        STOCK_ROUTE = f'/stock/s/{stock}/'
        request_url = URL+STOCK_ROUTE
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'cookie': 'csrftoken=nVa6eiP06hDlM1zyk6Lw3mO5ary4w3RPMtkFPDkkMT5rEYJpyRbygdsLyPS64559; Hm_lvt_eac4547169afd7579f80d05491ed45ef=1607913699; Hm_lpvt_eac4547169afd7579f80d05491ed45ef=1607929004'
        }
        s = requests.session()
        s.headers=headers
        result = s.get(request_url)
        # csrf_token1 = result.cookies['csrftoken']
        # print(csrf_token1)
        html = result.content
        html_doc = str(html, 'utf-8')
        tree = etree.HTML(html_doc)
        csrf_token2 = tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")
        csrf_token2 = str(csrf_token2[0])
        print(csrf_token2)

        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Content-Type':'application/json; charset=utf-8',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7,ja;q=0.6',
            'origin': URL,
            'referer': request_url,
            'sec-fetch-mode': 'cors',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': csrf_token2,
            'cookie':'csrftoken=nVa6eiP06hDlM1zyk6Lw3mO5ary4w3RPMtkFPDkkMT5rEYJpyRbygdsLyPS64559; Hm_lvt_eac4547169afd7579f80d05491ed45ef=1607913699; Hm_lpvt_eac4547169afd7579f80d05491ed45ef=1607929004'
        }
        login_req = s.post('https://androidinvest.com/stock/overviewsummary/sh600031/', headers=HEADERS)
        josndata = re.search('"success": true, (.+)', login_req.text).group(1)
        josndata='{'+josndata
        json_object  = json.dumps(eval(josndata), indent = 4)
        with open(f"StockDataset/stockdata/{stock}.json", "w") as outfile:
            outfile.write(json_object)
        print(login_req.text)
        print('a')
        if stock != stockList[-1]:
            print('sleeping for 20 seconds !\n')
            time.sleep(20)



