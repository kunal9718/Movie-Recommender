import numpy as np
from operator import itemgetter

class KNearestNeighbours:

    def __init__(self, data, target, test_point, k):
        self.data = data #data.json
        self.target = target #movie titles
        self.test_point = test_point # genre
        self.k = k # jitni movie chahiye
        self.distances = list()
        self.categories = list()
        self.indices = list()

    @staticmethod
    def dist(p1, p2):
        """Method returns the euclidean distance between two points"""
        return np.linalg.norm(np.array(p1) - np.array(p2))

    def fit(self):
        """Method that performs the KNN classification"""
        # Create a list of (distance, index) tuples from the test point to each point in the data
        self.distances.extend([(self.dist(self.test_point, point), i) for point, i in zip(self.data, [i for i in range(len(self.data))])])
        # Sort the distances in ascending order
        sorted_li = sorted(self.distances, key=itemgetter(0))
        # Fetch the indices of the k nearest point from the data
        self.indices.extend([index for (val, index) in sorted_li[:self.k]])
        # Fetch the categories from the train data target
        for i in self.indices:
            self.categories.append(self.target[i])
        
                                                                                             