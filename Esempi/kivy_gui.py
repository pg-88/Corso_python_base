from kivy.app import App
from kivy.logger import Logger as log

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class InputVeicolo(GridLayout):

    def __init__(self, **kwargs):
        super(InputVeicolo, self).__init__(**kwargs)
        self.cols = 2
        log.info("init input veicolo")
        self.add_widget(Label(text='Marca '))
        self.marca = TextInput(multiline=False)
        self.add_widget(self.marca)
        self.add_widget(Label(text='Modello '))
        self.modello = TextInput(multiline=False)
        self.add_widget(self.modello)
        self.mostra_veicolo = Button(text="Mostra Dati Inseriti")
        self.add_widget(self.mostra_veicolo)
        self.mostra_veicolo.bind(on_release=self.mostra_dati)
        
        # Etichetta per mostrare i dati inseriti
        self.dati_label = Label(text="")
        self.add_widget(self.dati_label)

    def mostra_dati(self, btn):
        self.dati_label.text = f"Inserimento veicolo: {self.marca.text} - {self.modello.text}"

class VeicoliApp(App):

    def build(self):
        return InputVeicolo()

if __name__ == '__main__':
    VeicoliApp().run()
