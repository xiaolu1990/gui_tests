import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.path)
window = QWidget()
window.setGeometry(100, 100, 400, 300)
window.setWindowTitle("PyQt5")
window.show()

sys.exit(app.exec_())