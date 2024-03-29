from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QHeaderView, \
    QWidget, QLabel, QVBoxLayout, QFrame


class View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.controller = None

        # Create the main layout with equal heights for upper and lower parts
        main_layout = QVBoxLayout()

        # Initialize the table widget for upper part
        self.table = QTableWidget()
        # Connect the slot to the signal
        self.table.itemSelectionChanged.connect(self.onSelectionChanged)

        lower_widget = QWidget()  # Create a QWidget for the lower part
        lower_layout = QVBoxLayout()
        lower_widget.setLayout(lower_layout)  # Set the layout for the lower widget
        main_layout.addWidget(self.table, stretch=1)  # Add widgets to the main layout
        main_layout.addWidget(lower_widget, stretch=1)

        # Create a red frame for the lower part background
        red_frame = QFrame()
        red_frame.setStyleSheet("background-color: red; border: 1px solid black;")
        lower_layout.addWidget(red_frame)  # Add the red frame to the lower layout

        # Create a layout for the labels within the red frame
        self.fileInfosLayout = QVBoxLayout()
        red_frame.setLayout(self.fileInfosLayout)

        # Set the main layout as the central widget's layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Set initial window size and resize mode
        self.resize(800, 600)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

    def updateTitleStates(self, titleStates):
        self.last_titleStates = titleStates
        self.table.setColumnCount(2)  # Set the number of columns in the table to 2
        self.table.setHorizontalHeaderLabels(
            ['Title', 'Duplicates'])  # Set the labels for the horizontal headers
        self.table.setRowCount(
            len(titleStates))  # Set the number of rows in the table based on the length of titleStates

        for row, (title, stateDict) in enumerate(titleStates.items()):
            titleItem = QTableWidgetItem(title)  # Create a QTableWidgetItem with the title
            duplicatesItem = QTableWidgetItem()

            if stateDict['duplicates'] is not None:
                duplicatesCombo = QComboBox()  # Create a QComboBox instance
                duplicatesCombo.addItems(stateDict['duplicates'])  # Add items to the QComboBox
                self.table.setCellWidget(row, 1,
                                         duplicatesCombo)  # Set the QComboBox as the cell widget in column 1
            else:
                none_label = QLabel('None')
                none_label.setAlignment(Qt.AlignCenter)
                self.table.setCellWidget(row, 1,
                                         none_label)  # Set the QLabel as the cell widget in column 1

            self.table.setItem(row, 0, titleItem)  # Set the QTableWidgetItem in column 0

    def resizeEvent(self, event):
        # Resize the last column to take up the remaining space in the table
        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)

        # Call the parent class's resizeEvent to ensure the rest of the UI is updated
        super().resizeEvent(event)

    def onSelectionChanged(self):
        # Clear the layout
        while self.fileInfosLayout.count():
            child = self.fileInfosLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Get the title of the selected row
        current_row = self.table.currentRow()
        title_item = self.table.item(current_row, 0)  # Get the 'Title' cell of the selected row
        if title_item:
            title = title_item.text()
            # find the key in the last_titleStates == title
            stateDict = self.last_titleStates[title]

            # Create a label with the title and add it to the layout
            title_label = QLabel(title)
            title_label.setAlignment(Qt.AlignLeft)  # Center the label
            self.fileInfosLayout.addWidget(title_label)

            # Create a label with the state and add it to the layout
            state_label = QLabel(stateDict['state'])
            state_label.setAlignment(Qt.AlignLeft)
            self.fileInfosLayout.addWidget(state_label)

            # If there are duplicates, create a label for each one and add them to the layout
            if stateDict['duplicates'] is not None:
                for duplicate in stateDict['duplicates']:
                    duplicate_label = QLabel(duplicate)
                    duplicate_label.setAlignment(Qt.AlignLeft)
                    self.fileInfosLayout.addWidget(duplicate_label)
            else:
                none_label = QLabel('None')
                none_label.setAlignment(Qt.AlignLeft)
                self.fileInfosLayout.addWidget(none_label)

    def setController(self, controller):
        self.controller = controller

    def changeEvent(self, event):
        if event.type() == QEvent.ActivationChange and self.isActiveWindow() and self.controller:
            self.controller.updateTitles()
        super().changeEvent(event)
