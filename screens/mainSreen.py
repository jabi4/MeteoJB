from tkinter import ttk
import tkinter as tk
from mqtt.MqttClient import MqttClient
from screens.ValueTab import ValueTab
from screens.ConfigTab import ConfigTab
from datasource.dto.ConfigDto import ConfigDto

class MainScreen(ttk.Frame):

    SERVER_URL = "edu-agrdan.plusvps.com"

    def __init__(self, mainWindow):
        super().__init__(master=mainWindow)
        self.grid()

        self.mqtt = MqttClient(self.SERVER_URL, 1883, "meteoJB/+")
        self.mqtt.start()
        self.cnfg = ConfigDto()
        self.createMainScreen()

    def createMainScreen(self):
        self.iotPanel = ttk.LabelFrame(self, text="Main screen")
        self.iotPanel.grid(row=0, column=1, pady=5, padx=5)

        self.tabs = ttk.Notebook(self.iotPanel)
        self.tabs.grid(row=0, column=0, padx=5, pady=5)

        self.tabValue = ttk.Frame(self.tabs)
        self.tabSimulator = ttk.Frame(self.tabs)

        self.tabs.add(self.tabValue, text="Value")
        self.tabs.add(self.tabSimulator, text="Simulator")

        self.tab1 = ValueTab(self.tabValue, self.mqtt)
        self.tab2 = ConfigTab(self.tabSimulator, self.mqtt)

        btnSave = ttk.Button(self, text="Save config", command=self.handleSaveBtn)
        btnSave.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.EW)


    def handleSaveBtn(self):
        configDto = self.tab2.configSelect.getConfiguration()
        configDto.type = self.tab1.typeSelect.choices[self.tab1.typeSelect.radioValue.get()]
        print(configDto)




