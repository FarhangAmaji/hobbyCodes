def removeExtension(file_name):
    if '.' in file_name:
        return file_name[:file_name.rindex('.')]
    else:
        return file_name

