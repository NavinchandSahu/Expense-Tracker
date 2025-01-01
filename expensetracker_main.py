# Running the app
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from expensetracker_database import init_db
from expensetracker_app import ExpenseApp

def main():
    app = QApplication(sys.argv)

    if not init_db("expensetracker.sql"):
        QMessageBox.critical(None,"Error","Could not load your database")
        sys.exit(1)


    window = ExpenseApp()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
