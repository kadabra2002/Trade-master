from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

registered_users = {}  # In-memory store for registered users

class RegisterPage(Screen):
    def __init__(self, **kwargs):
        super(RegisterPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=150, spacing=10,
                           pos_hint={'center_x': 0.5, 'top': 0.80})
        
        title = Label(text='Register', font_size=32, size_hint_y=None, height=60)
        layout.add_widget(title)
        
        self.username_input = TextInput(hint_text='Username', size_hint_y=None, height=40)
        layout.add_widget(self.username_input)
        
        self.email_input = TextInput(hint_text='Email', size_hint_y=None, height=40)
        layout.add_widget(self.email_input)
        
        self.password_input = TextInput(hint_text='Password', password=True, size_hint_y=None, height=40)
        layout.add_widget(self.password_input)
        
        register_button = Button(text='Register', size_hint_y=None, height=50)
        register_button.bind(on_press=self.register)
        layout.add_widget(register_button)
        
        back_button = Button(text='Already have an account? Login', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_to_login)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def register(self, instance):
        username = self.username_input.text
        email = self.email_input.text
        password = self.password_input.text
        
        if username == '' or email == '' or password == '':
            self.show_error_popup("Please fill in all fields.")
        elif username in registered_users:
            self.show_error_popup("Username already exists.")
        else:
            registered_users[username] = password
            from kivy.storage.jsonstore import JsonStore
            store = JsonStore('login_state.json')
            store.put('logged_in', username=username)
            self.manager.current = 'home'
    
    def go_to_login(self, instance):
        self.manager.current = 'login'
    
    def show_error_popup(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()
