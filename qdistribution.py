import quality
import numpy as np
from statsmodels import robust
import math


class QDistribution(quality.Quality):
    """Assess the distribution of traces per journey
        - if the journey_size is equal to 1, we qualify the quality as 0 as we cannot really talk about distribution
        robust.mad() could be an option to reduce the effect of outliers
        - not working, todo: how to normalize std?
    """

    def assess_quality(self, journeys, length_logs):

        journeys_size = []
        for journey in journeys:
            journeys_size.append(len(journey.close_traces_indices))

        if len(journeys)==1:
            self.set_quality(0.0)

        else:
            try:
                norm = [float(i) / sum(journeys_size) for i in journeys_size]
                std = float(np.power(np.array(norm).std(),0.5))
                score = 1.0 - std
                self.set_quality(score)

            except:
                self.set_quality(0.0)





