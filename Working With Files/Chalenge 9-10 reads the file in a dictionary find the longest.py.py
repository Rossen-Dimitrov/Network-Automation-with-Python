# def creaate_dict(file):
#     result = {}
#
#     with open(file, 'r') as f:
#         words = f.read().splitlines()
#         for w in words:
#             result[w] = len(w)
#
#     value_key_pairs = ((value, key) for (key, value) in result.items())
#     sorted_result = sorted(value_key_pairs, reverse=True)
#     for k, v in sorted_result:
#         print(f'{k} -> {v}')
#
#
# creaate_dict('american-english.txt')
#
#
# # Write a Python script that finds the first 100 longest words in a file.

with open('american-english.txt') as f:
    words = f.read().splitlines()

    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)

    # print(words_and_length)

    words_list = sorted(words_and_length.items(), key=lambda x: x[1], reverse=True)
    print(words_list[:100])
