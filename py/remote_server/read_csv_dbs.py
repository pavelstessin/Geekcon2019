#!/usr/bin/env python3
'''
-------------------------------------------------------------------------
File name    : read_csv_dbs.py
Title        :
Project      :
Developers   :  pavel
Created      : Thu Sep 19, 2019  10:43
Description  :
Notes        :
---------------------------------------------------------------------------
Copyright 2019 (c) Satixfy Ltd
---------------------------------------------------------------------------*/
'''
import sys
import codecs
bad_words = ['the','and','for','project','new','album','film','with','from','your','you','our']
words_dict = {}

def add_data(filename):
    global words_dict
    myfile = codecs.open(filename, 'r', encoding='utf-8', errors='ignore')
    lines = myfile.readlines()
    lines.pop(0)
    default_item = ["",0]
    for line in lines:
        sline = line.split(',')
        if len(sline) < 10:
            continue

        if sline[3] != 'Technology':
            continue

        if sline[2] in ['Web','App']:
            continue

        interesting_words = []
        for item in [sline[1]]:
            sitem = item.split("(")[0].split()
            sitem = [i.lower().replace('"','') for i in sitem if len(i) > 2]
            for item_word in sitem:
                for bad_word in bad_words:
                    if item_word == bad_word:
                        break

                word_failed = 1 if sline[9] == 'failed' else 0
                interesting_words.append([item_word, word_failed])

        for item in interesting_words:
            bad_word = False
            for word in bad_words:
                if item[0] == word:
                    bad_word = True
                    break

            if not bad_word:
                my_item = words_dict.get(item[0],[0,0])
                my_item[0] += 1
                my_item[1] += item[1]
                words_dict[item[0]] = my_item



add_data("db/ks-projects-201612.csv")
add_data("db/ks-projects-201801.csv")
total_list = []
for item in words_dict:
    total_list.append([item,words_dict[item]])

sortedd = sorted(total_list,key=lambda x:x[1],reverse=1)
for item in range(0,20):
    print(sortedd[item])
