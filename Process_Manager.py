#importing all required modules
import time     #enables the pause to limit CPU utilization
import os       #enables some managment of files
import shutil   #enables the movement of files
import threading
#Defining local paths to folders for files
Scource = "To Run"      #Path for task list
Sink = "Computed"       #Path for archived tasks
Output = "Outputs"      #Path for task outputs

#defining global for output
Out = False
FullFile = False
DirSize = len(os.listdir())

#Intitialising the main loop Flag
Running = True

#Adding awesome startup text!
print("""  ____  _      _           _           
 |  _ \| | ___(_) __ _  __| | ___  ___ 
 | |_) | |/ _ \ |/ _` |/ _` |/ _ \/ __|
 |  __/| |  __/ | (_| | (_| |  __/\__ \\
 |_|   |_|\___|_|\__,_|\__,_|\___||___/
                                       \n\n\n\n""")

#Defining fuction to locate and validate the first task
def Task():
    try:
        file = os.listdir(Scource)[0]                   #attempts to name the top task
    except IndexError:                                  #Handles the error of an empty task list
        return (False)                                  #Returns an invalid flag
    if str(file[len(file)-3:len(file)]) != ".py":       #Checks to see if the task is a python file
        return (False)                                  #Returns an invalid flag if the file is not valid
    else: return(file)                                  #Returns the file name if the file is valid

#Definig a function to run the task as a thread
def run(file):
    global Out                      #Enables changes to the task output flag
    if not Out:                     #Chacks to see that the task output flag is reset
        script = __import__(file)   #Imports the task as a module
        Output = script.main()      #Sets a local varialbe to run the task
        Out = Output                #Sets the task output flag to the task output


#Defining fuction to rprocess commands from the remote control file
def control():
    global Running                      #Ensures access to the main loop flag
    inst = open("control.txt","r")      #Opens remote control file
    cmd = str(inst.read())              #Offloads commands to a local variable
    inst.close()                        #Close the remote command file
    if cmd == "Kill":                   #If the kill command is present
        print("\n\nclosing program")        #Notify that the program is closing
        Running = False                     #Change the main loop flag to kill the program

#Initialising main loop
while Running:
    check = Task()
    if check and DirSize >= len(os.listdir()):    #Verifies that there is a task to be executed and no task is currently being executed
        FullFile = check                          #Gathers the first task name including ".py"
        print("Running '"+ FullFile + "'")                      #Notifies the fact that the task has started to be processed
        File =str(FullFile[:len(FullFile)-3])                   #Gathers the file name without the ".py"
        FileOut = (File+".txt")                                 #Creates the name for the output file
        FullPathScource = (Scource +"/"+FullFile)               #Creates the local path for where to gather the task from
        FullPathSink    = (Sink    +"/"+FullFile)               #Creates the local path for where to archive the task to
        FullPathOutput  = (Output  +"/"+FileOut)                #Creates the local path for where to save the output to
        shutil.move(FullPathScource,FullFile)                   #Moves the file from the source to the root folder
        t = threading.Thread(target=run, args = (str(File),))   #Creates a thread in which to execute the task
        t.start()                                               #Starts the thread
    if Out != False:                            #Checks if the task output is flagged
        output = open(FileOut,"w")                      #Creates the output file
        output.write(Out)                               #Writes the task output to the output file
        output.close()                                  #Closes the output file
        print("Script completed")                       #Notifies the scripts completion
        shutil.move(FileOut,FullPathOutput)             #Moves output file to storage location
        shutil.move(FullFile,FullPathSink)              #Moves task to archive
        Out = False                                     #Resets the task output flag

    control()                                   #Calls the process to check remote commands
    #time.sleep(0.01)                            #Allows time for syncing of remote commands and limits CPU usage for background tasks
    