from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QApplication, QHeaderView


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget()
        self.setCentralWidget(self.table)

        # Set the initial window size
        self.resize(800, 600)  # Adjust the width and height as desired

        # Set the resize mode of the horizontal headers to interactive
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)


    def updateTitleStates(self, titleStates):
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Title', 'Duplicates'])
        self.table.setRowCount(len(titleStates))

        for row, (title, stateDict) in enumerate(titleStates.items()):
            titleItem = QTableWidgetItem(title)
            duplicatesItem = QTableWidgetItem()

            if stateDict['duplicates'] is not None:
                duplicatesCombo = QComboBox()
                duplicatesCombo.addItems(stateDict['duplicates'])
                self.table.setCellWidget(row, 1, duplicatesCombo)
            else:
                duplicatesItem.setText('None')
                self.table.setItem(row, 1, duplicatesItem)

            self.table.setItem(row, 0, titleItem)

    def resizeEvent(self, event):
        # Resize the last column to take up the remaining space in the table
        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)

        # Call the parent class's resizeEvent to ensure the rest of the UI is updated
        super().resizeEvent(event)
