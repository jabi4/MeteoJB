from tkinter import ttk, IntVar, BooleanVar, DoubleVar
import tkinter as tk
from datasource.dto.ConfigDto import ConfigDto
from PIL import Image, ImageTk
from components.SelectTypeComponent import SelectTypeComponent



class ConfigComponent(ttk.LabelFrame):

    def __init__(self, parent, row, column):
        super().__init__(master=parent, text="Configuration")
        self.grid(row=row, column=column, padx=5, pady=5)
        self._loadImages()
        self.simulatedTab = parent
        self.select = SelectTypeComponent
        self.setView()

    def setView(self):

        self.lblTemp = ttk.Label(self, image=self.tkImgTem)
        self.lblTemp.grid(row=0, column=0, pady=5, padx=5)

        self.lblHum = ttk.Label(self, image=self.tkImgHum)
        self.lblHum.grid(row=1, column=0, pady=5, padx=5)

        self.lblpre = ttk.Label(self, image=self.tkImgPressure)
        self.lblpre.grid(row=2, column=0, pady=5, padx=5)

        self.temperature = DoubleVar()
        configTemperature = ttk.Scale(self, from_=-30, to=50, variable=self.temperature)
        configTemperature.grid(row=0, column=1, pady=5, padx=5)
        lblTemp = ttk.Label(self, textvariable=self.temperature)
        lblTemp.grid(row=0, column=2, padx=5, pady=5)

        self.humidity = DoubleVar()
        configHumidity = ttk.Scale(self, from_=0, to=100, variable=self.humidity)
        configHumidity.grid(row=1, column=1, pady=5, padx=5)
        lblHumidity = ttk.Label(self, textvariable=self.humidity)
        lblHumidity.grid(row=1, column=2, padx=5, pady=5)

        self.pressure = DoubleVar()
        configPressure = ttk.Scale(self, from_=980, to=1050, variable=self.pressure)
        configPressure.grid(row=2, column=1, pady=5, padx=5)
        lblPressure = ttk.Label(self, textvariable=self.pressure)
        lblPressure.grid(row=2, column=2, padx=5, pady=5)

        self.simulate = BooleanVar()
        cbSimulate = ttk.Checkbutton(self, text="Simulate", variable=self.simulate)
        cbSimulate.grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky=tk.EW)


    def _loadImages(self):
        imgTem = Image.open("./images/thermometer.png")
        imgHum = Image.open("./images/humidity.png")
        imgPressure = Image.open("./images/pressure.png")

        self.tkImgTem = ImageTk.PhotoImage(imgTem)
        self.tkImgHum = ImageTk.PhotoImage(imgHum)
        self.tkImgPressure = ImageTk.PhotoImage(imgPressure)

    def getConfiguration(self):
        config = ConfigDto()
        config.temperature = int(self.temperature.get())
        config.humidity = int(self.humidity.get())
        config.pressure = int(self.pressure.get())
        config.publish = self.simulate.get()
        return config

    def setConfiguration(self, configDto: ConfigDto):
        if configDto is not None:
            self.temperature.set(configDto.temperature)
            self.humidity.set(configDto.humidity)
            self.pressure.set(configDto.pressure)
            self.simulate.set(configDto.publish)


