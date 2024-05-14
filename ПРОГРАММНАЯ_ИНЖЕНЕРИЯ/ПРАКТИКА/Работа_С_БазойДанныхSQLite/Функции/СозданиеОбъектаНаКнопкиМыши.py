from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QPolygonF
from PySide6.QtCore import Qt, QPointF, QPoint
import random
import sys


class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисование фигур")

