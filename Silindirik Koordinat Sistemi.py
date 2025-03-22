import sys
import numpy as np
import pyvista as pv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
from pyvistaqt import QtInteractor

class CylindricalCoordinateVisualizer(QWidget):
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
        labels = {'r': 'Silindir Yarıçapı (r)', 'phi': 'Yarı Düzlem Açısı (φ)', 'z': 'Z Düzlemi (z)'}
        ranges = {'r': (0, 10), 'phi': (0, 360), 'z': (-10, 10)}
        initial_values = {'r': 5, 'phi': 45, 'z': 0}
        for coord in ['r', 'phi', 'z']:
            slider_layout.addWidget(QLabel(labels[coord]))
            slider = QSlider(Qt.Horizontal)
            slider.setRange(*ranges[coord])
            slider.setValue(initial_values[coord])
            slider.setTickPosition(QSlider.TicksBelow)
            slider.setTickInterval((ranges[coord][1] - ranges[coord][0]) // 10)
            slider.valueChanged.connect(self.update_plot)
            self.sliders[coord] = slider
            slider_layout.addWidget(slider)

        layout.addLayout(slider_layout)

        # Create label for point coordinates
        self.coord_label = QLabel("Point: (r: 5.00, φ: 45.00°, z: 0.00)")
        self.coord_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.coord_label)

        self.setLayout(layout)

        # Set up the initial plot
        self.setup_plot()

        self.setWindowTitle('SİLİNDİRİK KOORDİNAT SİSTEMİ')
        self.showMaximized()

    def create_cylinder_surface(self, radius):
        theta = np.linspace(0, 2*np.pi, 100)
        z = np.linspace(-10, 10, 50)
        theta, z = np.meshgrid(theta, z)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return pv.StructuredGrid(x, y, z)

    def create_phi_surface(self, phi_angle):
        r = np.linspace(0, 10, 50)
        z = np.linspace(-10, 10, 50)
        r, z = np.meshgrid(r, z)
        phi_rad = np.radians(phi_angle)
        x = r * np.cos(phi_rad)
        y = r * np.sin(phi_rad)
        return pv.StructuredGrid(x, y, z)

    def create_intersection_circle(self, radius, z):
        return pv.Circle(radius=radius, resolution=100).translate((0, 0, z))

    def create_phi_intersection_line(self, radius, phi):
        phi_rad = np.radians(phi)
        start_point = (radius * np.cos(phi_rad), radius * np.sin(phi_rad), -10)
        end_point = (radius * np.cos(phi_rad), radius * np.sin(phi_rad), 10)
        return pv.Line(start_point, end_point)

    def setup_plot(self):
        r = self.sliders['r'].value()
        phi = self.sliders['phi'].value()
        z = self.sliders['z'].value()

        r_cylinder = self.create_cylinder_surface(r)
        self.r_surface = self.plotter.add_mesh(r_cylinder, color='green', opacity=0.45)

        phi_plane = self.create_phi_surface(phi)
        self.phi_surface = self.plotter.add_mesh(phi_plane, color='blue', opacity=0.5)

        plane = pv.Plane(center=(0, 0, z), direction=(0, 0, 1), i_size=20, j_size=20)
        self.z_surface = self.plotter.add_mesh(plane, color='orange', opacity=0.5)

        circle = self.create_intersection_circle(r, z)
        self.intersection_circle = self.plotter.add_mesh(circle, color='black', line_width=5)

        phi_line = self.create_phi_intersection_line(r, phi)
        self.phi_intersection_line = self.plotter.add_mesh(phi_line, color='purple', line_width=5)

        x = r * np.cos(np.radians(phi))
        y = r * np.sin(np.radians(phi))
        self.point = self.plotter.add_mesh(pv.Sphere(radius=0.2, center=(x, y, z)), color='yellow')

        self.plotter.camera_position = [(20, 20, 10), (0, 0, 0), (0, 0, 1)]
        self.plotter.show_axes()

    def update_plot(self):
        r = self.sliders['r'].value()
        phi = self.sliders['phi'].value()
        z = self.sliders['z'].value()

        self.plotter.clear()
        self.plotter.show_axes()

        r_cylinder = self.create_cylinder_surface(r)
        self.r_surface = self.plotter.add_mesh(r_cylinder, color='black', opacity=0.25)

        phi_plane = self.create_phi_surface(phi)
        self.phi_surface = self.plotter.add_mesh(phi_plane, color='blue', opacity=0.5)

        plane = pv.Plane(center=(0, 0, z), direction=(0, 0, 1), i_size=20, j_size=20)
        self.z_surface = self.plotter.add_mesh(plane, color='orange', opacity=0.5)

        circle = self.create_intersection_circle(r, z)
        self.intersection_circle = self.plotter.add_mesh(circle, color='black', line_width=25, opacity=0.5)

        phi_line = self.create_phi_intersection_line(r, phi)
        self.phi_intersection_line = self.plotter.add_mesh(phi_line, color='purple', line_width=5)

        x = r * np.cos(np.radians(phi))
        y = r * np.sin(np.radians(phi))
        self.point = self.plotter.add_mesh(pv.Sphere(radius=0.2, center=(x, y, z)), color='yellow')

        self.coord_label.setText(f"Koordinat Noktası: (r: {r:.2f}, φ: {phi:.2f}°, z: {z:.2f})")

        self.plotter.render()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CylindricalCoordinateVisualizer()
    sys.exit(app.exec_())