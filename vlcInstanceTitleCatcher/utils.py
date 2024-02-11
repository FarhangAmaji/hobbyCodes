def removeExtension(fileName):
    if '.' in fileName:
        return fileName[:fileName.rindex('.')]
    else:
        return fileName
