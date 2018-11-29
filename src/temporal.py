####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding temporal users
####################################################################


import numpy as np
import random

#finds top users for a given n (n * std) and given window_size

def do(s,window):
	for t in time_dict:
		x = time_dict[t][0]
		mean = np.mean(x)	#mean
		std = np.std(x)		#standard deviation
		
		potential =  x[x >= mean + (s * std)]

		#all the user indices which satisfy mean + n * std formula
		indices = np.nonzero(x >= mean + (s * std))

		indices_min = []
		indices_max = []

		#all indices of neighbours
		for i in range(1,window+1):
			indices_min.append(indices[0]-i)
			indices_max.append(indices[0]+i)

		#indices of all potential users
		main_indices = []

		for i in indices_min:
			for j in i:
				if(j>0 and j<len(x) and j not in main_indices):
					main_indices.append(j)

		for i in indices[0]:
			if i not in main_indices:
				main_indices.append(i)

		for i in indices_max:
			for j in i:
				if(j>0 and j<len(x) and j not in main_indices):
					main_indices.append(j)

		#counting retweet count at peak
		for i in sorted(main_indices):
			
			if user_dict[t][i] not in potential_users_only_at_peak:
				potential_users_only_at_peak[user_dict[t][i]] = 1
			else:
				potential_users_only_at_peak[user_dict[t][i]] += 1

	#counting retweet count at any time
	for tw_id in user_dict:
		for u in user_dict[tw_id]:
			if u in potential_users_only_at_peak:
				if(u not in potential_users_any):
					potential_users_any[u] = 1
				else:
					potential_users_any[u] += 1

	# print len(potential_users_any)
	# print len(potential_users_only_at_peak)
	
	#random order of users
	u = potential_users_any.keys()

	shuffled = u
	for shh in range(10):
		shuffled = sorted(shuffled, key=lambda k: random.random())

	top_random = open("../STD "+str(st)+"/top_random_std_"+str(s)+"_window_"+str(window),'a+') 
	
	for ss in shuffled:
		top_random.write(ss)
		top_random.write("\n")

	top_random.close()

	#writing top users at any time
	top_any = sorted(potential_users_any.items(), key=lambda x:x[1],reverse=True)
	top_any_file = open("../STD "+str(st)+"/top_any_temporal_std_"+str(s)+"_window_"+str(window),'a+')

	for t in top_any:
		top_any_file.write(t[0])
		top_any_file.write('\n')

	#writing top users at peak time
	top_at_peak = sorted(potential_users_only_at_peak.items(), key=lambda x:x[1],reverse=True)
	top_at_peak_file = open("../STD "+str(st)+"/top_at_peak_temporal_std_"+str(s)+"_window_"+str(window),'a+')

	for t in top_at_peak:
		top_at_peak_file.write(t[0])
		top_at_peak_file.write('\n')

	top_any_file.close()
	top_at_peak_file.close()

	print "done",s,window

#input files
cascade_time_int = open("../data/cascade-time-int-all.txt")
cascade_user = open("../data/casc-user-id.txt") 

users = cascade_user.readlines()
time_intervals = cascade_time_int.readlines()

#mapping files to dictionaries
time_dict = dict()	#timestamps
user_dict = dict()	#userids

for t in time_intervals:

	timestamps = t.replace("\n",'').split(" ")

	tweet_id = timestamps[0]

	del(timestamps[0])

	if(len(timestamps)<2):
		continue

	x = np.array(timestamps)

	x = x.astype(np.int)

	time_dict[tweet_id] = list()

	time_dict[tweet_id].append(x)

for u in users:

	timestamps = u.replace("\n",'').split(" ")


	tweet_id = timestamps[0]

	del(timestamps[0])

	if(len(timestamps)<2):
		continue
	x = timestamps

	user_dict[tweet_id] = x



#st - standard deviation, win - window size
for st in range(1,5):
	for win in range(4):
		potential_users_only_at_peak = dict()
		potential_users_any = dict()
		do(st,win)
