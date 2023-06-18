def most_frequent(text: str) -> list[str]:
    dict_counts = {}
    SHOW_LIMIT = 10
    new_sorted_dictionary = {}
    new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower(). \
        strip()
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        dict_counts[word] = counter
    sorted_values = sorted(dict_counts.values())[::-1]
    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dictionary[k] = dict_counts[k]
    return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]


text = 'Есть урок , который идет не сорок пять минут, а всю жизнь. Этот урок проходит и в классе, и в поле, и дома, и в лесу.\
      Я назвал этот урок седьмым потому, что в школе обычно бывает не больше шести уроков. Не удивляйтесь, если я скажу,\
          что учителем на этом уроке может быть и береза возле ваше дома, и бабушка. и вы сами (В. Песков)'

print(most_frequent(text))