data = []
count=0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 10000 == 0:
			print(len(data))
print('留言紀錄共有',len(data),'筆')
num = input('請問您想要讀取第幾筆?')
num = int(num)
print(data[num-1])