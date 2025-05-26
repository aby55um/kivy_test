from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import datetime

class Item():
    def __init__(self, text):
        self.text = text
        self.completed = False
        self.date = datetime.datetime.now()

class TodoList(FloatLayout):
    def button_press(self, instance):
        item = Item(self.text_input.text)
        self.add_item(item)
        self.text_input.text=''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item_list = []
        self.button = Button(text="Add todo", size_hint=(.1,.05), pos=(250, 480))
        self.button.bind(on_press=self.button_press)
        self.text_input = TextInput(text="", multiline=False, size_hint=(.3,.05), pos=(350,480))
        self.add_widget(self.button)
        self.add_widget(self.text_input)

    def add_item(self, item):
        self.item_list.append(item)
        self.add_widget(Label(text=item.text, size_hint=(.1,.35), pos=(150,350 - 25 * len(self.item_list))))

class MyApp(App):

    def build(self):
        test = TodoList()
        return test

if __name__ == '__main__':
    MyApp().run()