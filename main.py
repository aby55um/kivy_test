from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

import datetime

width, height = Window.size

class Item():
    def __init__(self, text):
        self.text = text
        self.completed = False
        self.date = datetime.datetime.now()
        self.remove_button = None

    #def set_remove_button(self, label):
    #    self.remove_button = label

class TodoList(FloatLayout):
    def button_press(self, instance):
        item = Item(self.text_input.text)
        self.add_item(item)
        self.text_input.text=''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item_list = []
        self.button = Button(text="Add todo", size_hint=(.1,.05), pos=(0.25 * width, 0.8 * height))
        self.button.bind(on_press=self.button_press)
        self.text_input = TextInput(text="", multiline=False, size_hint=(.3,.05), pos=(0.4 * width,0.8 * height))
        self.add_widget(self.button)
        self.add_widget(self.text_input)

    def add_item(self, item):
        if item.text != '':
            self.item_list.append(item)
            self.add_widget(Label(text=item.text, size_hint=(.1,.35), pos=(0.25 * width,0.65 * height - 0.09 * height * len(self.item_list))))
            #item.remove_button = Label(text='Remove', size_hint=(.1,..35), pos=(0.25 * width,0.65 * height - 0.05 * height * len(self.item_list)))
            item.remove = Button(text='Remove', size_hint=(.09,.05), pos=(0.45 * width,0.80 * height - 0.09 * height * len(self.item_list)))
            self.add_widget(item.remove)

class MyApp(App):

    def build(self):
        test = TodoList()
        return test

if __name__ == '__main__':
    MyApp().run()