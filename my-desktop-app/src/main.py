from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys
# un comentario no esta demas
#otro comentario no esta demas

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
