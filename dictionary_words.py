import random
import sys

# Function for making a capitalized sentence of len words out of wordlist dict
def random_sentence(dict, len):
    words = random.sample(dict, len - 1)
    sentence = " " + " ".join(words) + "."
    sentence = random.choice(dict).title() + sentence
    return sentence


if __name__ == '__main__':
    # Obtain list of words from system wordlist
    dictionary = open('/usr/share/dict/words').read().splitlines()
    # Get length of generated "sentence"
    length = int(sys.argv[1])
    sentence = random_sentence(dictionary,length)
    print(sentence)
