import re

def find_words(num, str):
    return re.findall(r'\w'*num + '+', str) 
