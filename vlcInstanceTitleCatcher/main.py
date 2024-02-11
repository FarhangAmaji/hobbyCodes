import sys

from PyQt5.QtWidgets import QApplication

from vlcInstanceTitleCatcher.Controller import Controller
from vlcInstanceTitleCatcher.View import View
from vlcInstanceTitleCatcher.model import Model


def main():
    app = QApplication(sys.argv)  # Create the QApplication object
    try:
        model = Model([r'E:\vids\paint\uncat', r'I:\musicvideo'])
        view = View()
        # kkk
        #  review and relearn how the relationship between Controller and model
        #  and view should be; which one takes others as argument
        # kkk
        #  note the controller here doesn't do anything except it take self.updateTitles() in its init
        controller = Controller(model, view)
        view.show()  # Make the view visible

        sys.exit(app.exec_())  # Start the event loop
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
