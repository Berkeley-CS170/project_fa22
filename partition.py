import numpy as np
import utils
# GLOBAL VARS
G = utils.read_input("inputs/small1.in")
V = G.number_of_nodes()

class Partition():
    def __init__(self, assignment):
        """
        assignment [np.array]: entry i corrresponds to vertex i's team number. Team numbers are
        from 1 to k, where k is the number of teams.
        """

        self.assignment = assignment
        self.teams, self.team_sizes = np.unique(self.assignment, return_counts=True)
        k = np.max(self.teams) + 1
        self.b = (self.team_sizes / V) - 1 / k
        self.Cp = utils.cmp_Cp(self.b)
        self.Cw = sum(d for u, v, d in G.edges(data='weight') if assignment[u] == assignment[v])
        self.Ck = utils.cmp_Ck(k)

    def get_cost(self):
       return self.Cp + self.Cw + self.Ck

    def swap_vertices(self, v_i, v_j, new_Cw):
        i_team = self.assignment[v_i]
        j_team = self.assignment[v_j]

        self.assignment[v_i] = j_team
        self.assignment[v_j] = i_team

        self.Cw = new_Cw

    def calc_Cp_after_changing_vertex_team(self, i, j):
        # change a vertex v's team assignment from i to j

        # if num teams doesn't change
        b = self.b
        return np.exp(B_EXP*np.sqrt(np.linalg.norm(b) - b[i]**2 - b[j]**2 \
            + (b[i] - 1/V)**2 + \
                (b[j] + 1/V**2)))

        # TODO: if num team changes


    def calc_Cw_after_changing_vertex_team(self,i,j,v):
        # change a vertex v's team assignment from i to j
        for u in G.neighbors(v):
            if self.assigment[u] == i:
                Cw -= G[u][v]['weight']
            if self.assigment[u] == j:
                Cw += G[u][v]['weight']

    def calc_Cw_after_swapping_vertices(self, v_i, v_j):
        # invariants: v_i and v_j are not on the same team before or after the swap
        Cw = self.Cw

        i_team = self.assignment[v_i]
        j_team = self.assignment[v_j]

        #what if v_i and v_j were neighbors?
        for u in G.neighbors(v_i):
            if self.assignment[u] == i_team:
                # u will no longer be on v_i's team after the swap
                Cw -= G[u][v_i]['weight']
            if (self.assignment[u] == j_team) and (u != v_j):
                # u will be on the same team as v_i after the swap
                Cw += G[u][v_i]['weight']
        
        for u in G.neighbors(v_j):
            if self.assignment[u] == j_team:
                # u will no longer be on v_j's team after the swap
                Cw -= G[u][v_j]['weight']
            if (self.assignment[u] == i_team) and (u != v_i):
                Cw += G[u][v_j]['weight']
        
        return Cw

