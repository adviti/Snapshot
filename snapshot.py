import help
import lssnapsfiles
import createsnapshot
import comparesnapshots

def menu():
	print '''
	DIRECTORY/FILE COMPARISON TOOL
	====================================
	Please type a number and press enter:
	1. Create a snapshot
	2. List snapshot files
	3. Compare snapshots
	4. Help
	5. Exit
	'''
	choice = raw_input('ENter your choice')
 	return choice




choice = ''
while choice != '5':
	choice = menu()
	if choice == '1':
		direc = raw_input('Enter the path to the directory to create a snapshot of')
		out_file = raw_input('Enter the path to the snapshot file')
		createsnapshot.createsnapshot(direc, out_file)
	elif choice == '2':
		ext = raw_input("enter the xtension of the snapshot files which you want to list")
		print lssnapsfiles.listSnapshots(ext)
	elif choice== '3':
		snap1=raw_input('Enter the snapshots to be compared')
		snap2=raw_input('Enter the snapshot to be compared')
		comparesnapshots.compareSnapshots(snap1, snap2)
	elif choice == '4':
		help()
	elif choice == '5':
		print "Bye bye"
		break
	else:
		print 'Invalid choice'	

	
	
