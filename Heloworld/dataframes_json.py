# import json
# data = json.load(open("files/data.json","r"))
# print (data["rain"])
# -- DataFrames(JSON) - This script takes the user input (string) text and searches in the data.json file and return the value
# The Word here is the Key and Value is the meaning of the word (Key Value pair)

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("files/data.json", "r"))


def translate(word):
    word = word.lower()
    if word not in data:
        if len(get_close_matches(word, data.keys())) > 0:
            # return " Did  you mean %s instead ?" % get_close_matches(word, data.keys())[0]
            response_input = input(" Did  you mean %s instead ?. enter Y/N " % get_close_matches(word, data.keys())[0])
            if response_input == "Y":
                return data[get_close_matches(word, data.keys())[0]]
            elif response_input == "N":
                return" The word doesnt exist , Please double check it. "
            else:
                return" We didnt understand your entry "

    else:
        return data[word]


user_input = input("Enter word to search in Thesaurus: ")
output = translate(user_input)
if type(output) == list:
    for i in output:
        print (i)
else:
    print (output)