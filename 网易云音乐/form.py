from snownlp import SnowNLP
import matplotlib.pyplot as plt

comments = [
    "像是在寺庙中的梦境被铃声吵醒了",
    "3383首东方日推歌曲来啦～",
    "恋心糖！",
    "垂死病中惊坐起，不是新专又睡死。",
    "嗯，幻想万岁乐的前奏，然后还有恋恋的bgm"
]

stat = []
for i in range(0, 10):
    stat.append(0)
print(stat)

for i in comments:
    temp = SnowNLP(i) # 0 - 9
    score = temp.sentiments
    print(score)
    score = int(score*10)
    stat[score] += 1
    print(temp.pinyin)
    print(list(temp.tags))

plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], stat)
plt.show()
