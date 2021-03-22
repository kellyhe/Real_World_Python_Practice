import nltk
from nltk.draw.dispersion import dispersion_plot
import matplotlib.pyplot as plt
from nltk.text import Text

def main():
    hound = text_to_string('hound.txt')
    tokens = nltk.word_tokenize(hound)
    texts = Text(tokens)
    plt.ion()
    plt.figure(figsize=(12, 9))
    targets=['Holmes','Watson','Mortimer','Henry','Barrymore','Stapleton','Seldon','hound']
    dispersion_plot(texts, targets, ignore_case=True, title='Lexical Dispersion Plot')
    plt.show(block=True)
    
def text_to_string(filename):
    """Read a text file and return a string."""
    #with open(filename,'r',encoding='ISO-8859-1') as infile:
    with open(filename,encoding='utf-8', errors='ignore') as infile:
        return infile.read()
    
if __name__ == '__main__':
    main()