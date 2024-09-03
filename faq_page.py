from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

class FAQPage(Screen):
    def __init__(self, **kwargs):
        super(FAQPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.carousel = Carousel(direction='right', loop=False, size_hint=(1, 0.8))
        
        faq_contents = [
            ("FAQ Page 1", [
                "Q1: How do I register an account?",
                "A1: Click on the 'Register' button and fill in the required details.",
                "Q2: How do I reset my password?",
                "A2: Click on 'Forgot Password' on the login page and follow the instructions."
            ]),
            ("FAQ Page 2", [
                "Q1: How do I contact support?",
                "A1: Use the 'Feedback' button on the home page to send us a message.",
                "Q2: Can I change my username?",
                "A2: No, once set, the username cannot be changed."
            ]),
            ("FAQ Page 3", [
                "Q1: Where can I find the latest updates?",
                "A1: Check the 'News' section in the app for the latest updates.",
                "Q2: How do I delete my account?",
                "A2: Contact our support team through the 'Feedback' button to request account deletion."
            ]),
            ("FAQ Page 4", [
                "Q1: How do I update my profile information?",
                "A1: Go to 'Profile' settings and update your details.",
                "Q2: How do I change my email address?",
                "A2: Update your email address in 'Account Settings'."
            ]),
            ("FAQ Page 5", [
                "Q1: What should I do if I forget my password?",
                "A1: Use the 'Forgot Password' option on the login page to reset your password.",
                "Q2: How can I view my transaction history?",
                "A2: Go to 'Account' and select 'Transaction History'."
            ]),
            ("FAQ Page 6", [
                "Q1: Is my data secure with your app?",
                "A1: Yes, we use encryption and secure servers to protect your data.",
                "Q2: How do I report a bug?",
                "A2: Use the 'Feedback' button to report any bugs or issues."
            ]),
            ("FAQ Page 7", [
                "Q1: Can I use the app offline?",
                "A1: Some features require an internet connection, but offline functionality is available for certain features.",
                "Q2: How can I contact customer support?",
                "A2: Use the 'Contact Us' section in the app for support inquiries."
            ])
        ]
        
        for title, contents in faq_contents:
            page = BoxLayout(orientation='vertical', padding=200, spacing=10)
            page.add_widget(Label(text=title, font_size=32, size_hint_y=None, height=60))
            for content in contents:
                page.add_widget(Label(text=content, size_hint_y=None, height=40))
            self.carousel.add_widget(page)
        
        layout.add_widget(self.carousel)
        
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        prev_button = Button(text='Previous', on_press=self.on_prev)
        next_button = Button(text='Next', on_press=self.on_next)
        button_layout.add_widget(prev_button)
        button_layout.add_widget(next_button)
        
        layout.add_widget(button_layout)
        self.add_widget(layout)
    
    def on_prev(self, instance):
        if self.carousel.index > 0:
            self.carousel.load_slide(self.carousel.slides[self.carousel.index - 1])
    
    def on_next(self, instance):
        if self.carousel.index < len(self.carousel.slides) - 1:
            self.carousel.load_slide(self.carousel.slides[self.carousel.index + 1])
