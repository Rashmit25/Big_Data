
#!/usr/bin/python3
import sys
def read_input(file):
        for line in file:
                if('payment_type' in line):
                        pass
                else:
                        yield line.replace('\n','').split(',')

def main(separator='\t'):
        data=read_input(sys.stdin)
        for fields in data:
                print('%s%s%d' % (fields[11],separator,1))

if __name__ == '__main__':
        main()