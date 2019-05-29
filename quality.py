# Python 2
from abc import ABCMeta, abstractmethod

class Quality:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.quality_score = None
        self.name = None

    @abstractmethod
    def assess_quality(self):
        pass

    def set_quality(self, quality):
        self.quality_score = quality

    def set_weight(self, weight):
        self.weight = weight

    def get_quality(self):
        return self.quality_score

    def get_weight(self):
        return self.weight
