# translations.py
color_translations = {
    'english': {
        'red': 'vermelho',
        'orange': 'laranja',
        'yellow': 'amarelo',
        'green': 'verde',
        'blue': 'azul',
        'indigo': 'índigo',
        'violet': 'violeta'
    },
    'portuguese': {
        'vermelho': 'red',
        'laranja': 'orange',
        'amarelo': 'yellow',
        'verde': 'green',
        'azul': 'blue',
        'indigo': 'indigo',
        'violeta': 'violet'
    },
    'french': {
        'rouge': 'vermelho',
        'orange': 'laranja',
        'jaune': 'amarelo',
        'vert': 'verde',
        'bleu': 'azul',
        'indigo': 'índigo',
        'violet': 'violeta'
    }
}

portuguese_to_french_translations = {
    'vermelho': 'rouge',
    'laranja': 'orange',
    'amarelo': 'jaune',
    'verde': 'vert',
    'azul': 'bleu',
    'índigo': 'indigo',
    'violeta': 'violet'
}

french_to_english_translations = {
    'rouge': 'red',
    'orange': 'orange',
    'jaune': 'yellow',
    'vert': 'green',
    'bleu': 'blue',
    'indigo': 'indigo',
    'violet': 'violet'
}

english_to_french_translations = {
    'red': 'rouge',
    'orange': 'orange',
    'yellow': 'jaune',
    'green': 'vert',
    'blue': 'bleu',
    'indigo': 'indigo',
    'violet': 'violet'
}


def translate_color(color, from_lang, to_lang):
    if from_lang == 'english' and to_lang == 'portuguese':
        return color_translations['english'].get(color, 'unknown')
    
    elif from_lang == 'english' and to_lang == 'french':
     return english_to_french_translations.get(color, 'unknown')
 
    elif from_lang == 'portuguese' and to_lang == 'english':
        return color_translations['portuguese'].get(color, 'unknown')
    
    elif from_lang == 'portuguese' and to_lang == 'french':
        return portuguese_to_french_translations.get(color, 'unknown')

    elif from_lang == 'french' and to_lang == 'english':
     return french_to_english_translations.get(color, 'unknown')
 
    elif from_lang == 'french' and to_lang == 'portuguese':
     return color_translations['french'].get(color, 'unknown')
    
    else:
        return 'unknown'
