#!/usr/bin/python3

from itertools import groupby
from operator import itemgetter
import sys
from collections import Counter

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
hours=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
months=['January','February','March','April','May','June','July','August','September','October','November','December']

def read_mapper_output(file, separator='\t'):
        for line in file:
                yield line.rstrip().split(separator)

def main(separator='\t'):
        data=read_mapper_output(sys.stdin,separator=separator)
        dayTripCount={}
        dayPassCount={}
        generalPassCount=0.0
        generalTripCount=0.0
        monthPassCount=Counter()
        monthTripCount=Counter()
        for day, group in groupby(data, itemgetter(0)):
                try:
                        dayPassCount[day]=Counter()
                        dayTripCount[day]=Counter()
                        for day,month,hour,count,num in group:
                                dayPassCount[day][hour]+=int(count)
                                dayTripCount[day][hour]+=int(num)
                                monthPassCount[month]+=int(count)
                                monthTripCount[month]+=int(num)
                                generalPassCount+=int(count)
                                generalTripCount+=1
                except (ValueError):
                        pass

        print("Monthly Stats\n")
        for i in range(13):
                if(str(i) in monthPassCount.keys()):
                        avg=monthPassCount[str(i)]/monthTripCount[str(i)]
                        print(months[i].ljust(9," ")+" "+str(round(avg,4)))
                        del avg
        del monthPassCount
        del monthTripCount

        print("\nThrough the Week Stats\n")
        weekdayPass={}
        weekdayCount={}
        weekendPass={}
        weekendCount={}
        for i in range(7):
                totalDayPass=0.0
                totalDayCount=0.0
                if(str(i) in dayPassCount.keys()):
                        for hour in dayPassCount[str(i)].keys():
                                totalDayPass+=dayPassCount[str(i)][hour]
                                totalDayCount+=dayTripCount[str(i)][hour]
                                if(i<=4):
                                        weekdayPass[hour]=dayPassCount[str(i)][hour]
                                        weekdayCount[hour]=dayTripCount[str(i)][hour]
                                else:
                                        weekendPass[hour]=dayPassCount[str(i)][hour]
                                        weekendCount[hour]=dayTripCount[str(i)][hour]
                        avg=totalDayPass/totalDayCount
                        print(days[i].ljust(9," ")+" "+str(round(avg,4)))
                        del avg
                        del totalDayPass
                        del totalDayCount
        del dayPassCount
        del dayTripCount

        print("\nWeekdays Vs Weekends\n")
        print("Days".rjust(18," ")+"Ends".rjust(9," "))
        for key in hours:
                try:
                        if (key in weekdayPass.keys()):
                                weekdayAvg=weekdayPass[key]/weekdayCount[key]
                                weekdayAvg=round(weekdayAvg,4)
                                if(key in weekendPass.keys()):
                                        weekendAvg=weekendPass[key]/weekendCount[key]
                                        weekendAvg=round(weekendAvg,4)
                                else:
                                        weekendAvg=round(0.0,4)
                                if(key=='23'):
                                        print("23:00-00:00 - "+str(weekdayAvg)+" | "+str(weekendAvg))
                                else:
                                        print(key+":00-"+str(int(key)+1).rjust(2,'0')+":00 - "+str(weekdayAvg)+" | "+str(weekendAvg))
                except:
                        pass
        print("\nOverall Average Passengers per Trip: "+str(round(generalPassCount/generalTripCount,4)))

if __name__ == '__main__':
        main()