
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f: #把第一行多餘的符號拿掉
	for line in f:
		lines.append(line.strip()) #strip把換行符號拿掉

for line in lines:
	s = line.split(' ')
	time = s[0][:5] #把s0的字串當成清單來看,從0取到5(0,1,2,3,4[尾數不包含])
	name = s[0][5:]
	print(time)
	print(name)