import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn


def remove_adj(sen):
    words = sen.split(' ')
    new_words = []
    for word in words:
        pos_l = set()
        for tmp in wn.synsets(word):
            if tmp.name().split('.')[0] == word:
                pos_l.add(tmp.pos())
        if 'a' not in pos_l:
            new_words.append(word)

    return ' '.join(new_words)


if __name__=="__main__":
    print(remove_adj('a large airplane is sitting under a roof.'))