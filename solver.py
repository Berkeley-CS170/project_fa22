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
def assignment_array_to_graph(pi):
    '''
    Assigns G's teams from best policy's assignment.
    '''

def solve(G):
    '''
    Assign a team to v with G.nodes[v]['team'] = team_id
    Access the team of v with team_id = G.nodes[v]['team']
    '''
    # random assignment

    for k in feasible_ks:
        # do we assume an order to the nodes? or try to be evenly-spaced
        assignment = range(k) * (V/k)
        ct = 0
        for _ in range(len(next), V):
            assignment.append(ct)
            ct +=1
        init_pi = Parition(assignment)

        