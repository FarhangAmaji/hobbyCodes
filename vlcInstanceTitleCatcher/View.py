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


    def updateTitleStates(self, title_states):
        self.title_states = title_states
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Title', 'Duplicates'])
        self.table.setRowCount(len(self.title_states))

        for row, (title, state_dict) in enumerate(self.title_states.items()):
            title_item = QTableWidgetItem(title)
            duplicates_item = QTableWidgetItem()

            if state_dict['duplicates'] is not None:
                duplicates_combo = QComboBox()
                duplicates_combo.addItems(state_dict['duplicates'])
                self.table.setCellWidget(row, 1, duplicates_combo)
            else:
                duplicates_item.setText('None')
                self.table.setItem(row, 1, duplicates_item)

            self.table.setItem(row, 0, title_item)

    def resizeEvent(self, event):
        # Resize the last column to take up the remaining space in the table
        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)

        # Call the parent class's resizeEvent to ensure the rest of the UI is updated
        super().resizeEvent(event)
