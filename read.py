data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1             
		if count % 1000 ==0:          #每讀1000筆印出來,1000 的倍數才印出來
			print(len(data))                 
		
print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0])

sum_len = 0                           #資料平均長度
for d in data:
	sum_len += len(d)
print('平均是', sum_len/len(data), '個字')





new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')   #塞選小於100 長度的留言
print(new[0])
print(new[1])




good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到GOOD')    #留言提到GOOD
print(good[0])

#快寫法  good = [d for d in data if 'good' in d]



# 文字計數

wc = {}                               # word_count 字典
for d in data:
	words = d.split()                 # split 預設值就是空白鍵, 後面列印遇到連續空白不會切成空字串
	for word in words:
		if word in wc:
			wc[word] += 1             # word 次數加一
		else:
			wc[word] = 1              # wc 新增KEY進WC字典

for word in wc:                       # word = key
	if wc[word] > 1000000:            # 次數超過1000000 的字
		print(word, wc[word])         # key, 次數

print(len(wc)) 

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:	
		print(word, '出現的次數為:', wc[word])
	else:
		print('這個字沒出現過喔')
print('感謝查詢')