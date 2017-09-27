#Kelly Wang, Queenie Xiang
#SoftDev1 pd07
#HW03: StI/O: Divine your Destiny!
#2017-09-18

import random
occupations = {}

def selector():
    i = 0
    #Opening and reading file
    f = open("occupations.csv", 'rU')
    stuff = f.read();

    #Turning data into a list and taking out extra info
    lst = stuff.split('\n')
    lst = lst[1:-1]
    counter = 0 
    #print lst
    #print "\n"

    #iterating through the list of occupations and percentages 
    while i < len(lst) :
        #item consists of one occupation and its percentage
        item = lst[i]

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
        occupations[title] = [counter, counter+percent]
        i +=1
        counter += percent

    #Chooses a random number between 0 and 99.9
    num = random.random()*99.9

    #Compares the chosen number with the upper and lower bounds of each key
    #If the chosen number fits between a certain range of a key, then that key is chosen as the occupation to be returned
    for x in occupations:
        comparisons = occupations[x]
        if (comparisons[0] < num and comparisons[1] > num):
            chosen_occ = x         
    print chosen_occ
  
selector()
