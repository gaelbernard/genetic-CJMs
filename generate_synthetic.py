from dataGeneratorEngine import *
from db import *
from population import *
import numpy
import time
import pandas as pd

def run(parameters, serie_i):


    #1. LOADING event logs
    data = DataGeneratorEngine(parameters['original_pattern'], parameters['noise'], parameters['nb_traces'] , parameters['traces_distribution'] ,parameters['characteristics'], parameters['original_characteristic'])
    data.generate_data()
    data.build_categorical_matrix()
    activities = []
    original_pattern = []
    for t in data.traces.itervalues():
        activities.append("-".join(t['activities']))
        original_pattern.append("-".join(data.original_pattern[t['original_pattern']]))

    pd.Series(activities).to_csv("new_dataset/actual-"+str(parameters['noise'])+'-'+str(serie_i)+'.csv', index=False)
    pd.Series(original_pattern).to_csv("new_dataset/original-"+str(parameters['noise'])+'-'+str(serie_i)+'.csv', index=False)
    #quit()

    population = Population(list(data.activity_list), parameters['quality'], parameters['population_size'], parameters['elite_size'], parameters['heuristic_reasonable_size'], parameters['stop_if_no_improvement'])
    population.generate_ED_matrix(data)
    population.find_top_pattern(data)
    population.find_k(data, 12)
    population.create_initial_population(data)







hyper_parameters = []

# VALUE = 0
parameters = {}
parameters['original_pattern'] = {
    0: ['1', '2', '3', '7'],
    1: ['4', '1', '2', '3', '4'],
    2: ['5', '2', '4', '1'],
    3: ['3', '1', '3', '5'],
}
parameters['characteristics'] = {
    'employed': ['yes', 'no'],
    'income': ['low', 'middle', 'high'],
    'age': ['0-19yo', '20-39yo', '40-59yo', '60-79yo', '80yo+'],
}
parameters["original_characteristic"] = {
    0: {"income": ['low'], 'employed': ['yes'], "age": ['0-19yo']},
    1: {"income": ['middle'], 'employed': ['yes'], "age": ['40-59yo']},
    2: {"income": ['high'], 'employed': ['no'], 'age': ['60-79yo']},
    3: {"income": ['middle'], 'employed': ['no'], 'age': ['80yo+']},
}
parameters['traces_distribution'] = [0.10, 0.20, 0.50, 1]
hyper_parameters.append(parameters)

# VALUE = 1
parameters = {}
parameters['original_pattern'] = {
    0: ['2', '1', '2', '8'],
    1: ['6', '7', '2', '1', '2', '3'],
    2: ['8', '9', '3'],
}
parameters['characteristics'] = {
    'employed': ['yes', 'no'],
    'car_owner': ['yes', 'no'],
    'owner': ['yes', 'no'],
    'income': ['low', 'middle', 'high'],
}
parameters["original_characteristic"] = {
    0: {"employed": ['no'], "car_owner": ['yes'], "owner": ['no'], "income": ['low']},
    1: {"employed": ['yes'], "car_owner": ['no'], "owner": ['yes'], "income": ['high']},
    2: {"employed": ['yes'], "car_owner": ['yes'], "owner": ['no'], "income": ['middle']},
}
parameters['traces_distribution'] = [0.08, 0.18, 1]
hyper_parameters.append(parameters)

# VALUE = 2
parameters = {}
parameters['original_pattern'] = {
    0: ['10', '9', '2', '4'],
    1: ['5', '6', '7', '8', '1', '3'],
    2: ['1', '2', '9', '5'],
    3: ['2', '7', '6'],
}
parameters['characteristics'] = {
    'employed': ['yes', 'no'],
    'owner': ['yes', 'no'],
    'age': ['0-19yo', '20-39yo', '40-59yo', '60-79yo', '80yo+'],
}
parameters["original_characteristic"] = {
    0: {"owner": ['no']},
    1: {"owner": ['yes']},
    2: {"owner": ['yes']},
    3: {"owner": ['no']},
}
parameters['traces_distribution'] = [.1, .25, .35, 1]
hyper_parameters.append(parameters)

# VALUE = 3
parameters = {}
parameters['original_pattern'] = {
    0: ['1', '1', '2'],
    1: ['4', '3', '1'],
    2: ['2', '3', '1', '1', '1'],
}
parameters['characteristics'] = {
    'owner': ['yes', 'no'],
    'income': ['low', 'middle', 'high'],
}
parameters["original_characteristic"] = {
    0: {"income": ['middle']},
    1: {"income": ['low']},
    2: {"income": ['high']}
}
parameters['traces_distribution'] = [0.1, 0.2, 1]
hyper_parameters.append(parameters)

# VALUE = 4
parameters = {}
parameters['original_pattern'] = {
    0: ['2', '1', '3', '4', '1', '3', '3'],
    1: ['5', '5', '6', '7'],
    2: ['8', '9', '8', '6'],
    3: ['4', '5', '10', '11', '11'],
}
parameters['characteristics'] = {
    'employed': ['yes', 'no'],
    'car_owner': ['yes', 'no'],
    'owner': ['yes', 'no'],
    'income': ['low', 'middle', 'high'],
}
parameters["original_characteristic"] = {
    0: {"employed": ['yes'], "owner": ['no'], "car_owner": ['yes'], "income": ['middle']},
    1: {"employed": ['no'], "owner": ['no'], "car_owner": ['yes'], "income": ['high']},
    2: {"employed": ['yes'], "owner": ['yes'], "car_owner": ['no'], "income": ['low']},
    3: {"employed": ['no'], "owner": ['yes'], "car_owner": ['no'], "income": ['low', 'middle']},
}
parameters['traces_distribution'] = [0.25, 0.5, 0.75, 1]
hyper_parameters.append(parameters)

# VALUE = 5
parameters = {}
parameters['original_pattern'] = {
    0: ['4', '1', '4'],
    1: ['3', '2', '1', '4'],
    2: ['4', '1', '3', '8', '7', '6'],
    3: ['3', '10', '6', '11'],
    4: ['9', '1', '4', '4'],
}
parameters['characteristics'] = {
    'owner': ['yes', 'no'],
    'income': ['low', 'middle', 'high'],
    'age': ['0-19yo', '20-39yo', '40-59yo', '60-79yo', '80yo+'],
    'car_owner': ['yes', 'no'],
}
parameters["original_characteristic"] = {
    0: {"owner": ['yes'], "income": ['low'], "age": ['0-19yo'], "car_owner": ['yes']},
    1: {"owner": ['no'], "income": ['high'], "age": ['20-39yo'], "car_owner": ['yes']},
    2: {"income": ['middle'], "owner": ['no'], "age": ['60-79yo'], "car_owner": ['no']},
    3: {"income": ['high'], "owner": ['yes'], "age": ['40-59yo'], "car_owner": ['yes']},
    4: {"income": ['low'], "owner": ['yes'], "age": ['80yo+'], "car_owner": ['no']},
}
parameters['traces_distribution'] = [0.07, 0.16, 0.25, 0.30, 1]
hyper_parameters.append(parameters)

# VALUE = 6
parameters = {}
parameters['original_pattern'] = {
    0: ['1', '4', '7', '6', '5', '5', '2',
        '3'],
    1: ['3', '1', '4', '1', '5'],
    2: ['10', '6', '2', '3', '7'],
    3: ['10', '7', '8', '9'],
    4: ['9', '4', '2'],
}
parameters['characteristics'] = {
    'employed': ['yes', 'no'],
    'owner': ['yes', 'no'],
    'income': ['low', 'middle', 'high'],
    'age': ['0-19yo', '20-39yo', '40-59yo', '60-79yo', '80yo+'],
}
parameters["original_characteristic"] = {
    0: {"employed": ['no']},
    1: {"owner": ['yes']},
    2: {"employed": ['yes']},
    3: {"owner": ['no']},
    4: {"income": ['high']},

}
parameters['traces_distribution'] = [0.10, 0.20, 0.40, 0.60, 1]
hyper_parameters.append(parameters)

# VALUE = 7
parameters = {}
parameters['original_pattern'] = {
    0: ['10', '1', '2', '3'],
    1: ['2', '12', '10', '15'],
    2: ['10', '13', '8', '2'],
    3: ['2', '10', '3', '2'],
    4: ['5', '4', '2', '5'],
    5: ['12', '7', '6', '5', '2', '13', '14'],
}
parameters['characteristics'] = {
    'employed': ['yes', 'no'],
    'owner': ['yes', 'no'],
    'car_owner': ['yes', 'no'],
}
parameters["original_characteristic"] = {
    0: {"employed": ['no']},
    1: {"employed": ['yes']},
    2: {"owner": ['yes']},
    3: {"owner": ['no']},
    4: {"car_owner": ['yes']},
    5: {"car_owner": ['no']},
}
parameters['traces_distribution'] = [0.05, 0.10, 0.15, 0.20, 0.25, 1]
hyper_parameters.append(parameters)

# VALUE = 8
parameters = {}
parameters['original_pattern'] = {
    0: ['11', '3', '2', '3'],
    1: ['12', '2', '1', '15'],
    2: ['3', '2', '18', '2'],
    3: ['4', '5', '6', '7'],
    4: ['5', '4', '2', '5'],
    5: ['19', '20', '7', '2', '1', '3', '14'],
    6: ['14', '17', '16', '15', '2', '3', '1'],
    7: ['20', '6'],
    8: ['17', '16', '14', '15', '1', '4', '22'],
}
parameters['characteristics'] = {
    'employed': ['yes', 'no'],
    'owner': ['yes', 'no'],
    'car_owner': ['yes', 'no'],
}
parameters["original_characteristic"] = {
    0: {"employed": ['no']},
    1: {"employed": ['yes']},
    2: {"owner": ['yes']},
    3: {"owner": ['no']},
    4: {"car_owner": ['yes']},
    5: {"car_owner": ['no']},
}
parameters['traces_distribution'] = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 1]
hyper_parameters.append(parameters)

# VALUE = 9
parameters = {}
parameters['original_pattern'] = {
    0: ['1', '2', '3', '4', '20', '15', '19', '14', '15', '13'],
    1: ['3', '4', '6', '8', '9', '2', '3', '14', '15'],
    2: ['3', '1', '3', '1', '4', '5', '6'],
    3: ['1', '1', '2', '1', '2', '3', '4', '5'],
    4: ['4', '5', '6', '20', '21','13'],
    5: ['21', '14', '16', '12', '5', '7', '13'],
    6: ['9', '11', '19', '14'],
    7: ['3', '2', '1', '2', '3', '18', '21', '12', '16', '7'],
    8: ['17', '16', '14', '15', '1', '4', '22'],
}
parameters['characteristics'] = {
    'employed': ['yes', 'no'],
    'owner': ['yes', 'no'],
    'car_owner': ['yes', 'no'],
}
parameters["original_characteristic"] = {
    0: {"employed": ['no']},
    1: {"employed": ['yes']},
    2: {"owner": ['yes']},
    3: {"owner": ['no']},
    4: {"car_owner": ['yes']},
    5: {"car_owner": ['no']},
}
parameters['traces_distribution'] = [0.1, 0.20, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]
hyper_parameters.append(parameters)

checks = [[False, False, False],
[False, False, True],
[False, True, False],
[False, True, True],
[True, False, False],
[True, False, True],
[True, True, False],
[True, True, True]]
for i, hp in enumerate(hyper_parameters):
    '''
    nb_journey = len(hp['original_pattern'])
    nb_rules = 0
    for r in hp['original_characteristic'].itervalues():
        nb_rules += len(r)
    nb_element = 0
    distinct_act = set()
    for p in hp['original_pattern'].itervalues():
        nb_element += len(p)
        for g in p:
            distinct_act.add(g)
    distinct_act  = len(distinct_act)
    bins = []
    last = 0
    for v in hp['traces_distribution']:
        bins.append(v-last)
        last = v

    print i, nb_element

    stdev = numpy.std(bins)
    check_nb_journey = False
    if nb_element >= 20:
        check_nb_journey = True
    check_homo = False
    if float(nb_rules)/float(nb_journey) <= 1.:
        check_homo = True

    check_distinct = False
    if distinct_act >= 10:
        check_distinct = True


    check_distrib = False
    if stdev >= .25:
        check_distrib = True



    if (len(hp['traces_distribution'])!=nb_journey):
        print 'No good trace distrib ', i
        exit()

    previous_d = 0
    for d in hp['traces_distribution']:
        if previous_d>=d:
            print 'trace distrib does not make sense ', i
            exit()
        previous_d = d

    if hp['traces_distribution'][len(hp['traces_distribution'])-1] != 1.0:
        print 'last trace distrib should be one ', i



    if (numpy.sum(bins)!=1):
        print 'Bins not summing to 1 ', numpy.sum(bins)
        exit()




    for v in hp["original_characteristic"].itervalues():
        for key in v.iterkeys():
            if key not in hp['characteristics'].keys():
                print 'Rules are not in keys ', key, hp['characteristics'].keys()
                exit()

    for key in hp["original_characteristic"].iterkeys():
        if key not in hp['original_pattern'].keys():
            print 'Rules are not in original patterns ', key, hp['characteristics'].keys()
            exit()

    set_seq = set()

    count = 0
    for p in hp['original_pattern'].itervalues():
        set_seq.add('____'.join(p))
        count += len(p)
    if len(set_seq) < len(hp['original_pattern']):
        print 'DUPLICATES!'
        exit()

    for v in hp["original_characteristic"].itervalues():
        for key, values in v.iteritems():
            for value in values:
                if value not in hp['characteristics'][key]:
                    print 'Values is not in keys ', value, hp['characteristics'][key]
                    exit()



    #print i, ':', nb_element, float(nb_rules)/float(nb_journey), distinct_act, stdev,

    if ([(check_nb_journey and check_distinct), check_homo, check_distrib] != checks[i]):
        print 'NOT THE GOOD RULES for ', i, ': got ',[check_nb_journey, check_distinct, check_homo, check_distrib],' instead of', checks[i]
        exit()

    #for noise in [.1, .8, .9]:
    '''

    #for noise in [.0, .1, .2, .3, .4, .5, .6, .7, .8, .9]:
    for noise in [0.0,0.2, 0.6, 0.8 , 0.9, 0.95]:

        parameters = {}
        parameters['nb_traces'] = 1000
        parameters['population_size'] = 100
        parameters['elite_size'] = 5
        parameters['traces_distribution'] = hp['traces_distribution']
        parameters['noise'] = noise
        parameters['max_iterations'] = 1
        parameters['quality'] = {}
        parameters['qualityboost'] = 1.
        parameters['stop_if_no_improvement'] = 1.0
        parameters['original_pattern'] = hp['original_pattern']
        parameters['characteristics'] = hp['characteristics']
        parameters["original_characteristic"] = hp['original_characteristic']


        for fitness in [5.]:
            for simplicity in [0]:
                for naturalK in [1.]:
                    for homogeneity in [0.]:
                        for distribution in [0]:
                            for heuristic_reasonable_size in [30.]:

                                parameters['heuristic_reasonable_size'] = heuristic_reasonable_size

                                if fitness > 0:
                                    parameters['quality']['fitness'] = fitness
                                if simplicity > 0:
                                    parameters['quality']['simplicity'] = simplicity
                                if naturalK > 0:
                                    parameters['quality']['naturalk'] = naturalK
                                if homogeneity > 0:
                                    parameters['quality']['homogeneity'] = homogeneity
                                if distribution > 0:
                                    parameters['quality']['distribution'] = distribution


                                for _ in range(1):
                                    start_time = time.time()
                                    run(parameters,i)
                                    print('SERIE:', i, 'NOISE:', noise, "--- %s seconds ---" % (time.time() - start_time))




