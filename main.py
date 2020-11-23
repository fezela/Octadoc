from settings import *
import retrieveCSV
#import factoring
from JSDB import buildJSDB

def main():

    #STEPS
    '''
        1. Confirm the user location
        2. Change the settings (output/input) based on user location
        3. Was the test database updated?
            !This could be done with a file that contains the output from stat -c %y
            -yes?
                *Give the user the option of updating the csv files
        
                    -Do you want to commit the database changes to the JS database?
                        --yes?
                            *runRetrieveLibre() //updates the csv files located in csv folder
                        --no? 
                            *continue
        3. verify csv documents path
        4. run retrieveCSV.READ() on all necessary documents
        5. The containers that were built by retrieveCSV.READ() need to be stored in a LIST
        6. Take the list of containers and run buildJSDB()
    '''
'''
    print("Welcome to OctaDoc v{}".format(version))
    print()
    print("Geoffrey/Jafar/Blade/#9/Senor Once.  I have a few questions before we begin.")
    print("What are you using?")
    location = input("Desktop = D, Laptop = L\n>")
    
    if location in ['D','d']:
        print("So you're on your Desktop?")
    
    elif location in ['L','l']:
        print("So you're on your Laptop")

    else:
        print("That is not a valid input")
    
    if amHome == True:
        print('Are you on your desktop?')
        documents = home['csvDocs']
    else:
        print("Are you on your laptop?")
        documents = away['csvDocs']
   
    y = []
    for doc in documents:
        item = retrieveCSV.READ(doc[0], doc[1], doc[2])
        y.append(item)
    buildJSDB('QuizDB', y, JSON=False, writeFile=True)
    print("and.... we out")    
    '''

    
main()