import os
gridSize=int(raw_input("how big is your board"))
grid=[]
newGrid=[]
for item in range(0,(gridSize*gridSize)):
	grid.append("")
	newGrid.append("")
def makeGrid():
	output=""
	for line in range(0,gridSize):
		i=0
		while i<gridSize:
			output+=grid[posToNum(i,line)]
			i+=1
		output+="\n"
	return output
def posToNum(x,y):
	out=x+(y*gridSize)
	return out
def neighborsAlive(cellX,cellY):
	isCorner=False
	isEdge=False
	edgeNum=0
	cornerNum=0
	if cellX==0 and cellY==0:
		isCorner=True
		cornerNum=0
	elif cellX==gridSize-1 and cellY==0:
		isCorner=True
		cornerNum=1
	elif cellX==0 and cellY==gridSize-1:
		isCorner=True
		cornerNum=2
	elif cellX==gridSize-1 and cellY==gridSize-1:
		isCorner=True
		cornerNum=3
	elif cellY==0:
		isEdge=True
		edgeNum=0
	elif cellX==0:
		isEdge=True
		edgeNum=1
	elif cellX==gridSize-1:
		isEdge=True
		edgeNum=2
	elif cellY==gridSize-1:
		isEdge=True
		edgeNum=3
	if isCorner==True:
		if cornerNum==0:
			neighbor1State=getState(posToNum(1,0))
			neighbor2State=getState(posToNum(0,1))
			neighbor3State=getState(posToNum(1,1))
			output=neighbor1State+neighbor2State+neighbor3State
		elif cornerNum==1:
			neighbor1State=getState(posToNum(gridSize-2,0))
			neighbor2State=getState(posToNum(gridSize-1,1))
			neighbor3State=getState(posToNum(gridSize-2,1))
			output=neighbor1State+neighbor2State+neighbor3State
		elif cornerNum==2:
			neighbor1State=getState(posToNum(1,gridSize-1))
			neighbor2State=getState(posToNum(0,gridSize-2))
			neighbor3State=getState(posToNum(1,gridSize-2))
			output=neighbor1State+neighbor2State+neighbor3State
		elif cornerNum==3:
			neighbor1State=getState(posToNum(gridSize-2,gridSize-1))
			neighbor2State=getState(posToNum(gridSize-1,gridSize-2))
			neighbor3State=getState(posToNum(gridSize-2,gridSize-2))
			output=neighbor1State+neighbor2State+neighbor3State
	elif isEdge==True:
		if edgeNum==0:
			neighbor1State=getState(posToNum(cellX-1,0))
			neighbor2State=getState(posToNum(cellX+1,0))
			neighbor3State=getState(posToNum(cellX,1))
			neighbor4State=getState(posToNum(cellX+1,1))
			neighbor5State=getState(posToNum(cellX-1,1))
			output=neighbor1State+neighbor2State+neighbor3State+neighbor4State+neighbor5State
		elif edgeNum==1:
			neighbor1State=getState(posToNum(1,cellY))
			neighbor2State=getState(posToNum(0,cellY-1))
			neighbor3State=getState(posToNum(0,cellY+1))
			neighbor4State=getState(posToNum(1,cellY+1))
			neighbor5State=getState(posToNum(1,cellY-1))
			output=neighbor1State+neighbor2State+neighbor3State+neighbor4State+neighbor5State
		elif edgeNum==2:
			neighbor1State=getState(posToNum(gridSize-2,cellY))
			neighbor2State=getState(posToNum(gridSize-1,cellY-1))
			neighbor3State=getState(posToNum(gridSize-1,cellY+1))
			neighbor4State=getState(posToNum(gridSize-2,cellY-1))
			neighbor5State=getState(posToNum(gridSize-2,cellY+1))
			output=neighbor1State+neighbor2State+neighbor3State+neighbor4State+neighbor5State
		elif edgeNum==3:
			neighbor1State=getState(posToNum(cellX-1,cellY-1))
			neighbor2State=getState(posToNum(cellX+1,cellY-1))
			neighbor3State=getState(posToNum(cellX,cellY-2))
			neighbor4State=getState(posToNum(cellX+1,cellY-2))
			neighbor5State=getState(posToNum(cellX-1,cellY-2))
			output=neighbor1State+neighbor2State+neighbor3State+neighbor4State+neighbor5State
	else:
		neighbor1State=getState(posToNum(cellX-1,cellY))
		neighbor2State=getState(posToNum(cellX+1,cellY))
		neighbor3State=getState(posToNum(cellX,cellY-1))
		neighbor4State=getState(posToNum(cellX,cellY+1))
		neighbor5State=getState(posToNum(cellX-1,cellY-1))
		neighbor6State=getState(posToNum(cellX-1,cellY+1))
		neighbor7State=getState(posToNum(cellX+1,cellY-1))
		neighbor8State=getState(posToNum(cellX+1,cellY+1))
		output=neighbor1State+neighbor2State+neighbor3State+neighbor4State+neighbor5State+neighbor6State+neighbor7State+neighbor8State
	return output
def chkAll():
	for cellY in range(0,gridSize):
		i=0
		while i<gridSize:
			newGrid[posToNum(i,cellY)]=chkCell(i,cellY)
			i+=1
	for num in range(0,gridSize*gridSize):
		grid[num]=newGrid[num]
	updateScreen(makeGrid())
	return
def chkCell(cellX,cellY):
	alive=state(neighborsAlive(cellX,cellY),getState(posToNum(cellX,cellY)))
	output=""
	if alive==1:
		output="O"
	else:
		output=" "
	return output
def readTxt():
	textFile=open("board.txt")
	boardTest=""
	for charPos in range(0,gridSize*gridSize):
		char=textFile.read(1)
		boardTest+=char
		grid[charPos]=char
	textFile.close()
	return
def getState(pos):
	state=grid[pos]
	if state==" ":
		outState=0
	else:
		outState=1
	return outState
def updateScreen(board):
	os.system("cls")
	print(board)
	return
def state(neighbors,currentState):
	newState=0
	if currentState==1:
		if neighbors<2:
			newState=0
		elif neighbors>3:
			newState=0
	if neighbors==3:
		newState=1
	if neighbors==2:
		newState=currentState
	return newState