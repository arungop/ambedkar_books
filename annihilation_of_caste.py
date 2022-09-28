from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

file_content=open ("amb.txt").read()

#mask = np.array(Image.open('index_.png'))
wordcloud = WordCloud(stopwords = STOPWORDS,
                      background_color = 'black',
                        width = 1200,
                         height = 1000,
                            color_func = random_color_func
                            ).generate(file_content)

plt.imshow(wordcloud)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.title('Annihilation of Caste: Dr. B. R. Ambedkar')
plt.show()
