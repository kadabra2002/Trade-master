from kivy.uix.bubble import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

registered_users = {}  # In-memory store for registered users

class LoginPage(Screen):
   
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=150, spacing=10,
                           pos_hint={'center_x': 0.5, 'top': 0.80})
        title = Label(text='Login', font_size=32, size_hint_y=None, height=60)
        layout.add_widget(title)
        
        self.username_input = TextInput(hint_text='Username', size_hint_y=None, height=40)

        layout.add_widget(self.username_input)
        
        self.password_input = TextInput(hint_text='Password', password=True, size_hint_y=None, height=40)
        layout.add_widget(self.password_input)
        
        login_button = Button(text='Login', size_hint_y=None, height=50)
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)
        
        register_button = Button(text="Don't have an account? Register", size_hint_y=None, height=50)
        register_button.bind(on_press=self.go_to_register)
        layout.add_widget(register_button)
        
        self.add_widget(layout)
    
    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        if username == '' or password == '':
            self.show_error_popup("Please fill in both username and password.")
        elif username in registered_users and registered_users[username] == password:
            from kivy.storage.jsonstore import JsonStore
            store = JsonStore('login_state.json')
            store.put('logged_in', username=username)
            self.manager.current = 'home'
        else:
            self.show_error_popup("Incorrect username or password.")
    
    def go_to_register(self, instance):
        self.manager.current = 'register'
    
    def show_error_popup(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()
