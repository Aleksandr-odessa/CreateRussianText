import pymorphy3
from word_in_out import DocxReadWrite
from math import ceil
from random import sample
from if_title import if_title, if_name, par_to_list

morph = pymorphy3.MorphAnalyzer()


class Word(DocxReadWrite):

    @staticmethod
    def norm_word(text: str) -> list:
        paragraphs = par_to_list(text)
        word_norm = []
        for par in paragraphs:
            list_word = if_name(par)
            list_par = if_title(list_word)
            word_norm.append(", ".join(list_par))
        return word_norm

    @staticmethod
    def del_word(text: str, percent: int) -> list:
        paragraphs = par_to_list(text)
        text_str = []
        for sent in paragraphs:
            length: int = len(sent)
            if len(sent) > 1:
                del_list = sample(range(0, length), ceil(length * percent / 100))
                for ind in del_list:
                    sent[ind] = "_______"
            word_str = " ".join(sent)
            text_str.append(word_str)
        return text_str
