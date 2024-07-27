import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget


class Page(Widget):
    def transform(self):
        try:
            self.ids.Number_Entry_bin.text = bin(int(self.ids.Number_Entry_dec.text)).removeprefix("0b")
        except: self.ids.Number_Entry_bin.text = ""
    def transformb(self):
        try:
            binary = self.ids.Number_Entry_bin.text
            self.ids.Number_Entry_dec.text = str(int(binary,2))
        except:pass



class BinApp(App):
    def build(self):
        return Page()

Window.clearcolor = (0.118,0.118,0.118,1)
Window.size = (420,420)

if __name__ == '__main__':
    BinApp().run()