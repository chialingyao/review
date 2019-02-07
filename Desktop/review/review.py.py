data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:  #餘數概念
			print(len(data))
print('檔案讀取完畢了~共有', len(data), '筆資料')

# print(data[0])
# sumLen = 0 #計算每筆留言的平均長度
# for d in data:
# 	sumLen = sumLen + len(d)
# print('每筆留言平均長度是', sumLen / len(data), '字')	

# 宣告字典 每個字ㄉ計數
wc ={} #word_count
for d in data:#每一個留言是d (str)
	words = d.split(' ') #WORDS是字 
	for word in words: #去讀取每個字，要檢查每個字有沒有出現在字典裡
		if word in wc :
			wc[word] += 1 #去wc字典查找word, 如果有出現在字典裡就+1
		else:
			wc[word] = 1 #去wc字典查找word, 如果沒有出現在字典裡就新增那個字(新增key)

# for word in wc:
# 	if wc[word] > 1000000:
# 		print(word, wc[word]) #把字典跟次數印出來
# print(len(wc))

# 可以查詢的功能

while True:
	word = input('請問你想查啥字')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word], '次')
	else:
		print('這個字沒有出現過喔!')


print('感謝使用本查詢功能')


	


#篩選資料，建立一個新清單來篩，把小於100個字的留言塞到一個新資料裡面

#new = []
#for d in data:
#	if len(d) < 100:
#		new.append(d)
#print('一共有', len(new), '筆留言長度小於100個字')
#print(new[0])
#print(new[1])

#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('一共有', len(good), '筆提到good')
#print(good[0])

#good =[d for d in data if 'good' in d]
#print(good[2])
#print('一共有', len(good), '筆提到good')

#bad =['bad' in d for d in data]
#print(bad)