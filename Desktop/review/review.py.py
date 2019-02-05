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