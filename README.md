# Pleiades
A python script to run on a server that allows, via the use of cloud storage, computationally heavy python scripts to be offloaded to a different machine

The file structure is citical to its function:
the "Control.txt" file is there to allow remote control over the Process Manager (e.g. terminating it, wiping archives etc...).
the "To Run" folder is where the scripts to be offloaded are to be placed by the master computer (i.e. the one you're offloading from)
  Please note there is a specific structure to how these scripts must be set up (more on that later)
the "Outputs" folder is where the outputs from all the scripts will be saved with the same file name as their corresponding script
the "Computed" folder is an archive for scripts which have already been computed just to avoid deleting them

The scripts must be structured so all the computation is initialised by a "main()" function and must be spelt as such.. the output of the script must be the "Return()" of the "main()" function.

The remote controll script will be coming in a later update
I hope you find this useful :)
