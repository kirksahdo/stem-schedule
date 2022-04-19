from PyQt6 import QtWidgets, QtCore

class EventWidget(QtWidgets.QWidget):
    def __init__(self, parent, text, hour):
        super().__init__(parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("#evento{\n"
                                  "    border-bottom: 1px solid #f0f0f0;\n"
                                  "}")

        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_16.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_16.addWidget(self.label)
        self.label_2.setText(hour)
        self.label.setText(text)