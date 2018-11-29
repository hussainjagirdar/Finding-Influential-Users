####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding single seed simulation
####################################################################

import pickle
from Queue import Queue
import random
import os

users = []
data_DIR = "../data/"
followers_dict = pickle.load(open(data_DIR+"followers.p","r"))

def find_top_k_users(k,filename):
	f = open(filename)

	line = f.readline().replace("\n","")
	u = []
	for i in range(k):
		u.append(line)
		line = f.readline().replace("\n","")
	f.close()
	return u

def find_top_k_users_difference(filename):
	f = open(filename)

	line = f.readline().replace("\n","")
	uu = []
	while line:
		uu.append(line)	
		line = f.readline().replace("\n","")
	f.close()
	return uu

def bfs_with_probability(u,prob):
	mark = {}
	infect = Queue()
	time = {}
	for a in followers_dict:
		mark[a] = 0
		for b in followers_dict[a]:
			mark[b] = 0
	infect.put(u)

	#marking source infected
	mark[u] = 1

	#setting time to 0 of source
	time[u] = 0
	k = 1
	while(not infect.empty()):
		
		uu = infect.get()
		parent = uu
		flag = False
		if(uu in followers_dict):
			for v in followers_dict[uu]:
				if(mark[v] == 0):
					mark[v] = 1
					if(random.random() < 0.2):
						time[v] = time[parent] + 1
						flag = True
						infect.put(v)
						k += 1
	return k
	


def temporal():

	top = range(50,301,50)

	dirs = ['STD 1','STD 2','STD 3','STD 4']

	files = []

	for d in dirs:

		fi = os.listdir("../"+d)
		for f in sorted(fi):
			files.append("../"+d+"/"+f)
			
	output_file = open("../output/temp_single.txt","a+")
	output_file.write("All values are of top [50,100,150,200,250,300] users\n\n")

	for f_name in files:
		print f_name
		print "=================="
		results = []

		s_std = ''
		s_win = ''
		s_name = ''

		if("std_1" in f_name):
			s_std = "Standard Deviation 1"
		elif ("std_2" in f_name):
			s_std = "Standard Deviation 2"
		elif ("std_3" in f_name):
			s_std = "Standard Deviation 3"
		elif ("std_4" in f_name):
			s_std = "Standard Deviation 4"

		if("window_0" in f_name):
			s_win = "Window size 0"
		elif ("window_1" in f_name):
			s_win = "Window size 1"
		elif ("window_2" in f_name):
			s_win = "Window size 2"
		elif ("window_3" in f_name):
			s_win = "Window size 3"

		if("random" in f_name):
			s_name = "Ranking: Random"

		elif("any" in f_name):
			s_name = "Ranking: Count at any given point"

		elif("at" in f_name):
			s_name = "Ranking: Count at only peak time"

		# print s_std,s_name,s_win
		output_file.write(s_std+"\n")
		output_file.write(s_win+"\n")
		output_file.write(s_name+"\n")

		for t in top:
			users = []

			find_top_k_users(t,f_name)

			temp = 0
			for u in users: 
				temp += bfs_with_probability(u,0.2)

			results.append(temp/t)
			print t
		print results
		output_file.write(str(results))
		output_file.write('\n\n')

def structural():

	top = range(50,301,50)

	files = ["../output/newbrodaCountRank_500"]

	for f_name in files:
		print f_name
		print "=================="
		results = []
		for t in top:
			users = []

			users = find_top_k_users(t,f_name)

			temp = 0
			for u in users: 
				temp += bfs_with_probability(u,0.2)

			results.append(temp/t)
			print t
		print results

def structural_difference():


	# files = ["../output/s-t_50","../output/s-t_100","../output/s-t_150","../output/s-t_200","../output/s-t_250","../output/s-t_300"]
	files = ["../output/t-s_50","../output/t-s_100","../output/t-s_150","../output/t-s_200","../output/t-s_250","../output/t-s_300"]
	# files = []

	results = []
	for f_name in files:
		print f_name
		print "=================="

		users = []
		users = find_top_k_users_difference(f_name)
		print (len(users))
		temp = 0
		for u in users: 
			temp += bfs_with_probability(u,0.2)
		results.append(temp/len(users))
	print results

	# for f_name in files:
	# 	print f_name
	# 	print "=================="
	# 	for t in top:
	# 		users = []

	# 		find_top_k_users(t,f_name)

	# 		temp = 0
	# 		for u in users: 
	# 			temp += bfs_with_probability(u,0.2)

	# 		results.append(temp/t)
	# 		print t
	# 	print results

# temporal()
# structural_difference()
structural()