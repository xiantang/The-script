import urllib.request
import urllib.parse
from urllib.request import quote
import json
from lxml import etree
import re
#aaa
def thanslate(txt):#个别单词翻译，全文翻译调用api
    # os.chdir('e:\\python')
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
    data = {
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1519203291346',
        'sign': '29768db456ed01293a7b7f7eb5628c0a',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    data['i'] = txt
    data = urllib.parse.urlencode(data).encode('utf - 8')  # 转化为二进制提交
    wy = urllib.request.urlopen(url, data)
    html = wy.read().decode('utf - 8')
    try:
        ta = json.loads(html)
        if(ta['translateResult'][0][0]['tgt'] == txt):
            print('没有找到这个单词/词语！\n')
        elif ta['translateResult'][0][0]['tgt']:
            # print(type(ta['translateResult'][0][0]['tgt']))
            print('翻译结果: %s \n' % (ta['translateResult'][0][0]['tgt']))
    except:
        pass

def full_content(txt):#完整意思
    quete_code=quote(txt)
    try:
        data=urllib.request.urlopen('http://dict.youdao.com/w/{}/#keyfrom=dict2.top'.format(quete_code))
        data=data.read().decode('utf-8','ignore')
        selector=etree.HTML(data)
        for sel in selector.xpath('//*[@id="phrsListTab"]/div[2]/ul/li'):
            print("".join(sel.xpath('./text()')))
    except:
        pass

if __name__ == '__main__':
    while True:
        txt = input('输入要翻译的内容!（输入0退出）\n===>')
        if txt == '0':
            break
        else:
            thanslate(txt)
            full_content(txt)