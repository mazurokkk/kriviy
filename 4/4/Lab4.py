import pandas as pd
from colorama import init, Fore, Back, Style

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)
init(autoreset=True) 

with open('samokats.txt') as fileobject:
    samokats = []
    samokats = fileobject.readlines()
    samokats = [line.rstrip('\n') for line in samokats]

print("\n")
print(Style.BRIGHT + Fore.BLUE + "Самокати:",*samokats,sep="\n")
print("\n")

with open('parameters.txt') as fileparameters:
    parameters = []
    parameters = fileparameters.readlines()
    parameters = [line.rstrip('\n') for line in parameters]

print(Style.BRIGHT + Fore.BLUE + "Параметри:",*parameters,sep="\n")
print("\n")

with open('importance.txt') as fileimportance:
    importance = []
    importance = fileimportance.readlines()
    importance = [line.rstrip('\n') for line in importance]

file1 = open ('1.txt' , 'r')
exp1 = []
exp1 = [ line.split() for line in file1]

file2 = open ('2.txt' , 'r')
exp2 = []
exp2 = [ line.split() for line in file2]

file3 = open ('3.txt' , 'r')
exp3 = []
exp3 = [ line.split() for line in file3]

file4 = open ('4.txt' , 'r')
exp4 = []
exp4 = [ line.split() for line in file4]

def Price (samokat):
    price = float(importance[0]) * (float(exp1[samokat][0])+float(exp2[samokat][0])+float(exp3[samokat][0])+float(exp4[samokat][0]))
    return price

def Speed (samokat):
    speed = float(importance[1]) * (float(exp1[samokat][1])+float(exp2[samokat][1])+float(exp3[samokat][1])+float(exp4[samokat][1]))
    return speed

def Design (samokat):
    design = float(importance[2]) * (float(exp1[samokat][2])+float(exp2[samokat][2])+float(exp3[samokat][2])+float(exp4[samokat][2]))
    return design

def Performance (samokat):
    performance = float(importance[3]) * (float(exp1[samokat][3])+float(exp2[samokat][3])+float(exp3[samokat][3])+float(exp4[samokat][3]))
    return performance

def Load (samokat):
    load = float(importance[4]) * (float(exp1[samokat][4])+float(exp2[samokat][4])+float(exp3[samokat][4])+float(exp4[samokat][4]))
    return load


#Croissant
price1 = Price(0)
speed1 = Speed(0)
design1 = Design(0)
performance1 = Performance(0)
load1 = Load(0)

#Kalachi
price2 = Price(1)
speed2 = Speed(1)
design2 = Design(1)
performance2 = Performance(1)
load2 = Load(1)

#Brioche
price3 = Price(2)
speed3 = Speed(2)
design3 = Design(2)
performance3 = Performance(2)
load3 = Load(2)

#Pampushki
price4 = Price(3)
speed4 = Speed(3)
design4 = Design(3)
performance4 = Performance(3)
load4 = Load(3)

#Waffles
price5 = Price(4)
speed5 = Speed(4)
design5 = Design(4)
performance5 = Performance(4)
load5 = Load(4)

#Sum

sum1 = price1 + design1 + speed1 + load1 + performance1
sum2 = price2 + design2 + speed2 + load2 + performance2
sum3 = price3 + design3 + speed3 + load3 + performance3
sum4 = price4 + design4 + speed4 + load4 + performance4
sum5 = price5 + design5 + speed5 + load5 + performance5

parameters.append('')
importance.append('')

df = pd.DataFrame({'№': ['1', '2', '3', '4', '5', 'Сума'],
                   'Параметри': parameters,
                   'Вага': importance,
                   samokats[0]: [price1, speed1, design1, performance1, load1, sum1],
                   samokats[1]: [price2, speed2, design2, performance2, load2, sum2],
                   samokats[2]: [price3, speed3, design3, performance3, load3, sum3],
                   samokats[3]: [price4, speed4, design4, performance4, load4, sum4],
                   samokats[4]: [price5, speed5, design5, performance5, load5, sum5]})

print(Style.BRIGHT + Fore.GREEN + "Результат:")
print(df)
print('\n')

winer = ''
points = ''

if sum1 > sum5 and sum1 > sum3 and sum1 > sum2 and sum1 > sum4:
    winer = samokats[0]
    points = sum1
elif sum2 > sum5 and sum2 > sum3 and sum2 > sum1 and sum2 > sum4:
    winer = samokats[1]
    points = sum2
elif sum3 > sum5 and sum3 > sum2 and sum3 > sum1 and sum3 > sum4:
    winer = samokats[2]
    points = sum3
elif sum4 > sum5 and sum4 > sum2 and sum4 > sum1 and sum4 > sum3:
    winer = samokats[3]
    points = sum4
elif sum5 > sum4 and sum5 > sum2 and sum5 > sum1 and sum5 > sum3:
    winer = samokats[4]
    points = sum5
else:
    print("Щось пішло не так при обличсленнях переможця, або переможець не один!")

print(Fore.YELLOW + "Найкращим варіантом вийшов -",winer, '-', points)
print('\n')