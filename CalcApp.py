from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout


class CalcApp(App):

	def build(self):		
		bl = BoxLayout( orientation="vertical", 
						padding=[20, 40, 20, 20],
						spacing = 10,)

		bl.add_widget( Button(text='Тестовая кнопочка') )
		bl.add_widget( Button(text='Тестовая кнопочка') )
		bl.add_widget( Button(text='Тестовая кнопочка') )
		
		return bl

if __name__ == "__main__":
	CalcApp().run()

