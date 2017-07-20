sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

#
#   Maximum Likelihood Hypothesis
#
#
#   In this quiz we will find the maximum likelihood word based on the preceding word
#
#   Fill in the NextWordProbability procedure so that it takes in sample text and a word,
#   and returns a dictionary with keys the set of words that come after, whose values are
#   the number of times the key comes after that word.
#   
#   Just use .split() to split the sample_memo text into words separated by spaces.

def NextWordProbability(sampletext,word):
    #Split the text by spaces into an array
    words = sampletext.split(' ')
    
    #Construct dictionary
    result = dict()
    
    #Find the index of `word`
    index = 0
    while (index < len(words)) :
        if words[index] == word :
            break #found `word`
        index += 1 
    
    #Construct keys and their values according to problem
    for i, key in enumerate(words) :
        #Skip until we're at the index after `word`
        if i < (index + 1) :
            continue
        #Construct the key
        if words[i] not in result :
            #count the number of times it occurs after `word`
            count = 1
            pivot = i
            while (pivot < len(words)) :
                if words[pivot] == words[i] :
                    count += 1
                pivot += 1
            #Save count
            result[key] = count
    
    return result