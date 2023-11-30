import string
#
#   case sensitive
# letters = dict()
#
# for c in string.ascii_letters:
#     letters[c] = 0
#
# with open('american-english.txt', 'r') as words:
#     for w in words:
#         for char in string.ascii_letters:
#             letters[char] += w.count(char)
#
# print(letters)


# case insensitive
# letters = dict()
#
# for c in string.ascii_lowercase:
#     letters[c] = 0
#
# with open('american-english.txt', 'r') as words:
#     for w in words:
#         for c in string.ascii_lowercase:
#             letters[c.lower()] += w.count(c.lower())
#
# print(letters)

letters = dict()

for c in string.ascii_lowercase:
    letters[c] = 0

with open('american-english.txt', 'r') as words:
    for w in words:
        for c in string.ascii_lowercase:
            letters[c.lower()] += w.count(c.lower())

    sorted_dict = sorted(letters.items(), key=lambda x: x[1], reverse=True)[:3]

print(sorted_dict)

