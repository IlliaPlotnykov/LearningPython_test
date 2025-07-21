import datetime
import sys
sys.path.append("..")
from Package_Test.File_1 import Human as h

d_one = datetime.datetime.now(datetime.UTC)

print(d_one)
print(type(d_one))

one_human = h('Igor')
one_human.say()
