####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding top users using K-truss method (Global network)
# Date		: 15 Feb 2018
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


		#### WRITE K-TRUSS SCORE TO FILE ##########################################
		fp = open("../output/score_k_truss_from_dictionary", "a+")
		for key in dictNode.keys():
			line = str(key) + "\t" + str(dictNode[key]) + "\n"
			fp.write(line)
		fp.close()
	
	def save_graph_as_pickle_file(self):
		nx.write_gpickle(self.followers_graph, "../data/graph_after_ktruss")


f = Followers_graph()

f.create_followers_network()

f.k_truss_decomposition()