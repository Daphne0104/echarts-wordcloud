import jieba #分詞

from matplotlib import pyplot as plt  #繪圖數據可視化
from wordcloud import  WordCloud    #詞雲
from PIL import Image   #圖片處理
import numpy as np  #矩陣運算
import sqlite3  #數據庫

#1. 準備詞雲所需的詞
con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text=""
for item in data:
    text = text + item[0]
    #print(item[0])
print(text)

cur.close()
con.close()

#分詞
cut = jieba.cut(text)
string = " ".join(cut)
print(len(string))

# 2.準備遮罩圖片
img = Image.open('tree.jpg')    #打開遮罩圖片
img_array = np.array(img) #圖片轉換為數組
wc = WordCloud(     #詞雲對象封裝
    background_color='white',   #輸出圖片的背景
    mask=img_array,
    font_path="msyh.ttc" #C:\Windows\Fonts

)
wc.generate_from_text(string)   #輸入切好的詞

# 3. 繪製圖片
fig = plt.figure(1)
plt.imshow(wc)  #按照wc的規則顯示圖片
plt.axis("off") #是否顯示座標軸

#plt.show()  #顯示生成的詞雲圖片

#輸出詞雲圖片到文件
plt.savefig(r'wordtree.jpg',dpi=500)

