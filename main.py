from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.25, 0.90, 1)

class ArslenApp(App):
    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        root.add_widget(Label(
            text="[b]ARSLEN[/b]",
            markup=True,
            font_size=42,
            color=(1, 1, 1, 1)
        ))

        root.add_widget(Label(
            text="[b]fX[/b]",
            markup=True,
            font_size=75,
            color=(1, 1, 1, 1)
        ))

        root.add_widget(Label(
            text="ارسلان. فيس",
            font_size=25,
            color=(1, 1, 1, 1)
        ))

        btn = Button(
            text="دخول إلى التطبيق",
            font_size=20,
            size_hint_y=0.3
        )
        btn.bind(on_press=self.home)
        root.add_widget(btn)
        return root

    def home(self, instance):
        root = self.root
        root.clear_widgets()
        root.add_widget(Label(
            text="[b]ARSLEN - المنشورات[/b]",
            markup=True,
            font_size=28
        ))
        post = TextInput(
            hint_text="اكتب منشورك هنا...",
            size_hint_y=0.3
        )
        root.add_widget(post)
        root.add_widget(Button(
            text="نشر",
            size_hint_y=0.2
        ))

if __name__ == "__main__":
    ArslenApp().run()
