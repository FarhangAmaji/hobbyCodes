import os

from vlcInstanceTitleCatcher.utils import removeExtension


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.updateTitles()

    def checkTitleStates(self, titles):
        title_states = {}

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
                            duplicate_path = os.path.join(file['rootDir'], file['subDir'],
                                                          file['fileName'] + file['fileExtension'])
                        else:
                            duplicate_path = os.path.join(file['rootDir'],
                                                          file['fileName'] + file['fileExtension'])
                        duplicates.append(duplicate_path)
            else:
                state = "Not found"
            title_states[title] = {'state': state, 'duplicates': duplicates}

        return title_states

    def updateTitles(self):
        titles = self.model.getRealTitles()
        title_states = self.checkTitleStates(titles)

        self.view.updateTitleStates(title_states)
