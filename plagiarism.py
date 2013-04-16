'''
This program takes two inputs or more and check how much percent they are simmilar according to some rules
and hence checks the plagiarism
'''
#def filter(file1):

#for increasing the score
#def updateScore():
    
    
#for checking the matched words
def check(group1, group2):
    '''This function takes two arguments goup1 and group 2 
    and checks how many words are matching exactly and how many are matching partially
    '''
  for word in group1:
        
def parse(infile1, infile2):
    file1 = infile1.read().split()
    file2 = infile2.read().split()
    #for storing verbs of file1 and file2
    verb1=[]
    verb2=[]
    verb = open("Verb.txt")
    verb = verb.read().split('\n') #for taking the verb file
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

    check(verb1, verb2)
    
    
    
    

infile1 = open(raw_input('Enter the first file name : '), 'r')
infile2 = open(raw_input('Enter the second file name : '), 'r')
parse(infile1, infile2)
