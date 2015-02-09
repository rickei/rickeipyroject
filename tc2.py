#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import time

screen = curses.initscr()
screen.border(0)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
i=2
str = " how "
#screen.addstr(2,2,"This is a Sample Curses Script")
#screen.addstr(2,2," theffffffffffffffff")

#for i in range(1,10):
#  time.sleep(0.2)
#  screen.addstr(2,i," hello ")
#  i=i+1
screen.addstr(2,i,str)



while True:
    event = screen.getch()
    if event == ord("q"):
      break
    elif event == ord("k") :
      if i== 60 :
        i=60
      else :
          i=i+1
      screen.addstr(2,i,str)
      screen.refresh()

    elif event == ord("j") :
      if i== 2 :
        i=2
      else :
          i=i-1
      screen.addstr(2,i,str)
      screen.refresh()


    elif event == ord("m") :
      for i in range(i,20) :
        time.sleep(0.1)
        screen.addstr(2,i, str)
        screen.refresh()
        i=i+1

curses.endwin()
