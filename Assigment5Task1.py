dictionary = {"Alice":85,"Gourav":98,"Teja":85,"Vardhan":75}
name = str(input("Enter the student's name: "))
if str(dictionary.get(name)) == "None":
     print("Student not found.")
else:
     print(name +"'s marks: "+str(dictionary.get(name)))