# importing the necessery modules
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

# file object is created
file_ob = open(r"C:\Users\168\Desktop\sfaf.txt")

# reader object is created
reader_ob = csv.reader(file_ob)

# contents of reader object is stored .
# data is stored in list of list  format.
reader_contents = list(reader_ob)

# empty string is declare
text = ""

# iterating through list of rows
for row in reader_contents :

 #  iterating through words in the row
 for word in row :

  # concatenate the words
  text = text + " " + word

# show only 10 words in the wordcloud .
wordcloud = WordCloud(width=1920,  height=1080, max_words=10).generate(text)

# plot the WordCloud image
plt.figure()
plt.imshow(wordcloud,  interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()