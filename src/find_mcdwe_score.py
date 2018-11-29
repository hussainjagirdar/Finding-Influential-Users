####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding MCDWE Score on followers network
####################################################################

import pickle
import networkx as nx
import math
import operator

class Followers_graph(object):
	"""docstring for Followers_graph"""

	def __init__(self):
		self.data_DIR = "../data/"
		self.output_DIR = "../output/"

	#Creating follwers network from the pickle file
	def create_followers_network(self):
		followers_dict = pickle.load(open(self.data_DIR+"followers.p","r"))
		
		#Creating networkx object
		self.followers_graph = nx.Graph()
		self.backup_graph = nx.Graph()
		
		#Adding nodes
		self.followers_graph.add_nodes_from(followers_dict.keys())
		self.backup_graph.add_nodes_from(followers_dict.keys())

		#Adding Edges
		for node,edges in followers_dict.items():
			self.followers_graph.add_edges_from(([(node,edge) for edge in edges]))
			self.backup_graph.add_edges_from(([(node,edge) for edge in edges]))

	#Removing nodes with zero degrees
	def remove_zero_degree_nodes(self):
		
		while (True):

			#Finding degrees of nodes in the graph
			deg = dict(self.followers_graph.degree())
			count = 0
			
			#Removing nodes with degree 0
			for a in deg.keys():
				if(deg[a] == 0):
					count = count + 1
					self.followers_graph.remove_node(a)

			print count
			if(count==0):
				break

	#Crearing K-cores
	def create_cores(self):

		#Storing each cores and node detainls
		self.cores = {}
		self.node_scores = {}
		self.num_of_cores = 1

		while(True):

			#For undiected graph 436 unknown nodes
			if(len(self.followers_graph)==436): 
				break

			self.cores[self.num_of_cores] = []
			print "core created",
			print self.num_of_cores	

			while (True):

				#Getting degrees of nodes of the graph
				deg = dict(self.followers_graph.degree())
				count = 0

				#Removing nodes of degree on kth core
				for a in deg.keys():
					if(deg[a] == self.num_of_cores):
						count = count + 1
						self.cores[self.num_of_cores].append(a)
						if a not in self.node_scores:
							self.node_scores[a] = {}
						self.node_scores[a]["core"] = self.num_of_cores
						self.node_scores[a]["entropy"] = 0.0
						self.followers_graph.remove_node(a)

				#terminating condition of each core
				if(count==0):
					break

			#Starting new core
			self.num_of_cores = self.num_of_cores + 1

	#finding entropy
	def find_entropy(self):

		#finding friends in each core
		core_friend_counts = {}

		count = 1

		for a in self.node_scores.keys():
			core_friend_counts[a] = {}
			
			if(count%100==0):
				print "nodes calculated",
				print count

			#finding entropy in each core
			for i in range(1,self.num_of_cores):
				
				core_friend_counts[a][i] = 0
				
				for b in self.cores[i]:
					if(self.backup_graph.has_edge(a,b)):
						core_friend_counts[a][i] += 1
				
				#weighted entropy
				if(self.backup_graph.degree(a)!=0 and core_friend_counts[a][i]!=0):
					core_friend_counts[a][i] /= float(self.backup_graph.degree(a))
					temp = core_friend_counts[a][i] * math.log(core_friend_counts[a][i],10)
					temp /= float(self.num_of_cores-i)
					self.node_scores[a]["entropy"] += temp
			count += 1

	#finding MCDWE score
	def find_MCDWE_score(self,alpha,beta,gamma):

		self.final_score = {}

		for a in self.node_scores.keys():
			self.node_scores[a]["entropy"] *= -1

		highest_degree = 0
		highest_entropy = 0

		for a in self.node_scores.keys():
			if(self.node_scores[a]["entropy"] > highest_entropy):
				highest_entropy = self.node_scores[a]["entropy"]

			if(self.backup_graph.degree(a) > highest_degree):
				highest_degree = self.backup_graph.degree(a)

		print highest_degree,highest_entropy

		#Normilizing degree and entropy
		for a in self.node_scores.keys():
			self.final_score[a] = (self.node_scores[a]["entropy"] / highest_entropy * alpha) + (self.node_scores[a]["core"] / float(self.num_of_cores-1) * beta) + (self.backup_graph.degree(a) / float(highest_degree) * gamma)

	#Stroing result in output folder
	def store_result(self):

		sorted_x1 = sorted(self.final_score.items(), key=operator.itemgetter(1),reverse=True)
		
		s = 1

		for a in sorted_x1:
			if(s==100):
				break
			print a[0],
			print a[1]
			s += 1

		output_file = open(self.output_DIR+"mcdwe_score.txt","w")

		output_file.write("Node\t\t\tMCDWE_SCORE\n")
		output_file.write("======================\n\n")

		for a in sorted_x1:
			output_file.write(str(a[0]))
			output_file.write("\t\t\t")
			output_file.write(str(a[1]))
			output_file.write("\n")	
		output_file.close()

f = Followers_graph()

f.create_followers_network()

f.remove_zero_degree_nodes()

f.create_cores()

f.find_entropy()

f.find_MCDWE_score(1,1,1)

f.store_result()