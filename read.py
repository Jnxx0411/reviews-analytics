data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1             
		if count % 1000 ==0:          #每讀1000筆印出來,1000 的倍數才印出來
			print(len(data))                 
		
print('檔案讀取完了, 總共有', len(data), '筆資料')

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
