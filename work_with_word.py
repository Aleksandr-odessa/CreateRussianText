import pymorphy3
from word_in_out import DocxReadWrite
from math import ceil
from random import sample


class Word(DocxReadWrite):

    @staticmethod
    def norm_word(text: list) -> list:
        morph = pymorphy3.MorphAnalyzer()
        rez_text: list = []
        for p in text:
            str_norm: list = []
            list_sentence: list = p.split(".")
            for sent in list_sentence:
                list_s: list = sent.lstrip(" ").split(" ")
                list_word: list = []
                for _ in list_s:
                   word = morph.parse(_)[0]
                   # get up normal form of word
                   word_norm = word.normal_form
                   # add to list of words
                   list_word.append(word_norm)
                # create string
                word_str = ", ".join(list_word).capitalize()
                str_norm.append(word_str)
            text_new = ". ".join(str_norm)
            rez_text.append(text_new)
        return rez_text

    @staticmethod
    def del_word(text: list, percent: int) -> list:
        rez_text = []
        for p in text:
            list_sentence: list = p.split(".")
            text_str = []
            for word in list_sentence:
                list_word: list = word.lstrip(" ").split(" ")
                length: int = len(list_word)
                if length > 1:
                    del_count: int = ceil(length*percent/100)
                    del_list = sample(range(0, length), del_count)
                    for ind in del_list:
                        list_word.pop(ind)
                        list_word.insert(ind, "____")
                    word_str = " ".join(list_word)
                    text_str.append(word_str)
            text_new = ". ".join(text_str)
            rez_text.append(text_new)
        return rez_text
