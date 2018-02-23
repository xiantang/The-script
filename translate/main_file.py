import urllib.request
import urllib.parse
from urllib.request import quote
import json
import re
from lxml import etree
from dirctionary.greenhand import Tsl
#Tsl.text_to_python_dir() is zip


class Thanslate(object):
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
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
    def thanslate(self,txt):#个别单词翻译，全文翻译调用api
        self.data['i'] = txt
        data = urllib.parse.urlencode(self.data).encode('utf - 8')  # 转化为二进制提交
        wy = urllib.request.urlopen(self.url, data)
        html = wy.read().decode('utf - 8')
        try:
            ta = json.loads(html)
            if(ta['translateResult'][0][0]['tgt'] == txt):
                pass
                # print('没有找到这个单词/词语！\n')
            elif ta['translateResult'][0][0]['tgt']==None:
                # print(type(ta['translateResult'][0][0]['tgt']))
                # print('翻译结果: %s \n' % (ta['translateResult'][0][0]['tgt']))
                pass
            else:
                return ta['translateResult'][0][0]['tgt']
        except:
            pass

    def full_content(self,txt):#完整意思
        quete_code=quote(txt)
        try:
            data=urllib.request.urlopen('http://dict.youdao.com/w/{}/#keyfrom=dict2.top'.format(quete_code))
            data=data.read().decode('utf-8','ignore')
            selector=etree.HTML(data)
            for sel in selector.xpath('//*[@id="phrsListTab"]/div[2]/ul/li'):
                print("".join(sel.xpath('./text()')))
        except:
            pass

    def split_sentence(self,text):
        # words=text.split(' ')
        words=re.split(' ', text.replace('\'', '\"'))
        # print(type(Tsl.text_to_python_dir()))#class type dict
        translated_words=[]
        for word in words:
            if word.lower() in Tsl.text_to_python_dir():
                translated_words.append(word)
            elif re.search('[^\w]',word):
                comma=re.sub('\w','',word)
                comma=[i for i in reversed(comma)]
                comma_in_words = re.split('[^\w]', word)
                for index,comma_in_word in enumerate(comma_in_words):

                    if comma_in_word.lower() in Tsl.text_to_python_dir():
                        if len(comma) !=0:
                            translated_words.append(comma_in_word+comma.pop())
                    else:
                        if comma_in_word == '':
                            if len(comma)!=0:
                                translated_words.append(comma.pop())

                        else:
                            translated_word = self.thanslate(comma_in_word)
                            if translated_word is None:
                                if len(comma) != 0:
                                    translated_words.append(comma_in_word+comma.pop())
                                else:
                                    translated_words.append(comma_in_word + '({})'.format(translated_word))
                            else:
                                if len(comma)!=0:
                                    translated_words.append(comma_in_word+comma.pop() + '({})'.format(translated_word))
                                else:
                                    translated_words.append(comma_in_word  + '({})'.format(translated_word))
                                # for i in range(index):
                                #     translated_words.append(comma_in_word +comma[i]+ '({})'.format(translated_word))

            else:
                translated_word = self.thanslate(word)
                if translated_word is None:
                    translated_words.append(word) #如果是空的话就加入原来的
                else:
                    translated_words.append(word + '({})'.format(translated_word))

        translated_sentence=' '.join(translated_words)
        print(translated_sentence)
if __name__ == '__main__':
    while True:
        txt = input('输入要翻译的内容!（输入0退出）\n===>')
        if txt == '0':
            break
        else:
            Translator = Thanslate()
            # Translator.thanslate(txt)
            # Translator.full_content(txt)
            Translator.split_sentence(text=txt)
