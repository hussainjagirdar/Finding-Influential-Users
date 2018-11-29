####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding only structural and only temporal users
####################################################################


def return_users(filename):
	file1 = open(filename,"r")

	lines = file1.readlines()

	temporal_users = []

	for l in lines:
		temporal_users.append(l.replace("\n",""))

	return temporal_users

def find_difference(list1,list2,n,s):
	file = open("../output/"+s+"_"+str(n),"a+")
	count = 0
	for l in list1[:n]:
		if l not in list2[:n]:
			file.write(l)
			file.write("\n")
	file.close()

temporal = return_users("../ranked_lists/smit_top_any_temporal_std_3_window_0")
structural = return_users("../ranked_lists/K-truss.txt")

for i in range(50,301,50):
	print i,"temporal - structural",
	find_difference(temporal,structural,i,"t-s")
	print i,"structural - temporal",
	find_difference(structural,temporal,i,"s-t")