import random
from partition import Parition
import numpy as np
import utils

G = utils.read_input(...)
V = G.number_of_nodes()

def compute_new_partition_cost(G,pi1, pi2,vertices):
    # TODO: delete this function?

    #will return the cost of pi2 - cost of pi1
    for v in vertices:
        old,new = pi1.assignment[v], pi2.assignment[v]   
        pi1.update_Cp(old,new,v)
        pi2.update_Cw(old,new,v)
        pi1.b[pi1.assignment[v]] -= 1/V
        pi1.b[pi2.assignment[v]] += 1/V
        pi1.assignment[v] = pi2.assignment[v]
        
def assignment_array_to_graph(pi):
    '''
    Assigns G's teams from best policy's assignment.
    '''
    # TODO: delete this function?

def random_team_assignment(num_teams):
    # assigns a team number to every vertex

    vertices = G.nodes()
    random.shuffle(vertices)
    vertex_teams = [-1 for _ in range(len(vertices))]

    curr_team = 0
    for vertex in vertices:
        vertex_teams[vertex] = curr_team
        curr_team = (curr_team + 1) % num_teams
    
    return vertex_teams


def explore_swaps(partition):
    # this function returns the optimal set of swaps
    # note that Cp and Ck are not changed by a swap operation


    #simulated annealing
    suggested_swap = (None, None)
    lowest_Cw = partition.get_Cw()

    #create list of unmarked vertices
    # go through all unmarked pairs -> pick pair with the lagrest gain
    # updated costs internally without swapping, but update costs as if you've done so
    for v1 in G.nodes:
        for v2 in G.nodes:
            if (v1 != v2) and (partition.assignment[v1] != partition.assignment[v2]):
                
                if partition.calc_Cw_after_swapping_vertices(v1, v2) < lowest_Cw:
                    lowest_Cw = partition.get_cost()
                    suggested_swap = (v1, v2)

    return suggested_swap


def solve(G):
    '''
    Assign a team to v with G.nodes[v]['team'] = team_id
    Access the team of v with team_id = G.nodes[v]['team']
    '''
    num_partitions = 3 # number of starting points for each value of k
    partitions = dict()
    current_lowest_cost = float("inf")

    # this loop ends once we've reached a value of k where Ck (a lower bound)
    # is greater than the lowest current cost on record 
    k = 1
    while True:
        partitions[k] = [Partition(assignment=random_team_assignment(k)) for _ in range(num_partitions)]
        for partition in partitions[k]:
            # improve our team assignments for a set amount of time
            
            # suggested_swap = explore_swaps(partition)
            # do post-processing: take swap or not

        k += 1
        if cmp_Ck(k) > current_lowest_cost:
            break
           
    # focus on trimming down our search space

