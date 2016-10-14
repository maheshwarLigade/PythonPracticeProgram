import time
import webbrowser

total_break = 3
break_count = 0
print("This program is started at "+ time.ctime())

while(break_count < total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=9ycyT4nrTpY")
    break_count = break_count + 1

