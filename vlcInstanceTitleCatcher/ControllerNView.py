import tkinter as tk

from vlcInstanceTitleCatcher.model import Model

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

    def updateTitles(self):
        titles = self.model.getRealTitles()
        self.view.updateTitles(titles)


def main():
    model = Model()
    root = tk.Tk()
    root.geometry("500x400")
    view = View(root)
    controller = Controller(model, view)
    root.mainloop()


if __name__ == "__main__":
    main()