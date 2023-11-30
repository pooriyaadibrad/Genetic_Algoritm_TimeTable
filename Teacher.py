from sqlalchemy import Column, create_engine, INTEGER, String
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine("mssql+pyodbc://pooriya123:123@./geneticTime?driver=ODBC+Driver+17+for+SQL+Server")

base=declarative_base()
sessions=sessionmaker(bind=engine)
session=sessions()
class teacher(base):
    __tablename__="teacher"
    id=Column(INTEGER,primary_key=True)
    id1=Column(INTEGER)
    _name=Column(String)
    _family=Column(String)

    _DayAvalble=Column(String)
    _TimeAvalble=Column(INTEGER)
    def __init__(self,name="",family="",DayAvalble="",TimeAvalble=0,id=0):
        self.id1=id
        self.name=name
        self.family=family
        self.DayAvalble=DayAvalble
        self.TimeAvalble=TimeAvalble
    def setDayAvalble(self,value):
        self._DayAvalble=value
    def getDayAvalble(self):
        return self._DayAvalble
    DayAvalble=property(getDayAvalble,setDayAvalble)

    def setTimeAvalble(self, value):
        self._TimeAvalble = value

    def getTimeAvalble(self):
        return self._TimeAvalble

    TimeAvalble = property(getTimeAvalble, setTimeAvalble)
    def addTime(self, time):
        self.TimeAvalble.append(time)

    def setname(self,value):
        self._name=value
    def getname(self):
        return self._name
    name=property(getname,setname)
    def setfamily(self,value):
        self._family=value
    def getfamily(self):
        return self._family
    family = property(getfamily, setfamily)
base.metadata.create_all(engine)
teacher1=teacher(id=1,name="pooriya",family="adib",DayAvalble="monday",TimeAvalble=2)
teacher2=teacher(id=1,name="pooriya",family="adib",DayAvalble="sanday",TimeAvalble=4)
teacher3=teacher(id=1,name="pooriya",family="adib",DayAvalble="monday",TimeAvalble=3)


