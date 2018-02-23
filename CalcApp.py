from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class CalcApp(App):

    def pressing(self):  # вставляет символы в лейбл
        self.formula += str(isinstance)
        print(self.formula)

    def result(self)  # выполняет калькуляцию
        pass

    def build(self):

        bl = BoxLayout(orientation='vertical', padding=30)

        gl = GridLayout(cols=4, padding=4, spacing=2, size_hint=(1, .60))

        self.lbl = Label(text='232131231230adsasdasdaasa', font_size=30,
                         halign='right', valign='center',
                         size_hint=(1, .4), text_size=(370, 170))

        bl.add_widget(self.lbl)

        # gl.add_widget(Button(text='%'))
        # gl.add_widget(Button(text='sqrt(x)'))
        # gl.add_widget(Button(text='Х^2'))
        # gl.add_widget(Button(text='1/x'))

        # gl.add_widget(Button(text='CE'))
        # gl.add_widget(Button(text='C'))
        # gl.add_widget(Button(text='<='))
        # gl.add_widget(Button(text='/'))

        gl.add_widget(Button(text='7', on_press=self.pressing))
        gl.add_widget(Button(text='8', on_press=self.pressing))
        gl.add_widget(Button(text='9', on_press=self.pressing))
        gl.add_widget(Button(text='*', on_press=self.pressing))

        gl.add_widget(Button(text='4', on_press=self.pressing))
        gl.add_widget(Button(text='5', on_press=self.pressing))
        gl.add_widget(Button(text='6', on_press=self.pressing))
        gl.add_widget(Button(text='-', on_press=self.pressing))

        gl.add_widget(Button(text='1', on_press=self.pressing))
        gl.add_widget(Button(text='2', on_press=self.pressing))
        gl.add_widget(Button(text='3', on_press=self.pressing))
        gl.add_widget(Button(text='+', on_press=self.pressing))

        gl.add_widget(Button(text='.', on_press=self.pressing))
        gl.add_widget(Button(text='0', on_press=self.pressing))
        gl.add_widget(Button(text='='))
        gl.add_widget(Button(text='/', on_press=self.pressing))

        bl.add_widget(gl)

        return bl


if __name__ == "__main__":
    CalcApp().run()
