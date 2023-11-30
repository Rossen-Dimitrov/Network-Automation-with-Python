def count(file):
    with open(file, 'r') as f:
        content = f.read().splitlines()
        lin_count = len(content)
        words_count = 0
        chars_count = 0
        for line in content:
            words_count += len(line.split())
            chars_count += len(line)

    return f"Number of lines: {lin_count}; Number of words:{words_count} Numebr of Chars: {chars_count}"


print(count('sample_file.txt'))
