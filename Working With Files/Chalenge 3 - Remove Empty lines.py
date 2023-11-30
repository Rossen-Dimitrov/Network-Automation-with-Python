with open('file.txt', 'r') as f:
    txt = f.read().split()
    print('\n'.join(txt))


# # reading the file in a list
# with open('file.txt') as f:
#     content_list = f.readlines()
#
# # create a new list eliminating the elements that are empty strings or contain only spaces
# tmp_list = [line for line in content_list if line.strip() != '']
# print(tmp_list)
#
# # write to a new file
# with open('file_without_blanks.txt', 'w') as f:
#     f.write(''.join(tmp_list))
