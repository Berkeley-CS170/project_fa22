# GLOBAL VARS
from partition import Parition
import numpy as np
G
V = G.number_of_nodes()

def compute_new_partition_cost(G,pi1, pi2,vertices):
    for v in vertices:
        old,new = pi1.assignment[v], pi2.assignment[v]   
        pi1.update_Cp(old,new,v)
        pi2.update_Cw(old,new,v)
        pi1.b[pi1.assignment[v]] -= 1/V
        pi1.b[pi2.assignment[v]] += 1/V
        pi1.assignment[v] = pi2.assignment[v]
        #will return the cost of pi2 - cost of pi1
def assignment_array_to_graph(pi):
    '''
    Assigns G's teams from best policy's assignment.
    '''

def solve(G):
    '''
    Assign a team to v with G.nodes[v]['team'] = team_id
    Access the team of v with team_id = G.nodes[v]['team']
    '''
    feasible_k = #upperbound on k
    num_parititons = 1
    for i in range(feasible_k):

        #random assignment of teams
        vertices = G.nodes
        random.shuffle(vertices)

        partitions = [Partition() for _ in range(num_partitions)]
        vertex_teams = [-1 for _ in range(len(vertices))]

        # todo: different assignments for each starting point (paritions)
        # use some random library to assign teams or make helper function to assign teams
        curr_team = 0
        for vertex in vertices:
            vertex_teams[vertex] = curr_team
            curr_team += 1
            if curr_team == i:
                curr_team = 0
        
        vertices_copy = vertices
        #stimulated annealing
        swaps = (None, None)
        lowest_cost = #cost of v1 staying in this team

        # create set of unmarked vertices, while it is not empty -> go through the code below
        # choose unmarked pair of vertices with largest gain

        for v1 in vertices_copy:
            for v2 in vertices_copy:
                if (v1 != v2) and (vertex_teams[v1] != vertex_teams[v2]):
                    #add own cost function without making new partition objects
                    old_assignment = Partition(assignment=[vertex_teams[v1], vertex_teams[v2]])
                    new_assignment = Partition(assignment=[vertex_teams[v2], vertex_teams[v1]])
                    if compute_new_partition_cost(G, old_assignment, new_assignment, [v1, v2]) < lowest_cost:
                        lowest_cost = compute_new_partition_cost(G, old_assignment, new_assignment, [v1, v2])
                        swaps = (v1, v2)
                    else #swap with some probability
        if swaps != (None, None):
            #swap
