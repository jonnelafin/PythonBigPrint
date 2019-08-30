print("art.py by Jonnelafin")
import time

def fetch():
	red = ""
	full = []
	with open("presets/base.jfFont", 'r') as f:
		last = ""
		for x in f.read():
			if x == "~":
				full.append(red)
				red = ""
			elif x == "\n" and last == "~":
				1/1
			else:
				red = red + x
			last = x
	return full
def basi1(font = []):
	whitesp = 1	
	
	chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "?", "!", ":", ".", ",", "'", "-", "|"]
	text = input("Text: ").upper()
	rows = ["", "", "", "", ""]
	for letter in text:
		if letter == " ":
			art = "    \n"*len(rows)
		else:
			try:
				art = font[chars.index(letter)]
			except Exception as e:
				art = "  █   \n  █   \n  ██  \n  █   \n██████\n"
				print(e)
		artRows = []
		red = ""
		for i in art:
			if i == "\n":
				artRows.append(red + (" "*whitesp))
				red = ""
			else:
				red = red + i
		for i in range(len(rows)):
			rows[i] = rows[i] + artRows[i]
	for i in rows:
		time.sleep(0.1)
		print(i)
font = fetch()
basi1(font)
