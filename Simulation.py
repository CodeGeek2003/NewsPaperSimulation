import random
TotalProfit=0
Random_Type=[]
Demand=[]
Revenue=[]
LostProfit=[]
SalvageOfScrap=[]
Dailyprofit=[]
TypeOfNewsDay=[]
PaperCost= int(input("Enter the cost of buying one newspaper: "))
PaperProfit= int(input("Enter the profit of selling one newspaper: "))
PaperSell=int(input("Enter the price of selling one newspaper: "))
Scrap=int(input("Enter the scrap price of newspaper not sold at the end of the day: "))
purchase=int(input("Enter the number of newspapers purchased: "))
N=random.randint(1,100)
for i in range (N):
    Random_Type.append(random.randint(1,100))
    if 1 <= Random_Type[i] <= 35:
        TypeOfNewsDay.append( "Good")
    elif 36 <= Random_Type[i] <= 80:
        TypeOfNewsDay.append("Fair")
    else:
        TypeOfNewsDay.append("Poor")
    Demand.append(random.randint(1,100))
    if TypeOfNewsDay[i] == "Good":
        if 1 <= Demand[i] <= 3:
            Demand[i]=40
        elif 1 <= Demand[i] <= 3:
            Demand[i]=40
        elif 9 <= Demand[i] <= 23:
            Demand[i]=60
        elif 24 <= Demand[i] <= 43:
            Demand[i]=70
        elif 44 <= Demand[i] <= 78:
            Demand[i]=80
        elif 79 <= Demand[i] <= 93:
            Demand[i]=90
        else :
            Demand[i]=100
    elif TypeOfNewsDay[i] == "Fair":

        if 1 <= Demand[i] <= 10:
            Demand[i]=40
        elif 11 <= Demand[i] <= 28:
            Demand[i]=50
        elif 29 <= Demand[i] <= 68:
            Demand[i]=60
        elif 69 <= Demand[i] <= 88:
            Demand[i]=70
        elif 89 <= Demand[i] <= 96:
            Demand[i]=80
        else :
            Demand[i]=90
    else:
        if 1 <= Demand[i] <= 44:
            Demand[i]=40
        elif 45 <= Demand[i] <= 66:
            Demand[i]=50
        elif 67<= Demand[i] <= 82:
            Demand[i]=60
        elif 83 <= Demand[i] <= 94:
            Demand[i]=70
        else:
            Demand[i]=80
for i in range(N):
    if Demand[i] >= purchase:
        Revenue.append(PaperCost-PaperSell)
        LostProfit.append(((Demand[i]-purchase) * PaperProfit) / 100)
        SalvageOfScrap.append(0)
        Dailyprofit.append(Revenue[i]-PaperCost-LostProfit[i]+SalvageOfScrap[i])
        TotalProfit+=Dailyprofit[i]-LostProfit[i]

    else:
        Revenue.append((Demand[i] * PaperSell) / 100)
        LostProfit.append(0)
        SalvageOfScrap.append(((purchase-Demand[i]) * Scrap) / 100)
        Dailyprofit.append(Revenue[i]-PaperCost-LostProfit[i]+SalvageOfScrap[i])
        TotalProfit += Dailyprofit[i] - LostProfit[i]

print('''Day Type_of_NewsDa   Demand   Revenue_for_sale   LostProfit  Salvage_of_scap  DailyProfit''')

for i in range(N):
        if(Dailyprofit[i]<0):
            Dailyprofit[i]=0
        print("Day" , (i + 1) ,"    " ,
                         TypeOfNewsDay[i] , "           " ,
                         Demand[i] , "      " ,
                         Revenue[i] , "              " ,
                         LostProfit[i] , "          " ,
                         SalvageOfScrap[i] , "           " ,
                         Dailyprofit[i] , "       " )

if TotalProfit>=0:
    print("Total profit: ", TotalProfit)
else:
    print("There is no profit ")




