words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def multiplication(dictionary):
    for key, value in dictionary.items():
        result = key * value
        print(result)


multiplication(words)
