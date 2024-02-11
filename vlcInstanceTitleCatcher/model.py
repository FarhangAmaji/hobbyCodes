import os

import pandas as pd
import pygetwindow as gw


class Directories:
    def __init__(self, directories):
        self.directories = directories
        self.fileInfos = self.processDirectories()
        self.duplicateFiles = self.findDuplicateFiles()

    def findDuplicateFiles(self):
        duplicateFileNames = {}
        df = self.fileInfos
        duplicate_files = df[df.duplicated(subset='fileName', keep=False)]
        for _, row in duplicate_files.iterrows():
            file_name = row['fileName']
            if file_name not in duplicateFileNames:
                duplicateFileNames[file_name] = []
            duplicateFileNames[file_name].append(row.to_dict())
        return duplicateFileNames

    def processDirectories(self):
        fileInfoList = []
        for directory in self.directories:
            for root_dir, sub_dirs, files in os.walk(directory):
                for file in files:
                    file_name = os.path.splitext(file)[0]
                    file_extension = os.path.splitext(file)[1]
                    file_info = {
                        'fileName': file_name,
                        'rootDir': root_dir,
                        'subDir': os.path.relpath(root_dir, directory),
                        'fileExtension': file_extension
                    }
                    fileInfoList.append(file_info)
        df = pd.DataFrame(fileInfoList)
        return df
class VlcTitleCatcher:
    def getVlcTitles(self):
        windows = gw.getWindowsWithTitle('VLC media player')
        titles = [w.title for w in windows]
        return titles

    def getRealTitles(self):
        return [title.replace(' - VLC media player', '') for title in self.getVlcTitles()]

class Model:
    def __init__(self, directories):
        self.directories = Directories(directories)
        self.vlcTitleCatcher = VlcTitleCatcher()

    def getRealTitles(self):
        return self.vlcTitleCatcher.getRealTitles()

    def processDirectories(self):
        return self.directories.fileInfos

    def findDuplicateFiles(self):
        return self.directories.duplicateFiles
# z = Model([r'E:\vids\paint\uncat', r'I:\musicvideo']).processDirectories()
z2 = Model([r'E:\vids\paint\uncat', r'I:\musicvideo']).findDuplicateFiles()
