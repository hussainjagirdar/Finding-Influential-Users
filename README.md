Directory Structure:

================================================================================
data folder:
- cascade-time-int-all.txt
- casc-user-id.txt
- followers.p

================================================================================
STD folders:
- top users at peak time [eg. top_at_peak_temporal_std_1_window_0]
- top users at any time [eg. top_any_temporal_std_1_window_0]
- top users in random order [eg. top_random_std_1_window_0]

================================================================================
output folder:
- Average gain exposure (structural and temporal)
- Average relative gain (structural and temporal)
- Single seed simulation (structural and temporal)
- borda with k-truss (ranked list [k-truss, page rank, MCDWE])
- s-t ranked lists
- t-s ranked lists

================================================================================
ranked_lists folder:

- contains ranked top users

================================================================================
graphs folder:

- contains all the graphs

================================================================================
src folder:

1. find_k_truss_decomposition_on_active_network.py
- finds active network
- implemented k-truss on active network
- output in active_k_truss_score file in output folder

2. find_k_truss_decomposition_on_global_network.py
- implemented k-truss on global network
- output in score_k_truss_from_dictionary file in output folder

3. find_mcdwe_score.py
- implemented mcdwe method on global network
- output in mcdwe_score.txt file in output folder (node - value pair)

4. find_page-rank_and_degree-centrality.py
- implemented page rank and degree centrality on global network
- output in page_rank_cent_directed.txt and degree_cent_score.txt file in output folder (node - value pair)

5. find_t-s.py
- Finds only temporal and only structural users
- output in output folder (s-t_[number of top users] and t-s_[number of top users] files)

6. metric_average_gain_exposure.py
- metric implemented from the main.pdf paper
- three functions (temporal, structural,structural_difference)
- for temporal users, files from [STD 1, STD 2, STD 3, STD 4] folders are used (ranked lists)
- temporal output in temp_expo.txt file in output folder.
- for structural all structural ranked lists ranked_lists folder is used.
- same for only structural and only temporal users.

7. metric_average_relative_gain.py
- metric implemented from the main.pdf paper
- three functions (temporal, structural,structural_difference)
- for temporal users, files from [STD 1, STD 2, STD 3, STD 4] folders are used (ranked lists)
- temporal output in temp_expo.txt file in output folder.
- for structural all structural ranked lists ranked_lists folder is used.
- same for only structural and only temporal users.

8. metric_multi_seed.py
- metric implemented from the main.pdf paper
- two functions (temporal, structural)
- for temporal users, files from [STD 1, STD 2, STD 3, STD 4] folders are used (ranked lists)
- temporal output in temp_expo.txt file in output folder.
- for structural all structural ranked lists ranked_lists folder is used.

9. metric_single_seed_simulation.py
- metric implemented from the main.pdf paper
- three functions (temporal, structural,structural_difference)
- for temporal users, files from [STD 1, STD 2, STD 3, STD 4] folders are used (ranked lists)
- temporal output in temp_expo.txt file in output folder.
- for structural all structural ranked lists ranked_lists folder is used.
- same for only structural and only temporal users.

10. plot_graph.py
- all the values are calculated from the above files.
- x - axis (top users [50,100,150,200,250,300]) 
- y - axis (metric values)

11. temporal.py
- temporal users 
- output in STD [sta dev num] folders