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
    for i in range(feasible_k):

        #random assignment of teams
        vertices = G.nodes
        random.shuffle(vertices)

        partitions = [Partition() for _ in range(i)]

        curr_team = 0
        for vertex in vertices:
            G.nodes[vertex]['team'] = partitions[curr_team]
            curr_team += 1
            if curr_team == i:
                curr_team = 0
        
        vertices_copy = vertices
        #stimulated annealing
        swaps = {} 
        lowest_cost = #cost of v1 staying in this team
        for v1 in vertices_copy:
            other_vertices = vertices_copy.remove(v1)
            for v2 in other_vertices:
                if G.nodes[v1]['team'] != G.nodes[v2]['team']:


                    #confused what compute_new_partition_cost() does
                    if compute_new_partition_cost() ##cost of this swap < lowest_cost:
                        swaps[v1] = G.nodes[v2]['team']
                        


        
