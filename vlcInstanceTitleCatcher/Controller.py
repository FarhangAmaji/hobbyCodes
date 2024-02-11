import os

from vlcInstanceTitleCatcher.utils import removeExtension


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.updateTitles()

    def checkTitleStates(self, titles):
        titleStates = {}

        for title in titles:
            title = removeExtension(title)
            duplicates = None
            if title in self.model.directories.fileInfos['fileName'].values:
                state = "single file"
                if title in self.model.directories.duplicateFiles.keys():
                    state = "has duplicates"
                    duplicates_ = self.model.directories.duplicateFiles[title]
                    duplicates = []
                    for file in duplicates_:
                        if file['subDir'] != '.':
                            duplicatePath = os.path.join(file['rootDir'], file['subDir'],
                                                          file['fileName'] + file['fileExtension'])
                        else:
                            duplicatePath = os.path.join(file['rootDir'],
                                                          file['fileName'] + file['fileExtension'])
                        duplicates.append(duplicatePath)
            else:
                state = "Not found"
            titleStates[title] = {'state': state, 'duplicates': duplicates}

        return titleStates

    def updateTitles(self):
        titles = self.model.getRealTitles()
        titleStates = self.checkTitleStates(titles)

        self.view.updateTitleStates(titleStates)
