from os import getcwd
from random import choice
from vocabulary.vocabulary import Vocabulary as vb

def get_info(word):
    pass

def get_words(path):
    words_data = open(path, "r")
    words = words_data.read().split("\n")
    random_word = choice(words)
    print(random_word)

def get_path():
    working_dir_path = getcwd().replace("\\", "\\\\")
    full_path = working_dir_path + "\\assets\\words.txt" # replace it with your path

    return full_path

if __name__ =="__main__":
    path = get_path()

    print(vb.synonym(get_words(path))
    