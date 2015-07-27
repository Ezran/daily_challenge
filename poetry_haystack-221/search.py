input_file = open('input.txt','r')

gramlist = dict()

#calculate fitness by ngram frequency sum divided by length of word
def ngram(word):
    total = 0
    if len(word) == 1 and word == 'a' or word == 'i':
        return 1000000
    for i in xrange(len(word) - 1):
        if word[i:i+2:] in gramlist:
            total = total + gramlist[word[i:i+2:]]
    return total / len(word)

with open('bigrams.txt','r') as f:
    for line in f:
        l = line.split()
        gramlist[l[0].lower()] = int(l[1])

    for index,line in enumerate(input_file,start=1):
        printed = False
        for word in line.split():
            fitness = ngram(word)
            if fitness > 990000:
                print word, fitness


#            if fitness > 500:
#                if printed == False:
#                    print index, ':'
#                print word
#                printed = True
#        if printed == True:
#            print '\n'

#for each word in the input file, add the frequency of all bigrams in the word divided by the length of the word.  the highest scores should be real words. then just go through the list and print the highest scored words to see if i was right.
