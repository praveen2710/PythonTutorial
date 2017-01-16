princ = input("Enter principal:")
time = input("Enter time in years:")
roi = input("Enter interest %:")

princ = int(princ)
time = int(time)
roi = int(roi)

si = (princ*time*roi)/100

print(si)
