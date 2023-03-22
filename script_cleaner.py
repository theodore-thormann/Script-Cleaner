from nltk.corpus import stopwords
import re

script = '/film_script.txt'

def get_chars(script):
    #Creates an empty character output list
    char_output = []
    
    #Uses regex and NLTK stopwords to filter superfluous words
    rx = r'\n\s{2,}(?!(?:INT\.?|EXT\.?)\b)([A-Z]{2,}(?:\s[A-Z]+)*)(?: \(V\.?[Oo]\.\))?'
    stop_words = set(stopwords.words('english'))

    #Opens and reads in film script
    with open(script, 'r') as f:
        lines = f.read()
    
    #Creates a string of characters based on the regex requirements
    chars = re.findall(rx, lines)

    #Filters the character list to remove stop words and onomatopoeia
    char_output = [s for s in chars if not any([s[i] == s[i+1] == s[i+2] for i in range(len(s) - 2)])]
    char_output = [s for s in char_output if not any([word.lower() in stop_words for word in s.split()])]
            
    char_output = list(set(char_output)) #Remove duplicates
    char_output.sort() #Sort list
    
    return char_output

def get_scene(script):
    #Creates an empty scene output list
    scene_output = []
    
    #Opens and reads in film script
    with open(script, 'r') as f:
        script = f.read()
        
        #Creates regex pattern to find scene headings
        pattern = r'^\s*(?:INT\.|EXT\.|INT\/EXT\.|I\/E\/|EST\.|MONTAGE|INT\:|EXT\:)\s+.*$'

        # Use regular expressions to find all the scene headings
        scenes = re.findall(pattern, script, flags=re.MULTILINE)

        # Print out each scene and remove excess
        for scene in scenes:
            scene_output.append(scene.strip())
            
    return scene_output
