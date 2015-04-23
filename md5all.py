"""
Script for mass MD5'ing a directory. Run and automagicilly receive your output CSV <default == output.md5>
version 0.0.0.0.2
@gimbi
"""
import os, shutil, hashlib

PATH = "."
OUTPUT_FILE = "output.md5"

def md5_file(f, block_size = 2**20):
 """
 Generates MD5 hash. Credited to Laurent Luce http://www.laurentluce.com/
 """
 md5 = hashlib.md5()
 with open(f,'rb') as file_:
  while 1:
   data = file_.read(block_size)
   if not data: break
   md5.update(data)
  return md5.hexdigest()

def main():
 """
 Whatevs, yo.
 """
 file_list = os.listdir(PATH)
 with open(OUTPUT_FILE, 'w') as output_file:
  for file_name in file_list:
   try: output_file.write(md5_file(file_name) + ',' + file_name + '\n')
   except: 
    print "File %s skipped" % (file_name)
  
if __name__ == '__main__':
 main()
