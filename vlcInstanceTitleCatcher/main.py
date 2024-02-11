import sys

from PyQt5.QtWidgets import QApplication

from vlcInstanceTitleCatcher.Controller import Controller
from vlcInstanceTitleCatcher.View import View
from vlcInstanceTitleCatcher.model import Model


# kkk alireza jj which is a duplicate in subDir doesnt have dropdown
def main():
    app = QApplication(sys.argv)  # Create the QApplication object
    try:
        model = Model([r'E:\vids\paint\uncat', r'I:\musicvideo'])
        view = View()
        controller = Controller(model, view)
        view.show()  # Make the view visible

        sys.exit(app.exec_())  # Start the event loop
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
