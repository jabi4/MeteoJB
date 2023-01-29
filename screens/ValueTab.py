from tkinter import ttk, Frame
from mqtt.MqttClient import MqttClient
from components.SelectTypeComponent import SelectTypeComponent


class ValueTab(Frame):

    def __init__(self, parent, mqtt: MqttClient):
        super().__init__(master=parent)
        self.grid(padx=5, pady=5)
        self.setView()

    def setView(self):
        self.typeSelect = SelectTypeComponent(self, 0, 0)

    def handleRadiobutton(self):
        self.type = self.typeSelect.choices[self.typeSelect.radioValue.get()]
        print(self.type)

    # def setupConfig(self):
    #     self.type = self.typeSelect.choices[self.typeSelect.radioValue.get()]
    #     configDto: ConfigDto = self.configurationService.readConfiguration(self.type)
    #     if configDto is not None:
    #         self.configSelect.setConfiguration(configDto)
    #     else:
    #         empty = ConfigDto()
    #         self.configSelect.setConfiguration(empty)







