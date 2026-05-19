from Qt.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QWidget,
    QHBoxLayout,
    QTextEdit,
    QDialogButtonBox,
)
from Qt.QtCore import Qt


class AssetPublishDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Publish Asset")
        self.resize(600, 300)

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self.build_header()
        self.build_description()
        self.build_buttons()

    def build_header(self):
        """Add the title"""
        title = QLabel("Publish Asset")
        title.setStyleSheet("font-size: 24px; font-weight: 700;")
        title.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(title)

    def build_description(self):
        """Add the version title and description fields"""
        # Version title row
        self.version_title_row = QWidget()
        version_title_layout = QHBoxLayout(self.version_title_row)

        version_title_layout.addWidget(QLabel("Version Title"))

        self.version_title = QLineEdit()
        self.version_title.setPlaceholderText("Title...")
        version_title_layout.addWidget(self.version_title)

        self._layout.addWidget(self.version_title_row)

        # Version description note field
        self.note_field = QTextEdit()
        self.note_field.setPlaceholderText("Optional details about this version...")

        self._layout.addWidget(self.note_field)

    def build_buttons(self):
        """Create the Publish and Cancel buttons"""
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.output_contents)
        button_box.rejected.connect(self.reject)

        self._layout.addWidget(button_box)

    def output_contents(self):
        """For now, just prints the contents of the text fields"""
        print(self.version_title.text())
        description = self.note_field.toPlainText()
        if description != "":
            print(description)

        self.accept()
