import os

import pygetwindow as gw


class Model:
    def __init__(self, directories):
        self.directories = directories

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
        return fileInfoList

    def getVlcTitles(self):
        windows = gw.getWindowsWithTitle('VLC media player')
        titles = [w.title for w in windows]
        return titles

    def getRealTitles(self):
        return [title.replace(' - VLC media player', '') for title in self.getVlcTitles()]


z=Model([r'E:\vids\paint\uncat', r'I:\musicvideo']).processDirectories()
