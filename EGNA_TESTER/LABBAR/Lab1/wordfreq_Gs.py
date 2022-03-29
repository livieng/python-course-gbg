def tokenize(lines):

    words = []
    for line in lines:
        line = line.lower()
        
        start = 0
        end = 0
        while(end < len(line)):
            
            if(line[start].isalpha()):
                while(end < len(line) and line[end].isalpha()):
                    end += 1
                
                words.append(line[start:end])
                start = end

            elif(line[start].isdigit()):
                while(end < len(line) and line[end].isdigit()):
                    end += 1
                
                words.append(line[start:end])
                start = end

            elif(line[start].isspace()):
                start += 1
                end += 1

            else:
                words.append(line[start])
                start += 1
                end += 1
    
    return(words)
                