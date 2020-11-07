def letters(word):
    iter = 0
    while iter < len(word):
        yield word[iter]
        iter += 1
