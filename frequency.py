import string


def clean_word(dirty):
    clean = ""
    if(len(dirty) > 1):
        clean = dirty[:-1] + dirty[-1].translate(None, string.punctuation)
    else:
        clean = dirty.translate(None, string.punctuation)
    return clean.lower()


def histogram(source_text):
    histogram = []
    # read in the text file into a list of strings line by line
    source_list = open(source_text).read().split()
    for word in source_list:
        print('"' + clean_word(word) + '"')
    return histogram


def unique_words(histogram):
    return 0


def frequency(histogram, word):
    return 0

if __name__ == '__main__':
    histogram('./onepager.txt')
