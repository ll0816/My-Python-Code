# !/usr/bin/python
# -*- coding: utf-8 -*-
# Transliterate non-ASCII to ASCII
# Liu L.
# 12-04-15

import urllib2
from bs4 import BeautifulSoup

def transliterate(word, translit_table):
    converted_word = ''
    for char in word:
        transchar = ''
        if char in translit_table:
            transchar = translit_table[char]
        else:
            transchar = char
        converted_word += transchar
    return converted_word

cyrillic_translit={u'\u0410': 'A', u'\u0430': 'a',
u'\u0411': 'B', u'\u0431': 'b',
u'\u0412': 'V', u'\u0432': 'v',
u'\u0413': 'G', u'\u0433': 'g',
u'\u0414': 'D', u'\u0434': 'd',
u'\u0415': 'E', u'\u0435': 'e',
u'\u0416': 'Zh', u'\u0436': 'zh',
u'\u0417': 'Z', u'\u0437': 'z',
u'\u0418': 'I', u'\u0438': 'i',
u'\u0419': 'I', u'\u0439': 'i',
u'\u041a': 'K', u'\u043a': 'k',
u'\u041b': 'L', u'\u043b': 'l',
u'\u041c': 'M', u'\u043c': 'm',
u'\u041d': 'N', u'\u043d': 'n',
u'\u041e': 'O', u'\u043e': 'o',
u'\u041f': 'P', u'\u043f': 'p',
u'\u0420': 'R', u'\u0440': 'r',
u'\u0421': 'S', u'\u0441': 's',
u'\u0422': 'T', u'\u0442': 't',
u'\u0423': 'U', u'\u0443': 'u',
u'\u0424': 'F', u'\u0444': 'f',
u'\u0425': 'Kh', u'\u0445': 'kh',
u'\u0426': 'Ts', u'\u0446': 'ts',
u'\u0427': 'Ch', u'\u0447': 'ch',
u'\u0428': 'Sh', u'\u0448': 'sh',
u'\u0429': 'Shch', u'\u0449': 'shch',
u'\u042a': '"', u'\u044a': '"',
u'\u042b': 'Y', u'\u044b': 'y',
u'\u042c': "'", u'\u044c': "'",
u'\u042d': 'E', u'\u044d': 'e',
u'\u042e': 'Iu', u'\u044e': 'iu',
u'\u042f': 'Ia', u'\u044f': 'ia',
u'\xa0': ''}

if __name__ == '__main__':
    page = urllib2.urlopen('http://lists.memo.ru/d1/f1.htm')
    # print page.headers['content-type']

    encoding = page.headers['content-type'].split('charset=')[1]
    content = page.read()
    content = unicode(content, encoding)
    # print content[200: 300]

    converted_content = transliterate(content, cyrillic_translit)
    #print converted_content

    converted_soup = BeautifulSoup(converted_content, 'lxml')

    names = []
    for entry in converted_soup.find_all(class_="name"):
        names.append(entry.get_text())

    print len(names)
    print names[:20]