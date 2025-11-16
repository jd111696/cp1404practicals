__author__ = 'Parker Duncanson'

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class SquaringApp(App):
    """App to square a number entered by the user."""
    result_text = StringProperty("Result")

    def build(self):
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        """Handle the calculation when the button is pressed."""
        text = self.root.ids.input_number.text
        try:
            number = int(text)
            result = number ** 2
        except ValueError:
            result = 0
        self.result_text = str(result)


if __name__ == '__main__':
    SquaringApp().run()

