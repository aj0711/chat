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
	#print(lines)
	return lines #回傳lines清單

#分析轉換檔案
def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_img_count = 0
	viki_img_count = 0

	for line in lines: #for 就是把清單(lines)中的東西用某個檔名(line)一個個叫出來
		s = line.split(' ')	#遇到空白鍵就切割
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2]== '貼圖':
				allen_sticker_count += 1
			elif s[2]== '圖片':
				allen_img_count += 1
			else:	
				for m in s[2:]: #清單分割
					allen_word_count += len(m) #把字串長度加入allen_word_account
		elif name == 'Viki':	
			if s[2]== '貼圖':
				viki_sticker_count += 1
			elif s[2]== '圖片':
				viki_img_count += 1
			else:	
				for m in s[2:]: #清單分割
					viki_word_count += len(m) #把字串長度加入allen_word_account
	print('allen說', allen_word_count, '貼圖', allen_sticker_count,'圖片', allen_img_count)		
	print('viki說', viki_word_count, '貼圖', viki_sticker_count,'圖片', viki_img_count)	

def write_file(filename, lines):
	with open(filename, 'w', encoding='UTF-8') as f:
		for line in lines:
			f.write(line + '\n')


#定義主功能
def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines) 
	# write_file('output_ck.txt', lines)

#執行程式
main()

