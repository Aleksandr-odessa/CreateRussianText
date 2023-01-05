from work_with_word import Word

s = """О начало русский государство наш летопись рассказывать следующее: новгородский славянин и кривич находиться под власть варяг и платить они дань. Вывести из терпение господство варягов, они прогнать они и стать управляться по старинный родовой обычаям, но вскоре среди они начаться усобица. \n Тогда этот племя по совет новгородский старейшина гостомысел решить отправить посол к варяг. 
Посол отправиться за море к варяжский племя русь и сказали: „земля наш большой и обильна, а порядок в она нет: приходить княжить и владеть мы. Три варяжский князя, братья, рюрик, синеус и трувор прислать в славянский земля. Рюрик поселиться в новгороде, синеус—ич белоозере, трувор— в изборск. """


def testing_def(text:str) -> list:
    list_par: list = text.lstrip(" ").split("\n")
    return list_par


doc = Word('Text.doc', 'uploads')
text_in: list = testing_def(s)
rez = doc.norm_word(text_in)
print(rez)