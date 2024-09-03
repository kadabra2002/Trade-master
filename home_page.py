from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window

# Set the background color
Window.clearcolor = (0, 0, 1, 1)  # Blue color

registered_users = {}  # In-memory store for registered users

class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)

        # Initialize FloatLayout
        layout = FloatLayout()

        # Navigation Button
        nav_button = Button(text='≡', size_hint=(None, None), size=(50, 50),
                            on_press=self.toggle_nav_popup, background_color=(1, 1, 1, 1),
                            pos_hint={'right': 1, 'top': 1})  # Position it at the top right
        layout.add_widget(nav_button)

        # Title
        title = Label(text='Welcome To Trade Master', font_size=32, size_hint_y=None, height=60,
                      pos_hint={'center_x': 0.5, 'top': 0.90})  # Centered horizontally, below the nav button
        layout.add_widget(title)

        # Search Engine
        search_layout = BoxLayout(size_hint_y=None, height=40, spacing=10,
                                  padding=[50, 0, 50, 0],  # Add horizontal padding
                                  pos_hint={'center_x': 0.5, 'top': 0.80})  # Center horizontally, adjust top
        self.search_input = TextInput(hint_text='Search...', size_hint_x=0.8)
        search_button = Button(text='Search', size_hint_x=0.2, on_press=self.perform_search)
        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_button)
        layout.add_widget(search_layout)

        # Image Slider
        self.carousel = Carousel(direction='left', loop=True, size_hint=(1, None), height=300,
                                 pos_hint={'center_x': 0.5, 'top': 0.6})
        self.carousel.add_widget(Image(source='one.jpg'))
        self.carousel.add_widget(Image(source='two.jpg'))
        self.carousel.add_widget(Image(source='three.jpg'))
        self.carousel.add_widget(Image(source='four.jpg'))
        self.carousel.add_widget(Image(source='five.jpg'))
        self.carousel.add_widget(Image(source='six.jpg'))
        layout.add_widget(self.carousel)

        self.add_widget(layout)

        # Schedule automatic sliding
        Clock.schedule_interval(self.slide, 3)

    def slide(self, dt):
        self.carousel.load_next()

    def perform_search(self, instance):
        search_query = self.search_input.text
        self.show_search_popup(f"Search results for: {search_query}")

    def show_search_popup(self, message):
        popup = Popup(title='Search Results',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def toggle_nav_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        nav_popup = Popup(title='Navigation',
                          content=content,
                          size_hint=(None, None), size=(200, 300))
        content.add_widget(Button(text='Home', on_press=lambda x: self.switch_screen('home')))
        content.add_widget(Button(text='Login', on_press=lambda x: self.switch_screen('login')))
        content.add_widget(Button(text='Register', on_press=lambda x: self.switch_screen('register')))
        content.add_widget(Button(text='Feedback', on_press=self.show_feedback_popup))
        content.add_widget(Button(text='FAQ', on_press=lambda x: self.switch_screen('faq')))
        content.add_widget(Button(text='Logout', on_press=self.logout))
        nav_popup.open()

    def switch_screen(self, screen_name):
        self.manager.current = screen_name

    def logout(self, instance):
        self.manager.current = 'login'

    def show_feedback_popup(self, instance=None):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Please provide your feedback:'))
        self.feedback_input = TextInput(size_hint_y=None, height=200)
        content.add_widget(self.feedback_input)
        submit_button = Button(text='Submit', size_hint_y=None, height=50, on_press=self.submit_feedback)
        content.add_widget(submit_button)
        self.feedback_popup = Popup(title='Feedback',
                      content=content,
                      size_hint=(None, None), size=(400, 400))
        self.feedback_popup.open()

    def submit_feedback(self, instance):
        feedback = self.feedback_input.text
        if feedback:
            print("Feedback submitted:", feedback)
            self.show_success_popup("Thank you for your feedback!")
            self.feedback_popup.dismiss()
        else:
            self.show_error_popup("Feedback cannot be empty.")

    def show_error_popup(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_success_popup(self, message):
        popup = Popup(title='Success',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()
