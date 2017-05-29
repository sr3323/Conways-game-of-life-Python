oldBoard=open("Gameboard.txt","r")
newBoard=open("board.txt","w")
for line in range(0,int(raw_input("what is the size of your grid?"))):
	lineRead=oldBoard.readline()
	lineRead=lineRead.strip("\n")
	newBoard.write(lineRead)
oldBoard.close()
newBoard.close()