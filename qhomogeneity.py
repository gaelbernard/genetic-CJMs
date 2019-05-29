import quality
import numpy as np
import scipy.stats as stats
import copy
import pandas as pd
from sklearn import tree
from sklearn.metrics import pairwise_distances
from sklearn import metrics
from kmodes.kmodes import KModes



from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, classification_report, f1_score, adjusted_mutual_info_score, normalized_mutual_info_score, adjusted_mutual_info_score, adjusted_rand_score, fowlkes_mallows_score
import math
import itertools
from scipy.spatial.distance import cosine

class QHomogeneity(quality.Quality):

    """Assess the distribution of traces per journey
    """

    def assess_quality(self, journeys, matrix_dummy, xes_length):

        retained_journey = []
        for journey in journeys:
            if len(journey.close_traces_indices)>(math.ceil(xes_length*0.03)):
                retained_journey.append(list(journey.close_traces_indices))

        if len(retained_journey) <= 1:
            self.set_quality(0)
            return



        data = [matrix_dummy.iloc[journey].drop('predictor', 1).sum().values.reshape(1, -1) for journey in retained_journey]
        distances = [cosine(matrix[0],matrix[1]) for matrix in itertools.combinations(data, 2)]

        self.set_quality(np.mean(distances))