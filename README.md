# folderXMLcompare

Script for comparing all the xml files in two folders with each other utilizing the **[xmldiff]([xmldiff · PyPI](https://pypi.org/project/xmldiff/))** library.

Names are not taken into account in the comparison process. Nodes in the XML files can have different places and are considered to be the same. XML files are therefore compared only semantically.

## Environment:

1. PC running Windows 10

2. VS Code with Python extension for VS Code version v2023.18.0

3. xmldiff library  version 2.6.3

## How to use:

1) test.py represents the script that compares two folders (folder1 and folder2)

2) diffTest.py was used in development to check how the xmldiff library works and can be deleted or ignored.

3) In order for the script to function, [xmldiff]([xmldiff · PyPI](https://pypi.org/project/xmldiff/)) library must be installed.
   
   1) Command for installing: `pip install xmldiff`
   
   2) Command used in Windows with VS Code: `py -m pip install xmldiff`
   
   3) With PyCharm, it can be installed using a graphical interface.

4) Folder 1 represents the folder which can contain files other than the ones being compared to in folder 2.

5) Folder 2 contains XML files that **MUST** be contained in folder 1.
   
   1) Names of the XML files is not taken into account for comparison, only the content of the XML files.

6) The script goes through each file in the folder 2 and compares it with **EVERY** file in folder 1 until a pair is found. As soon as the pair is found, comparison with other files in folder 1 is stopped in order not to waste time.

7) If any of the files in folder 2 doesn't have a pair in folder 1, the script prints out a message.

## Room for improvement:

1. Files in folder 2 found to have a pair can be skipped in further search in order not to waste time.
