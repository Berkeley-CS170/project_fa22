import random
from partition import Partition

# GLOBAL VARS
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
def random_team_assignment(num_teams):
    vertex_teams = [-1 for _ in range(len(vertices))]

    curr_team = 0
    vertices = G.nodes
    random.shuffle(vertices)

    for vertex in vertices:
        vertex_teams[vertex] = curr_team
        curr_team = (curr_team + 1) % num_teams
    
    return vertex_teams


def explore_swaps(partition):
    #simulated annealing
    suggested_swap = (None, None)
    lowest_Cw = partition.get_Cw()

    #create list of unmarked vertices
    # go through all unmarked pairs -> pick pair with the lagrest gain
    # updated costs internally without swapping, but update costs as if you've done so

    # might have to create a new function that calculates C_w outside of partition

    for v1 in G.nodes:
        for v2 in G.nodes:
            if (v1 != v2) and (partition.assignment[v1] != partition.assignment[v2]):
                # note that Cp and Ck are not changed by this operation
                if partition.calc_Cw_after_swapping_vertices(v1, v2) < lowest_Cw:
                    lowest_Cw = partition.get_cost()
                    suggested_swap = (v1, v2)

    return suggested_swap


def solve(G):
    '''
    Assign a team to v with G.nodes[v]['team'] = team_id
    Access the team of v with team_id = G.nodes[v]['team']
    '''
    feasible_k = #upperbound on k
    num_partitions = 3
    for k in range(feasible_k):
        # multiple starting points where there are k teams
        partitions = [Partition(assignment=random_team_assignment(k)) for _ in range(num_partitions)]

        for partition in partitions:
            suggested_swap = explore_swaps(partition)
            #do post-processing: take swap or not