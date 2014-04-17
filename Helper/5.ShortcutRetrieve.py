
import sys
import win32com.client
 
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut("Music.lnk")
print(shortcut.Targetpath)
       
