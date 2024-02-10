import pygetwindow as gw
import tkinter as tk
import pygetwindow as gw


def get_vlc_titles():
    windows = gw.getWindowsWithTitle('VLC media player')
    titles = [w.title for w in windows]
    return titles


titles = get_vlc_titles()
realTitles = [title.replace(' - VLC media player', '') for title in titles]
class Model:
    def __init__(self):
        pass

    def get_vlc_titles(self):
        windows = gw.getWindowsWithTitle('VLC media player')
        titles = [w.title for w in windows]
        return titles

    def get_real_titles(self):
        return [title.replace(' - VLC media player', '') for title in self.get_vlc_titles()]


class View:
    def __init__(self, root):
        self.root = root
        self.title_label = tk.Label(root, text="Real Titles:")
        self.title_label.pack()
        self.title_listbox = tk.Listbox(root)
        self.title_listbox.pack()

    def update_titles(self, titles):
        self.title_listbox.delete(0, tk.END)
        for title in titles:
            self.title_listbox.insert(tk.END, title)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.update_titles()

    def update_titles(self):
        titles = self.model.get_real_titles()
        self.view.update_titles(titles)


def main():
    model = Model()
    root = tk.Tk()
    view = View(root)
    controller = Controller(model, view)
    root.mainloop()


if __name__ == "__main__":
    main()
