import quality
import math

class QFitness(quality.Quality):
    """Assess the fitness of a CJM using a three steps approach:
    1) For each traces (observed events) measure the edit distance
    with each journeys (i.e., that are on the map)
    (done in population.assign_trace_to_closest_journey())
    2) Assign each traces to the closest journeys (i.e., the one that
    has the smallest edit distance
    3) Sum these smallest edit distance
    """

    def assess_quality(self, journeys, length_logs, sum_activity):

        sum_edit_distance = sum(float(journey.sum_edit_distance_from_observed_traces) for journey in journeys)
        self.set_quality(1-(sum_edit_distance/sum_activity))
