from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QPolygonF
from PySide6.QtCore import Qt, QPointF, QPoint
import random
import sys


# Хранениеее информации о нарисованных фигурах
class Shape:
    def __init__(self, shape_type, position, size, color):
        self.shape_type = shape_type
        self.position = position
        self.size = size
        self.color = color


# Главный виджет, который будет обрабатывать события и рисовать фигуры
class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисование фигур")
        self.shapes = []  # Список фигур, которые будут нарисованы на виджете
        self.rel_mouse = ''

    def random_color(self):
        # Генерирует случайный цвет
        return QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def mouseReleaseEvent(self, event):
        self.rel_mouse = ''
        position = event.position()
        size = random.randint(20, 60)
        color = self.random_color()
        if event.button() == Qt.MouseButton.LeftButton:
            self.shapes.append(Shape("circle", position, size, color))
        elif event.button() == Qt.MouseButton.RightButton:
            self.shapes.append(Shape("square", position, size, color))
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.rel_mouse = 'left'
        elif event.button() == Qt.MouseButton.RightButton:
            self.rel_mouse = 'right'

    def mouseMoveEvent(self, event):
        # Обработка нажатия кнопки мыши
        position = event.position()  # Используем position() вместо устаревшего x() и y()
        size = random.randint(20, 60)
        color = self.random_color()

        if self.rel_mouse == 'left':
            # Если нажата левая кнопка мыши, рисуем круг
            self.shapes.append(Shape("circle", position, size, color))
        elif self.rel_mouse == 'right':
            # Если нажата правая кнопка мыши, рисуем квадрат
            self.shapes.append(Shape("square", position, size, color))
        self.update()  # Обновляем виджет, чтобы нарисовать фигуру

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            position = self.mapFromGlobal(self.cursor().pos())  # Используйте mapFromGlobal
            size = random.randint(20, 60)
            color = self.random_color()
            self.shapes.append(Shape("triangle", position, size, color))

        elif event.key() == Qt.Key.Key_C:
            position = self.mapFromGlobal(QPoint(1920/2, 1080/2))
            # Используйте mapFromGlobal
            size = 1920
            color = QColor(255, 255, 255)
            self.shapes.append(Shape("clear_pole", position, size, color))
        self.update()  # Обновляем виджет, чтобы нарисовать фигуру

    def paintEvent(self, event):
        # Отрисовка фигур на виджете
        painter = QPainter(self)
        for shape in self.shapes:
            painter.setBrush(shape.color)
            position = shape.position  # Убедитесь, что это корректный атрибут
            size = shape.size
            if shape.shape_type == "circle":
                painter.drawEllipse(position.x() - size / 2, position.y() - size / 2, size, size)
            elif shape.shape_type == "triangle":
                half_size = size / 2
                points = [
                    QPointF(position.x(), position.y() - half_size),
                    QPointF(position.x() - half_size, position.y() + half_size),
                    QPointF(position.x() + half_size, position.y() + half_size),
                ]
                painter.drawPolygon(QPolygonF(points))
            elif shape.shape_type == "square":
                painter.drawRect(position.x() - size / 2, position.y() - size / 2, size, size)
            elif shape.shape_type == "clear_pole":
                painter.drawRect(position.x() - size / 2, position.y() - size / 2, size, size)

