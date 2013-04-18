'''
This program takes two inputs or more and check how much percent they are simmilar according to some rules
and hence checks the plagiarism
'''
def filter(file1):
    '''
    Take one list as input
    removes special characters from the end including apostrophe s
    returns the new list with edited words
    '''
    
    tmp = []
    for word in file1:
        tmp.append(word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"''s'"))
    return tmp

#for increasing the score
#def updateScore():
    
    
    
#for checking the matched words
def check(group1, group2):
    '''This function takes two arguments goup1 and group 2 
    and checks how many words are matching exactly and how many are matching partially
    '''
    global score
    
    #for checking whether word of group1(original) is present on group2 if present increase the score and remove that word from group2
    for word in group1:
        if word in group2:
            score += 1
            group2.remove(word)
         
      
      
def prints(file2):
    '''
    prints the score of the copied context if more then score will be more 
    if less copied then score will be less
    '''
    print "%d words are copied out of %d number of words" % (score, len(file2))
    

def parse(infile1, infile2):
    file1 = infile1.read().split()
    file2 = infile2.read().split()
    
    #for filtering --> removing special characters from the end of the word
    file1 = filter(file1)
    file2 = filter(file2)
    
    #for storing verbs of file1 and file2
    verb1=[]
    verb2=[]
    verb = open("Data/Verb.txt")
    verb = verb.read().split() #for taking the verb file
    for word in file1:
        if word in verb:
            verb1.append(word.lower())
    for word in file2:
        if word in verb:
                verb2.append(word.lower())
                
    
    
    #for storing adjectives of file1 and file2
    'to be implemented'
    #for storing adverbs of file1 and file2
    'to be implemented'
    
    #for storing pronoun of file1 and file2
    'to be implemented'
    
    #for storing noun of file1 and file2
    'to be implemented'
    
    #for storing preposition of file1 and file2
    'to be implemented'
    
    #checking verb groups for increasing the score
    check(verb1, verb2)
    
    
    prints(file2)
    

infile1 = open(raw_input('Enter the first(original) file name : '), 'r')
infile2 = open(raw_input('Enter the second file name : '), 'r')
score = 0
parse(infile1, infile2)

