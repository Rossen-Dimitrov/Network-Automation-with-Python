import json
import pickle


def serialize(obj, serialized_result, protocol):
    if protocol == 'pickle':
        with open(serialized_result, 'wb') as f:
            pickle.dump(obj, f)

    elif protocol == 'json':
        with open(serialized_result, 'wt') as f:
            json.dump(obj, f, indent=4)
    else:
        print('Invalid serialization. Use pickle or json!')


def deserialize(serialized_file, protocol):
    if protocol == 'pickle':
        with open(serialized_file, 'rb') as f:
            obj = pickle.load(f)

    elif protocol == 'json':
        with open(serialized_file) as f:
            obj = json.load(f)
    else:
        print('Invalid serialization. Use pickle or json!')

    return obj


# Declaring a dictionary
# test = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}
#
# serialize(test, 'test_pickle.dat', 'pickle')
# serialize(test, 'test_json.dat', 'json')
#
# print(deserialize('test_pickle.dat', 'pickle'))
# print(deserialize('test_json.dat', 'json'))
