    def reduced(self) -> Word:
        reducedWord : Word = Word(self.word[:])
        newWord : Word = Word([])

        if reducedWord.word != []:
            reduced : bool = True
            reducedInPrevCycle : bool = False
            while reduced:
                reduced = False
                for index in range(len(reducedWord.word) - 1):

                    if reducedInPrevCycle:
                        reducedInPrevCycle = False
                        continue

                    currentSym : Symbol = reducedWord.word[index].sym

                    if currentSym == reducedWord.word[index + 1].sym:
                        newWord.word.append(Elem(
                            symbol = currentSym, 
                            exponent = reducedWord.word[index].exp + reducedWord.word[index + 1].exp
                        ))
                        reduced = True
                        reducedInPrevCycle = True
                    elif reducedWord.word[index].exp == 0:
                        reduced = True
                    else:
                        newWord.word.append(reducedWord.word[index])

                if not reducedInPrevCycle:
                    lastElem : Elem = reducedWord.word[::-1][0]
                    if lastElem.exp != 0:
                        newWord.word.append(lastElem)
                
                reducedWord = newWord if newWord.word != [] else reducedWord
                newWord = Word([])

        if len(reducedWord.word) == 1 and reducedWord.word[0].exp == 0:
            return Word([])
        return reducedWord
