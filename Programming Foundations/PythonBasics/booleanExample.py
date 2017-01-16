username = "resident"
password = "admin123"

if username == "admin" and password == "admin123":
    print("welcome")
elif username == "resident" or password == "res":
    print("welcome resident")
else:
    print("intruder")