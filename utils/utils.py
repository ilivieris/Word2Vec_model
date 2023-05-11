import re
from gensim.utils import tokenize

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
    
def preprocess(text:str=None):
    # Replace \n with .
    text = text.replace('\n', '.')
    # Replace \t with 'space'
    text = text.replace('\t', ' ')
    # Count URLs and Remove it 
    text = re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , text)
    # Remove RT 
    text = re.sub(r'\brt\b', '', text).strip()

    return list(tokenize(text))




def get_unique_values(L:list):
 
    # insert the list to the set
    list_set = set(L)
    # convert the set to the list
    unique_list = list(list_set)

    return unique_list