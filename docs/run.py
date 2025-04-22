import sys
import subprocess
import os
current_file_dir = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable,"-m",'pip','install','-r',f'{current_file_dir}\\requirement.txt','-U'])
subprocess.run([sys.executable,f"{current_file_dir}\\manage.py",'migrate'])
subprocess.run([sys.executable,f"{current_file_dir}\\manage.py",'createsuperuser'])
subprocess.run([sys.executable,f"{current_file_dir}\\waitress-run.py"])