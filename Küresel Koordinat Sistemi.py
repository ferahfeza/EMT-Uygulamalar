import sys
import numpy as np
import pyvista as pv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
from pyvistaqt import QtInteractor

class SphericalCoordinateVisualizer(QWidget):
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
        labels = {'r': 'Küre Yarıçapı (R)', 'theta': 'Koni Açısı (θ)', 'phi': 'Yarı Düzlem (φ)'}
        ranges = {'r': (0, 10), 'theta': (0, 180), 'phi': (0, 360)}
        initial_values = {'r': 5, 'theta': 90, 'phi': 45}
        for coord in ['r', 'theta', 'phi']:
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
        self.coord_label = QLabel("Koordinat Noktası: (r: 5.00, θ: 90.00°, φ: 45.00°)")
        self.coord_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.coord_label)

        self.setLayout(layout)

        # Set up the initial plot
        self.setup_plot()

        self.setWindowTitle('KÜRESEL KOORDİNAT SİSTEMİ')
        self.showMaximized()

    def create_sphere_surface(self, radius):
        sphere = pv.Sphere(radius=radius, theta_resolution=100, phi_resolution=100)
        return sphere

    def create_theta_surface(self, theta):
        u = np.linspace(0, 2*np.pi, 100)
        v = np.linspace(0, 10, 50)
        u, v = np.meshgrid(u, v)
        x = v * np.sin(np.radians(theta)) * np.cos(u)
        y = v * np.sin(np.radians(theta)) * np.sin(u)
        z = v * np.cos(np.radians(theta))
        return pv.StructuredGrid(x, y, z)

    def create_phi_surface(self, phi):
        u = np.linspace(0, np.pi, 100)
        v = np.linspace(0, 10, 50)
        u, v = np.meshgrid(u, v)
        x = v * np.sin(u) * np.cos(np.radians(phi))
        y = v * np.sin(u) * np.sin(np.radians(phi))
        z = v * np.cos(u)
        return pv.StructuredGrid(x, y, z)

    def create_r_theta_intersection(self, r, theta):
        u = np.linspace(0, 2*np.pi, 100)
        x = r * np.sin(np.radians(theta)) * np.cos(u)
        y = r * np.sin(np.radians(theta)) * np.sin(u)
        z = r * np.cos(np.radians(theta)) * np.ones_like(u)
        return pv.PolyData(np.column_stack((x, y, z)))

    def create_r_phi_intersection(self, r, phi):
        u = np.linspace(0, np.pi, 100)
        x = r * np.sin(u) * np.cos(np.radians(phi))
        y = r * np.sin(u) * np.sin(np.radians(phi))
        z = r * np.cos(u)
        return pv.PolyData(np.column_stack((x, y, z)))

    def setup_plot(self):
        r = self.sliders['r'].value()
        theta = self.sliders['theta'].value()
        phi = self.sliders['phi'].value()

        sphere = self.create_sphere_surface(r)
        self.r_surface = self.plotter.add_mesh(sphere, color='red', opacity=0.5)

        theta_surface = self.create_theta_surface(theta)
        self.theta_surface = self.plotter.add_mesh(theta_surface, color='green', opacity=0.5)

        phi_surface = self.create_phi_surface(phi)
        self.phi_surface = self.plotter.add_mesh(phi_surface, color='blue', opacity=0.5)

        r_theta_intersection = self.create_r_theta_intersection(r, theta)
        self.r_theta_line = self.plotter.add_mesh(r_theta_intersection, color='purple', line_width=5)

        r_phi_intersection = self.create_r_phi_intersection(r, phi)
        self.r_phi_line = self.plotter.add_mesh(r_phi_intersection, color='orange', line_width=5)

        x = r * np.sin(np.radians(theta)) * np.cos(np.radians(phi))
        y = r * np.sin(np.radians(theta)) * np.sin(np.radians(phi))
        z = r * np.cos(np.radians(theta))
        self.point = self.plotter.add_mesh(pv.Sphere(radius=0.2, center=(x, y, z)), color='yellow')

        self.plotter.camera_position = [(20, 20, 10), (0, 0, 0), (0, 0, 1)]
        self.plotter.show_axes()

    def update_plot(self):
        r = self.sliders['r'].value()
        theta = self.sliders['theta'].value()
        phi = self.sliders['phi'].value()

        self.plotter.clear()
        self.plotter.show_axes()

        sphere = self.create_sphere_surface(r)
        self.r_surface = self.plotter.add_mesh(sphere, color='red', opacity=0.5)

        theta_surface = self.create_theta_surface(theta)
        self.theta_surface = self.plotter.add_mesh(theta_surface, color='green', opacity=0.5)

        phi_surface = self.create_phi_surface(phi)
        self.phi_surface = self.plotter.add_mesh(phi_surface, color='blue', opacity=0.5)

        r_theta_intersection = self.create_r_theta_intersection(r, theta)
        self.r_theta_line = self.plotter.add_mesh(r_theta_intersection, color='purple', line_width=5)

        r_phi_intersection = self.create_r_phi_intersection(r, phi)
        self.r_phi_line = self.plotter.add_mesh(r_phi_intersection, color='orange', line_width=5)

        x = r * np.sin(np.radians(theta)) * np.cos(np.radians(phi))
        y = r * np.sin(np.radians(theta)) * np.sin(np.radians(phi))
        z = r * np.cos(np.radians(theta))
        self.point = self.plotter.add_mesh(pv.Sphere(radius=0.2, center=(x, y, z)), color='yellow')

        self.coord_label.setText(f"Point: (r: {r:.2f}, θ: {theta:.2f}°, φ: {phi:.2f}°)")

        self.plotter.render()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SphericalCoordinateVisualizer()
    sys.exit(app.exec_())