import json
FILE_NAME ="students.json"
#-----------LOAD DATA------------
def load_data():
   try:
      with open(FILE_NAME,"r") as file:
         data=json.load(file)
         return data
   except:
      return []#if file doesnt exist

#-------------SAVE DATA-------------------
def save_data(students):
   with open(FILE_NAME,"w") as file:
      json.dump(students,file,indent=4)

#LOAD EXISTING STUDENTS
students=load_data()

while True:
   print("----------STUDENT MANAGEMENT SYSTEM----------------\n")
   print("1.Add student")
   print("2.View student")
   print("3.Search Student")
   print("4.Update student")
   print("5.Show Topper")
   print("6.Del student")
   print("7.Exit")
   choice=input("Enter your choice:")
   #Add
   if choice=="1":
      sid=int(input("Enter ID:"))
      name=input("Enter your name")
      marks=input("Enter your marks")
      student={
         "id":sid,
         "name":name,
         "marks":marks
      }
      students.append(student)
      save_data(students)
      print("STUDENT ADDED SUCCESSFULLY!")

   #VIEW STUDENT
   elif choice=="2":
      if len(students)==0:
         print("No students found.")
      else:
         for student in students:
           print("\n----------")
           print("ID:",student["id"])
           print("Name",student["name"])
           print("Marks:",student["marks"])

   #SEARCH STUDENT
   elif choice=="3":
      sid=int(input("Enter ID to search"))
      found=False
      for student in students:
         if student["id"]==sid:
            print("Student Found!")
            print("ID:",student["id"])
            print("Name",student["name"])
            print("Marks:",student["marks"])
            found=True
            break
         
         if not found:
            print("Student not found")
   #UPDATE 
   elif choice=="4":
      sid=int(input("Enter ID to update"))
      Found=False
      for s in students:
         if s["id"]==sid:
            print("\ncurrent details:")
            print("ID:",s["id"])
            print("Name:",student["name"])
            print("Marks:",s["marks"])
            new_name=input("Enter new name:")
            new_marks=input("Enter new marks:")
            s["name"]=new_name
            s["marks"]=new_marks
            save_data(students)
            print("Student updated successfully!")
            Found=True
            break
      if not Found:
         print("Student not found.")

   elif choice=="5":
      if len(students)==0:
         print("No student found.")
      else:
         topper=students[0]
         for s in students:
            if s["marks"]>topper:
               topper=s
            print("\n🏆 Topper Student")
            print("ID:", topper["id"])
            print("Name:", topper["name"])
            print("Marks:", topper["marks"])
   #DELETE
   elif choice=="6":
      sid=int(input("Enter ID to delete:"))
      Found=False
      for student in students:
         if student["id"]==sid:
            students.remove(student)
            save_data(students)
            print("Student deleted successfully")
            found=True
            break
         if not found:
            print("student not found")
            
   # EXIT  
   elif choice=="7":
      print("Exiting program...")
      break
    
   else:
      print("Invalid choice.Try again")
