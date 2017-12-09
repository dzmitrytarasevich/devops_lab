import sys
import platform
import subprocess
from termcolor import colored

# 1. Print Python version
print(colored("1. Python version: ", 'green') + platform.python_version() + '\n')
# 2. Print virtual environment
virt_env = subprocess.Popen(['pyenv', 'version-name'], stdout=subprocess.PIPE)
virt_env, err = virt_env.communicate()
print(colored("2. Virtual environment: ", 'green') + virt_env + '\n')
# 3. Print executable location
print(colored("3. Executable location: ", 'green') + sys.executable + '\n')
# 4. Print pip location
pip_location = subprocess.Popen(['which', 'pip'], stdout=subprocess.PIPE)
pip_location, err = pip_location.communicate()
print(colored("4. Pip location: ", 'green') + pip_location + '\n')
# 5. Print pythonpath
print(colored("5. $PYTHONPATH: ", 'green') + sys.executable + '\n')
# 6. Print installed packages
pip_freeze = subprocess.Popen(['pip', 'freeze'], stdout=subprocess.PIPE)
pip_freeze, err = pip_freeze.communicate()
print(colored("6. Installed packages:", 'green') + '\n' + pip_freeze + '\n')
# 7. Print site-packages location
pack_location = next(p for p in sys.path if "site-packages" in p)
print(colored("7. Site-packages location:", 'green') + pack_location + '\n')
