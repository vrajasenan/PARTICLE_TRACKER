import numpy as np
from scipy.spatial.distance import cdist

distances = []


def neighbours(particle_centers):

    distances1 = []
    distances2 = []
    dist = cdist(particle_centers,particle_centers)


    if len(dist)>2:#more than 2 particles
        min_ind = dist.argsort()[:, :]


        for i in range(len(dist)):
            #print(dist[i, min_ind[i, 1]])#closest
            distances.append(dist[i, min_ind[i, 1]])
            #distances2.append(dist[i, min_ind[i, 2]])








            #distances[0,i] = dist[i,min_ind[i,1]]#closest particle
            #distances[1, i] = dist[i, min_ind[i, 2]]#second closest
        #print("distance matrix:",dist)#second closest

        return distances

def concentration(particle_centers,volume):
    nos = len(particle_centers);
    conc = nos/volume;



    return conc

