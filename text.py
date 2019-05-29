import random
import numpy


nb_operations = []
for _ in xrange(1000000):
    nb_operation = 0

    transformed = False
    while transformed is False:
        for _ in xrange(3):

            # Add a journey
            if random.random() < 0.1: #0.1
                nb_operation += 1
                transformed = True

            # Delete a random activity to a random journey in a CJM (only if length > 1)
            if random.random() < 0.1:
                nb_operation += 1
                transformed = True

            #Add a random activity to a random journey in a CJM
            if random.random() < 0.1:
                nb_operation += 1
                transformed = True

            #Delete a journey
            if random.random() < 0.1: #0.1
                nb_operation += 1
                transformed = True

    nb_operations.append(nb_operation)

#print numpy.mean(nb_operations)
print numpy.mean(nb_operations)