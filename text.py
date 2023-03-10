import pymorphy3
from math import ceil
from random import shuffle, randint

morph = pymorphy3.MorphAnalyzer()


class TextSeparted:  
    def __init__(self, text):
        self.text = text 

    def support_function(self, words:list)-> str:
        shuffle(words)
        return " ".join(words)+"."

    def main_function(self, *args)-> list:
       # to brake into sentences
        sentences = [sentences.split('.') for sentences in self.text]
        list_shuffle = []
        sentences_shuffle = []
        # iterations for sentences
        for sentence in sentences:
            # iterations into sentence
            for sent in sentence:
                if sent: 
                    words = sent.strip().split()
                    words_ = self.support_function(words, *args)
                    list_shuffle.append(words_)
            sentences_shuffle.append(" ".join(list_shuffle))
            list_shuffle.clear()
        return sentences_shuffle

class TextNormal(TextSeparted):

    def normal_forms(self, words:list) -> list:
        list_word = []
        for w in words:
            word = morph.parse(w)[0]
            list_word.append(word.normal_form.title()) if w.istitle() else list_word.append(word.normal_form)
        return list_word

    def support_function(self, words:list)-> str:
        sentence = self.normal_forms(words)
        return " ".join(sentence)+"."     

class DeleteWord(TextSeparted):
   
    def support_function(self, words:list, percent:int = 20)-> str:
        length = len(words)
        count_del = ceil(length * percent / 100)
        del_list = [randint(0, length-1) for _ in range(count_del)]
        for ind in del_list:
            words[ind] = "_______"
        return " ".join(words)+"." 