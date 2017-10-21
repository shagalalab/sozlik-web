#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def converter(sentence):
    character_mapping_upper = {
        'А': "A",
        'Ә': "Á",
        'Б': "B",
        'В': "V",
        'Г': "G",
        'Ғ': "Ǵ",
        'Д': "D",
        'Е': "E",
        'Ё': "Yo",
        'Ж': "J",
        'З': "Z",
        'И': "Í",
        'Й': "Y",
        'К': "K",
        'Қ': "Q",
        'Л': "L",
        'М': "M",
        'Н': "N",
        'Ң': "Ń",
        'О': "O",
        'Ө': "Ó",
        'П': "P",
        'Р': "R",
        'С': "S",
        'Т': "T",
        'У': "U",
        'Ү': "Ú",
        'Ў': "W",
        'Ф': "F",
        'Х': "X",
        'Ҳ': "H",
        'Ц': "C",
        'Ч': "Ch",
        'Ш': "Sh",
        'Щ': "Sh",
        'Ъ': "",
        'Ы': "I",
        'Ь': "",
        'Э': "E",
        'Ю': "Yu",
        'Я': "Ya",
    }

    character_mapping_lower = {
        'а': "a",
        'ә': "á",
        'б': "b",
        'в': "v",
        'г': "g",
        'ғ': "ǵ",
        'д': "d",
        'е': "e",
        'ё': "yo",
        'ж': "j",
        'з': "z",
        'и': "i",
        'й': "y",
        'к': "k",
        'қ': "q",
        'л': "l",
        'м': "m",
        'н': "n",
        'ң': "ń",
        'о': "o",
        'ө': "ó",
        'п': "p",
        'р': "r",
        'с': "s",
        'т': "t",
        'у': "u",
        'ү': "ú",
        'ў': "w",
        'ф': "f",
        'х': "x",
        'ҳ': "h",
        'ц': "c",
        'ч': "ch",
        'ш': "sh",
        'щ': "sh",
        'ъ': "",
        'ы': "ı",
        'ь': "",
        'э': "e",
        'ю': "yu",
        'я': "ya",

    }

    for k, v in character_mapping_upper.iteritems():
        sentence = sentence.replace(k, v)

    for k, v in character_mapping_lower.iteritems():
        sentence = sentence.replace(k, v)

    return sentence


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nScript will convert karakalpak cyrillic text to new latin script, and save to a new file.")
        print("Usage: python latin_file_converter.py <filename>\n")
    else:
        filename = sys.argv[1]
        r = open(filename, 'r')
        lines = r.readlines()
        r.close()

        w = open(filename + '_convert', 'w')
        for line in lines:
            w.write(converter(line))
        w.close()
