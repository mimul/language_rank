#!/usr/bin/env python
#

import urllib
import re

langs = ('ASP','ActionScript','Ada','Arc','Arduino','Assembly','AutoHotkey','Boo','C#','C++','C','Clojure','CoffeeScript','ColdFusion','Common Lisp','D','Delphi','Dylan','Eiffel','Emacs Lisp','Erlang','FORTRAN','Factor','Fancy','Go','Gosu','Groovy','HaXe','Haskell','Io','Ioke','Java','JavaScript','Lua','Matlab','Mirah','Nemerle','Nu','OCaml','Objective-C','Objective-J','PHP','Parrot','Perl','Prolog','Pure Data','Python','R','Racket','Rebol','Ruby','Rust','Scala','Scheme','Self','Shell','Smalltalk','Standard ML','SuperCollider','Tcl','Turing','VHDL','Vala','Verilog','VimL','Visual Basic','XQuery','ooc')
surl = 'http://stackoverflow.com/questions/tagged/'

counts = {}
HexCharacters = "0123456789abcdef"

def UrlEncode(s):
    r = ''
    for c in s:
        o = ord(c)
        if (o >= 48 and o <= 57) or \
            (o >= 97 and o <= 122) or \
            (o >= 65 and o <= 90) or \
            o == 36 or o == 45 or o == 95 or \
            o == 46 or o == 43 or o == 33 or \
            o == 42 or o == 39 or o == 40 or \
            o == 41 or o == 44:
            r += c
        else:
            r += '%' + CleanCharHex(c)
    return r

def CleanCharHex(c):
    o = ord(c)
    r = HexCharacters[o / 16]
    r += HexCharacters[o % 16]
    return r

for lang in langs:
    enclang = UrlEncode(lang)
    response = urllib.urlopen(surl + enclang).read()
    message = re.search('summarycount.*>(.*)<', response)
    if message!=None:
        count = int(message.group(1).replace(',', ''))
    else:
        count = 0
    counts[lang] = count
    #print lang, ':', count
sorted_counts = sorted(counts.items(), key=lambda(k,v):(v,k))
sorted_counts.reverse()
for i in range(0, 68):
   print sorted_counts[i][0],',',i+1