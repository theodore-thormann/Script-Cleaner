from nltk.corpus import stopwords
import re

script = '/film_script.txt'

def get_chars(script):
    output = []
    
    #Uses regex and NLTK stopwords to filter superfluous words
    rx = r'\n\s{2,}(?!(?:INT\.?|EXT\.?)\b)([A-Z]{2,}(?:\s[A-Z]+)*)(?: \(V\.?[Oo]\.\))?'
    stop_words = set(stopwords.words('english'))

    #Opens and reads in film script
    with open(script, 'r') as f:
        lines = f.read()
    
    #Creates a string of characters based on the regex requirements
    chars = re.findall(rx, lines)

    #Filters the character list to remove stop words
    for words in chars:
        split_words = words.split()
        if not any([word.lower() in stop_words for word in split_words]):
            output.append(words)
            
    output = list(set(output)) #Remove duplicates
    output.sort() #Sort list
    
    return output