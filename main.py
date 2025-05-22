import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class HelloKivy(App):
    def build(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='center')

        btn1 = Button(text="Add daily task", size_hint=(None, None), size=(200, 50))
        btn2 = Button(text="View tasks", size_hint=(None, None), size=(200, 50))

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

helloKivy = HelloKivy()
helloKivy.run()
