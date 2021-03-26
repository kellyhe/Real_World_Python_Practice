import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS   

# Images from https://www.pngimages.pics/
# Load an image as a NumPy array. 
mask_male = np.array(Image.open('mask_male.png'))
mask_female = np.array(Image.open('mask_female.jpg'))


# Get stop words as a set and add extra words.
stopwords = STOPWORDS
stopwords.update(['Harry','Potter','Ron','Weasley','Hermione','Granger','Cho'\
                  ,'Chang','Luna','Lovegood','description','rowling','year'\
                  ,'series','character','actor','Rupert','Grint'])

def create_word_cloud(name,mask,stopwords):
    """Create word cloud for given text file."""
    # Test files from Wiki or https://harrypotter.fandom.com
    # Load text files as a string. 
    with open('{}.txt'.format(name)) as infile:
        text = infile.read()
    # Generate word cloud.
    wc = WordCloud(max_words=50,
               relative_scaling=0.5,
               mask=mask,
               background_color='white',
               stopwords=stopwords,
               margin=2,
               random_state=7,
               contour_width=1,
               contour_color='brown',
               colormap='copper').generate(text)

    # Turn wc object into an array.
    colors = wc.to_array()

    # Plot and save word cloud.
    plt.figure(figsize=(10, 6))
    plt.title("Harry Potter Characters Word Cloud",fontsize=15, color='brown')
    plt.imshow(colors, interpolation="bilinear")
    plt.axis('off')
    #plt.show()
    plt.savefig('{}_wordcloud.png'.format(name))


create_word_cloud('Harry_Potter',mask_male,stopwords)
create_word_cloud('Ron_Weasley',mask_male,stopwords)
create_word_cloud('Hermione_Granger',mask_female,stopwords)
create_word_cloud('Cho_Chang',mask_female,stopwords)
create_word_cloud('Luna_Lovegood',mask_female,stopwords)

   
    