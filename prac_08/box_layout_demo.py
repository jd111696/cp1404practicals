from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class BoxLayoutDemo(App):
    """Simple demo that greets the user and can clear the fields."""
    greeting_text = StringProperty("Enter your name")

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle pressing the Greet button."""
        name = self.root.ids.input_name.text.strip()
        if name:
            self.greeting_text = f"Hello {name}"
        else:
            self.greeting_text = "Enter your name"

    def handle_clear(self):
        """Handle pressing the Clear button."""
        self.root.ids.input_name.text = ''
        self.greeting_text = ""


if __name__ == '__main__':
    BoxLayoutDemo().run()