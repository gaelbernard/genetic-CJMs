from dataGeneratorEngine import *
from db import *
from population import *
import numpy
import time


def run(schema, parameters):


    db = Db(schema)
    db.start(parameters)

    #1. LOADING event logs
    data = DataGeneratorEngine(parameters['original_pattern'], parameters['noise'], parameters['nb_traces'] , parameters['traces_distribution'] ,parameters['characteristics'], parameters['original_characteristic'])
    data.generate_data()
    data.build_categorical_matrix()

    print (data.traces)
    quit()
    db.insert_xes(data, parameters['original_pattern'])

    population = Population(list(data.activity_list), parameters['quality'], parameters['population_size'], parameters['elite_size'], parameters['heuristic_reasonable_size'], parameters['stop_if_no_improvement'])
    population.generate_ED_matrix(data)
    population.find_top_pattern(data)
    bool_homo = 'homogeneity' in parameters['quality']
    population.find_k(data, 12)
    population.create_initial_population(data)

    db.insert_best_cjm(population,data)

    for _ in range(parameters['max_iterations']):
        if (population.generate_next_generation(data)):
            #print 'generation', _
            db.insert_best_cjm(population,data)

        else:
            break

    db.end()






hyper_parameters = []

# VALUE = 0
parameters = {}
parameters['original_pattern'] = {
    0: ['activity_01', 'activity_02', 'activity_03', 'activity_07'],
    1: ['activity_04', 'activity_01', 'activity_02', 'activity_03', 'activity_04'],
    2: ['activity_05', 'activity_02', 'activity_04', 'activity_01'],
    3: ['activity_03', 'activity_01', 'activity_03', 'activity_05'],
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
    0: ['activity_02', 'activity_01', 'activity_02', 'activity_08'],
    1: ['activity_06', 'activity_07', 'activity_02', 'activity_01', 'activity_02', 'activity_03'],
    2: ['activity_08', 'activity_09', 'activity_03'],
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
    0: ['activity_10', 'activity_09', 'activity_02', 'activity_04'],
    1: ['activity_05', 'activity_06', 'activity_07', 'activity_08', 'activity_01', 'activity_03'],
    2: ['activity_01', 'activity_02', 'activity_09', 'activity_05'],
    3: ['activity_02', 'activity_07', 'activity_06'],
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
    0: ['activity_01', 'activity_01', 'activity_02'],
    1: ['activity_04', 'activity_03', 'activity_01'],
    2: ['activity_02', 'activity_03', 'activity_01', 'activity_01', 'activity_01'],
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
    0: ['activity_02', 'activity_01', 'activity_03', 'activity_04', 'activity_01', 'activity_03', 'activity_03'],
    1: ['activity_05', 'activity_05', 'activity_06', 'activity_07'],
    2: ['activity_08', 'activity_09', 'activity_08', 'activity_06'],
    3: ['activity_04', 'activity_05', 'activity_10', 'activity_11', 'activity_11'],
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
    0: ['activity_04', 'activity_01', 'activity_04'],
    1: ['activity_03', 'activity_02', 'activity_01', 'activity_04'],
    2: ['activity_04', 'activity_01', 'activity_03', 'activity_08', 'activity_07', 'activity_06'],
    3: ['activity_03', 'activity_10', 'activity_06', 'activity_11'],
    4: ['activity_09', 'activity_01', 'activity_04', 'activity_04'],
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
    0: ['activity_01', 'activity_04', 'activity_07', 'activity_06', 'activity_05', 'activity_05', 'activity_02',
        'activity_03'],
    1: ['activity_03', 'activity_01', 'activity_04', 'activity_01', 'activity_05'],
    2: ['activity_10', 'activity_06', 'activity_02', 'activity_03', 'activity_07'],
    3: ['activity_10', 'activity_07', 'activity_08', 'activity_09'],
    4: ['activity_09', 'activity_04', 'activity_02'],
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
    0: ['activity_10', 'activity_01', 'activity_02', 'activity_03'],
    1: ['activity_02', 'activity_12', 'activity_10', 'activity_15'],
    2: ['activity_10', 'activity_13', 'activity_08', 'activity_02'],
    3: ['activity_02', 'activity_10', 'activity_03', 'activity_02'],
    4: ['activity_05', 'activity_04', 'activity_02', 'activity_05'],
    5: ['activity_12', 'activity_07', 'activity_06', 'activity_05', 'activity_02', 'activity_13', 'activity_14'],
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

checks = [[False, False, False],
[False, False, True],
[False, True, False],
[False, True, True],
[True, False, False],
[True, False, True],
[True, True, False],
[True, True, True]]
for i, hp in enumerate(hyper_parameters):

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


    #for noise in [.0, .1, .2, .3, .4, .5, .6, .7, .8, .9]:
    for noise in [0., 0.2, 0.4, 0.6, 0.8]:

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

                                database="size"+str(parameters['nb_traces'])
                                print database

                                for _ in range(1):
                                    start_time = time.time()
                                    run(database, parameters)
                                    print(database, 'SERIE:', i, 'NOISE:', noise, "--- %s seconds ---" % (time.time() - start_time))




