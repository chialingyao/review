data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:  #餘數概念
			print(len(data))
print('檔案讀取完畢了~共有', len(data), '筆資料')

sumLen = 0 #計算每筆留言的平均長度
for d in data:
	sumLen = sumLen + len(d)
print('每筆留言平均長度是', sumLen / len(data), '字')	

#篩選資料，建立一個新清單來篩，把小於100個字的留言塞到一個新資料裡面

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100個字')
print(new[0])
print(new[1])

#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('一共有', len(good), '筆提到good')
#print(good[0])

good =[d for d in data if 'good' in d]
print(good[2])
print('一共有', len(good), '筆提到good')

bad =['bad' in d for d in data]
print(bad)