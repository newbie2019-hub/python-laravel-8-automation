@echo off

set fn=%1

If "%1"=="" (
    echo Error! Projname missing
)else ( 
    C:\Users\Sabay\AppData\Local\Programs\Python\Python37\python.exe D:\YVANSABAY\python-create\create.py %fn%
)