import os
import sys

print('Аргументы командой строки')
for i in sys.argv:
    print(i)

print('\n\nПерменная PYTHONPATH содержит', sys.path, '\n')

print(os.getcwd())
