from kivy.app import App
from kivy.uix.widget import Widget


class PonGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PonGame()


if __name__ == '__main__':
    PongApp().run()
