from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.core.window import Window
import qrcode

Builder.load_string("""

<Primeira>:
    MDFloatLayout:
        md_bg_color: 0/255, 153/255, 215/255, 1
        Image:
            source: "qr.png"
            size_hint: 0.6 , 0.6
            pos_hint: {"center_x": 0.5 , "center_y": 0.7}
        MDLabel:
            text: "CREATE YOUR QR CODE! "
            pos_hint: {"center_x": 0.7 , "center_y": 0.45}
            font_size:"18sp"
            font_name: "Poppins-Medium.ttf"
            
        MDLabel:
            id: mostruario
            text: "Create a perfect and" 
            font_size:"14sp"
            font_name: "Poppins-Regular.ttf"
            pos_hint: {"center_y": 0.40}
            halign: "center"

        MDLabel:
            id: mostruario
            text: "usually QR CODE" 
            font_size:"14sp"
            font_name: "Poppins-Regular.ttf"
            pos_hint: {"center_y": 0.35}
            halign: "center"
        
        Button:
            font_size: "14sp"
            font_name: "Poppins-Medium.ttf"
            text: "GO!"
            pos_hint: {"center_x": 0.5 , "center_y": 0.2}
            size_hint: .6 , .065
            background_color: 0, 0, 4, 1
            on_press:
                root.manager.transition.direction = "left"
                root.login()

<Segunda>:
    MDFloatLayout:
        md_bg_color: 0/255, 153/255, 215/255, 1
        MDIconButton:
            icon: "home"
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.current = "primeira-tela"
            pos_hint: {"center_x": 0.1 , "center_y": 0.95}
        Image:
            source: "tech.png"
            size_hint: 0.8 , 0.8
            haling: "center"
            pos_hint: {"center_x": 0.5 , "center_y": 0.7}
        MDLabel:
            id: label_1
            text: "INSERT YOUR URL"
            pos_hint: {"center_y": 0.5}
            halign: "center"
        TextInput:
            id: link_qr
            hint_text : "link.."
            pos_hint: {"center_x": 0.55 , "center_y": 0.4}
            background_color: 1,1,1,0
            size_hint: .6 , .065

        Button:
            text: "GENERATE"
            font_size: "14sp"
            font_name: "Poppins-Medium.ttf"
            pos_hint: {"center_x": 0.5 , "center_y": 0.2}
            size_hint: .6 , .065
            background_color: 0, 0, 2, 1
            on_press:
                root.generate()
            
""")


class Primeira(Screen):
    def login(self):
        MDApp.get_running_app().root.current = "segunda-tela"
        
class Segunda(Screen):
    def generate(self):
        link = self.ids.link_qr.text
        data = link
        img = qrcode.make(data) 
        img.save('MyQRCode1.png')
        self.ids.label_1.text = "GENERATED"
        self.ids.link_qr.text = ""


class QR(MDApp):
    def build(self):
        Window.size = (350 , 600)
        sm = ScreenManager()
        sm.add_widget(Primeira(name = "primeira-tela"))
        sm.add_widget(Segunda(name = "segunda-tela"))
        return sm

QR().run()

