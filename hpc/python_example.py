#!/usr/bin/python

import sys, getopt, resource, time 

def main(argv):
   wait_time = 10
   listlength = 0
   try:
      opts, args = getopt.getopt(argv,"ht:l:o",["time=","length=","output="])
   except getopt.GetoptError as err:
      print str(err)
      print 'python_example.py -t <wait time> -l <list length> -o <output file>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'python_example.py -t <wait time> -l <list length> -o <output file>'
         sys.exit()
      elif opt in ("-t", "--time"):
         wait_time = max(10, float(arg) );
      elif opt in ("-l", "--length"):
         listlength = max(0, int(arg) );
      elif opt in ("-o", "--output"):
         output_file = arg
   print 'Wait time is:', wait_time, 'seconds'
   print 'List length is:', listlength
     
   list = []
   for i in range(0, listlength ):
     list.append(1)
     
   time.sleep( wait_time )
     
   print 'Memory usage:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0, 'MB'

if __name__ == "__main__":
   main(sys.argv[1:])