def tokenize(lines):
    words= []
    for line in lines:
        line = line.lower()

        start = 0
        while (start < len(line)):

            if (line[start].isspace()):                 # error whith a while-loop...
                start += 1
            elif (line[start].isalpha()):
                end = start
                while (end < len(line) and line[end].isalpha()):
                    end += 1
                words.append(line[start:end])
                start=end
            elif (line[start].isdigit()):
                end = start
                while (end < len(line) and line[end].isdigit()):
                    end += 1
                words.append(line[start:end])
                start=end
            else:
                words.append(line[start])
                start += 1
            
    return words


def countWords(words, stopWords):
    frequencies = {}

    for w in words:
        if w in stopWords:
            pass
        else:
            if w in frequencies:
                frequencies[w] += 1
            else:
                frequencies[w] = 1

    return frequencies


def printTopMost(frequencies, n):
    #newList = []
    output = ""
    #for word,freq in frequencies.items():
    newList = sorted(frequencies.items(), key = lambda x: -x[1])

    for word,freq in newList[:n]:
        output += str(word).ljust(20) + str(freq).rjust(5) + "\n"

    return output 