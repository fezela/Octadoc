from settings import amHome, home, away

def buildJSDB(configFile, DBname, TableData, JSON=False, writeFile=False):
    statement = ""
    def write():
        if writeFile != False and JSON == True:
            f = open(configFile.JSON_DATABASE, "w")
            for line in statement:
                f.write(line)
        
        elif writeFile != False:
            f = open(configFile.JSDATABASE, "w")
            for line in statement:
                f.write(line)
        
            
    #######################-Main code begins below-####################
    if JSON != True:
               
        print("Now running JS version of buildJSDB()")
        print("\n" * 2)
        statement += "var {} = ".format(DBname) # setting the name of the DB
        statement += "{" # creating the database as an object
        for collection  in TableData:
            statement += "\n\t" + collection['tableName'] + ": [" #printing the table names
            for tabIndx in range(len(collection['tables'])):
                statement += "\n\t    {" + collection['objectName'] + ": {" #printing the object names of each table
                for index, header in enumerate(collection['headers']):
                    statement += header + ": " + "\"" + collection['tables'][tabIndx][index] #printing out the contents of the table seperating each value with ""
                    statement += "\""
                    if index == len(collection['headers']) - 1: #determining whether this is the last of the content in a table row
                        statement += " " 
                    else:
                        statement += ", "
                if tabIndx == len(collection['tables']) - 1: #determining whether this is the end of a row or not
                    statement += "}}"

                else:
                    statement += "}},"
            statement += "\n\t]," #closing the list of a table property
            statement += "\n"
        statement += "};" # closing the database object

                

    else:
        #THIS ISN'T WORKING
        print("Now running JSON version of buildJSDB()!")
        print() * 5
        
        statement += "READ THE NOTES JACKASS"
    write()
    return statement

if __name__ == "__main__":
    """
    #There is no path argument in the getCSV function 
    from retrieveCSV import getCSV
    
    x = [('Answers','Answer', 'Answers.csv'), ('Questions','Question','Questions.csv')]
    y = []
    for i in x:
        item = getCSV(i[0], i[1], i[2])
        y.append(item)
    z = buildJSDB('TESTDB', y, JSON=False, writeFile=True)
    print(z)
    """
            
            
    
