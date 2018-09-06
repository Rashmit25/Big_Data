#!/usr/bin/python3
import sys
import datetime
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def read_input(file):
        for line in file:
                if('VendorID' in line):
                        pass
                else:
                        yield line.replace('\n','').split(',')

def main(separator='\t'):
        data=read_input(sys.stdin)
        for fields in data:
                year,month,day=fields[1][0:4],fields[1][5:7],fields[1][8:10]
                date=datetime.date(int(year),int(month),int(day))
                hour=fields[1][-8:-6]
                print('%d%s%d%s%s%s%d%s%d' % (date.weekday(),separator,int(month)-1,separator,hour,separator,int(fields[3]),separator,1))
                del year
                del month
                del day
                del date
                del hour

if __name__ == '__main__':
        main()
        del days
