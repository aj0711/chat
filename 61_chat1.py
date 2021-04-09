#讀取檔案
#分析檔案
#產出檔案
#執行功能

#寫fun
#讀檔案
#def read_file():   read_file為function name
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='UTF-8-sig') as f: #-sig是將記事本存檔的\ufeff這些字拿掉
		for line in f:
			lines.append(line.strip()) #.strip是把換行符號拿掉
	print(lines)
	return lines #回傳lines清單

#分析轉換檔案
def convert(lines):
	new = []
	person = None
	for line in lines: #for 就是把清單(lines)中的東西用某個檔名(line)一個個叫出來
		if line == 'Allen':
			person = 'Allen'
			continue #跳到下一個迴圈
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:	
			new.append(person + ': ' + line)
	print(new)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding='UTF-8') as f:
		for line in lines:
			f.write(line + '\n')


#定義主功能
def main():
	lines = read_file('input.txt')
	lines = convert(lines) 
	write_file('output_ck.txt', lines)

#執行程式
main()

