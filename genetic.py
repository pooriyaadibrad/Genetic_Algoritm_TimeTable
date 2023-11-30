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
        self.pupiolation = 2
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
        chromosomesWithFittnes=[]
        for chromosome in chromosomes:
            chromosomesWithFittnes.append(self.Compration(chromosome))



    def Compration(self,chromosome):
        FittnesAfterConfilictCheck=self.Confilict(chromosome)
        FinalFittnes=self.DayFittnes(chromosome,FittnesAfterConfilictCheck)
        return (chromosome,FinalFittnes)
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
            iTimes=chromosome.index(times)
            for TeacherId in times:
                CheckResult=self.Data(TeacherId,iTimes)
                if CheckResult:
                    FittnesAfterConfilictCheck+=1
        FittnesAfterSoftCheck=FittnesAfterConfilictCheck
        return FittnesAfterSoftCheck

    def Data(self,id,iTimes):
        Check=False
        teacherAvalable=session.query(teacher).filter(teacher.id1 == id).all()
        for Teacher in teacherAvalable:
            if Teacher.DayAvalble==self.day and Teacher.TimeAvalble== iTimes:
                return Check
        Check=True
        return Check


sample=geneticTimeTable(time=4,teacher_num=10,class_num=8,day="monday")

