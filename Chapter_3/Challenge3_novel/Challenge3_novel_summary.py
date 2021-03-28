import requests
import bs4
from gensim.summarization import summarize

url = 'http://www.gutenberg.org/files/2852/2852-h/2852-h.htm'

page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
chapter_elems = soup.select('div[class="chapter"]')
chapters = chapter_elems[2:]

chapter_content = dict()
for i, ch in enumerate(chapters):
    p_elems = [element.text for element in ch.find_all('p')]
    chapter_content[i] = ' '.join(p_elems)  # Be sure to join using a space!
    print("\nSummary of Chapter {}:".format(i+1))
    print(summarize(chapter_content[i], word_count=75))