# -*- coding: utf-8 -*-
from languages import LANGUAGES

"""This is the entry point of the program."""

def get_word_count(text, list_of_words):
    '''Counts how many words in text appear in list_of_words.'''
    
    count = 0
    text_l = text.split()
    
    for word in text_l:
        if word in list_of_words:
            count += 1
            
    return count

def detect_language(text, LANGUAGES):
    """Returns the detected language of given text."""
    lang = None
    word_count = 0
    our_test = []
    
    for language in LANGUAGES:
        
        result = get_word_count(text, language['common_words'])
        #print(result)
        if result > word_count:
            lang = language['name']
            
    return lang

#print(detect_language('ich bin du bist sie ist zu', LANGUAGES))