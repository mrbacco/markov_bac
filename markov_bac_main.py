"""
Created on June 2021
updated July 2021
@author: mrbacco 2021
"""


#### importing the modules
import random
import csv
from nltk.tokenize import regexp_tokenize
from collections import Counter
import pandas as pd

# opening a file of pronouns and storing the content in a variable 
with open('/home/pi/Documents/CODE/PYTHON/ARISTO__PLATO/pronouns.txt', "r") as f2:
    spamreader = csv.reader(f2, delimiter=',')
    words=[i for row in spamreader for i in row]

# defining the pandas dataframe in 3 columns
dict_df = pd.DataFrame(columns = ["first","second","freq"])
dict_df["first"] = words
second = words[1:]
second.append("Endword")

# empty list for words to end the sentence
end_words = []
for word in words:
    if word [-1] in [".","!","?"] and word != ".":
        end_words.append(word)
print(end_words)
