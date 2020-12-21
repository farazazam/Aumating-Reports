#!/usr/bin/env python
# coding: utf-8



get_ipython().run_line_magic('matplotlib', '')
from pathlib import Path
from textblob import TextBlob
blob = TextBlob(Path('RomeoAndJuliet.txt'). read_text())
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
items = blob.word_counts.items()
items = [item for item in items if item[0] not in stop_words]
from operator import itemgetter
sorted_items= sorted(items,key=itemgetter(1),reverse=True)
top20 = sorted_items[0:20]

import pandas as pd
df = pd.DataFrame(top20, columns=['word','count'])
axes = df.plot.bar(x= 'word', y='count',legend=False)


from pathlib import Path
text = Path('RomeoAndJuliet.txt').read_text()
import imageio
mask_image = imageio.imread('mask_heart.png')
from wordcloud import WordCloud
wordcloud = WordCloud(width=1000, height=1000, colormap='prism', mask=mask_image, background_color='white')
wordcloud = wordcloud.generate(text)

plt.imshow(wordcloud)
