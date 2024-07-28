from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)  # Red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # Magenta


class DynamicLabelsApp(App):
    """Main app class for dynamically creating labels."""
    status_text = StringProperty('')

    def __init__(self, **kwargs):
        """Initialize the app with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Dulari", "Smiley", "Happy", "Eve"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def add_labels(self):
        """add labels to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.bind(on_release=self.press_entry)
            temp_label.background_color = NEW_COLOUR
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        """Handle pressing on labels."""
        name = instance.text
        instance.color = ALTERNATIVE_COLOUR
        self.status_text = self.names[name]


def clear_all(self):
    """Clear all widgets that are children of the "entries_box" layout widget."""
    self.root.ids.entries_box.clear_widgets()


DynamicLabelsApp().run()
