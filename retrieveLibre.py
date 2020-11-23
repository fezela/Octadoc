import pyoo
import libreCall
from settings import *












 
def writeCSV(content, path):
    for d in content:
        with open(path + d['sheetName'] + ".csv", mode='w') as f:
            myStr = ""
            for i, l in enumerate(d['headers']):
                if i == len(d['headers']) - 1:
                    myStr += l
                else:
                    myStr += l + d['delimiter']
            myStr += "\n"
            for row in d['rows']:
                for j, r in enumerate(row):
                    if j == len(row) - 1:
                        myStr += str(r)
                    else:
                        myStr += str(r) + d['delimiter']

                myStr += "\n"
            f.writelines(myStr)
            f.close()


def readLibre(document):
    document = document
    content = []
    for index, sheet in enumerate(document.sheets):
        sheet = document.sheets[index]
        data = {
            'sheetName': sheet.name,
            'headers':  None,
            'rows': [],
            'delimiter': ","

        }
        info = []
        y = 0
        x = 0
        print("+++ {} +++".format(sheet))
    
        while sheet[y][0].value != "":
            
            if sheet[y][x].value != "":
                info.append(sheet[y][x].value)
                
                x+= 1
            else:
                if y == 0:
                    data['headers'] = info[:]
                    print(info)
                    info.clear()
                
                else:
                    data['rows'].append(info[:])
                    print(info)
                    info.clear()    
                
                x = 0
                y+= 1
            
        content.append(data)    
        print("\n")
    return content   
    


def runRetrieveLibre():
    print("running retrieveLibre.py")
    if amHome == True:
        port = int(home['librePort'])
        myPath = home['csvpath']

    else:
        port = int(away['librePort'])
        myPath = away['csvpath']

    #Call deactivateLibreOffice first to exit any running instances of LibreOffice !DONE!
    #if possible it should also prompt the user to save their work.
    #This script also needs to deal with the port not being available.
    libreCall.deactivateLibreOffice()
    libreCall.activateLibreOffice()
    desktop = pyoo.Desktop('localhost', port)

    if amHome == True:
        doc = desktop.open_spreadsheet(home['osdPath'])

    else:
        doc = desktop.open_spreadsheet(away['osdPath'])

    x = readLibre(doc)
    writeCSV(x, myPath)
    doc.close()
    libreCall.deactivateLibreOffice()