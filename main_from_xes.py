from xes import *
from db import *
from population import *
import time

hyper_parameters = []
if 1==1:
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
        0: {"employed": ['no']},
        1: {"owner": ['yes']},
        2: {"owner": ['yes']},
        3: {"age": ['0-19yo']},
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

for loop in range(10): #10
    for index_param in range(8): #8

        folder_number = index_param+1

        #xes_folder = "input/try5/dataset/"+str(folder_number)+"/excluding-solution/"
        xes_folder = "input/size100/dataset/"+str(folder_number)+"/excluding-solution/"
        #xes_folder = "input/"

        for noise_index in range(5): #5

            start = time.time()

            noise_name_file = noise_index+1

            xes_file = xes_folder+str(noise_name_file)+".xes"
            #xes_file = xes_folder+"BPI_challenge_2017.xes"
            #xes_file = xes_folder+"chicago-AGE+DAYWEEK.xes"

            parameters = {}
            parameters['population_size'] = 100
            parameters['elite_size'] = 5
            parameters['max_iterations'] = 5000
            parameters['xes_file'] = xes_file
            parameters['quality'] = {}

            #############
            #############
            ###### PARAM

            schema = "a101"

            #74 = 0.3 et 0.1 (0.3 for insert)
            #75 = 0.2 for all
            #76 = 0.4 for all
            parameters['quality']['fitness'] = 5.
            parameters['quality']['simplicity'] = 0.
            parameters['quality']['homogeneity'] = 0.
            parameters['quality']['distribution'] = 0.
            parameters['quality']['naturalk'] = 1.

            #############
            #############

            print 'schema', schema

            #parameters['heuristic_reasonable_size'] = 30.
            parameters['heuristic_reasonable_size'] = 30.
            parameters['stop_if_no_improvement'] = 50.0

            #noise
            noises = [0.,0.2, 0.4, 0.6, 0.8]
            #noises = [.0, .5, .8, .9]
            noise = noises[noise_index]

            #Manually added param

            parameters['noise'] = noise
            parameters['original_pattern'] = hyper_parameters[index_param]['original_pattern']
            parameters['characteristics'] = hyper_parameters[index_param]['characteristics']
            parameters['original_characteristic'] = hyper_parameters[index_param]['original_characteristic']
            parameters['traces_distribution'] = hyper_parameters[index_param]['traces_distribution']

            #parameters['quality']['distribution'] = 12.0
            db = Db(schema)
            db.start(parameters)

            #1. LOADING event logs
            data = Xes(parameters['xes_file'])
            data.parse_xes()
            data.build_categorical_matrix()


            db.insert_xes(data, [])


            population = Population(list(data.activity_list), parameters['quality'], parameters['population_size'], parameters['elite_size'], parameters['heuristic_reasonable_size'], parameters['stop_if_no_improvement'])

            population.generate_ED_matrix(data)
            population.find_top_pattern(data)
            population.find_k(data, 12)

            population.create_initial_population(data)

            db.insert_best_cjm(population,data)

            print 'parameters', parameters
            for _ in range(parameters['max_iterations']):

                if (population.generate_next_generation(data)):

                    db.insert_best_cjm(population,data)
                else:
                    break
            db.end()

            # print (population.reset_assignation_time+ population.create_next_time+ population.assign_trace_time+population.assess_quality_time+ population.elite_selection_time), population.reset_assignation_time, population.create_next_time, population.assign_trace_time, population.assess_quality_time, population.elite_selection_time
            print _, population.ED.matrix.shape
            print 'time', (time.time() - start)



