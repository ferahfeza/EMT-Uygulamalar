import sys
import numpy as np
import pyvista as pv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
from pyvistaqt import QtInteractor

class PlaneIntersectionVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        # Create the PyVista plot widget
        self.plotter = QtInteractor(self)
        layout.addWidget(self.plotter)

        # Create sliders
        slider_layout = QHBoxLayout()
        self.sliders = {}
        for plane in ['X', 'Y', 'Z']:
            slider_layout.addWidget(QLabel(f"{plane} Plane:"))
            slider = QSlider(Qt.Horizontal)
            slider.setRange(-10, 10)
            slider.setValue(0)  # Set initial value to 0 (origin)
            slider.setTickPosition(QSlider.TicksBelow)
            slider.setTickInterval(1)
            slider.valueChanged.connect(self.update_plot)
            self.sliders[plane] = slider
            slider_layout.addWidget(slider)

        layout.addLayout(slider_layout)

        # Create label for intersection point coordinates
        self.coord_label = QLabel("Kesişim Noktası: (0.00, 0.00, 0.00)")
        self.coord_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.coord_label)

        self.setLayout(layout)

        # Set up the initial plot
        self.setup_plot()

        self.setWindowTitle('Kartezyen Koordinat Yüzeyleri')
        self.showMaximized()  # Start in full-screen mode

    def setup_plot(self):
        # Create planes
        self.planes = {}
        self.colors = {'X': 'green', 'Y': 'red', 'Z': 'blue'}
        for plane in ['X', 'Y', 'Z']:
            self.planes[plane] = self.create_plane(plane, 0)  # Start at origin

        # Create intersection lines
        self.lines = {}
        line_colors = {'XY': 'purple', 'XZ': 'orange', 'YZ': 'cyan'}
        for pair in ['XY', 'XZ', 'YZ']:
            line = pv.Line([-10, -10, -10], [10, 10, 10])
            self.lines[pair] = self.plotter.add_mesh(line, color=line_colors[pair], line_width=3)

        # Create intersection point
        point = pv.PolyData(np.array([[0, 0, 0]], dtype=np.float32))
        self.point = self.plotter.add_mesh(point, color='yellow', point_size=15)

        # Set up the camera
        self.plotter.camera_position = [(20, 20, 20), (0, 0, 0), (0, 0, 1)]
        self.plotter.show_axes()

    def create_plane(self, plane, value):
        if plane == 'X':
            origin = (value, 0, 0)
            normal = (1, 0, 0)
        elif plane == 'Y':
            origin = (0, value, 0)
            normal = (0, 1, 0)
        else:  # Z plane
            origin = (0, 0, value)
            normal = (0, 0, 1)
        
        plane_mesh = pv.Plane(center=origin, direction=normal, i_size=20, j_size=20)
        return self.plotter.add_mesh(plane_mesh, color=self.colors[plane], opacity=0.5)

    def update_plot(self):
        x, y, z = [self.sliders[plane].value() for plane in ['X', 'Y', 'Z']]

        # Update planes
        for plane, value in zip(['X', 'Y', 'Z'], [x, y, z]):
            self.plotter.remove_actor(self.planes[plane])
            self.planes[plane] = self.create_plane(plane, value)

        # Update intersection lines
        self.lines['XY'].GetMapper().GetInput().points = np.array([[x, y, -10], [x, y, 10]], dtype=np.float32)
        self.lines['XZ'].GetMapper().GetInput().points = np.array([[x, -10, z], [x, 10, z]], dtype=np.float32)
        self.lines['YZ'].GetMapper().GetInput().points = np.array([[-10, y, z], [10, y, z]], dtype=np.float32)

        # Update intersection point
        self.point.GetMapper().GetInput().points = np.array([[x, y, z]], dtype=np.float32)

        # Update coordinate label
        self.coord_label.setText(f"Intersection Point: ({x:.2f}, {y:.2f}, {z:.2f})")

        # Update the plot
        self.plotter.render()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PlaneIntersectionVisualizer()
    sys.exit(app.exec_())