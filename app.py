import random
from flask import Flask, render_template
app = Flask(__name__)


#assign following fxn to run when root route requested 
@app.route("/") 
def hello_world():
    retStr = ""
    retStr += "<center>Hello, nice to meet you! Click on the picture for a surprise!<br>" 
    retStr += "<a href = /occupations>"
    retStr += "<img src = /static/quokka.jpg> </a> <br>  </center>" 
    
    return retStr



@app.route("/occupations")

def selector():
    occupations={} 
    i = 0
    #Opening and reading file
    f = open("occupations.csv", 'rU')
    stuff = f.read();

    #Turning data into a list and taking out extra info
    lst = stuff.split('\n')
    lst = lst[1:-1]
    counter = 0
    #print lst 


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


        occupations[title] = percent
        i+=1

        return occupations
    

def test_tmplt():
    return render_template('occupations_template.html', occupations = selector())


if __name__ == "__main__":
    app.debug = True
    app.run()
