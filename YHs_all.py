






import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException




from retrying import retry
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 正则和lxml混用
def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！



    selector = etree.HTML(html)
    Price = selector.xpath('//*[@id="spFP"]/div[1]/span[1]/text()')
    for item in Price:
        big_list.append(item)








def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l




def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)






'''
1. 创建 URL队列, 响应队列, 数据队列 在init方法中
2. 在生成URL列表中方法中,把URL添加URL队列中
3. 在请求页面的方法中,从URL队列中取出URL执行,把获取到的响应数据添加响应队列中
4. 在处理数据的方法中,从响应队列中取出页面内容进行解析, 把解析结果存储数据队列中
5. 在保存数据的方法中, 从数据队列中取出数据,进行保存
6. 开启几个线程来执行上面的方法
'''

def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper




def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num



class JSPool_M1(object):

    def __init__(self,url):
        self.url = url

    def page_request(self):
        ''' 发送请求获取数据 '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        response = requests.get(self.url,headers=headers)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            pass

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)
        mid_url = '//*[@id="uamods-topics"]/div/div/div/ul/li/a/@href'


        c1 = element.xpath(mid_url)
        for item in c1:
            big_list1.append(item)


class JSPool_M2(object):

    def __init__(self,url):
        self.url = url

    def page_request(self):
        ''' 发送请求获取数据 '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        response = requests.get(self.url,headers=headers)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            pass

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)
        f_url = '//*[@id="uamods-pickup"]/div[2]/div/p/a/@href'


        c1 = element.xpath(f_url)
        for item in c1:
            big_list2.append(item)











if __name__ == '__main__':
    t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    big_list1 = []
    big_list2 = []
    all_ur = ["https://news.yahoo.co.jp/categories/domestic", "https://news.yahoo.co.jp/categories/world",
              "https://news.yahoo.co.jp/categories/business", "https://news.yahoo.co.jp/categories/entertainment",
              "https://news.yahoo.co.jp/categories/sports", "https://news.yahoo.co.jp/categories/it",
              "https://news.yahoo.co.jp/categories/science", "https://news.yahoo.co.jp/categories/life",
              "https://news.yahoo.co.jp/categories/local"]





    for item1 in all_ur:

        jsp1 = JSPool_M1(item1)# 这里把请求和解析都进行了处理
        jsp1.page_parse_()
    for item2 in big_list1:
        j2 = JSPool_M2(item2)
        j2.page_parse_()

    for f_item in big_list2:

        with open('{0}_all.txt'.format(t), 'a') as file_handle:
            # .txt可以不自己新建,代码会自动新建
            file_handle.write(f_item+"")  # 写入
            file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据


#1720
# 1803
# 3612
# 4555
