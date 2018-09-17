data = []
count=0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 10000 == 0:
			print(len(data))
print('留言紀錄共有',len(data),'筆')

print(data[0])
#num = input('請問您想要讀取第幾筆?')
#num = int(num)
#print(data[num-1])
# sum_len = 0
# for d in data:
# 	sum_len += len(d)

# print('平均每筆留言有',int(sum_len/len(data)),'字')

# new =[]
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('共有', len(new), '筆留言長度小於100') 
# print(new[5])

# #good =[]
# #term = input('請輸入要篩選的字?')
# #for d in data:
# #	if term in d:
# #		good.append(d)
# #print('共有',len(good),'筆留言提到',term)
# #print(good[0])

# term = input('請輸入要篩選的字?')
# good = [d for d in data if term in d] #速寫法

# print('共有',len(good),'筆留言提到',term)

#計數程序
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #直接把查找字典結果的值進行運算
		else:
			wc[word] = 1 #新增key的value
print('此檔案中共出現', len(wc), '個不同的字!')

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請輸入您想查的字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '共出現', wc[word], '次')
	else:
		print('您要找的字沒有出現過!')
print('感謝您的使用!')
