import kivy
kivy.require('1.10.0')

from kivy.app import App
#from kivy.uix.button import Label
from kivy.uix.button import Button

class HelloKivy(App):
	def build(self):
		return Button(text = "Add daily task", size=(150, 50), size_hint=(None, None), pos_hint={'center_x':0.5, 'center_y':0.5})

helloKivy = HelloKivy()
helloKivy.run()