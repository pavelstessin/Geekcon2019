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
blurbs = []
nltk_types = ["NNP","NN","NNS","JJ","VBP","VBD"]
randomization_list = [[],[],[],[],[],[]]
types_list = [{},{},{},{},{},{}]
rewrite = 0
debug = 0


def add_data(filename, name_loc, write_data):
    global titles,blurbs,types_list,randomization_list
    if write_data:
        myfile = codecs.open(filename, 'r', encoding='utf-8', errors='ignore')
        lines = myfile.readlines()
        lines.pop(0)
        slines = [i.split(",") for i in lines]
        for project in slines:
            if len(project) >= 24 and project[23] == "technology" and project[22] not in ["Apps","Web"] and len(project[name_loc].split()) > 2:
                title = project[name_loc].replace("(Canceled)","").lower()
                blurb = project[3]
                blurb = blurb.replace("I","You").replace(" me "," you ").replace(" my "," your ")
                titles.append(title)
                blurbs.append(blurb)

        with open("../db/titles_list.txt","w") as f:
            f.write(",".join(titles))

        with open("../db/blurbs_list.txt","w") as f:
            f.write(",".join(blurbs))

        nltks = [nltk.pos_tag(nltk.word_tokenize(i)) for i in titles[:]]
        for this_nltk in nltks[:]:
            for item in this_nltk:
                citem = item[0].lower()
                for ind,nltk_type in enumerate(nltk_types):
                    if item[1] == nltk_type and len(citem) > 1 and citem not in bad_words:
                        if citem not in types_list[ind]:
                            types_list[ind][citem] = 1
                        else:
                            types_list[ind][citem] += 1
    else:
        with open("../db/titles_list.txt") as f:
            titles = f.readline().split(",")

        with open("../db/blurbs_list.txt") as f:
            blurbs = f.readline().split(",")

    if write_data:
        for ind,nltk_type in enumerate(nltk_types):
            sortedd = sorted(types_list[ind].items(),key=lambda x: x[1],reverse=1)
            for item in sortedd:
                if item[1] > 20:
                    randomization_list[ind].extend([item[0]]*item[1])
                else:
                    break

        with open("../db/nnp_randomization_list.txt","w") as f:
            for ind,nltk_type in enumerate(nltk_types):
                f.write(",".join(randomization_list[ind]))
                f.write("\n")
    else:
        with open("../db/nnp_randomization_list.txt") as f:
            for ind,nltk_type in enumerate(nltk_types):
                randomization_list[ind] = f.readline().strip().split(",")


add_data("../db/kickstarter.csv",9,rewrite)

def get_project():
    local_rand_list = []
    for rand_list in randomization_list:
        local_rand_list.append(rand_list[:])

    # print(local_rand_list)
    selected_title = random.choice(titles)
    selected_blurb = blurbs[titles.index(selected_title)]
    selected_title_nltk = nltk.pos_tag(nltk.word_tokenize(selected_title))
    if debug:
        print("ORIGINAL:",selected_title)
        print(nltk.pos_tag(nltk.word_tokenize(selected_title)))

    for ind,nltk_type in enumerate(nltk_types):
        selected_title_type = [i[0] for i in selected_title_nltk if i[1] == nltk_type]

        for nltk_type in selected_title_type:
            type_to_replace_with = random.choice(local_rand_list[ind])
            local_rand_list[ind].remove(type_to_replace_with)
            selected_title = selected_title.replace(nltk_type,type_to_replace_with)
            selected_blurb = selected_blurb.replace(nltk_type,type_to_replace_with)

    if debug:
        print("NEW:",selected_title)

    return selected_title,selected_blurb

if __name__ == "__main__":
    for i in range(1):
        print(get_project())

