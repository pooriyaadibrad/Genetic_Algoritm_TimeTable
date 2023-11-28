from tkinter import *
from tkinter import ttk
from Teacher import teacher
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("mssql+pyodbc://pooriya123:123@./geneticTime?driver=ODBC+Driver+17+for+SQL+Server")


session=sessionmaker(bind=engine)
sessions=session()




class app(Frame):
    txtNameVar = ""
    txtFamilyVar = ""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWiget()
        self.Reed()

    """
    main frame

    """

    def createWiget(self):
        self.creatVar()
        self.img = PhotoImage(file="img/mainIMG.png")
        self.lblImg = Label(self.master, image=self.img).pack(side="right", fill=BOTH)
        self.btnStart = Button(self.master, text="Start", width=30, height=7, font=30, bg="#DDF2FD")
        self.btnStart.bind("<Button-1>", self.ActiveDashbord)
        self.btnStart.place(x=30, y=200)
        self.dashbord = Frame(self.master, background="#A9A9A9", width=417, height=700)

        self.createWigetFrame1()
        self.Table = Frame(self.master, height=600, width=800, bg="white")
        self.Table.place(x=500, y=50)
        self.Table.place_forget()
        self.createWigetFrame2()
        self.dashbord.place(x=0, y=0)
        self.dashbord.place_forget()

    """
    register frame

    """

    def createWigetFrame1(self):

        self.imgDashbord = PhotoImage(file="img/Dashbord.png")
        self.lblImgDashbord = Label(self.dashbord, image=self.imgDashbord).place(x=0, y=0)
        self.DashborClose = PhotoImage(file="img/DashbordClose.png")
        self.btnClose = Button(self.dashbord, image=self.DashborClose)
        self.btnClose.bind("<Button-1>", self.DiActiveDashbord)
        self.btnClose.place(x=390, y=0)
        self.txtid = Entry(self.dashbord, justify="center",textvariable=self.txtidVar)

        self.lblid = Label(self.dashbord, text="id")
        self.lblid.configure(bg="white", font=10, fg="black", borderwidth=2, relief="ridge", padx=5, pady=0)
        self.lblid.place(x=40, y=203)
        self.txtid.place(x=135, y=210)
        self.txtName = Entry(self.dashbord, justify="center", textvariable=self.txtNameVar)
        self.txtName.bind("<KeyRelease>", self.ActtivBtn)
        self.lblName = Label(self.dashbord, text="اسم")
        self.lblName.configure(bg="white", font=10, fg="black", borderwidth=2, relief="ridge", padx=5, pady=0)
        self.lblName.place(x=40, y=243)
        self.txtName.place(x=135, y=250)
        self.txtFamily = Entry(self.dashbord, justify="center", textvariable=self.txtFamilyVar)
        self.lblFamily = Label(self.dashbord, text="فامیلی")
        self.lblFamily.configure(bg="white", font=10, fg="black", borderwidth=2, relief="ridge", padx=5, pady=0)
        self.txtFamily.bind("<KeyRelease>", self.ActtivBtn)
        self.lblFamily.place(x=40, y=283)
        self.txtFamily.place(x=135, y=290)
        day = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
        self.comboDay = ttk.Combobox(self.dashbord, values=day)
        self.lblDay = Label(self.dashbord, text="روز مقدور")
        self.lblDay.configure(bg="white", font=10, fg="black", borderwidth=2, relief="ridge", padx=5, pady=0)
        self.lblDay.place(x=40, y=323)
        self.comboDay.place(x=135, y=330)
        Time = [0,1,2,3]
        self.comboTime = ttk.Combobox(self.dashbord, values=Time)
        self.lblTime = Label(self.dashbord, text="زمان مقدور")
        self.lblTime.configure(bg="white", font=10, fg="black", borderwidth=2, relief="ridge", padx=5, pady=0)
        self.lblTime.place(x=40, y=363)
        self.comboTime.place(x=135, y=370)

        self.btnRegister = Button(self.dashbord, text="Register", width=10, background="#005B41", fg="white", font=2,
                                  borderwidth=5, relief="raised", padx=5, pady=0)
        #self.btnRegister.bind("<Button-1>", self.onclickRegister)
        self.btnRegister.configure(state=DISABLED)
        self.btnRegister.place(x=135, y=500)

        self.btnRegister = Button(self.dashbord, text="Register", width=10, background="#005B41", fg="white", font=2,
                                  borderwidth=5, relief="raised", padx=5, pady=0)
        #self.btnRegister.bind("<Button-1>", self.onclickRegister)
        self.btnRegister.configure(state=DISABLED)
        self.btnRegister.place(x=135, y=500)

    """
    Table frame

    """

    def createWigetFrame2(self):
        columns = ("c1", "c2", "c3", "c4","c5")
        self.myTable = ttk.Treeview(self.Table, height=25, columns=columns, show="headings")

        self.myTable.column(columns[0], width=160, anchor="center")
        self.myTable.heading(columns[0], text="id")
        self.myTable.column(columns[1], width=160, anchor="center")
        self.myTable.heading(columns[1], text="Name")
        self.myTable.column(columns[2], width=160)
        self.myTable.heading(columns[2], text="Family")
        self.myTable.column(columns[3], width=160)
        self.myTable.heading(columns[3], text="DAY")
        self.myTable.column(columns[4], width=160)
        self.myTable.heading(columns[4], text="Time")
        self.myTable.bind("<Button-1>", self.getselection)
        self.myTable.place(x=0, y=0)
        self.btnsearch = Button(self.Table, text="Search", width=10, background="#005B41", fg="white", font=2,
                                borderwidth=5, relief="raised", padx=5, pady=0)

        self.txtSearch = Entry(self.Table, justify="center", width=45, font=20, background="#005B41")
        self.txtSearch.place(x=200, y=540)
        self.btnsearch.place(x=30, y=530)

    """
    select item from table

    """

    def getselection(self, e):
        select = self.myTable.selection()
        if select != ():
            Data = self.myTable.item(select)["values"]
            self.txtidVar.set(Data[0])
            self.txtNameVar.set(Data[1])
            self.txtFamilyVar.set(Data[2])
            self.comboDay.set(Data[3])
            self.comboTime.set(Data[4])
            self.btnRegister.configure(state=NORMAL)

    """

    active and di active dashbord
    """

    def DiActiveDashbord(self, e):
        self.btnStart.place(x=30, y=200)
        self.dashbord.place_forget()
        self.Table.place_forget()

    def ActiveDashbord(self, e):
        self.btnStart.place_forget()
        self.Table.place(x=500, y=50)
        self.dashbord.place(x=0, y=0)


    def ActtivBtn(self, e):
        if self.txtName.get() != "" and self.txtFamily.get() != "":
            self.btnRegister.configure(state=NORMAL)
        else:
            self.btnRegister.configure(state=DISABLED)

    def onclickRegister(self, e):
        if self.btnRegister.cget("state") == NORMAL:
            teacher1=teacher(id=self.txtid.get(),name=self.txtName.get(),family=self.txtFamily.get(),DayAvalble=self.comboDay.get(),TimeAvalble=self.comboTime.get())
            self.Register(teacher1)
            self.InsertTable(teacher1)

    def InsertTable(self, value):
        self.myTable.insert('', "end", values=[value.id1,value.name, value.family, value.DayAvalble, value.TimeAvalble])

    def Register(self, value):
        sessions.add(value)
        sessions.commit()

    def Reed(self):
        result = sessions.query(teacher).all()
        for item in result:
            self.InsertTable(item)


    def creatVar(self):
        self.txtidVar=StringVar()
        self.txtNameVar = StringVar()
        self.txtFamilyVar = StringVar()


if __name__ == "__main__":
    win = Tk()
    win.geometry("%dx%s+%d+%d" % (1420, 700, 100, 20))

    app1 = app(win)
    win.mainloop()