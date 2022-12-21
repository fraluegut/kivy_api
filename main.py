import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

# URL de la API Flask
API_URL = 'http://localhost:5000/api/data'

class MainWindow(BoxLayout):
    name_input = ObjectProperty()
    email_input = ObjectProperty()

    def send_data(self):
        # Obtiene los datos del formulario
        name = self.name_input.text
        email = self.email_input.text

        # Envía los datos a la API Flask
        data = {'name': name, 'email': email}
        response = requests.post(API_URL, json=data)

        # Muestra el resultado de la petición
        print(response.status_code)
        print(response.json())

class FormApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    FormApp().run()
