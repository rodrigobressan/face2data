# dataset_dict = {
#     'race_id': {
#         0: 'white',
#         1: 'black',
#         2: 'asian',
#         3: 'indian',
#         4: 'others'
#     },
#     'gender_id': {
#         0: 'male',
#         1: 'female'
#     }
# }

dataset_dict = {
    'race': {
        "White": 0,
        "Latino/Hispanic": 1,
        "Indian": 2,
        "East Asian": 3,
        "Black": 4,
        "Southeast Asian": 5,
        "Middle Eastern": 6
    },
    'gender': {
        'Male': 0,
        'Female': 1
    }
}

dataset_dict['race_id'] = dict((g, i) for i, g in dataset_dict['race'].items())
dataset_dict['gender_id'] = dict((g, i) for i, g in dataset_dict['gender'].items())