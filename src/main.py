from kivy.app import App
from kivy.core.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import webbrowser
# from FileSharer import FileSharer
import time

from src.FileSharer import FileSharer

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        """Method which turns camera on when Start camera button is pressed"""
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Method which turns camera off when stop camera button is pressed"""
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """Method which changes GUI page and stores picture as .jpg file
        in directory captured. This happens after 'Capture' button is pressed
        """
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = '../captured/' + current_time + ".png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.ids.camera.play = False
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_does_not_exist_error_message = "Create a Link First!"
    def create_link(self):
        """ Method which uploades and then generates URL of picture when
        'Create sharable link' button is pressed
        """
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        file_sharer = FileSharer(filepath=file_path)
        self.url = file_sharer.share()
        self.ids.link.text = self.url
        # print(url)

    def copy_link(self):
        """ Method which copies a link when copy link button is pressed"""
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_does_not_exist_error_message

    def open_link(self):
        """ Method which opens a link when open link button is pressed"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_does_not_exist_error_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        # cam = Camera(play=True)
        # setting the resolution when play is True causes the crash
        # cam.resolution = (320, 240)
        return RootWidget()


MainApp().run()
