def loading(file_name):
    print("Loaded weather data from",file_name[0].upper()+file_name[1:-4],"\n")

def daily(file_name):
    date = input("Give a date (dd.mm): ") #06.10
    search="2019-"+date[3:]+"-"+date[0:2]
    with open(file_name, "r") as weather_file:
        weather_file.readline()
        for line in weather_file:
            if search in line:
                data=line.split(";")
                print("The weather on",date,"was on average",data[2],"centigrade")
                print("The lowest temperature was",data[3],"and the highest temperature was",data[4])
                print("There was",data[1],"mm rain \n")

def statistics(file_name):
    sum1=0
    sum2=0
    sum3=0
    i=0
    with open(file_name,"r") as wf:
        wf.readline()
        for row in wf:
            details=row.split(";")
            sum1=sum1+float(details[2])
            sum2=sum2+float(details[3])
            sum3=sum3+float(details[4])
            i=i+1
        average1=sum1/i
        average2=sum2/i
        average3=sum3/i
        
        print("The average temperature for the 25 day period was",round(average1,1))
        print("The average lowest temperature was",round(average2,1))
        print("The average highest temperature was",round(average3,1),"\n")
        
def print_temperature_line(day, month, temp): 
    
    print(day + "." + month + " ", end="")

    print("   "*(temp+5) + "-", end="")
    
    print()

def print_temperature_axis():
    print("      ", end="")
    for i in range(-5,16):
        print("{:02d} ".format(i), end="")
    print()
    
    
while True:
    print("ACME WEATHER DATA APP")
    print("""1) Choose weather data file \n2) See data for selected day \n3) Calculate average statistics for the data \n4) Print a scatterplot of the average temperatures \n0) Quit program""")
    choice=int(input("Choose what to do: "))
    if choice==0:
        break
    elif choice==1:
        file_name=input("Give name of the file: ")
        loading(file_name)
    elif choice==2:
        daily(file_name)
    elif choice==3:
        statistics(file_name)
    elif choice==4:
        with open(file_name,"r") as f:
            f.readline()
            for row in f:
                info=row.split(";")
                time=info[0]
                day=time[9:11]
                month=time[6:8]
                temp=float(info[2])
                temp=round(temp)
                print_temperature_line(day, month, temp)
        print_temperature_axis()