####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Finding Degree and page rank centrality
####################################################################

import pickle
import networkx as nx
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
		
		#Adding nodes
		self.followers_graph.add_nodes_from(followers_dict.keys())

		#Adding Edges
		for node,edges in followers_dict.items():
			self.followers_graph.add_edges_from(([(node,edge) for edge in edges]))

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

	def find_degree_centrality(self):
		self.deg_cent = nx.degree_centrality(self.followers_graph)

	def find_page_rank_centrality(self):
		self.page_rank_cent = nx.pagerank(self.followers_graph)


	#Stroing result in output folder
	def store_result(self):

		print "Degree Centrality"
		#Degree_centrality
		sorted_x1 = sorted(self.deg_cent.items(), key=operator.itemgetter(1),reverse=True)
		s = 1
		for a in sorted_x1:
			if(s==10):
				break
			print a[0],
			print a[1]
			s += 1

		output_file = open(self.output_DIR+"degree_cent_score.txt","w")

		output_file.write("Node\t\t\tdeg_cent\n")
		output_file.write("======================\n\n")

		for a in sorted_x1:
			output_file.write(str(a[0]))
			output_file.write("\t\t\t")
			output_file.write(str(a[1]))
			output_file.write("\n")	

		output_file.close()

		print "Page rank Centrality"
		#Page_rank_centrality
		sorted_x1 = sorted(self.page_rank_cent.items(), key=operator.itemgetter(1),reverse=True)

		s = 1

		for a in sorted_x1:
			if(s==10):
				break
			print a[0],
			print a[1]
			s += 1
		    
		output_file = open(self.output_DIR+"page_rank_cent_directed.txt","w")

		output_file.write("Node\t\t\tdeg_cent\n")
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

f.find_degree_centrality()

f.find_page_rank_centrality()

f.store_result()



