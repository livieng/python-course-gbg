import wordfreq
import sys
import urllib.request


    
def main():

    inp_file = open(sys.argv[1])                                  # stopwords

    if 'http://' or 'https://' in sys.argv[2]:                    # URL (https TLS certificate invalid)
        response = urllib.request.urlopen(sys.argv[2])
        inp_2nd_file = response.read().decode("utf8").splitlines()
    else:
        inp_2nd_file = open(sys.argv[2])                          # ex. article
   
    n = int(sys.argv[3])            
   
    stopWords = wordfreq.tokenize(inp_file)  
    words = wordfreq.tokenize(inp_2nd_file)
    frequencies = wordfreq.countWords(words, stopWords)
    print(wordfreq.printTopMost(frequencies,n))

    inp_file.close()
    response.close()

main()
