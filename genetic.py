import random
from Teacher import teacher
from collections import Counter
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("mssql+pyodbc://pooriya123:123@./geneticTime?driver=ODBC+Driver+17+for+SQL+Server")


session=sessionmaker(bind=engine)
sessions=session()
class geneticTimeTable():
    def __init__(self, time, teacher_num, class_num, day):
        self.time = time
        self.teacher_num = teacher_num
        self.class_num = class_num
        self.day = day
        self.pupiolation = 6
        self.mutateRate=0.1
        self.InitPopulation()
    def InitPopulation(self):
            chromosomes = []
            for i in range(self.pupiolation):
                day = []
                for item in range(self.time):
                    times = []
                    for item1 in range(self.class_num):
                        gen = random.randint(1, self.teacher_num)
                        times.append(gen)
                    day.append(times)
                chromosomes.append(day)
            print(chromosomes)

sample=geneticTimeTable(time=4,teacher_num=10,class_num=8,day="monday")