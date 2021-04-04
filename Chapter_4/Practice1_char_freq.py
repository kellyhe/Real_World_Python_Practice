from collections import Counter
import matplotlib.pyplot as plt

#read the text file The Lost World as string
with open('lost.txt') as f:
    text = f.read().lower()

#make dictionary of characters frequency
char_freq = Counter(text)

#sort descending by frequency
char_freq_sorted = dict(sorted(char_freq.items(), key=lambda item: item[1] \
                               ,reverse=True))

#make a simple bar chart    
plt.bar(char_freq_sorted.keys(), char_freq_sorted.values())
plt.title('Characters Frequency in The Lost World')
plt.xlabel('Character')
plt.ylabel('Count')
plt.show()    
