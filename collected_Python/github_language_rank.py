#!/usr/bin/env python

import urllib, re
from multiprocessing import Pool

content = urllib.urlopen("http://github.com/languages").read()
ranks = {}

def fetch(lang):
    lang = urllib.unquote(lang)
    sub = urllib.urlopen("http://github.com/languages/" + lang).read()
    matches = re.findall("is the #([0-9]+)", sub)
    if(len(matches) > 0):
        rank = matches[0]
        ranks[lang] = rank
        print lang,',',rank
    else:
       matches = re.findall("is <strong>the most</strong> popular", sub)
       if(len(matches) > 0):
          ranks[lang] = 1
          print lang,',',1

if __name__ == '__main__':
    langs = re.findall("/languages/(.+)\"", content)
    p = Pool(45)
    p.map(fetch, langs)
