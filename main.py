from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from home_page import HomePage
from login_page import LoginPage
from register_page import RegisterPage
from faq_page import FAQPage
from kivy.storage.jsonstore import JsonStore

store = JsonStore('login_state.json')

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(HomePage(name='home'))
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(RegisterPage(name='register'))
        sm.add_widget(FAQPage(name='faq'))
        
        # Set the initial screen
        if 'logged_in' in store:
            sm.current = 'home'
        else:
            sm.current = 'login'
        
        return sm

if __name__ == '__main__':
    MyApp().run()
