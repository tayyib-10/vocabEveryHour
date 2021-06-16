from os import getcwd
import json
from random import choice
from PyDictionary import PyDictionary


def get_info(word):
    dictionary = PyDictionary()
    
    # gets synonyms
    synonyms_list = dictionary.synonym(word)
    synonyms = ""
    for synonym in synonyms_list[3:7]:
        synonyms += (synonym + ", ")
    
    # get antonyms
    antonyms_list = dictionary.antonym(word)
    antonyms = ""
    for antonym in antonyms_list[3:7]:
        antonyms += (antonym + ", ")

    return synonyms + "\n\n" + antonyms
def get_word(path):
    words_data = open(path, "r")
    words = words_data.read().split("\n")
    random_word = choice(words)
    return random_word

def get_path():
    working_dir_path = getcwd().replace("\\", "\\\\")
    full_path = working_dir_path + "\\assets\\words.txt" # replace it with your path

    return full_path

if __name__ =="__main__":
    path = get_path()
    print(get_word(path))
    print(get_info(get_word(path)))
    
    

    
    