####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding MCDWE Score on followers network
# Date		: 15 Feb 2018
####################################################################


import pickle
import networkx as nx
import math
import operator

fp = open("../data/casc-user-id.txt", "r")

data = fp.readlines()
fp.close()

activeUsersList = []

for line in data:
	userIdList = line.split(" ")
	for userId in userIdList:
		activeUsersList.append(userId)


print activeUsersList[:10]

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

	#Finding Active network
	def find_active_network(self):
		print "Nodes=", len(self.followers_graph.nodes()), "\tEdges=", len((self.followers_graph).edges())
		for node in list(self.followers_graph.nodes()):
			if not node in activeUsersList:
				#print node
				(self.followers_graph).remove_node(node)
		print "Nodes=", len(self.followers_graph.nodes()), "\tEdges=", len((self.followers_graph).edges())

	def k_truss_decomposition(self, k=3):

		dictNode = {}
		
		while ((self.followers_graph).number_of_edges()) != 0:
			current_number_of_edges = (self.followers_graph).number_of_edges()
			previous_number_of_edges = 0
			
			print k, "\t", current_number_of_edges
			
			while current_number_of_edges != previous_number_of_edges:
				for edge in list((self.followers_graph).edges()):
					
					if len(sorted(nx.common_neighbors(self.followers_graph, edge[0], edge[1])))	< k-2:
						
						##### NODE FROM EDGE AT 0TH INDEX ###############
						if edge[0] in dictNode:
							if dictNode[edge[0]] < k-1:
								dictNode[edge[0]] = k-1
						else:
							dictNode[edge[0]] = k-1


						##### NODE FROM EDGE AT 1st INDEX ###############
						if edge[1] in dictNode:
							if dictNode[edge[1]] < k-1:
								dictNode[edge[1]] = k-1
						else:
							dictNode[edge[1]] = k-1
						
						(self.followers_graph).remove_edge(edge[0], edge[1])
			

				previous_number_of_edges = current_number_of_edges
				current_number_of_edges = (self.followers_graph).number_of_edges()
			
			k += 1

		fp = open("../output/active_k_truss_score", "a+")
		for node in list(dictNode.keys()):
			fp.write(str(node) + "\t" + str(dictNode[node]) + "\n")

		fp.close()


f = Followers_graph()

f.create_followers_network()

f.find_active_network()

f.k_truss_decomposition()