import difflib
import json


dictionary=json.load(open("dict.json","r"))
def expand(wrd):
    wrd=wrd.lower()
    if wrd in dictionary.keys():
        print(dictionary[wrd])
    elif len(difflib.get_close_matches(wrd,dictionary.keys()))>0:
        match=difflib.get_close_matches(wrd,dictionary.keys())[0]
        yn=int(input("do you mean to say {}??Type 1 for yes else type 0".format(match)))
        if yn==1:
            print(dictionary[match])
        elif yn==0:
            print("Sorry could not find your word in the dictionary")
        else:
            print("Sorry could not understand your choice")
            
    else:
        print("Sorry could not find your word in the dictionary")
        
        


if __name__=='__main__':
    
    choice=1
    while choice==1:
        word=input("please enter a word that you would like to look for in the dictionary---->")
        expand(word)
        choice=int(input("press 1 for another word search and 0 to exit"))
        
        
    
    