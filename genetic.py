import random
from Teacher import teacher
from collections import Counter
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("mssql+pyodbc://pooriya123:123@./geneticTime?driver=ODBC+Driver+17+for+SQL+Server")


sessions=sessionmaker(bind=engine)
session=sessions()
class geneticTimeTable():
    def __init__(self, time, class_num, day):
        self.time = time
        self.teacher_num = 0
        self.class_num = class_num
        self.day = day
        self.numGenerations=0
        self.pupiolation =100
        self.mutateRate=0.1
        self.InitPopulation()
    def NumberOfTeacher(self):
        count=0
        date=session.query(teacher).all()
        for i in date:
            if i.id1>count:
                count=i.id1
        return count
    def InitPopulation(self):
        self.teacher_num=self.NumberOfTeacher()
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
        print(self.sortANDreverse(chromosomesWithFittnes))
        newPopulation=self.Selectparent(chromosomesWithFittnes)
        self.DetectiveResult(newPopulation)

    def Compration(self,chromosome):
        FittnesAfterConfilictCheck=self.Confilict(chromosome)
        FinalFittnes=self.DayFittnes(chromosome,FittnesAfterConfilictCheck)
        return (chromosome,FinalFittnes)
    def Confilict(self,chromosome):
        if self.numGenerations!=100:
            fittnes = 0
            for times in chromosome:
                counter = Counter(times)
                for element, count in counter.items():
                    if count == 1:
                        continue
                    else:
                        fittnes += count - 1
            return fittnes
        else:
            fittnes = 0
            for times in chromosome:
                counter = Counter(times)
                for element, count in counter.items():
                    if count == 1:
                        continue
                    else:
                        print(chromosome)
                        print(times,chromosome.index(times))
                        print(element)
                        fittnes += count - 1
            return fittnes
    def DayFittnes(self,chromosome,FittnesAfterConfilictCheck):
        if self.numGenerations!=100:
            for times in chromosome:
                iTimes=chromosome.index(times)
                for TeacherId in times:
                    CheckResult=self.Data(TeacherId,iTimes)
                    if CheckResult:
                        FittnesAfterConfilictCheck+=1
            FittnesAfterSoftCheck=FittnesAfterConfilictCheck
            return FittnesAfterSoftCheck
        else:
            for times in chromosome:
                iTimes = chromosome.index(times)
                for TeacherId in times:
                    CheckResult = self.Data(TeacherId, iTimes)
                    if CheckResult:
                        print(times)
                        print(TeacherId)
                        FittnesAfterConfilictCheck += 1
            FittnesAfterSoftCheck = FittnesAfterConfilictCheck
            return FittnesAfterSoftCheck

    def Data(self,id,iTimes):
        Check=False
        teacherAvalable=session.query(teacher).filter(teacher.id1 == id).all()
        for Teacher in teacherAvalable:
            if Teacher.DayAvalble==self.day and Teacher.TimeAvalble== iTimes:
                return Check
        Check=True
        return Check

    def Selectparent(self, chromosoms):
        chromosoms=self.sortANDreverse(chromosoms)
        chromosoms.reverse()
        ave=self.avrage_fittnes(chromosoms)
        selectList=[]
        for k in range(2):
            selectList.append(chromosoms[k])
            selectList.append(chromosoms[-(k+1)])
        childlist = []
        for i in range(0, 3):
            for j in range(i + 1, 4):
                parent1 = selectList[i]
                parent2 = selectList[j]

                childlist.extend(self.crossover(parent1, parent2,ave))

        childlist=self.sortANDreverse(childlist)
        childlist.reverse()
        childlist=childlist[0:4]
        secureChildlist=[]
        selectList=self.sortANDreverse(selectList)

        for i in range(len(childlist)):
            if not self.check(childlist[i],selectList):
                secureChildlist.append(childlist[i])
        childlist=self.sortANDreverse(secureChildlist)
        childlist.reverse()
        chromosoms=self.PlaceMent(selectList,secureChildlist,chromosoms)
        self.numGenerations += 1
        return chromosoms
    def PlaceMent(self,selectList,secureChildList,chromosoms):
        for child in secureChildList:
            chromosoms[chromosoms.index(selectList[0])]=child
            selectList.remove(selectList[0])
        return chromosoms




    def check(self,child,selectList):
        for item in selectList:
            if item==child:
                return True
        return False
    def crossover(self, parent1, parent2,ave):
        resultchild=[]
        parent1_without_f = parent1[0]
        parent2_without_f = parent2[0]
        parent1_without_f_half = [list(parent1_without_f[:int(self.time/2)]),
                                  list(parent1_without_f[int(self.time/2):])]
        parent2_without_f_half = [list(parent2_without_f[:int(self.time/2)]),
                                  list(parent2_without_f[int(self.time/2):])]

        child1 = parent1_without_f_half[0] + parent2_without_f_half[1]
        child2 = parent1_without_f_half[1] + parent2_without_f_half[0]
        childs=[child1,child2]
        for i in range(2):
            random_number = random.random()
            print(random_number)
            if random_number<self.mutateRate:
                childs[i]=self.mutate(childs[i])
        child_with_f1 = self.Compration(childs[0])
        child_with_f2 = self.Compration(childs[1])
        if child_with_f1[1]<ave:
            resultchild.append(child_with_f1)
        if child_with_f2[1] < ave:
            resultchild.append(child_with_f2)
        return resultchild
    def mutate(self,child):
        random_index_gen = random.randint(0, self.time - 1)
        chromosome = []
        for item1 in range(self.class_num):
            gen = random.randint(1, self.teacher_num)
            chromosome.append(gen)
        child[random_index_gen]=chromosome
        return child

    def sortANDreverse(self,chromosoms):

        sort_chromosomes_by_fittnes = sorted(chromosoms, key=lambda x: x[1])
        sort_chromosomes_by_fittnes.reverse()

        return sort_chromosomes_by_fittnes
    def avrage_fittnes(self, chromosomes_with_fittneses):
        ave = 0

        for item in chromosomes_with_fittneses:
            ave += int(item[1])
        return ave / self.pupiolation

    def DetectiveResult(self, chromosoms):
        if self.numGenerations!=101:
            self.sortANDreverse(chromosoms)
            if chromosoms[0][1] == 0:
                print(chromosoms[0][1])
            newPopulation=self.Selectparent(chromosoms)
            self.DetectiveResult(newPopulation)
        else:
            print(chromosoms)

sample=geneticTimeTable(time=4,class_num=8,day="monday")

