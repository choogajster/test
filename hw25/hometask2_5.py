import subprocess
import  os

# os.mkdir('Output')
os.chdir('a')

subprocess.run(['convert.exe', '*.jpg', '-resize', '200x200'])