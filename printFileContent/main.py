"""
this is useful to pass file content to chatGpt
"""
import os

import pyperclip

fullPathsOfFiles = r"""
F:\projects\public github projects\private repos\hubbyCodes\vlcInstanceTitleCatcher\Controller.py

F:\projects\public github projects\private repos\hubbyCodes\vlcInstanceTitleCatcher\View.py

"""
fullPathsOfFiles = fullPathsOfFiles.split('\n')
fullPathsOfFiles = [path for path in fullPathsOfFiles if path]
# open each file and read its content
finalText = ""
for i, path in enumerate(fullPathsOfFiles):
    with open(path, 'r') as file:
        fileContent = file.read()
        # remove empty lines from the file content
        fileContent = '\n'.join([line for line in fileContent.split('\n') if line])
        # also rstrip each line
        fileContent = '\n'.join([line.rstrip() for line in fileContent.split('\n')])
        finalText += '"' * 3 + os.path.basename(path) + '\n'
        finalText += fileContent + '\n' + '"' * 3+'\n'
        if i != len(fullPathsOfFiles) - 1:
            finalText += "-"*25+'\n'

# move the final text to clipboard
pyperclip.copy(finalText)

