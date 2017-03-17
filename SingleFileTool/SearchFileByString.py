import os
def find(file,key,code):
	while True:
		context=file.readline()
		if key in context:
			print("[OK]Find(" + code + "):" + i)
			break
		elif context=='':
			break
walk=os.walk(input("path:"))
files=[]
for i in walk:
	for j in i[2]:
		files.append(os.path.join(i[0],j))
while True:
	key=input("Search(\\x00 exit):")
	if key=='':
		exit()
	for i in files:
		try:
			file=open(i,"r",encoding="utf-8")
			find(file,key,"utf-8")
		except:
			try:
				file=open(i,"r",encoding="big5")
				find(file,key,"big5")
			except:
				try:
					file=open(i,"r",encoding="gb")
					find(file,key,"gb")
				except:
					#print("[ER]Not plan text:" + i)
					pass
	print("Final ...")
