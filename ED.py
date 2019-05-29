import numpy as npimport editdistanceimport operatordef chunkify(lst, n):    return [lst[i::n] for i in xrange(n)]def assign_traces(m, cjm, actual_journeys, rep_i):    m_journey = m[:, rep_i]    where = np.where(m_journey == np.min(m_journey))[0]    where_0 = where[0]    # No TIE, i.e., there is only one reprentative journey with min distance with actual journey    # => assign all actual journey with pattern == [rep_i] to the actual journey    if len(where) == 1:        cjm[where_0].add_close_observed_traces_with_cost(actual_journeys[rep_i], m_journey[where_0])    else:        journeys = [(cjm[indice], len(cjm[indice].close_traces_indices)) for indice in where]        journeys.sort(key=operator.itemgetter(1))        cut_cake = chunkify(actual_journeys[rep_i], where.shape[0])        [journey[0].add_close_observed_traces_with_cost(cut_cake[i], m_journey[where_0]) for i, journey in enumerate(journeys)]def distribute_actual_journeys(unique_representative_journeys, matrix, width, actual_journeys, cjm, i):    keys = [unique_representative_journeys.index(tuple(journey.activities)) for journey in cjm[i].journey]    m = matrix[keys, :]    [assign_traces(m, cjm[i].journey, actual_journeys, x) for x in xrange(width)]    return cjm[i]class ED:    def __init__(self, xes):        self.xes = xes        self.unique_actual_journeys = []        self.actual_journeys = {} # key=index_unique_actual_journey, value=vectors indices xes id        self.unique_representative_journeys = []        self.representative_journeys = {} # key=index unique_representative_journeys, value=vectors indices journey in map        self.parse_actual_journeys(xes)        self.width = None        self.matrix = self.build_matrix()    def parse_actual_journeys(self, xes):        for key, traces in xes.traces.iteritems():            traces = tuple(traces['activities'])            if traces not in self.unique_actual_journeys:                self.unique_actual_journeys.append(traces)                index = self.unique_actual_journeys.index(traces)                self.actual_journeys[index] = []            index = self.unique_actual_journeys.index(traces)            self.actual_journeys[index].append(key)    def build_matrix(self):        self.width = len(self.unique_actual_journeys)        return np.empty([0, self.width])    def add_new_representative_journeys(self, cjm):        for journey in cjm.journey:            journey = tuple(journey.activities)            if journey not in self.unique_representative_journeys:                self.unique_representative_journeys.append(journey)                index = self.unique_representative_journeys.index(journey)                self.representative_journeys[index] = []                self.add_line_matrix(index)    def add_line_matrix(self, index_rep):        new_line = []        seq1 = self.unique_representative_journeys[index_rep]        for index_act in xrange(self.width):            seq2 = self.unique_actual_journeys[index_act]            new_line.append(float(editdistance.eval(seq1, seq2)))        self.matrix = np.concatenate([self.matrix, np.asarray(new_line, dtype=np.int8).reshape(1,self.width)])    def distribute_actual_journeys(self, cjm):        keys = [self.unique_representative_journeys.index(tuple(journey.activities)) for journey in cjm]        m = self.matrix[keys, :]        [assign_traces(m, cjm, self.actual_journeys, x) for x in xrange(self.width)]    def distribute_actual_journeys(self, cjm):        keys = [self.unique_representative_journeys.index(tuple(journey.activities)) for journey in cjm]        m = self.matrix[keys, :]        [assign_traces(m, cjm, self.actual_journeys, x) for x in xrange(self.width)]