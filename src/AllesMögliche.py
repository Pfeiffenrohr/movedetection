import os
import glob

lines = []
basedir =  "C:/temp/motion"
source_dir = os.path.join(basedir, "source")
dest_dir= os.path.join(basedir, "dest")
lines=os.listdir(source_dir)
# hoffentlich sind es nicht so viele Zeilen. ;-)
for line in lines:
  # Parent Directory path
  # Path
  parts = line.split('.')
  path = os.path.join(dest_dir, parts [0])
  print(path)
  os.mkdir(path)