import numpy as np
from utils import *
# GLOBAL VARS
G
V = G.number_of_nodes()

class Partition():
    def __init__(self, assignment):
        """
        assignment [np.array]: entry i corrresponds to vertex i's team number. Team numbers are
        from 1 to k, where k is the number of teams.
        """

        self.assignment = assignment
        self.teams, self.team_sizes = np.unique(self.output, return_counts=True)
        k = np.max(self.teams)
        self.b = (self.team_sizes / V) - 1 / k
        self.Cp = math.exp(B_EXP * np.linalg.norm(self.b))
        self.C_w = sum(d for u, v, d in G.edges(data='weight') if assignment[u] == assignment[v])
    
    def get_Cw(self):
        return self.Cw

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
        Cw = self.C_w

        i = self.assignment[v_i]
        j = self.assignment[v_j]

        #what if v_i and v_j were neighbors?
        for u in G.neighbors(v_i):
            if (self.assignment[u] == i) and (u != v_j):
                Cw -= G[u][v_i]['weight']
            if (self.assignment[u] == j) and (u != v_j):
                Cw += G[u][v_i]['weight']
        
        for u in G.neighbors(v_j):
            if (self.assignment[u] == j) and (u != v_i):
                Cw -= G[u][v_j]['weight']
            if (self.assignment[u] == i) and (u != v_i):
                Cw += G[u][v_j]['weight']
        
        return Cw


    def get_cost(self):
       return self.Cp + self.Cw + cmp_Ck(self.k)

