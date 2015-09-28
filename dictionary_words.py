import random
import sys

def random_sentence(dict, len):
    words = random.sample(dict, len - 1)
    sentence = " " + " ".join(words) + "."
    sentence = random.choice(dict).title() + sentence
    return sentence


if __name__ == '__main__':
    dictionary = open('/usr/share/dict/words').read().splitlines()
    length = int(sys.argv[1])
    sentence = random_sentence(dictionary,length)
    print(sentence)
