#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead","could"]

'''
Imported from previous exercise
'''
def NextWordProbability(sampletext,word):
    #Split the text by spaces into an array
    words = sampletext.split(' ')
    
    #Construct dictionary
    result = dict()
    
    #Iterate through text and calculate based on problem
    count = 0
    for i, key in enumerate(words) :
        if key == word :
            count += 1 #how many times we find the word
            if words[i + 1] in result :
                result[words[i + 1]] += 1
            else :
                result[words[i + 1]] = 1
    #Iterate and calculate relative probabilites
    for word in result :
        result[word] = result[word] / float(count)
    print result
    return result

def LaterWords(sample,word,distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    probabilities = NextWordProbability(sample, word)
    
    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.
    '''
    1. Iterate through each word in the previous probabilities and add their probabilities to a new current list
    2. Do this `distance` number of times
    3. Find the key with the highest value and this is our answer
    '''
    for i in range(distance - 1) :
        current = dict()
        #Iterate through each word in the previous probabilities
        for word in probabilities :
            print word
            #Calculate the next word probabilities into a list
            result = NextWordProbability(sample, word)
            #Iterate and add this to our current list
            for key in result :
                if key in current : #To find the cumulative probabilities
                    current[key] *= result[key]
                else :
                    current[key] = result[key] * probabilities[word]
        probabilities = current
        print probabilities
    #Find the max key value pair and return
    key = max(probabilities, key = probabilities.get)
        
    return key
print LaterWords(sample_memo,"need",2)