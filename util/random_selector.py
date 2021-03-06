"""
Queenie Xiang and Kelly Wang 
SoftDev1 pd7
HW5 -- Jinja Tuning
2017-09-26
"""

import random
occupations = {}

def ret_occ():
    i = 0
    #Opening and reading file
    f = open("occupations.csv", 'rU')
    contents = f.read();

    #Turning data into a list and taking out extra info
    list = contents.split('\n')
    list = list[1:-1]
    counter = 0
    print list; 
    #print list
    #print "\n"

    #iterating through the list of occupations and percentages 
    while i < len(list) :
        #item consists of one occupation and its percentage
        item = list[i]

        #when the occupation is between quotations, everything inside the quotes is the job title. The percentage is after the comma after the closing quotation. 
        if item[0] == '"' :
            item = item[1:]
            pos = item.find('"')
            title = item[0:pos]
            percent = item[pos+2:]
            #print "title: " + title
            #print "percent: " + percent
        #in other cases, the job title is before the comma and the percentage comes after. 
        else:
           pos = item.find(',')
           title = item[0:pos]
           percent = item[pos+1:]
           #print "title: " + title
           #print "percent: " + percent

        #Grabs the percentage of the occupation and converts it to a float
        percent = float(percent)

        #Adding to the occupations dictionary:
        #Each key is the name of the occupation
        #Each key has a value of a list that has an upper and lower bound for the percentage value
        #i.e. for management, it looks like this: 'management':[0, 6.1]
        occupations[title] = [percent, counter, counter+percent]
        i +=1
        counter += percent

    return occupations; 




def rand_selector():
    #Chooses a random number between 0 and 99.9
    num = random.random()*99.9

    #Compares the chosen number with the upper and lower bounds of each key
    #If the chosen number fits between a certain range of a key, then that key is chosen as the occupation to be returned

    for x in occupations:
        comparisons = occupations[x]
        if (comparisons[1] < num and comparisons[2] > num):
            chosen_occ = x         
            return chosen_occ
            

    

    
    
