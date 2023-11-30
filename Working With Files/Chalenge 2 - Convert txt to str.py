with open('sample_file.txt', 'r') as f:
    text = f.read()
    print(str(text))

# with open('sample_file.txt', 'r') as f:
#     # reading the file in a list
#     content = f.read().splitlines()
#     # concatenating the list back into a string
#     my_str = '\n'.join(content)
#     print(my_str)