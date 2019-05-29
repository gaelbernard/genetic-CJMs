import quality
import numpy
import math

class QSimplicity(quality.Quality):
    """Assess the simplicity of a customer journey map
    """

    def assess_quality(self, journeys, heuristic_reasonable_size):

        different_activities = set()
        sum_activities = 0.0

        for journey in journeys:
            for activity in journey.activities:
                different_activities.add(activity)
                sum_activities += 1.0

        quality_number_touchpoint = 1.0-((1.0) / (1.0 + math.exp(-(0.1 * (sum_activities+(len(journeys)*3.) - heuristic_reasonable_size)))))
        self.set_quality(quality_number_touchpoint)



