import imp
from turtle import width
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
# from kivy.uix.carousel import Carousel
# from kivy.uix.checkbox import CheckBox


# define defference screen
class FirstWindow(Screen):
    pass


class SecondWinow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# Designate Our .kv design file
kv = Builder.load_file('main.kv')


class AwesomeApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    AwesomeApp().run()
