from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
import jieba

with open('wufu.txt', 'r') as f:
    text = f.read()
wufu = " ".join(jieba.cut(text))

#加载背景图片
cloud_mask = np.array(Image.open("fu0.png"))
#生成wordcloud对象
wc = WordCloud(background_color='white',#背景为白色的png图片，背景为无色时不行！
    mask=cloud_mask,
    max_words=2000,
    font_path="simsun.ttc",#此处需要python环境中有对应TXT文件中读取的字体；
    min_font_size=5,
    max_font_size=50,
    width=800,
    height=400
    )
wc.generate(wufu)
wc.to_file("wu_fu.png")