import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))
def findWord(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,key))>0:
        yn=input("Did you mean '%s' instead? if Yes press 'Y' or 'N' for No!\n"
                     %(get_close_matches(word,key)[0]))
        if yn=='y':
            return data[get_close_matches(word,key)[0]]
        elif yn=='n':
            return "Please double check tha word you entered"
        else: return"incorrect input, please press y or n"

    else:
        return"You entered incorrect word"
    
word=input("Enter the word to be searched\n").lower()
key=data.keys()
output=findWord(word)
if type(output)==list:
    j=1
    for i in output:
        print ("\n"+str(j)+') '+i+'\n')
        j+=1
else: print (output)
