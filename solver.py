import random
from partition import Partition
import numpy as np
import utils

G = utils.read_input("inputs/small1.in")

def random_team_assignment(num_teams):
    # assigns a team number to every vertex

    vertices = list(G.nodes())
    random.shuffle(vertices)
    vertex_teams = [-1 for _ in range(len(vertices))]

    curr_team = 0
    for vertex in vertices:
        vertex_teams[vertex] = curr_team
        curr_team = (curr_team + 1) % num_teams
    
    return vertex_teams


def explore_swaps(partition):
    # this function returns the optimal swap to take
    # note that Cp and Ck are not changed by a swap operation

    suggested_swap = (None, None)
    lowest_Cw = partition.Cw
    for v1 in list(G.nodes):
        for v2 in list(G.nodes):
            if (v1 < v2) and (partition.assignment[v1] != partition.assignment[v2]):
                updated_Cw = partition.calc_Cw_after_swapping_vertices(v1, v2)
                if updated_Cw < lowest_Cw:
                    suggested_swap = (v1, v2)
                    lowest_Cw = updated_Cw
                    
    return suggested_swap, lowest_Cw


def solve():
    '''
    Assign a team to v with G.nodes[v]['team'] = team_id
    Access the team of v with team_id = G.nodes[v]['team']
    '''
    print("starting")
    num_partitions = 3 # number of starting points for each value of k
    partitions = dict()
    current_lowest_cost = float("inf")

    # this loop ends once we've reached a value of k where Ck (a lower bound)
    # is greater than the lowest current cost on record 
    k = 1
    while True:
        print(k, utils.cmp_Ck(k), current_lowest_cost)
        partitions[k] = [Partition(assignment=random_team_assignment(k)) for _ in range(num_partitions)]
        for partition in partitions[k]:
            # improve our team assignments for a set amount of time
            for counter in range(15):
                suggested_swap, new_Cw = explore_swaps(partition)
                if suggested_swap == (None, None):
                    break
                partition.swap_vertices(*suggested_swap, new_Cw)

                if counter % 3 == 0:
                    print("step")

            if partition.get_cost() < current_lowest_cost:
                current_lowest_cost = partition.get_cost()

            # TODO: where do we add randomness?
            # do post-processing: take swap or not

        k += 1
        if utils.cmp_Ck(k) > current_lowest_cost:
            break
           
    # now, we have a set range for k
    # focus on trimming down our search space

if __name__ == "__main__":
    solve()