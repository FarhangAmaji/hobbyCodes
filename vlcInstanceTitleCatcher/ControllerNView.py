import os
import tkinter as tk

from vlcInstanceTitleCatcher.model import Model
from vlcInstanceTitleCatcher.utils import removeExtension


class View:
    def __init__(self, root):
        self.root = root
        self.titleLabel = tk.Label(root, text="Real Titles:")
        self.titleLabel.pack()
        self.titleListbox = tk.Listbox(root)
        self.titleListbox.pack(fill=tk.BOTH, expand=True)

    def updateTitles(self, titles):
        self.titleListbox.delete(0, tk.END)
        for title in titles:
            self.titleListbox.insert(tk.END, title)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.updateTitles()

    def checkTitleStates(self, titles):
        title_states = {}

        for title in titles:
            title = removeExtension(title)
            if title in self.model.directories.fileInfos['fileName'].values:
            duplicates = None
                state = "single file"
                    state = "has duplicates"
                if title in self.model.directories.duplicateFiles.keys():
                    duplicates_ = self.model.directories.duplicateFiles[title]
                    duplicates = []
                        if file['subDir'] != '.':
                    for file in duplicates_:
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

        self.view.updateTitles(titles)


def main():
    model = Model([r'E:\vids\paint\uncat', r'I:\musicvideo'])
    root = tk.Tk()
    root.geometry("500x400")
    view = View(root)
    controller = Controller(model, view)
    root.mainloop()


if __name__ == "__main__":
    main()
