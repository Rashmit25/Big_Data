#!/usr/bin/python3

from itertools import groupby
from operator import itemgetter
import sys
paymentType=['Credit Card','Cash','No Charge','Dispute','Unknown','Voided Trip']

def read_mapper_output(file, separator='\t'):
        for line in file:
                yield line.rstrip().split(separator,1)

def main(separator='\t'):
        data=read_mapper_output(sys.stdin,separator=separator)
        for current_type, group in groupby(data, itemgetter(0)):
                try:
                        total_count=sum(int(count) for current_type, count in group)
                        print('%s%s%d' % (paymentType[int(current_type)-1].ljust(11," "),separator,total_count))
                except ValueError:
                        pass

if __name__ == '__main__':
        main()