from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QHeaderView, \
    QWidget, QLabel, QVBoxLayout, QFrame



class View(QMainWindow):
    def __init__(self):
        super().__init__()

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
                duplicatesItem.setText('None')  # Set the text of the QTableWidgetItem to 'None'
                self.table.setItem(row, 1, duplicatesItem)  # Set the QTableWidgetItem in column 1

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
        selected_items = self.table.selectedItems()
        if selected_items:
            title = selected_items[0].text()

            # Create a label with the title and add it to the layout
            title_label = QLabel(title)
            title_label.setAlignment(Qt.AlignCenter)  # Center the label
            self.fileInfosLayout.addWidget(title_label)
