import os
import pickle
from datetime import datetime

def enlistFiles(base_path):
	list_directory=[]
	list_files=[]
	for roots, dirs, files in os.walk(base_path):
	
		list_directory.append(roots)
		for each_file in files:
			list_files.append(roots+'/'+each_file)
	return (list_files, list_directory)		

def createsnapshot(base_path, output_file):
	p=enlistFiles(base_path)
	try:
		
		output=open(output_file+'.snp', 'wb')
	except IOError:
		print 'Error in opening the file'
		return	
	 
 	#metadata contains date of creation of snapshot and basepath
	metadata=[datetime.utcnow(), base_path]

	pickle.dump(metadata, output, -1)
	pickle.dump(p[1],output, -1)
	pickle.dump(p[0], output, -1)
	
	output.close()
	print 'Snapshot successfully created'
	
	return
	
			
		
	

	

