def read_file():
	chat = []
	with open('-LINE-Viki.txt', 'r', encoding='utf-8-sig') as file:
		for line in file:
			chat.append(line.strip())
		return chat
def convert(chat):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in chat:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:				
				for m in s[2:]:
					allen_word_count += len(m)

		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allensay:', allen_word_count, '個字', '傳了', allen_sticker_count, '個貼圖 ', viki_image_count, '個圖片')
	print('Vikisay:', viki_word_count, '個字', '傳了', viki_sticker_count, '個貼圖 ', allen_image_count, '個圖片')
	return 


		
# def write_file(chat):
# 	with open('Viki_out.txt', 'w', encoding='utf-8-sig') as file:

def main():
	chat = read_file()	
	convert(chat)
	
main()