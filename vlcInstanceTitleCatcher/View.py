from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QApplication, QHeaderView


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget()  # Create a QTableWidget instance
        self.setCentralWidget(self.table)  # Set the QTableWidget as the central widget of the QMainWindow

        # Set the initial window size
        self.resize(800, 600)  # Adjust the width and height as desired

        # Set the resize mode of the horizontal headers to interactive
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)


    def updateTitleStates(self, titleStates):
        self.table.setColumnCount(2)  # Set the number of columns in the table to 2
        self.table.setHorizontalHeaderLabels(['Title', 'Duplicates'])  # Set the labels for the horizontal headers
        self.table.setRowCount(len(titleStates))  # Set the number of rows in the table based on the length of titleStates

        for row, (title, stateDict) in enumerate(titleStates.items()):
            titleItem = QTableWidgetItem(title)  # Create a QTableWidgetItem with the title
            duplicatesItem = QTableWidgetItem()

            if stateDict['duplicates'] is not None:
                duplicatesCombo = QComboBox()  # Create a QComboBox instance
                duplicatesCombo.addItems(stateDict['duplicates'])  # Add items to the QComboBox
                self.table.setCellWidget(row, 1, duplicatesCombo)  # Set the QComboBox as the cell widget in column 1
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
