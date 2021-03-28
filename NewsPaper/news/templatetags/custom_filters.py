# антимат antimat profanity-filter
# https://www.cyberforum.ru/python-beginners/thread2492074.html
#  https://github.com/jaredmessenger/profanity-filter
from django import template

register = template.Library()

@register.filter(name='Censor')

def Censor(value):
    bad_words = ['bad','word']
    arr_words = value.split(' ')
    for word in arr_words:
        if word in bad_words:
            idx = arr_words.index(word)
            arr_words[idx] = '***'
    return ' '.join(arr_words)