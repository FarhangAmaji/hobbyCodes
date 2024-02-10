import pygetwindow as gw


class Model:
    def __init__(self):
        pass

    def getVlcTitles(self):
        windows = gw.getWindowsWithTitle('VLC media player')
        titles = [w.title for w in windows]
        return titles

    def getRealTitles(self):
        return [title.replace(' - VLC media player', '') for title in self.getVlcTitles()]
