import pickle

class NotSameBasepath(Exception):
	pass
def printpattern(heading,lis):
	print heading
	for each_element in lis:
		print '\t'+each_element
	print


def checkSnapTimeline(time1, time2,file1, file2):
	if time1 > time2 :
		file1, file2 = file2, file1			
		
	return	
		
	
	
def checkIfSameBasepath(basepath1, basepath2):
	print basepath1
	print basepath2
	if basepath1 == basepath2:
		return
	else:
		raise NotSameBasepath

def compareSnapshots(snap1, snap2):
	try:
		file1=open(snap1, 'rb')
		file2=open(snap2, 'rb')
	except IOError:
		print 'Error in opening the files'
		return
	try:	
		metadata1 = pickle.load(file1)
		metadata2= pickle.load(file2)
		print metadata1

		print metadata2
		checkIfSameBasepath(metadata1[1], metadata2[1])
		checkSnapTimeline(metadata1[0], metadata2[0], file1, file2)
		dirs1=pickle.load(file1)
		files1=pickle.load(file1)
		
		
		dirs2=pickle.load(file2)
		files2=pickle.load(file2)
		
	except EOFError: 
		print 'file cant be unpickled, since having different  extension from that of snapshot files' 
		return
	file1.close()
	file2.close()

	added_files=[]
	added_directories=[]
	removed_files= []
	removed_directories =[]
	
	for each_dir in dirs1:
		if each_dir not in dirs2:
			removed_directories.append(each_dir)
	printpattern('removed_directories',removed_directories)
	for each_dir in dirs2:
		if each_dir not in dirs1:
			added_directories.append(each_dir)
	printpattern('added_directories',added_directories)
	
	
	for each_file in files1:
		if each_file not in files2:
			removed_files.append(each_file)
	printpattern('removed_files',removed_files)
	for each_file in files2:
		if each_file not in files1:
			added_files.append(each_file)
	printpattern('added_files',added_files)
	
	
		
