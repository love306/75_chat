def read_file(filename):
	chat = []
	with open('input.txt', 'r', encoding='utf-8-sig') as dialog:
		for line in dialog:
			chat.append(line.strip())
		print(chat)
		return chat
def convert(chat):
	new = []
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ':' + line)
		return chat
	print(new)
def write_file(filename, chat):
	with open (filename, 'w', encoding='utf-8-sig') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read_file('input.txt')
	chat = convert(chat)
	write_file('123.txt',chat)

main()
