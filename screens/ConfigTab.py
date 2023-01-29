from tkinter import ttk, Frame
from mqtt.MqttClient import MqttClient
from components.ConfigComponent import ConfigComponent, ConfigDto


class ConfigTab(Frame):

    def __init__(self, parent, mqtt: MqttClient):
        super().__init__(master=parent)
        self.grid(padx=5, pady=5)
        self.setView()

    def setView(self):
        self.configSelect = ConfigComponent(self, 0, 0)








