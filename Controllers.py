from settings import home, away, version
from retrieveLibre import runRetrieveLibre
from retrieveCSV import getCSV
from JSDB import buildJSDB


def welcomeMessage():
    print("Welcome to Octadoc v{}!".format(version))
    print("Let's configure your settings.\n")

def confirmUserDevice(configFile, userName='Geoffrey', unitTest=False):
    print("We will now configure DEVICE settings.\n")
    if unitTest == True:
        configFile.LAPTOP = True
        configFile.DESKTOP = True
        configFile.AMHOME = False
        print("This is an automated unit test")
        deviceSelected = True
        print("Now printing configInfo")
        print(configFile)
    
    else:
        deviceSelected = False
        while deviceSelected != True:
            print("What device are  you using {}?".format(userName))
            location = input("Desktop = D, Laptop = L, X = exit\n>")
            if location in ['D', 'd']:
                print("So you're on your Desktop?")
                validate = input("Yes = Y, No = N\n>")
                if validate in ['Y', 'y']:
                    print("setting device as DESKTOP in configuration file!")
                    configFile.DESKTOP = True
                    configFile.AMHOME = True
                    #########PROBLEM -THIS IS GOING TO CAUSE A PROBLEM
                    configFile.OSDPATH = home['osdPath']
                    configFile.JSDATABASE = home['jsDatabase']
                    ##################################################
                    print("DESKTOP = {}".format(configFile.DESKTOP))
                    deviceSelected = True
                elif validate in ['N', 'n']:
                    continue
                else:
                    print('That is not a valid selection')
            elif location in ['L', 'l']:
                print("So you're using your laptop?")
                validate = input("Yes = Y, No = N\n")
                if validate in ['Y', 'y']:
                    print("\nSetting device as LAPTOP in configuration file!")
                    configFile.LAPTOP = True
                    print("LAPTOP = {}".format(configFile.LAPTOP))
                    deviceSelected = True
                elif validate in ['N', 'n']:
                    continue
                else:
                    print("That is not a valid selection")

            elif location in ['X', 'x', 'exit']:
                break
            else:
                print("That is not a valid selection")
        return configFile

def setCSVPath(configFile):
    amHome = configFile.AMHOME
    if amHome == True:
        configFile.CSVPATH = home['csvpath']
    elif amHome == False:
        configFile.CSVPATH = away['csvpath']
    else:
        print("issue in setPath()")
        
    print("configFile.CSVPATH set to: {}\n".format(configFile.CSVPATH))
    return configFile


def setCSVDocsPath(configFile):
    amHome = configFile.AMHOME
    if amHome == True:
        configFile.DOCUMENTS = home['csvDocs']

    elif amHome == False:
        configFile.DOCUMENTS = away['csvDocs']
    else:
        print("issue in setCSVDocsPath()")
    
    print("configFile.DOCUMENTS set to {}".format(configFile.DOCUMENTS))
    return configFile


def setLibrePort(configFile):
    portConfirmed = False
    print("\nOctadoc uses LibreOffice/Openoffice to create a prototype database")
    print("Octadoc communicates with this application using LIBREPORT")
    while portConfirmed != True:
        
        print("LIBREPORT is currently set to use port: {}\n".format(configFile.LIBREPORT))
        print("Would you like to change the current port of LIBREPORT?\n")
        print("'No' is a safe choice here.")
        choice = input("Y = yes, N = No, X = exit\n>")
        if choice in ['Y', 'y']:
            print("\nSo you want to change the port?")
            portSelect = input("Please enter port number now, or press 'C' to cancel.\n>")
            try:
                portSelect = int(portSelect)
                if isinstance(portSelect,int):
                    if portSelect <= 65535:
                        configFile.LIBREPORT = portSelect
                        continue
                    else:
                        print("That is not a valid port number!!!")
                        continue
            except ValueError:
                if portSelect in ['C', 'c']:
                    continue

                else:
                    print("That is not a valid selection!")
                    continue

        elif choice in ['N', 'n']:
            portConfirmed = True

        elif choice in ['X', 'x', 'exit']:
            break

        else:
            print("That is not a valid selection!")
    return configFile

def createJSfile(configFile): #This argument is going to need to change, probably.
    """This function needs to somehow morph the table names into objects for the JS database"""
    path = configFile.CSVPATH
    csvFiles = configFile.DOCUMENTS
    content = []
    for i in csvFiles:
        item = getCSV(path,i[0], i[1], i[2])
        content.append(item)
    database = buildJSDB(configFile, configFile.TESTDBNAME, content, JSON=False, writeFile=True)
    print(database)
    

def updateCSVFiles(configFile):
    
    choiceSelected = False
    while choiceSelected != True:
        print("Would you like to run an update of CSV files?")
        choice = input("Y = yes, N = No, X = exit\n>")
        if choice in ['Y', 'y', 'yes']:
            runRetrieveLibre(configFile)

            choiceSelected = True
            """
        This is where the updated version of runRetrieveLibre()
        should go.  But it would be also be a good idea to give
        the user the option of selection which source database should
        be used to update CSV files."""
        

        elif choice in ['N', 'n', 'no']:
            choiceSelected = True

        elif choice in ['X', 'x', 'exit']:
            break
        
        else:
            print("That is not a valid selection.")
            continue
    return configFile

def outputJSFile(configFile):
    choiceSelected = False
    while choiceSelected != True:
        print("Would you like to create a JS database file?")
        choice = input("Y = yes, N = No, X = exit\n>")
        if choice in ['Y', 'y', 'yes']:
            createJSfile(configFile)

            choiceSelected = True
            """
        This is where the updated version of runRetrieveLibre()
        should go.  But it would be also be a good idea to give
        the user the option of selection which source database should
        be used to update CSV files."""
        

        elif choice in ['N', 'n', 'no']:
            choiceSelected = True

        elif choice in ['X', 'x', 'exit']:
            break
        
        else:
            print("That is not a valid selection.")
            continue
    #return configFile

def Octadoc(configFile):
    a = confirmUserDevice(configFile)
    b = setCSVPath(a)
    c = setCSVDocsPath(b)
    '''
    There needs to be another function here to check whether or not
    the selected default database has been changed.
    '''
    #databaseRecentlyUpdated()
    d = updateCSVFiles(c)
    outputJSFile(d)



if __name__ == "__main__":
    from Documents import ConfigFile
    
    cf = ConfigFile()
    Octadoc(cf)


    