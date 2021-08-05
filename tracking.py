import numpy as np
from scipy.spatial.distance import cdist
distances = []



def neighbours(particle_centers):


    dist = cdist(particle_centers,particle_centers)


    if len(dist)>1:#more than 2 particles
        min_ind = dist.argsort()[:, :]


        for i in range(len(dist)):

            distances.append(dist[i, min_ind[i, 1]])




        return distances

