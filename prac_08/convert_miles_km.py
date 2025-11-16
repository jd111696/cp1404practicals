from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """Convert miles to kilometres."""
    output_km = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Convert miles to kilometres and update the StringProperty."""
        miles = self.get_valid_miles()
        kilometres = miles * MILES_TO_KM
        self.output_km = f"{kilometres:.3f}"

    def handle_increment(self, change):
        """Change the miles value by 'change' (int). If current value is invalid, treat as 0 first."""
        miles = self.get_valid_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_valid_miles(self):
        """Get the miles value from the TextInput. Return 0 if it's invalid or empty."""
        text = self.root.ids.input_miles.text
        try:
            miles = float(text)
        except ValueError:
            miles = 0.0
        return miles


if __name__ == '__main__':
    ConvertMilesKmApp().run()
