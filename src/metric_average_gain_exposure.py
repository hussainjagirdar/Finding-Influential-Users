####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding average_gain_exposure
####################################################################

from random import randint
import pickle
import os

data_DIR = "../data/"
output_DIR = "../output/"
followers_dict = pickle.load(open(data_DIR+"followers.p","r"))
users = []
user_cascade_number = {}
user_retweet_influence = {}

def find_top_k_users(k,filename):
	f = open(filename)

	line = f.readline().replace("\n","")

	for i in range(k):
		users.append(line)
		user_cascade_number[line] = 0
		user_retweet_influence[line] = 0.		
		line = f.readline().replace("\n","")
	f.close()

def find_top_k_users_difference(filename):
	f = open(filename)

	line = f.readline().replace("\n","")

	while line:
		users.append(line)
		user_cascade_number[line] = 0
		user_retweet_influence[line] = 0.		
		line = f.readline().replace("\n","")
	f.close()

def average_gain_exposure():
	f = open("../data/casc-user-id.txt")
	c = f.readline()

	while c:
		cascde = c.replace("\n","").split(" ")
		tweet_id = cascde[0]
		us = cascde[1:]
		for u in users:
			if u in us:
				user_cascade_number[u] += 1
				n=len(us)
				k=(us.index(u)+1)
				prevList=us[0:k-1]
				afterList=us[k+1:n]
				uElements=0
				for afterElement in afterList:
					intIndex=0
					for prevElement in prevList:
						if prevElement in followers_dict:
							if afterElement in followers_dict[prevElement]:
								break
							else:
								intIndex+=1
						else:
							intIndex+=1
					if intIndex==len(prevList):
						uElements+=1

				temp = (uElements/(us.index(u)+1))
				user_retweet_influence[u] += temp
		c = f.readline()

	result = 0
	for u in user_cascade_number:
		if user_cascade_number[u] != 0:
			user_retweet_influence[u] = user_retweet_influence[u] / user_cascade_number[u]
		# print u,user_cascade_number[u],user_retweet_influence[u]
		result += user_retweet_influence[u]
	return result/len(user_retweet_influence)
	f.close()

#for temporal users
def temporal():
	top = range(50,301,50)

	# files = ["../output/k_truss.txt"]
	# files = ["../output/degree_cent_score.txt","../output/mcdwe_score.txt","../output/page_rank_cent.txt","../output/brodaCountRank_500","../output/ranked_ktruss"]

	dirs = ['STD 1','STD 2','STD 3','STD 4']

	files = []


	for d in dirs:

		fi = os.listdir("../"+d)
		for f in sorted(fi):
			files.append("../"+d+"/"+f)

	output_file = open("../output/temp_expo.txt","a+")
	output_file.write("All values are of top [50,100,150,200,250,300] users\n\n")
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

		tempList=[]
		for t in top:
			users = []
			user_cascade_number = {}
			user_retweet_influence = {}
			find_top_k_users(t,f_name)
			r = average_gain_exposure()
			tempList.append(round(r,3))
			print t
		print tempList

		output_file.write(str(tempList))
		output_file.write('\n\n')
		# break

	output_file.close()

#for structural users
def structural():
	top = range(50,301,50)
	files = ["../output/newbrodaCountRank_500"]
	# files = ["../output/k_truss.txt"]
	# files = ["../output/degree_cent_score.txt","../output/mcdwe_score.txt","../output/page_rank_cent.txt","../output/brodaCountRank_500","../output/ranked_ktruss"]

	for f_name in files:
		print f_name
		print "=================="


		tempList=[]
		for t in top:
			users = []
			user_cascade_number = {}
			user_retweet_influence = {}
			find_top_k_users(t,f_name)
			r = average_gain_exposure()
			tempList.append(round(r,3))
			print t
		print tempList

def structural_difference():
	# top = range(50,301,50)

	# files = ["../output/s-t_50","../output/s-t_100","../output/s-t_150","../output/s-t_200","../output/s-t_250","../output/s-t_300"]
	files = ["../output/t-s_50","../output/t-s_100","../output/t-s_150","../output/t-s_200","../output/t-s_250","../output/t-s_300"]
	# files = ["../output/degree_cent_score.txt","../output/mcdwe_score.txt","../output/page_rank_cent.txt","../output/brodaCountRank_500","../output/ranked_ktruss"]

	tempList=[]
	for f_name in files:
		print f_name
		print "=================="

		users = []
		user_cascade_number = {}
		user_retweet_influence = {}
		find_top_k_users_difference(f_name)
		r = average_gain_exposure()
		tempList.append(round(r,3))
	print tempList

# temporal()
# structural_difference()
structural()