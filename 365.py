import webbrowser
import pyperclip

z=input("enter name of project\n")
y=input("what day of project \n")
x=input("what date today\n")
a=f"{y} of the 365 chalenge in 2022 1 day 1"
b=f"-  [x] {x} {z}"
webbrowser.open("https://github.com/new")
webbrowser.open("https://github.com/liad07/365/edit/main/README.md")
pyperclip.copy(a)
pyperclip.copy(z)
print(a)
print(b)


