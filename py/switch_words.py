#!/usr/bin/env python3
'''
-------------------------------------------------------------------------
File name    : switch_words.py
Title        :
Project      :
Developers   :  Doron
Created      : Fri Sep 20, 2019  12:19
Description  :
Notes        :
---------------------------------------------------------------------------
'''
import sys
import codecs
import nltk
import random
bad_words = ['the','and','for','project','new','album','film','with','from','your','you','our']
titles = []
nnp_list = {}
randomization_list = []
rewrite = 0
debug = 0

def add_data(filename, name_loc, write_data):
    global titles,nnp_list,randomization_list
    if write_data:
        myfile = codecs.open(filename, 'r', encoding='utf-8', errors='ignore')
        lines = myfile.readlines()
        lines.pop(0)
        slines = [i.split(",") for i in lines]
        titles = [i[name_loc].replace("(Canceled)","") for i in slines if len(i) >= 24 and i[23] == "technology" and i[22] not in ["Apps","Web"] and len(i[name_loc].split()) > 2]
        with open("../db/titles_list.txt","w") as f:
            f.write(",".join(titles))

        nltks = [nltk.pos_tag(nltk.word_tokenize(i)) for i in titles[:]]
        for this_nltk in nltks[:]:
            for item in this_nltk:
                citem = item[0].lower()
                if item[1] == "NNP" and len(citem) > 1 and citem not in bad_words:
                    if citem not in nnp_list:
                        nnp_list[citem] = 1
                    else:
                        nnp_list[citem] += 1
    else:
        with open("../db/titles_list.txt") as f:
            titles = f.readline().split(",")

    if write_data:
        sortedd = sorted(nnp_list.items(),key=lambda x: x[1],reverse=1)
        # print(sortedd[0:1000])
        for item in sortedd:
            if item[1] > 20:
                randomization_list.extend([item[0]]*item[1])
            else:
                break

        with open("../db/nnp_randomization_list.txt","w") as f:
            f.write(",".join(randomization_list))
    else:
        with open("../db/nnp_randomization_list.txt") as f:
            randomization_list = f.readline().split(",")




def test_random_switch(filename, name_loc):
    global titles
    s1_nnp = []
    s2_nnp = []
    myfile = codecs.open(filename, 'r', encoding='utf-8', errors='ignore')
    lines = myfile.readlines()
    lines.pop(0)
    slines = [i.split(",") for i in lines]
    titles = [i[name_loc] for i in slines if len(i) >= 10]# and i[3] == "Technology"]
    while len(s1_nnp) < 3 or len(s2_nnp) < 4:
        s1 = random.choice(titles)
        s2 = random.choice(titles)
        s1_nltk = nltk.pos_tag(nltk.word_tokenize(s1))
        s2_nltk = nltk.pos_tag(nltk.word_tokenize(s2))
        s1_nnp = [i[0] for i in s1_nltk if i[1] == "NNP"]
        s2_nnp = [i[0] for i in s2_nltk if i[1] == "NNP"]

    print("Sent' 1:",s1)
    print("S1 nltk:",s1_nltk)
    print("S1 nnp:",s1_nnp)
    print("Sent' 2:",s2)
    print("S2 nltk:",s2_nltk)
    print("S2 nnp:",s2_nnp)
    s1_new = s1.replace(random.choice(s1_nnp),random.choice(s2_nnp))
    s2_new = s2.replace(random.choice(s2_nnp),random.choice(s1_nnp))
    s1_new = s1_new.replace(random.choice(s1_nnp),random.choice(s2_nnp))
    s2_new = s2_new.replace(random.choice(s2_nnp),random.choice(s1_nnp))
    print(s1_new,"\n",s2_new)
    # for line in lines:
        # sline = line.split(',')
        # if sline[3] != 'Technology':
            # continue

        # tokens = nltk.word_tokenize(sline[1])
        # tagged = nltk.pos_tag(tokens)
        # entities = nltk.chunk.ne_chunk(tagged)
        # # tagged.draw()
        # for ent in tagged:
            # print("XXXXXXXXXXXX")
            # print(ent)
            # print("XXXXXXXXXXXX")

#add_data("db/ks-projects-201612.csv",1)
# add_data("../db/ks-projects-201801.csv",1)
add_data("../db/kickstarter.csv",9,rewrite)

for i in range(100):
    local_rand_list = randomization_list[:]
    # print(local_rand_list)
    selected_title = random.choice(titles)
    selected_title_nltk = nltk.pos_tag(nltk.word_tokenize(selected_title))
    selected_title_nnps = [i[0] for i in selected_title_nltk if i[1] == "NNP"]
    if debug:
        print("ORIGINAL:",selected_title)
        print(nltk.pos_tag(nltk.word_tokenize(selected_title)))
    for nnp in selected_title_nnps:
        nnp_to_replace_with = random.choice(randomization_list)
        local_rand_list.remove(nnp_to_replace_with)
        selected_title = selected_title.replace(nnp,nnp_to_replace_with)

    if debug:
        print("NEW:",selected_title)

    print(selected_title)
# print(nnp_list)
#print(title_list)
