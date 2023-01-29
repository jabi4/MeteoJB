from tkinter import ttk, IntVar
from datasource.enum.TypeEnum import TypeEnum
from PIL import Image, ImageTk


class SelectTypeComponent(ttk.LabelFrame):

    def __init__(self, parent, row, column):
        super().__init__(master=parent, text="Type choice")
        self.grid(row=row, column=column, padx=5, pady=5)
        self._loadImages()
        self.valueTab = parent
        self.radioValue = IntVar()
        self.choices = [type.name for type in TypeEnum]
        self.radioValue.set(0)
        self.setView()


    def setView(self):
        self.lblHouse = ttk.Label(self, image=self.tkImgHouse)
        self.lblHouse.grid(row=0, column=0, pady=5, padx=5)

        self.lblPark = ttk.Label(self, image=self.tkImgPark)
        self.lblPark.grid(row=1, column=0, pady=5, padx=5)

        self.lblCity = ttk.Label(self, image=self.tkImgCity)
        self.lblCity.grid(row=2, column=0, pady=5, padx=5)

        rbIndoor = ttk.Radiobutton(
            self,
            text=self.choices[TypeEnum.INDOOR.value],
            variable=self.radioValue,
            value=TypeEnum.INDOOR.value,
            command=self.valueTab.handleRadiobutton
        )
        rbIndoor.grid(row=0, column=1, pady=5, padx=5)

        rbOutdoor = ttk.Radiobutton(
            self,
            text=self.choices[TypeEnum.OUTDOOR.value],
            variable=self.radioValue,
            value=TypeEnum.OUTDOOR.value,
            command=self.valueTab.handleRadiobutton
        )
        rbOutdoor.grid(row=1, column=1, pady=5, padx=5)

        rbCity = ttk.Radiobutton(
            self,
            text=self.choices[TypeEnum.CITY.value],
            variable=self.radioValue,
            value=TypeEnum.CITY.value,
            command=self.valueTab.handleRadiobutton
        )
        rbCity.grid(row=2, column=1, pady=5, padx=5)

    def _loadImages(self):
        imgCity = Image.open("./images/city.png")
        imgHouse = Image.open("./images/house.png")
        imgPark = Image.open("./images/park.png")

        self.tkImgCity = ImageTk.PhotoImage(imgCity)
        self.tkImgHouse = ImageTk.PhotoImage(imgHouse)
        self.tkImgPark = ImageTk.PhotoImage(imgPark)

