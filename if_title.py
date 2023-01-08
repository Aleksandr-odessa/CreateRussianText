import pymorphy3
morph = pymorphy3.MorphAnalyzer()


def par_to_list(text: str) -> list:
    return [sent.split() for ind, sent in enumerate(text)]


def if_title(paragraph: list) -> list:
    list_word = []
    for w in paragraph:
        word = morph.parse(w)[0]
        list_word.append(word.normal_form.title()) if w.istitle() else list_word.append(word.normal_form)
    return list_word


def if_name(paragraph: list) -> list:
    return [w.title() if any(('Name' in morph.parse(w)[0].tag, 'Patr' in morph.parse(w)[0].tag,
                              'Surn' in morph.parse(w)[0].tag, 'Geox' in morph.parse(w)[0].tag))
            else w for w in paragraph]
