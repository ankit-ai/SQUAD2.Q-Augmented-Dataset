
# --------------- Produce SQUAD 2.Q augmented dataset --------------------------------------------------
#  Description: Augment Questions in SQUAD 2.0 dataset with syntatic variance produced by Back Translation
#               Using Neural Machine Translation System (NMT)
#               Designed to work with Google Cloud Translate API
#               The API Translates the original question (English to French) and then back translates (French to English)
#-- Developed by Ankit R. Chadha (ankitrc@stanford.edu) and Rewa Sood (rrsood@stanford.edu)

import json
import random
from math import floor
import secrets

with open('./train-v2.0.json',encoding='utf-8') as f:
    data = json.load(f)
from google.cloud import translate

client = translate.Client()

def randomly_replace_synonym(tmp_in,percentage=0.5):  
    len_in = len(tmp_in)
    #Deep Copy
    tmp_in_ip = tmp_in[:]

    if True:
        #Translate En -> Fr
        target = 'fr'
        translation = client.translate(tmp_in,target_language=target)
        trans_output = translation["translatedText"].replace('&#39;',"'")
        trans_output = trans_output.replace('&quot;',"'")

        #Translate Fr -> En
        target = 'en'
        translation_en = client.translate(trans_output,target_language=target)
        tmp_out = translation_en["translatedText"].replace('&#39;',"'").replace('&quot;', "'")
        tmp_out = tmp_out.encode('utf8')

    return tmp_out
     


for i in range(0,len(data["data"])):
    for j in range(0,len(data["data"][i]["paragraphs"])):
        for k in range(0,len(data["data"][i]["paragraphs"][j]["qas"])):
            tmp_in = data["data"][i]["paragraphs"][j]["qas"][k]["question"]
            #print('Og is',tmp_in)
            tmp_out_list = randomly_replace_synonym(tmp_in)
            #print('before',len(data["data"][i]["paragraphs"][j]["qas"]))
            #print(tmp_out_list)
            if tmp_out_list != '':
                dict = data["data"][i]["paragraphs"][j]["qas"][k]
                dict["id"] = secrets.token_hex(15)
                dict["question"] = tmp_out_list.decode('utf8').replace("'", '"')
                data["data"][i]["paragraphs"][j]["qas"].append(dict)
                print('after',len(data["data"][i]["paragraphs"][j]["qas"]))
                print('paragraph number is', j)

print('Writing Final JSON')
with open('train-v2q.json', 'w') as outfile:
    json.dump(data, outfile)              