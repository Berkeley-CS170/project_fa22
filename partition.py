import numpy as np
from utils import *
# GLOBAL VARS
G
V = G.number_of_nodes()

class Partition():
    def __init__(self, assignment):
        '''
        Assignment: an array whose indices are vertex indices and entries
        are the team for each vertex.
        '''
        self.assignment = assignment #[G.nodes[v]['team'] for v in range(V)]
        self.teams, self.team_sizes = np.unique(self.output, return_counts=True)
        k = np.max(self.teams)
        self.b = (self.team_sizes/ V) - 1 / k
        self.Cp = math.exp(B_EXP * np.linalg.norm(self.b))
        self.C_w = sum(d for u, v, d in G.edges(data='weight') if assignment[u] == assignment[v])

    def update_Cp(self,i, j, v):
        # G.nodes[v]['team'] = j
        b = self.b
        self.Cp = np.exp(B_EXP*np.sqrt(np.linalg.norm(b) - b[i]**2 - b[j]**2 \
            + (b[i] - 1/V)**2 + \
                (b[j] + 1/V**2)))

    def update_Cw(self,G,i,j,v):
        for u in G.neighbors(v):
            if self.assigment[u] == i:
                Cw -= G[u][v]['weight']
            if self.assigment[u] == j:
                Cw += G[u][v]['weight']
    
