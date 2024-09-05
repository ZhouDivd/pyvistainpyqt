import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from pyvistaqt import QtInteractor
import pyvista as pv

class MainWindow(QMainWindow):
    def __init__(self, parent=None, show=True):
        QMainWindow.__init__(self, parent)

        # 创建一个中心部件和一个垂直布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # 创建一个PyVista QtInteractor部件并添加到布局中
        self.plotter = QtInteractor(self)
        layout.addWidget(self.plotter.interactor)
        # 设置窗口标题
        self.setWindowTitle("PyVista Qt Example")
        # 设置窗口大小
        self.resize(800, 600)
        #设置窗口背景为黑色
        self.plotter.background_color = "black"
    
        #循环添加菜单，菜单栏为列表[File, Edit, View, Tools, Help],
        menu_bar = self.menuBar()
        for menu_name in ["File", "Edit", "View", "Tools", "Help"]:
            menu = menu_bar.addMenu(menu_name)
    
        #在左侧添加一个垂直布局，水平宽度为200，竖向宽度为600
        left_layout = QVBoxLayout()
  
        # 设置中心部件
        self.setCentralWidget(central_widget)
        #设置pyvista布局为2*3
       
        # 创建一个示例3D圆柱体并添加到场景中
        
        cylinder = pv.Cylinder(radius=1, height=2, center=(0, 0, 0))

        self.plotter.add_mesh( cylinder)

        if show:
            self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())