from kivy.app import App
from kivy.core.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
# from FileSharer import FileSharer
import time

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        filename = current_time + ".png"
        self.ids.camera.export_to_png('../captured/'+filename)
        self.manager.current = 'image_screen'


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        # cam = Camera(play=True)
        # setting the resolution when play is True causes the crash
        # cam.resolution = (320, 240)
        return RootWidget()


MainApp().run()
