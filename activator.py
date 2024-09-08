import os

path = os.path.abspath(__file__)[0:-12]
os.system(f'start cmd /k "cd {path} & activate & cd ../.."')