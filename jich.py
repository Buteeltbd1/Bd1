from datetime import date, timedelta
from prettytable import PrettyTable

year1 = 5
year2 = 7
year3 = 4
total_years = year1 + year2 + year3

start_date = date(2006, 9, 1) #анхны хичээлийн жилийн эхлэх хугацаа
ee_date = date(2007,6,1)

end_date1 = date(start_date.year + year1, 6, 1) #бага ангийн хичээлийн жилийн дуусах хугацаа
start_date1 = date(end_date1.year, 9, 1) #дунд, ахлах ангийн хичээлийн жилийн эхлэх хугацаа
end_date2 = date(start_date1.year + year2, 6, 1) #дунд, ахлах ангийн хичээлийн жилийн дуусах хугацаа
start_date2 = date(end_date2.year, 9, 1) #их сургуулийн хичээлийн жилийн эхлэх хугацаа

end_date = date(start_date.year + total_years, 6, 1) #сүүлийн хичээлийн жилийн дуусах хугацаа

minus_date = 30 + 31 + 31 #6,7,8 сар

total_days1 = (end_date1 - start_date).days - ((year1 - 1) * minus_date)#нийт өдөр(бага анги)
total_days2 = (end_date2 - start_date1).days - ((year2 - 1) * minus_date)#нийт өдөр(дунд,ахлах анги)
total_days3 = (end_date - start_date2).days - ((year3 - 1) * minus_date)#нийт өдөр(их сургууль анги)
total_days = (end_date - start_date).days - ((total_years - 1) * minus_date) #нийт өдөр



workdays1 = 0
for day in range(total_days1):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 5: 
        workdays1 += 1        

workdays2 = 0
for day in range(total_days2+1):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 5: 
        workdays2 += 1

workdays3 = 0
for day in range(total_days3+1):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 5:  
        workdays3 += 1

workdays = 0
for day in range(total_days+1):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 5:
        workdays += 1

        
        
total_time1 = workdays1 * 4 * 30 
total_time2 = workdays2 * 6 * 35 
total_time3 = workdays3 * 3 * 90 

#дунд сургуулийн сурагчдын нийт өдөр

dav = 0
for day in range((ee_date-start_date).days):
    current_date = start_date + timedelta(days=day)
    check_date = current_date + timedelta(days=6)
    if current_date.weekday() == 0 and check_date.weekday() == 6: 
        dav += 1
if check_date != ee_date:
            dav -= 1        
davtlaga = dav * 4

dav1 = 0
for day in range(total_days2):
    current_date = start_date1 + timedelta(days=day)
    check_date = current_date + timedelta(days=6)
    if current_date.weekday() == 0 and check_date.weekday() == 6: 
        dav1 += 1
if check_date != end_date2:
            dav1 -= 1        
davtlaga1 = dav1 * 4

myTable = PrettyTable(["Эхэлсэн огноо", "Дууссан огноо","Суралцсан жил","Нийт хоног","Ажлын хоног","Нийт хичээлийн цаг","7 хоногийн хичээлийн цаг", "Сонирхсон хичээлийн цаг"])
myTable.add_row([start_date, end_date1, year1,total_days1, workdays1, total_time1, 4 * 5,davtlaga])
myTable.add_row([start_date1, end_date2, year2,total_days2, workdays2, total_time2, 6 * 5, davtlaga1])
myTable.add_row([start_date2, end_date, year3,total_days3, workdays3, total_time3, 3 * 5, 0])


myTable1 = PrettyTable(["Эхэлсэн огноо", "Дууссан огноо","Нийт хоног","Ажлын хоног","Нийт хичээлийн цаг(минут)","Сонирхсон хичээлийн цаг"])
sum = 0
for i in range(year1+year2):     
    s_date = date(start_date.year + i, 9, 1)
    e_date = date(start_date.year + 1 + i, 6, 1)
    tot_date = (e_date - s_date).days 
    works = 0
    for day in range(tot_date):
        current_date = start_date + timedelta(days=day)
        if current_date.weekday() < 5:
            works += 1
    dav = 0
    if (s_date.year <= s_date.year + 12):
        for day in range(tot_date):
            current_date = s_date + timedelta(days=day)
            check_date = current_date + timedelta(days=6)
            if current_date.weekday() == 0 and check_date.weekday() == 6: 
                dav += 1
        if check_date != e_date:
                    dav -= 1        
        davtlaga = dav * 4    
    if (i < 5):
        tot_time = works * 4 * 30
        myTable1.add_row([s_date, e_date, tot_date, works, f"{works} өдөр * 4 цаг * 30 мин = {tot_time} мин" ,davtlaga]) 
        sum += tot_time
    elif (i < 12):
        tot_time = works * 6 * 35
        myTable1.add_row([s_date, e_date, tot_date, works, f"{works} өдөр * 6 цаг * 35 мин = {tot_time} мин" ,davtlaga])
        sum += tot_time
    elif (i < 16):
        tot_time = works * 3 * 90
        myTable1.add_row([s_date, e_date, tot_date, works, f"{works} өдөр * 3 цаг * 90 мин = {tot_time} мин" ,davtlaga])  
        sum += tot_time 
myTable1.add_row([0,0,0,0,sum,0])
print(myTable1)

myTable2 = PrettyTable(["Эхэлсэн огноо", "Дууссан огноо","Дадлагын хоног","Дадлагын цаг эзлэх хувь"])
dadlaga = 8 * 5
for i in range(year3):
    s_date = date(start_date2.year + i, 9, 1)
    e_date = date(start_date2.year + 1 + i, 6, 1)
    tot_date = (e_date - s_date).days 
    dad = 0
    for day in range(tot_date):
        current_date = start_date + timedelta(days=day)
        if current_date.weekday() < 5: 
            dad += 1
    d = dadlaga * 100 / dad
    myTable2.add_row([s_date, e_date, dadlaga, "{:.2f}".format(d)])
