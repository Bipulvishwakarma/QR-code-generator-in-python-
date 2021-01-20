import pyqrcode
name=input("enter your name")
age=input("enter your age")
nameage=name+age
qr=pyqrcode.create(nameage)
qr.png("name.png",scale=6)
