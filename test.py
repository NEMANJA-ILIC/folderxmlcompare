from os import listdir
from xmldiff import main

folder1path='folder1'
folder2path='folder2'   # All of these files need to be in folder1

# Get list of all files from folder 1
folder1=listdir(folder1path)

# Get list of all files from folder 2
folder2=listdir(folder2path)

# Compare all the elements from the folder 2 with all the elements from folder1
allFilesSame=True
for file2 in folder2:
    location2="./"+folder2path+'/'+file2
    comparisonResult=[]
    filesAreTheSame=False
    # Search for the matching file in folder 1
    for file1 in folder1:
        location1="./"+folder1path+'/'+file1    # TODO: Maybe change '\\' to '/'

        # Once the location of both files has been determened, compare them
        comparisonResult=main.diff_files(location1, location2)

        if (len(comparisonResult) != 0):
            # Files not identical, check if maybe just the nodes are in the different order
            # Go through all of the differences present in the list and count the number of MoveNode changes
            numberOfMoveNodes=0
            for difference in comparisonResult:
                if difference.__class__.__name__ == "MoveNode":
                    numberOfMoveNodes+=1

            if (len(comparisonResult) != numberOfMoveNodes):
                filesAreTheSame=False 
                continue    # Move to the next file in folder 1
            else:
                filesAreTheSame=True    # All the differences are just the nodes being moved arround
                break   # Move to the next file in folder 2
        else:
            filesAreTheSame=True    # Files are identical
            break   # Found the match, no need to itterate further

    if (filesAreTheSame == False):
        print(location2 + " not OK!")
        allFilesSame=False

if (allFilesSame==False):
    print("Some files are different!")
else:
    print("All files are the SAME!")
    