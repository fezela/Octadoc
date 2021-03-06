import csv
 




def getCSV(path, tableName, objectName, csvFileName, verbose=False):
    print("running retrieveCSV.READ() on....{}".format(csvFileName))
    try:
        with open(path + csvFileName, 'x') as csvFile:
            container = {'tableName': '', 'objectName': '', 'headers': [], 'tables': []}
            readCSV = csv.reader(csvFile, delimiter=",")
            container['tableName'] = tableName
            container['objectName'] = objectName
            for index, row in enumerate(readCSV):
                if index == 0:
                    for i in row:
                        container['headers'].append(i)

                else:
                    container['tables'].append(row)
            print("returning {} container".format(tableName))
    except FileExistsError:
        with open(path + csvFileName) as csvFile:
            container = {'tableName': '', 'objectName': '', 'headers': [], 'tables': []}
            readCSV = csv.reader(csvFile, delimiter=",")
            container['tableName'] = tableName
            container['objectName'] = objectName
            for index, row in enumerate(readCSV):
                if index == 0:
                    for i in row:
                        container['headers'].append(i)

                else:
                    container['tables'].append(row)
            print("returning {} container".format(tableName))    
    finally:
        if verbose != False:
            print("+++++++++++++++++")
            print("contianer: {}".format(tableName))
            print(container)
            print("+++++++++++++++++")
        else:
            print("+++++++++++++++++")
            print("container: {}".format(tableName))
            print("verbose is currently set to \'False\'.")
            print("please set to \'True\' if you want to view container contents")
            print("+++++++++++++++++")
            print("\n")
        print("retrieveCSV.READ() finished!")
        return container

if __name__ == "__main__":
    """
    #Theres no path in the getCSV functions
    x = [('Answers','Answer', 'Answers.csv'), ('Questions','Question','Questions.csv')]
    
    print("This is an automated test from retrieveCSV.py")
    print("\n\n")
    print("******!!!!!!!!!!!!!!!******")
    print("verbose has been set to \'True\'")
    print("******!!!!!!!!!!!!!!!******")
    print("OUTPUT BELOW\n\n")
    for i in x:
        item = getCSV(i[0], i[1], i[2],True)
    print("OUTPUT ENDS OUTPUT ENDS OUTPUT ENDS")
    print("\n\n\n")
    print("!!!!!!**************!!!!!!!")
    print("verbose has been set to \'False\'")
    print("!!!!!***************!!!!!!!")
    print("OUTPUT BELOW\n\n")
    for i in x:
        item = getCSV(i[0], i[1], i[2], False)
    print("OUTPUT ENDS OUTPUT ENDS OUTPUT ENDS")
    """