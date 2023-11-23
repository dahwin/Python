from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from datetime import datetime
from kivy.clock import Clock

class DateTimeApp(App):
    def build(self):
        # Create a box layout to hold the label
        layout = BoxLayout(orientation='vertical')

        # RGB values for text color (e.g., black)
        text_color_rgb = (138,43,226)

        # Add alpha value (opacity) for RGBA
        text_color_rgba = text_color_rgb + (1,)

        # Create a label to display the formatted date and time
        self.label = Label(text="", font_size='50sp', color=text_color_rgba)

        # Add the label to the layout
        layout.add_widget(self.label)

        # Schedule the update function to be called every second
        Clock.schedule_interval(self.update_datetime, 1)

        # Set the background color of the label
        with self.label.canvas.before:
            Color(1, 1, 1, 1)  # White background color
            self.rect = Rectangle(size=self.label.size, pos=self.label.pos)

        return layout

    def update_datetime(self, dt):
        # Get the current date and time
        current_datetime = datetime.now()

        # Format date as "12 November 2023"
        formatted_date = current_datetime.strftime("%d %B %Y")

        # Format time in local AM/PM format
        formatted_time = current_datetime.strftime("%I:%M:%S %p")

        # Combine formatted date and time
        formatted_datetime = f"{formatted_date}\n{formatted_time}"

        # Update the label text
        self.label.text = formatted_datetime

        # Update the background color rectangle size and position
        self.rect.size = self.label.size
        self.rect.pos = self.label.pos

if __name__ == '__main__':
    DateTimeApp().run()
