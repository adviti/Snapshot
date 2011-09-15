import os
def listSnapshots(extension):
	snaplist=[]
	filelist=os.listdir(os.curdir)
	for item in filelist:
		if item.find(extension) != -1:
			snaplist.append(item)
	return snaplist
#c=listSnapshots(raw_input('Enter the extension of snapshot files'))
#print c
