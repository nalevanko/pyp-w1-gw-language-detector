# -*- coding: utf-8 -*-
from languages import LANGUAGES

"""This is the entry point of the program."""

def get_word_count(text, list_of_words):
    '''Counts how many words in text appear in list_of_words.'''
    
    count = 0
    text_l = text.split()
    
    for word in text_l:
        if word.lower() in list_of_words:
            count += 1
            
    return count

def detect_language(text, LANGUAGES):
    """Returns the detected language of given text."""
    lang = None
    word_count = 0
    our_test = []
    
    for language in LANGUAGES:
        
        result = get_word_count(text, language['common_words'])
        print(result)
        #import pdb; pdb.set_trace()
        if result > word_count:
            lang = language['name']
            word_count = result
            
    return lang

print(detect_language('''Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán. Considerado con frecuencia el
            mejor jugador del mundo y calificado en el ámbito deportivo como el
            más grande de todos los tiempos, Messi es el único futbolista en la
            historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
            ellos en forma consecutiva– y el primero en
            recibir tres Botas de Oro.''', LANGUAGES))