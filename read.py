data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

print(data[0])


sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度是: ', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('有', len(new), '筆資料長度小於100')
print(new[0])
print(new[1])



#文字計數
wc = {}  #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  #新增新的key進wc字典

for word in wc:
    if wc[word] > 100:
        print(word, wc[word])

print(len(wc))

while True:
    word = input('輸入想查找的字: ')
    if word == 'q':
        break
    else:
        if word in wc:
            print(word, '出現過: ', wc[word], ' 次')
        else:
            print('這個字沒有出現過喔!')

print('謝謝您的使用!')