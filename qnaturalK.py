import quality
import numpy
import math

class QNaturalk(quality.Quality):
    """Assess the simplicity of a customer journey map
    """

    def assess_quality(self, len_journey, k):

        score = (1.) / (1. + math.pow((abs(len_journey-k) / 5.), 2.))
        self.set_quality(score)

