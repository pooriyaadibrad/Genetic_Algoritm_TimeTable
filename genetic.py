import random
from Teacher import teacher
from collections import Counter
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("mssql+pyodbc://pooriya123:123@./geneticTime?driver=ODBC+Driver+17+for+SQL+Server")


sessions=sessionmaker(bind=engine)
session=sessions()
class geneticTimeTable():
    def __init__(self, time, teacher_num, class_num, day):
        self.time = time
        self.teacher_num = teacher_num
        self.class_num = class_num
        self.day = day
        self.pupiolation = 6
        self.mutateRate=0.1

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
    def Compration(self,chromosome):
        FittnesAfterConfilictCheck=self.Confilict(chromosome)

    def Confilict(self,chromosome):
        fittnes = 0
        for times in chromosome:
            counter = Counter(times)
            for element, count in counter.items():
                if count == 1:
                    continue
                else:
                    fittnes += count - 1
        return fittnes
    def DayFittnes(self,chromosome,FittnesAfterConfilictCheck):
        for times in chromosome:
            for TeacherId in times:
                pass
    def Data(self,id):
        data=session.query(teacher).filter(teacher.id1 == id).all()
        for i in data:
            print(i.name)

sample=geneticTimeTable(time=4,teacher_num=10,class_num=8,day="monday")


sample.Data(1)

