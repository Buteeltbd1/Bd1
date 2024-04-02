from datetime import date, timedelta
from prettytable import PrettyTable

year1 = 3
year2 = 5
year3 = 2
year4 = 5
total_years = year1 + year2 + year3 + year4

start_date = date(1978, 9, 1) #анхны хичээлийн жилийн эхлэх хугацаа
e_date = date(1979,6,1)

end_date1 = date(start_date.year + year1, 6, 1)
start_date1 = date(end_date1.year, 9, 1)
end_date2 = date(start_date1.year + year2, 6, 1) 
start_date2 = date(end_date2.year, 9, 1)
end_date3 = date(start_date2.year + year3, 6, 1)
start_date3 = date(end_date3.year, 9, 1)
end_date = date(start_date.year + total_years, 6, 1) #сүүлийн хичээлийн жилийн дуусах хугацаа

minus_date = 30 + 31 + 31 #6,7,8 сар

total_days1 = (end_date1 - start_date).days - ((year1 - 1) * minus_date)
total_days2 = (end_date2 - start_date1).days - ((year2 - 1) * minus_date)
total_days3 = (end_date3 - start_date2).days - ((year3 - 1) * minus_date)
total_days4 = (end_date - start_date3).days - ((year4 - 1) * minus_date)
total_days = (end_date - start_date).days - ((total_years - 1) * minus_date) #нийт өдөр
 
toto_date = (e_date - start_date).days

workdays1 = 0
for day in range(total_days1):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 6: 
        workdays1 += 1

workdays2 = 0
for day in range(total_days2):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 6:  
        workdays2 += 1

workdays3 = 0
for day in range(total_days3):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 6:  
        workdays3 += 1

workdays4 = 0
for day in range(total_days4):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 6:  
        workdays4 += 1

workdays = 0
for day in range(total_days):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 6:  
        workdays += 1

work = 0
for day in range(toto_date):
    current_date = start_date + timedelta(days=day)
    if current_date.weekday() < 6:
        work += 1

total_time1 = workdays1 * 4 *45 
total_time2 = int(workdays2 * 34 * 45 / 6) 
total_time3 = workdays3 * 6 *45 
total_time4 = workdays4 * 3 * 90  

dav = 0
for day in range(total_days1):
    current_date = start_date + timedelta(days=day)
    check_date = current_date + timedelta(days=6)
    if current_date.weekday() == 0 and check_date.weekday() == 6: 
        dav += 1
if check_date != end_date1:
            dav -= 1        
davtlaga = dav * 4
dav1 = 0
for day in range(total_days2):
    current_date = start_date + timedelta(days=day)
    check_date = current_date + timedelta(days=6)
    if current_date.weekday() == 0 and check_date.weekday() == 6: 
        dav1 += 1
if check_date != end_date2:
            dav1 -= 1        
davtlaga1 = dav1 * 4
dav2 = 0
for day in range(total_days3):
    current_date = start_date + timedelta(days=day)
    check_date = current_date + timedelta(days=6)
    if current_date.weekday() == 0 and check_date.weekday() == 6: 
        dav2 += 1
if check_date != end_date3:
            dav2 -= 1        
davtlaga2 = dav2 * 4

print(toto_date,work)

myTable = PrettyTable(["Эхэлсэн огноо", "Дууссан огноо","Суралцсан жил","Нийт хоног","Ажлын хоног","Нийт хичээлийн цаг(минут)","7 хоногийн хичээлийн цаг", "Сонирхсон хичээлийн цаг"])
myTable.add_row([start_date, end_date1, year1,total_days1, workdays1, total_time1, 4 * 6,davtlaga])
myTable.add_row([start_date1, end_date2, year2,total_days2, workdays2, total_time2, 6 * 6, davtlaga1])
myTable.add_row([start_date2, end_date3, year3,total_days3, workdays3, total_time3, 34, davtlaga2])
myTable.add_row([start_date3, end_date, year4,total_days4, workdays4,  total_time4, 3 * 6 , 0])


myTable1 = PrettyTable(["Эхэлсэн огноо", "Дууссан огноо","Нийт хоног","Ажлын хоног","Нийт хичээлийн цаг(минут)","Сонирхсон хичээлийн цаг"])
sum = 0
for i in range(year1+year2+year3):     
    s_date = date(start_date.year + i, 9, 1)
    e_date = date(start_date.year + 1 + i, 6, 1)
    tot_date = (e_date - s_date).days 
    works = 0
    for day in range(tot_date):
        current_date = start_date + timedelta(days=day)
        if current_date.weekday() < 6:
            works += 1
    dav = 0
    if (s_date.year <= s_date.year + 10):
        for day in range(tot_date):
            current_date = s_date + timedelta(days=day)
            check_date = current_date + timedelta(days=6)
            if current_date.weekday() == 0 and check_date.weekday() == 6: 
                dav += 1
        if check_date != e_date:
                    dav -= 1        
        davtlaga = dav * 4  
    if (i < 3):
        tot_time = works * 4 * 45
        myTable1.add_row([s_date, e_date, tot_date, works, f"{works} өдөр * 4 цаг * 45 мин = {tot_time} мин" ,davtlaga])
        sum += tot_time 
    elif (i < 8):
        tot_time = int(works * 34 * 45 / 6)
        myTable1.add_row([s_date, e_date, tot_date, works,  f"{works} өдөр * 34 цаг / 6 хоног * 45 мин  = {tot_time} мин" ,davtlaga])
        sum += tot_time 
    elif (i < 11):
        tot_time = works * 6 * 45  
        myTable1.add_row([s_date, e_date, tot_date, works,  f"{works} өдөр * 6 цаг * 45 мин = {tot_time} мин"  ,davtlaga])
        sum += tot_time 
    elif (i < 16):
        tot_time = works * 3 * 90
        myTable1.add_row([s_date, e_date, tot_date, works,  f"{works} өдөр * 3 цаг * 90 мин = {tot_time} мин"  ,davtlaga])
        sum += tot_time    
myTable1.add_row([0,0,0,0,sum,0])    
print(myTable1)

myTable2 = PrettyTable(["Эхэлсэн огноо", "Дууссан огноо","Дадлагын хоног","Дадлагын цаг эзлэх хувь"])
dadlaga = 8 * 6
for i in range(year4):
    s_date = date(start_date3.year + i, 9, 1)
    e_date = date(start_date3.year + 1 + i, 6, 1)
    tot_date = (e_date - s_date).days 
    dad = 0
    for day in range(tot_date):
        current_date = start_date + timedelta(days=day)
        if current_date.weekday() < 6: 
            dad += 1
    d = dadlaga * 100 / dad
    myTable2.add_row([s_date, e_date, dadlaga, "{:.2f}".format(d)])
