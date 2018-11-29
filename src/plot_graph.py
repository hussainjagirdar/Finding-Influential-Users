####################################################################
# Authors	: Hussain Jagirdar
#			  Nikhil Agarval
#		 	  Shah Smit Ketankumar
# Aim		: Ploting graph
####################################################################


import matplotlib.pyplot as plt

def average_relative_gain():

	a = [50,100,150,200,250,300]

	#Degree
	# b1 = [1.40709043888,1.24913448117,1.23670383629,1.46806247015,1.3738258997,1.37998768836,]

	#MCDWE
	# b2 = [1.33566196972,1.36889274457,1.63836472523,1.76505583065,1.92819599386,1.82742195493]

	#Page Rank
	# b3 = [1.07658312196,1.2290898623,1.07537260001,1.1301583576,1.32338188047,1.21631219562]

	#K-truss
	b4 = [2.516853656646678, 2.1220352432849214, 2.423175328872327, 2.269124323188423, 2.345708041003448, 2.3200127641455954]

	#broda-count
	# b5 = [1.5545904388777374, 1.5345357246333011, 1.524526655744268, 1.4530047603688268, 1.4559958047142543, 1.6956967894550936]
	
	#temporal count only at peak (window=0)
	# b6 = [1.5569075710299511, 1.2962805071370536, 1.23423407205643, 6.213794679451415, 5.33200954348667, 4.677855226670704]

	#temporal global (window=0)	 
	b7 = [1.779, 2.144, 8.023, 6.97, 6.97, 6.97]

	#s-t
	b8 = [2.533, 2.122, 2.431, 2.272, 2.349, 2.321]

	#t-s
	b9 = [1.765, 2.144, 8.097, 7.061, 7.06, 7.051]


	# x1, = plt.plot(a,b1,label='Degree Centrality')
	# x2, = plt.plot(a,b2,label='MCDWE Score')
	# x3, = plt.plot(a,b3,label='Page rank Centrality')
	x4, = plt.plot(a,b4,label='K-truss')
	# x5, = plt.plot(a,b5,label='Broda Count')
	# x6, = plt.plot(a,b6,label='temporal count only at peak (window=0)')
	x7, = plt.plot(a,b7,label='Temporal')
	x8, = plt.plot(a,b8,label='Only Structural')
	x9, = plt.plot(a,b9,label='Only Temporal')
	# plt.legend(handles=[x1, x2, x3, x4, x5, x6, x7])
	plt.legend(handles=[x4, x7, x8, x9])
	plt.ylabel('Average Relative Gain')
	plt.xlabel('Top Users')
	plt.show()

def cascade_by_average_gain():

	a = [50,100,150,200,250,300]

	#Degree
	b1 = [0.002184564401522425, 0.0014102380876400617, 0.001308187781386423, 0.0014277968127558412, 0.0012993104234658194, 0.001270841043762675]

	#MCDWE
	b2 = [0.0009097253184957719, 0.001302284974359116, 0.001092701838614478, 0.001272281479611573, 0.0013109463666306892, 0.0012550152097985474]

	#Page Rank
	b3 = [0.000864510859899581, 0.0013637481693476003, 0.0012213618491848058, 0.001208806387167788, 0.0012950782139515336, 0.0011567234242176678]

	#K-truss
	b4 = [0.0018784162304488457, 0.0014670728664412367, 0.0016259239776494428, 0.0016543163452366397, 0.001757115765127631, 0.0017716362961668149]

	#broda-count
	b5 = [0.002287531242709162, 0.0017503844707453852, 0.0015266749773156902, 0.0013595290237875231, 0.0012956729805312197, 0.0014813497414033249]
	x1, = plt.plot(a,b1,label='Degree Centrality')
	x2, = plt.plot(a,b2,label='MCDWE Score')
	x3, = plt.plot(a,b3,label='Page rank Centrality')
	x4, = plt.plot(a,b4,label='K-truss')
	x5, = plt.plot(a,b5,label='Broda Count')
	plt.legend(handles=[x1, x2, x3, x4, x5])
	plt.ylabel('Impact on final cascade size by Average gain')
	plt.xlabel('Top Users')
	plt.show()

def cascade_by_average_exposure():

	a = [50,100,150,200,250,300]

	#Degree
	b1 = [0.0015287958115183244, 0.0009336823734729495, 0.0008214077952297847, 0.0008132635253054099, 0.0007064572425828971, 0.0006771378708551484]

	#MCDWE
	b2 = [0.0006178010471204189, 0.0008673647469458986, 0.0007062245491564861, 0.0007670157068062827, 0.0007727748691099479, 0.0006992437463641655]

	#Page Rank
	b3 = [0.0005828970331588133, 0.0009179755671902269, 0.000777196044211751, 0.0006849912739965094, 0.0006966841186736474, 0.0006061663757998837]

	#K-truss
	b4 = [0.0010959860383944154, 0.000844677137870855, 0.000949389179755672, 0.0009554973821989533, 0.0010045375218150087, 0.000980802792321117]

	#broda-count
	b5 = [0.001609075043630017, 0.0010471204188481674, 0.0008923792902850495, 0.0007652705061082024, 0.0006848167539267017, 0.0007725421756835371]

	x1, = plt.plot(a,b1,label='Degree Centrality')
	x2, = plt.plot(a,b2,label='MCDWE Score')
	x3, = plt.plot(a,b3,label='Page rank Centrality')
	x4, = plt.plot(a,b4,label='K-truss')
	x5, = plt.plot(a,b5,label='Broda Count')
	plt.legend(handles=[x1, x2, x3, x4, x5])
	plt.ylabel('Impact on final cascade size by Average exposure')
	plt.xlabel('Top Users')
	plt.show()

def single_seed_simulation():

	a = [50,100,150,200,250,300]

	#Degree
	# b1 = [2.5429268397465483, 2.8388029214520873, 2.986774340424451, 3.0665115347541296, 3.0538457562972785, 3.150310278596625]
	# b1 = [1830.68, 1833.74, 1830.5733333333333, 1804.795, 1772.732, 1759.3866666666668]

	#MCDWE
	# b2 = [1.8679718901161206, 1.5436658007687314, 1.547203318976114, 1.613597471547554, 1.7085589757975281, 1.849983490160718]
	# b2 = [1391.44, 1090.22, 962.06, 948.015, 989.12, 973.0066666666667]

	#Page Rank
	# b3 = [2.5463484721462026, 2.7977063350089084, 2.9833656582098294, 3.109098278472518, 3.12138192872144, 3.1968967519749447]
	# b3 = [1895.18, 1852.54, 1825.4733333333334, 1810.515, 1799.204, 1767.5166666666667]

	#k-truss
	# b4 = [2.9606468146060623, 2.8282414513650918, 2.82994618482713, 2.8132824284439, 2.7065364088769948, 2.736665440466802]
	b4 = [1542.36, 1540.98, 1587.9066666666668, 1519.78, 1443.568, 1421.63]

	#broda
	# b5 = [2.590342245045404, 2.6794224796937494, 2.757137130347925, 2.866221911610778, 2.883389439168013, 3.005639932804901]
	# b5 = [1814.84, 1711.64, 1650.1733333333334, 1611.93, 1594.212, 1557.8333333333333]

	#s-t
	b6 = [1613, 1581, 1586, 1547, 1438, 1412]

	#t-s
	b7 = [1073, 591, 366, 369, 440, 383]

	#temporal
	b8 = [1010, 627, 407, 351, 275, 235]
	
	# x1, = plt.plot(a,b1,label='Degree Centrality')
	# x2, = plt.plot(a,b2,label='MCDWE Score')
	# x3, = plt.plot(a,b3,label='Page rank Centrality')
	x4, = plt.plot(a,b4,label='K-truss')
	# x5, = plt.plot(a,b5,label='Broda Count')
	x6, = plt.plot(a,b6,label='Only Structural')
	x7, = plt.plot(a,b7,label='Only Temporal')
	x8, = plt.plot(a,b8,label='Temporal')
	# plt.legend(handles=[x1, x2, x3, x4, x5])
	plt.legend(handles=[x4, x6, x7, x8])
	plt.ylabel('Single Seed Simulation')
	plt.xlabel('Top Users')
	plt.show()

def multi_seed_simulation():

	a = [50,100,150,200,250,300]

	#Degree
	# b1 = [2.5429268397465483, 2.8388029214520873, 2.986774340424451, 3.0665115347541296, 3.0538457562972785, 3.150310278596625]
	b1 = [2719, 2735, 2747, 2750, 2756, 2759]

	#MCDWE
	# b2 = [1.8679718901161206, 1.5436658007687314, 1.547203318976114, 1.613597471547554, 1.7085589757975281, 1.849983490160718]
	b2 = [2675, 2685, 2685, 2685, 2685, 2685]

	#Page Rank
	# b3 = [2.5463484721462026, 2.7977063350089084, 2.9833656582098294, 3.109098278472518, 3.12138192872144, 3.1968967519749447]
	b3 = [2759, 2779, 2787, 2795, 2798, 2802]

	#k-truss
	# b4 = [2.9606468146060623, 2.8282414513650918, 2.82994618482713, 2.8132824284439, 2.7065364088769948, 2.736665440466802]
	b4 = [2559, 2578, 2581, 2593, 2598, 2599]

	#broda
	# b5 = [2.590342245045404, 2.6794224796937494, 2.757137130347925, 2.866221911610778, 2.883389439168013, 3.005639932804901]
	b5 = [2645, 2658, 2666, 2672, 2677, 2679]


	x1, = plt.plot(a,b1,label='Degree Centrality')
	x2, = plt.plot(a,b2,label='MCDWE Score')
	x3, = plt.plot(a,b3,label='Page rank Centrality')
	x4, = plt.plot(a,b4,label='K-truss')
	x5, = plt.plot(a,b5,label='Broda Count')
	plt.legend(handles=[x1, x2, x3, x4, x5])
	plt.ylabel('Multi Seed Simulation')
	plt.xlabel('Top Users')
	plt.show()

def average_gain_based_on_exposure():

	a = [50,100,150,200,250,300]

	#Degree
	# b1 = [0.9921172248803828, 0.8932490886306675, 0.8441660590871116, 0.9373690662851181, 0.8507962801055919, 0.826271014862108]

	#MCDWE
	# b2 = [0.9555263157894737, 0.9028919457735247, 1.1085668527379051, 1.194348982920207, 1.3356073813295781, 1.2168104116622425]

	#Page Rank
	# b3 = [0.7555263157894737, 0.8839157552973341, 0.7148605035315563, 0.6920860827768722, 0.814258551167863, 0.7270011735922668]

	#k-truss
	b4 = [1.5635604395604394, 1.4076683776749568, 1.688672385136541, 1.5408753205984376, 1.5836057813886233, 1.5125671821905649]
	
	#broda count
	# b5 = [1.1071172248803827, 0.9809157552973342, 0.9840611591561246, 0.9009908611569127, 0.854641173774015, 1.0486814244298068]
	
	#temporal count only at peak (window=0)
	b6 = [0.544, 1.171, 7.314, 6.342, 6.342, 6.342]

	#temporal global (window=0)	 
	# b7 = [0.6074451149337637, 0.883025407394732, 1.1487947160409322, 1.1334293703640324, 0.9207434962912261, 4.060619580242686]

	#s-t
	b8 = [1.578, 1.412, 1.705, 1.551, 1.592, 1.516]

	#t-s
	b9 = [0.516, 1.17, 7.396, 6.439, 6.438, 6.432]

	# x1, = plt.plot(a,b1,label='Degree Centrality')
	# x2, = plt.plot(a,b2,label='MCDWE Score')
	# x3, = plt.plot(a,b3,label='Page rank Centrality')
	x4, = plt.plot(a,b4,label='K-truss')
	# x5, = plt.plot(a,b5,label='Broda Count')
	x6, = plt.plot(a,b6,label='Temporal')
	# x7, = plt.plot(a,b7,label='temporal global (window=0)')
	x8, = plt.plot(a,b8,label='Only Structural')
	x9, = plt.plot(a,b9,label='Only Temporal')
	# plt.legend(handles=[x1, x2, x3, x4, x5, x6, x7])
	plt.legend(handles=[x4, x6, x8, x9])
	plt.ylabel('Average Gain Based on exeposure')
	plt.xlabel('Top Users')
	plt.show()

def overlap():

	a = [50,100,150,200,250,300]

	#Degree Centrality Page Rank
	b1 = [0.92,0.9,0.933333333333,0.895,0.912,0.893333333333]

	#DegreCent k_truss
	b2 = [0.22,0.34,0.466666666667,0.505,0.516,0.52]

	#DegreCent Broda
	b3 = [0.92,0.76,0.733333333333,0.72,0.736,0.73]

	#PageRank K_truss
	b4 = [0.2,0.29,0.426666666667,0.435,0.46,0.46]
	
	#PageRank Broda
	b5 = [0.86,0.73,0.706666666667,0.68,0.688,0.68]
	
	#K-truss Broda
	b6 = [0.22,0.4,0.513333333333,0.525,0.536,0.543333333333]
	
	#deg-mcdwe
	b7 = [0.76, 0.57, 0.486666666667, 0.455, 0.428, 0.436666666667]
	
	#page-mcdwe
	b8 = [0.74, 0.54, 0.46, 0.43, 0.404, 0.41]

	#k_truss-mcdwe
	b9 = [0.2, 0.27, 0.406666666667, 0.445, 0.484, 0.5]

	#broda-mcdwe
	b10 = [0.76, 0.58, 0.546666666667, 0.555, 0.56, 0.593333333333]

	#all
	b11 =[0.2, 0.25, 0.32, 0.32, 0.312, 0.323333333333]
	x1, = plt.plot(a,b1,label='Degree Centrality - Page Rank')
	x2, = plt.plot(a,b2,label='Degre Centrality -  k_truss')
	x3, = plt.plot(a,b3,label='DegreCent Broda')
	x4, = plt.plot(a,b4,label='PageRank K_truss')
	x5, = plt.plot(a,b5,label='PageRank Broda')
	x6, = plt.plot(a,b6,label='K-truss Broda')
	x7, = plt.plot(a,b7,label='deg-mcdwe')
	x8, = plt.plot(a,b8,label='page-mcdwe')
	x9, = plt.plot(a,b9,label='k_truss-mcdwe')
	x10, = plt.plot(a,b10,label='broda-mcdwe')
	# x11, = plt.plot(a,b11,label='all')
	plt.legend(handles=[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10])
	plt.ylabel('Average Gain Based on exeposure')
	plt.xlabel('Top Users')
	plt.show()

#relative gain at any
def temporal():
	a = [50,100,150,200,250,300]

	#STD 1
	b1 = [2.635, 2.52, 2.481, 2.478, 2.509, 2.511]

	#STD 2
	b2 = [1.981, 2.168, 2.329, 2.233, 1.877, 4.928]

	#STD 3
	b3 = [1.779, 2.144, 8.023, 6.97, 6.97, 6.97]

	#STD 4
	b4 = [1.996, 2.099, 2.064, 1.81, 2.474, 7.104]

	x1, = plt.plot(a,b1,label='STD DEV 1')
	x2, = plt.plot(a,b2,label='STD DEV 2')
	x3, = plt.plot(a,b3,label='STD DEV 3')
	x4, = plt.plot(a,b4,label='STD DEV 4')

	plt.legend(handles=[x1, x2, x3, x4])
	plt.ylabel('Average Relative Gain Temporal')
	plt.xlabel('Top Users')
	plt.show()

#gain expo at any
def temporal1():
	a = [50,100,150,200,250,300]

	#STD 1
	b1 = [1.052, 0.973, 0.952, 1.008, 1.06, 1.094]

	#STD 2
	b2 = [0.607, 0.883, 1.149, 1.133, 0.921, 4.061]

	#STD 3
	b3 = [0.544, 1.171, 7.314, 6.342, 6.342, 6.342]

	#STD 4
	b4 = [1.097, 3.101, 2.223, 1.739, 1.459, 4.02]

	x1, = plt.plot(a,b1,label='STD DEV 1')
	x2, = plt.plot(a,b2,label='STD DEV 2')
	x3, = plt.plot(a,b3,label='STD DEV 3')
	x4, = plt.plot(a,b4,label='STD DEV 4')

	plt.legend(handles=[x1, x2, x3, x4])
	plt.ylabel('Average Gain Exposure Temporal')
	plt.xlabel('Top Users')
	plt.show()

#relative gain at peak
def temporal2():
	a = [50,100,150,200,250,300]

	#STD 1
	b1 = [1.895, 1.968, 1.94, 2.04, 1.997, 1.958]

	#STD 2
	b2 = [1.557, 1.296, 1.234, 6.214, 5.332, 4.678]

	#STD 3
	b3 = [1.011, 10.686, 7.902, 6.97, 6.97, 6.97]

	#STD 4
	b4 = [1.633, 3.624, 2.718, 2.245, 1.977, 4.564]

	x1, = plt.plot(a,b1,label='STD DEV 1')
	x2, = plt.plot(a,b2,label='STD DEV 2')
	x3, = plt.plot(a,b3,label='STD DEV 3')
	x4, = plt.plot(a,b4,label='STD DEV 4')

	plt.legend(handles=[x1, x2, x3, x4])
	plt.ylabel('Average Relative Gain Temporal')
	plt.xlabel('Top Users')
	plt.show()

#gain expo at peak
def temporal3():
	a = [50,100,150,200,250,300]

	#STD 1
	b1 = [0.363, 0.468, 0.523, 0.653, 0.636, 0.61]

	#STD 2
	b2 = [0.557, 0.491, 0.489, 5.453, 4.56, 3.933]

	#STD 3
	b3 = [0.344, 10.072, 7.263, 6.342, 6.342, 6.342]

	#STD 4
	b4 = [1.097, 3.101, 2.223, 1.739, 1.459, 4.02]

	x1, = plt.plot(a,b1,label='STD DEV 1')
	x2, = plt.plot(a,b2,label='STD DEV 2')
	x3, = plt.plot(a,b3,label='STD DEV 3')
	x4, = plt.plot(a,b4,label='STD DEV 4')

	plt.legend(handles=[x1, x2, x3, x4])
	plt.ylabel('Average Gain Exposure Temporal')
	plt.xlabel('Top Users')
	plt.show()

def compare():
	a = [50,100,150,200,250,300]

	#K-truss Average gain
	b1 = [2.516853656646678, 2.1220352432849214, 2.423175328872327, 2.269124323188423, 2.345708041003448, 2.3200127641455954]

	#K-truss Exposure
	b2 = [1.5635604395604394, 1.4076683776749568, 1.688672385136541, 1.5408753205984376, 1.5836057813886233, 1.5125671821905649]

	#K-truss Single seed
	b3 = [1542.36, 1540.98, 1587.9066666666668, 1519.78, 1443.568, 1421.63]

	#Borda Average gain
	b4 = [1.244, 1.647, 1.661, 1.666, 1.66, 1.66]

	#Borda Exposure
	b5 = [0.773, 1.066, 1.037, 1.004, 0.995, 0.995]

	#Borda Single Seed
	b6 = [1801, 1727, 1701, 1701, 1360, 1141]

	# x1, = plt.plot(a,b1,label='K-truss Relative gain')
	# x2, = plt.plot(a,b2,label='K-truss Exposure')
	x3, = plt.plot(a,b3,label='K-truss Single seed')
	# x4, = plt.plot(a,b4,label='Borda Relative gain')
	# x5, = plt.plot(a,b5,label='Borda Exposure')
	x6, = plt.plot(a,b6,label='Borda Single seed')

	# plt.legend(handles=[x1, x2, x3, x4, x5,x6])
	plt.legend(handles=[x3, x6])
	plt.ylabel('Average Relative Gain Temporal')
	plt.xlabel('Top Users')
	plt.show()

# average_relative_gain()
# single_seed_simulation()
# average_gain_based_on_exposure()
# cascade_by_average_gain()
# cascade_by_average_exposure()
# overlap()
# multi_seed_simulation()
# temporal()
# temporal1()
# temporal2()
# temporal3()
compare()