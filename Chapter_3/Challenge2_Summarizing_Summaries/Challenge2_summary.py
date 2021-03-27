from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from gensim.summarization import summarize


def main():
    # Load text files as a string. 
    with open('Harry_Potter.txt') as infile:
        text = infile.read()

    # remove references buckets, remove extra spaces, digits, and punctuation.
    text = re.sub('\[\d+\]', '', text) #example: [33]
    text = re.sub('\s+/', ' ', text) 
    text_edit = re.sub('[^a-zA-Z/-]', ' ', text) #/- allow "-", example: 11-inch
    text_edit = re.sub('\s+', ' ', text_edit)
    

    # Request input.
    while True:
        max_words = input("Enter max words per sentence for summary: ")
        num_sents = input("Enter number of sentences for summary: ")
        if max_words.isdigit() and num_sents.isdigit():
            break
        else:
            print("\nInput must be in whole numbers.\n")
                      
    # Run functions to generate sentence scores.
    text_edit_no_stop = remove_stop_words(text_edit)
    word_freq = get_word_freq(text_edit_no_stop)
    sent_scores = score_sentences(text, word_freq, max_words)

    # Summary 1: Print the top-ranked sentences.
    counts = Counter(sent_scores)
    summary = counts.most_common(int(num_sents))
    print("\nSummary based on word frequency:")
    for i in summary:
        print(i[0])
        
    # Summary 2: Compare to the summary from gensim   
    # It uses a graph-based ranking algorithm called TextRank. The sentence 
    # that is the most like the others is considered the most important.   
    total_words =  int(max_words) * int(num_sents)   
    print("\nSummary from gensim:")
    print(summarize(text, word_count=total_words))  
        

def remove_stop_words(speech_edit):
    """Remove stop words from string and return string."""
    stop_words = set(stopwords.words('english'))
    speech_edit_no_stop = ''
    for word in nltk.word_tokenize(speech_edit):
        if word.lower() not in stop_words:
            speech_edit_no_stop += word + ' '  
    return speech_edit_no_stop

def get_word_freq(speech_edit_no_stop):
    """Return a dictionary of word frequency in a string."""
    word_freq = nltk.FreqDist(nltk.word_tokenize(speech_edit_no_stop.lower()))
    return word_freq

def score_sentences(speech, word_freq, max_words):
    """Return dictionary of sentence scores based on word frequency."""
    sent_scores = dict()
    sentences = nltk.sent_tokenize(speech)
    for sent in sentences:
        sent_scores[sent] = 0
        words = nltk.word_tokenize(sent.lower())
        sent_word_count = len(words)
        if sent_word_count <= int(max_words):
            for word in words:
                if word in word_freq.keys():
                    sent_scores[sent] += word_freq[word]
            sent_scores[sent] = sent_scores[sent] / sent_word_count
    return sent_scores

if __name__ == '__main__':
    main()
