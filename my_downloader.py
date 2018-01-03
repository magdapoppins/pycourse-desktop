from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import urllib.request


class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        url_label = QLabel("URL Address")
        self.url = QLineEdit()
        save_label = QLabel("Save Location")
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("Save in...")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(url_label)
        layout.addWidget(self.url)
        layout.addWidget(save_label)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setWindowTitle("Generic Downloader")
        self.setFocus()

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse)

    def browse(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save file as", directory=".", filter="All Files (*.*)")
        self.save_location.setText(save_file)

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "Download failed")
            return

        QMessageBox.information(self, "Information", "Download completed")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")

    def report(self, num, size, total_size):
        progress = num * size
        if total_size > 0:
            percent = progress * 100 / total_size
            self.progress.setValue(int(percent))


app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()
