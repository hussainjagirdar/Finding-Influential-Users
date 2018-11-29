####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding multi seed simulation
####################################################################

import pickle
from Queue import Queue
import random
import os


def find_top_k_users(k,filename):
	f = open(filename)

	line = f.readline().replace("\n","")

	for i in range(k):
		users.append(line)
		line = f.readline().replace("\n","")
	f.close()

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
						if(v not in k and v not in kkk):
							k.append(v)
					else:
						kkk.append(v)

users = []

data_DIR = "../data/"
followers_dict = pickle.load(open(data_DIR+"followers.p","r"))

def temporal():
	top = range(50,301,50)

	dirs = ['STD 1','STD 2','STD 3','STD 4']

	files = []

	for d in dirs:

		fi = os.listdir("../"+d)
		for f in sorted(fi):
			files.append("../"+d+"/"+f)
			
	output_file = open("../output/temp_multi.txt","a+")
	output_file.write("All values are of top [50,100,150,200,250,300] users\n\n")


	# files = ["../output/k_truss.txt"]
	# files = ["../output/brodaCountRank_500"]
	# files = ["../output/degree_cent_score.txt","../output/mcdwe_score.txt","../output/page_rank_cent.txt","../output/k_truss.txt","../output/brodaCountRank_500"]

	for f_name in files:
		print f_name
		print "=================="

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

		results = []
		for t in top:
			users = []
			k = []
			kkk = []

			find_top_k_users(t,f_name)
			temp = 0
			for u in users:
				bfs_with_probability(u,0.2)
			results.append(len(k))
			print t
		print results
		output_file.write(str(results))
		output_file.write('\n\n')

def structural():
	top = range(50,301,50)
	files = []

	for f_name in files:
		print f_name
		print "=================="

		results = []
		for t in top:
			users = []
			k = []
			kkk = []

			find_top_k_users(t,f_name)
			temp = 0
			for u in users:
				bfs_with_probability(u,0.2)
			results.append(len(k))
			print t
		print results

temporal()