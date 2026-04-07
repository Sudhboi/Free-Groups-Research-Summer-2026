inverse = {}
for i in range(65, 65 + 25):
    inv = i + 32
    inverse[chr(i)] = chr(inv)
    inverse[chr(inv)] = chr(i)

def reduce(word : str) -> (str, bool):
    if word == "":
        return ("", False)

    reducedWord = ""
    reduced = False
    reduceNext = False

    for i in range(0, len(word) - 1):
        if reduceNext:
            reduceNext = False
            continue
        if (word[i + 1] == inverse[word[i]]):
            reduced = True
            reduceNext = True
        else:
            reducedWord += word[i]

    if not reduceNext:
        reducedWord += word[len(word) - 1]

    return (reducedWord, reduced)

def reducer(word : str) -> str:
    reduced_word, did_reduce = reduce(word)
    while did_reduce != False:
        reduced_word, did_reduce = reduce(reduced_word)
    return reduced_word

def morphism(word : str, map : dict[str, str]) -> str:
    return "".join([map[i] for i in word])

print(reducer("AaaAb"))

