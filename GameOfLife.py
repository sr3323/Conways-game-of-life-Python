import gOL
gOL.readTxt()
empty=True
gOL.updateScreen(gOL.makeGrid())
while empty==True:
	inputCheck=raw_input('press or hold enter for next state')
	if not inputCheck.strip("/n")=="":
		empty=False
	else:
		gOL.chkAll()