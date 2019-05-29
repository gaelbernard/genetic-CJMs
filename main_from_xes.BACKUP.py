from xes import *
from db import *
from population import *

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
        0: ['activity_01', 'activity_02', 'activity_03', 'activity_01', 'activity_02', 'activity_03'],
        1: ['activity_04', 'activity_01', 'activity_05'],
        2: ['activity_05', 'activity_01', 'activity_02', 'activity_05', 'activity_03'],
        3: ['activity_03', 'activity_02', 'activity_01', 'activity_04', 'activity_01'],
        4: ['activity_08', 'activity_02', 'activity_01', 'activity_02']
    }
    parameters['characteristics'] = {
        'employed': ['yes', 'no'],
        'income': ['low', 'middle', 'high'],
        'age': ['0-19yo', '20-39yo', '40-59yo', '60-79yo', '80yo+'],
    }
    parameters["original_characteristic"] = {
        0: {"income": ['low'], "age": ['0-19yo'], 'employed': ['yes']},
        1: {"income": ['high'], 'employed': ['no'], 'age': ['20-39yo']},
        2: {"income": ['middle'], 'employed': ['yes'], 'age': ['40-59yo', '60-79yo']},
        3: {"income": ['low'], 'employed': ['no'], 'age': ['40-59yo', '60-79yo']},
        4: {"income": ['high'], 'employed': ['yes'], 'age': ['40-59yo', '60-79yo']},
    }
    parameters['traces_distribution'] = [0.08, 0.16, 0.25, 0.4, 1]
    hyper_parameters.append(parameters)

    # VALUE = 2
    parameters = {}
    parameters['original_pattern'] = {
        0: ['activity_01', 'activity_01', 'activity_02'],
        1: ['activity_04', 'activity_03', 'activity_05', 'activity_02'],
        2: ['activity_05', 'activity_01', 'activity_02', 'activity_05', 'activity_03'],
    }
    parameters['characteristics'] = {
        'employed': ['yes', 'no'],
        'income': ['low', 'middle', 'high']
    }
    parameters["original_characteristic"] = {
        0: {"employed": ['yes']},
        1: {"income": ['low']},
        2: {"income": ['middle']},
    }
    parameters['traces_distribution'] = [0.15, 0.40, 1]
    hyper_parameters.append(parameters)

    # VALUE = 3
    parameters = {}
    parameters['original_pattern'] = {
        0: ['activity_10', 'activity_01', 'activity_02', 'activity_03'],
        1: ['activity_04', 'activity_05', 'activity_06'],
        2: ['activity_07', 'activity_08', 'activity_09', 'activity_01', 'activity_02'],
    }
    parameters['characteristics'] = {
        'employed': ['yes', 'no'],
        'owner': ['yes', 'no'],
        'income': ['low', 'middle', 'high'],
    }
    parameters["original_characteristic"] = {
        0: {"employed": ['yes'], "owner": ['yes'], "income": ['middle']},
        1: {"employed": ['no'], "owner": ['yes'], "income": ['low']},
        2: {"employed": ['yes'], "owner": ['no'], "income": ['high']},
    }
    parameters['traces_distribution'] = [0.15, 0.55, 1]
    hyper_parameters.append(parameters)

    # VALUE = 4
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

    # VALUE = 5
    parameters = {}
    parameters['original_pattern'] = {
        0: ['activity_01', 'activity_02', 'activity_03', 'activity_04', 'activity_05', 'activity_01', 'activity_03'],
        1: ['activity_03', 'activity_01', 'activity_04', 'activity_01'],
        2: ['activity_05', 'activity_04', 'activity_02'],
        3: ['activity_01', 'activity_04', 'activity_07', 'activity_06', 'activity_05', 'activity_05', 'activity_02'],
    }
    parameters['characteristics'] = {
        'employed': ['yes', 'no'],
        'car_owner': ['yes', 'no'],
        'owner': ['yes', 'no'],
        'income': ['low', 'middle', 'high'],
    }
    parameters["original_characteristic"] = {
        0: {'car_owner': ['no']},
        1: {"car_owner": ['yes']},
        2: {"income": ['low']},
        3: {"owner": ['yes']},
    }
    parameters['traces_distribution'] = [0.15, 0.40, 0.60, 1]
    hyper_parameters.append(parameters)

    # VALUE = 6
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

    # VALUE = 7
    parameters = {}
    parameters['original_pattern'] = {
        0: ['activity_04', 'activity_01', 'activity_04'],
        1: ['activity_03', 'activity_02', 'activity_01', 'activity_04'],
        2: ['activity_04', 'activity_01', 'activity_03', 'activity_08', 'activity_07', 'activity_06'],
        3: ['activity_03', 'activity_04', 'activity_06'],
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

    # VALUE = 8
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

    # VALUE = 9
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

    # VALUE = 10
    parameters = {}
    parameters['original_pattern'] = {
        0: ['activity_01', 'activity_02', 'activity_03', 'activity_11'],
        1: ['activity_04', 'activity_05', 'activity_12', 'activity_06', 'activity_01'],
        2: ['activity_07', 'activity_08', 'activity_09', 'activity_10', 'activity_03', 'activity_09'],
    }
    parameters['characteristics'] = {
        'owner': ['yes', 'no'],
        'car_owner': ['yes', 'no'],
        'income': ['low', 'middle', 'high'],
    }
    parameters["original_characteristic"] = {
        0: {"car_owner": ['yes'], "owner": ['yes'], "income": ['low']},
        1: {"car_owner": ['no'], "owner": ['no'], "income": ['middle']},
        2: {"car_owner": ['yes'], "owner": ['no'], "income": ['high']},
    }
    parameters['traces_distribution'] = [0.1, 0.2, 1]
    hyper_parameters.append(parameters)

    # VALUE = 11
    parameters = {}
    parameters['original_pattern'] = {
        0: ['activity_01', 'activity_07', 'activity_02'],
        1: ['activity_02', 'activity_03', 'activity_04', 'activity_02'],
        2: ['activity_01', 'activity_03', 'activity_05', 'activity_02'],
        3: ['activity_06', 'activity_07', 'activity_01'],
        4: ['activity_03', 'activity_01', 'activity_08', 'activity_09', 'activity_11'],
        5: ['activity_10', 'activity_11', 'activity_03'],
        6: ['activity_08', 'ativity_01', 'activity_04', 'ativity_03', 'ativity_11'],
    }
    parameters['characteristics'] = {
        'owner': ['yes', 'no'],
        'car_owner': ['yes', 'no'],
        'income': ['low', 'middle', 'high'],
    }
    parameters["original_characteristic"] = {
        4: {"owner": ['no']},
        5: {"owner": ['yes']},
        2: {"income": ['low']},
        1: {"income": ['middle']},
        0: {"income": ['high']},
        3: {"car_owner": ['yes']},
        6: {"car_owner": ['no']},
    }
    parameters['traces_distribution'] = [0.06, 0.12, 0.18, 0.24, 0.30, 0.36, 1]
    hyper_parameters.append(parameters)

    # VALUE = 12
    parameters = {}
    parameters['original_pattern'] = {
        0: ['activity_01', 'activity_03', 'activity_02'],
        1: ['activity_04', 'activity_05', 'activity_06'],
        2: ['activity_06', 'activity_07', 'activity_08'],
        3: ['activity_09', 'activity_10', 'activity_11'],
        4: ['activity_12', 'activity_13', 'activity_12'],
        5: ['activity_05', 'activity_09', 'activity_04'],
    }
    parameters['characteristics'] = {
        'age': ['0-19yo', '20-39yo', '40-59yo', '60-79yo', '80yo+'],
        'owner': ['no', 'yes'],
    }
    parameters["original_characteristic"] = {
        0: {"age": ['0-19yo']},
        1: {"age": ['20-39yo']},
        2: {"age": ['40-59yo']},
        3: {"age": ['60-79yo']},
        4: {"age": ['80yo+']},
        5: {"owner": ['no']},
    }
    parameters['traces_distribution'] = [0.05, 0.10, 0.15, 0.20, 0.25, 1]
    hyper_parameters.append(parameters)

    # VALUE = 13
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
        0: {"employed": ['no'], "owner": ['yes'], "income": ['middle'], "age": ['40-59yo']},
        1: {"employed": ['yes'], "owner": ['yes'], "income": ['low'], "age": ['0-19yo']},
        2: {"employed": ['no'], "owner": ['no'], "income": ['low'], "age": ['20-39yo']},
        3: {"employed": ['yes'], "owner": ['no'], "income": ['middle'], "age": ['80yo+']},
        4: {"employed": ['no'], "owner": ['no'], "income": ['high'], "age": ['60-79yo']},

    }
    parameters['traces_distribution'] = [0.05, 0.10, 0.15, 0.20, 1]
    hyper_parameters.append(parameters)

    # VALUE = 14
    parameters = {}
    parameters['original_pattern'] = {
        0: ['activity_01', 'activity_02', 'activity_03', 'activity_01', 'activity_02', 'activity_03'],
        1: ['activity_04', 'activity_04', 'activity_02', 'activity_04', 'activity_01'],
        2: ['activity_05', 'activity_06', 'activity_03', 'activity_03', 'activity_06', 'activity_01', 'activity_02',
            'activity_03', 'activity_06', 'activity_05'],
    }
    parameters['characteristics'] = {
        'employed': ['yes', 'no'],
        'income': ['low', 'middle', 'high'],
    }
    parameters["original_characteristic"] = {
        1: {"income": ['low']},
        2: {"income": ['high']},
        0: {"employed": ['no']},
    }
    parameters['traces_distribution'] = [0.09, 0.18, 1]
    hyper_parameters.append(parameters)

    # VALUE = 15
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

for loop in range(1):
    for index_param in range(16):

        folder_number = index_param+1

        xes_folder = "input/try3/dataset/"+str(folder_number)+"/excluding-solution/"

        for noise_index in range(10):

            noise_name_file = noise_index+1

            xes_file = xes_folder+str(noise_name_file)+".xes"
            #xes_file = xes_folder+"chicago-simplified-with-prom-age-cleaned.xes"

            parameters = {}
            parameters['population_size'] = 60
            parameters['elite_size'] = 3
            parameters['max_iterations'] = 5000
            parameters['xes_file'] = xes_file
            parameters['quality'] = {}

            #############
            #############
            ###### PARAM

            schema = "genetic_final_117"

            #74 = 0.3 et 0.1 (0.3 for insert)
            #75 = 0.2 for all
            #76 = 0.4 for all
            parameters['quality']['fitness'] = 4.
            parameters['quality']['simplicity'] = 0.
            parameters['quality']['homogeneity'] = 1.
            parameters['quality']['distribution'] = 0.
            parameters['quality']['naturalk'] = 1.

            '''parameters['quality']['fitness'] = 5.
            parameters['quality']['simplicity'] = 1.
            parameters['quality']['homogeneity'] = 1.
            parameters['quality']['distribution'] = 0.
            parameters['quality']['naturalk'] = .5'''
            #############
            #############

            print 'schema', schema

            #parameters['heuristic_reasonable_size'] = 30.
            parameters['heuristic_reasonable_size'] = 30.
            parameters['stop_if_no_improvement'] = 100.0

            #noise
            noises = [0.,0.32, 0.45, 0.55, 0.63, 0.71, 0.77, 0.84, 0.89, 0.95]
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
                #start = time.time()
                if (population.generate_next_generation(data)):
                    print _, population.ED.matrix.shape
                    #print (time.time() - start)
                    db.insert_best_cjm(population,data)
                else:
                    break
            db.end()


            print (population.reset_assignation_time+ population.create_next_time+ population.assign_trace_time+population.assess_quality_time+ population.elite_selection_time), population.reset_assignation_time, population.create_next_time, population.assign_trace_time, population.assess_quality_time, population.elite_selection_time




