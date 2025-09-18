# 這個是主要用來輸出的文件，所以 from "Lesson5_hello_world", import "hello" function
import sys
from Lesson5_hello_world import hello
from Lesson5_hello_world import goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])
else:
    hello(None)
    goodbye(None)

# using terminal to output by type in: python Lesson5_import_with_hello_world.py
