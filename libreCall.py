import subprocess
import time

def activateLibreOffice(port): #This needs to take in to account port numbers
    port = str(port)
    print("activating temporary instance of LibreOffice!!!")
    subprocess.run("soffice --accept=\"socket,host=localhost,port={};urp;\" --headless &".format(port), check=True, shell=True)
    print("running SLEEP for (5) secs to validate code has processed.")
    time.sleep(5)#I'm using sleep to validate the code went through.  
    #This needs to return something to verify process was actually called.
    #I could run a while loop with p1....statement could be while len(pid) == 0: p1
    p1 = subprocess.run("pidof soffice.bin", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pid = p1.stdout.decode("utf-8").rstrip("\n")#This praticular call is pretty complex. INFO below.
    print("Instance of LibreOffice activated @ PID: {}".format(pid))
    print("activateLibreOffice().....complete!")

def deactivateLibreOffice():
   #This should branch and run a check whether libreoffice is running at all.
    print("running deactivateLibreOffice now....")
    print("closing any active instances of LibreOffice NOW!!!")
    p2 = subprocess.run("pidof soffice.bin", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pid = p2.stdout.decode("utf-8").rstrip("\n")#This praticular call is pretty complex. INFO below.
    if len(pid) != 0:
        print("instance of LibreOffice running at PID: {}".format(pid))
        print("killing process.")
        subprocess.run("kill {}".format(pid), shell=True, check=True)
    
    else:
        print("No instances of LibreOffice running....")
        print("Continuing OCTADOC protocols!")
  
    print("deactivateLibreOffice().......complete!")
    """
        stdout is a property of the subprocess class.  It returns a byte object
        decode converts the byte object to a string using utf-8 encoding
        for some reason the string contains a \n at the end. So rstrip removes that.
    """




