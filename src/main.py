from kivy.app import App
from kivy.core.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
# from FileSharer import FileSharer
import time

from src.FileSharer import FileSharer

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
        self.filepath = '../captured/' + current_time + ".png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        file_sharer = FileSharer(filepath=file_path)
        url = file_sharer.share()
        self.ids.link.text = url
        # print(url)



class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        # cam = Camera(play=True)
        # setting the resolution when play is True causes the crash
        # cam.resolution = (320, 240)
        return RootWidget()


MainApp().run()
