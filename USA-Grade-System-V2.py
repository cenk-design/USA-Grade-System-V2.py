note = []
toplam1 = 0
çarp = []
toplam2 = 0
grade = []

clas = int(input("What are you grade in? "))
if clas == 6:
    grade_6_courses = [
        "English Language Arts (ELA)",
        "6th Grade Mathematics",
        "Earth & Space Science",
        "World History & Geography",
        "Physical Education (PE)",
        "Health Education",
        "Custom / Other"
    ]
    
    print()
    
    print("Please finish writing when you've completed your elective courses!!")
    
    print()
    
    while True:
        electives = input("Please enter your elective course: ")
        print()
        
        if electives == "finish":
            break
        
        grade_6_courses.append(electives)
        
    print()
    
    for zmn in grade_6_courses:
        time = int(input(f"{zmn} class time: "))
        çarp.append(time)
        
        print()
        
        
        
    for ders in grade_6_courses:
        
        notum = input(f"{ders} Letter or Numerical Grade: ")
        note.append(notum)
 
        try:
            sayı = float(notum)

            
            if sayı >= 97:
                grade.append(4.0)
            elif sayı >= 93:
                grade.append(4.0)
            elif sayı >= 90:
                grade.append(3.7)
            elif sayı >= 87:
                grade.append(3.3)
            elif sayı >= 83:
                grade.append(3.0)
            elif sayı >= 80:
                grade.append(2.7)
            elif sayı >= 77:
                grade.append(2.3)
            elif sayı >= 73:
                grade.append(2.0)
            elif sayı >= 70:
                grade.append(1.7)
            elif sayı >= 67:
                grade.append(1.3)
            elif sayı >= 65:
                grade.append(1.0)
            elif sayı >= 0:
                grade.append(0.0)
            else:
                break
        
        except ValueError:
            if notum == "A" or notum == "A+":
                grade.append(4)
            elif notum == "A-":
                grade.append(3.7)
            elif notum == "B+":
                grade.append(3.3)
            elif notum == "B":
                grade.append(3.0)
            elif notum == "B-":
                grade.append(2.7)
            elif notum == "C+":
                grade.append(2.3)
            elif notum == "C":
                grade.append(2.0)
            elif notum == "C-":
                grade.append(1.7)
            elif notum == "D":
                grade.append(1.0)
            elif notum == "F":
                grade.append(0.0)
            else:
                break
    
    print("Toplam not sayısı:", len(grade_6_courses))
    print("Notlar: ", note)
    
    print()
    
    for i in range(len(note)):
        toplam1 += çarp[i]
        toplam2 += çarp[i] * grade[i]
        
    ort1 = toplam2 / toplam1
    print('Ortalama: ', ort1)
    
    
if clas == 7:
    grade_7_core_subjects = [
    "English Language Arts (ELA 7)",
    "7th Grade Mathematics",
    "Pre-Algebra",                     
    "Life Science / Biology Basics",    
    "Ancient World History & Geography",
    "Physical Education (PE 7)",
    "Health & Wellness",
    "Custom / Other"                   
]


    print()
    
    print("Please finish writing when you've completed your elective courses!!")
    
    print()
    
    while True:
        electives = input("Please enter your elective course: ")
        print()
        
        if electives == "finish":
            break
        
        grade_7_core_subjects.append(electives)
        
    print()
    
    for zmn in grade_7_core_subjects:
        time = int(input(f"{zmn} class time: "))
        çarp.append(time)
        
        print()
        
        
    
    for ders in grade_7_core_subjects:
        notum = input(f"{ders} Letter Grade: ")
        note.append(notum)
        
        try:
            sayı = float(notum)
        
            if sayı >= 97:
                grade.append(4.0)
            elif sayı >= 93:
                grade.append(4.0)
            elif sayı >= 90:
                grade.append(3.7)
            elif sayı >= 87:
                grade.append(3.3)
            elif sayı >= 83:
                grade.append(3.0)
            elif sayı >= 80:
                grade.append(2.7)
            elif sayı >= 77:
                grade.append(2.3)
            elif sayı >= 73:
                grade.append(2.0)
            elif sayı >= 70:
                grade.append(1.7)
            elif sayı >= 67:
                grade.append(1.3)
            elif sayı == 65:
                grade.append(1.0)
            elif sayı == 0:
                grade.append(0.0)
            else:
                break
            
        except ValueError:
            if notum == "A" or notum == "A+":
                grade.append(4.0)
            elif notum == "A-":
                grade.append(3.7)
            elif notum == "B+":
                grade.append(3.3)
            elif notum == "B":
                grade.append(3.0)
            elif notum == "B-":
                grade.append(2.7)
            elif notum == "C+":
                grade.append(2.3)
            elif notum == "C":
                grade.append(2.0)
            elif notum == "C-":
                grade.append(1.7)
            elif notum == "D+":
                grade.append(1.3)
            elif notum == "D":
                grade.append(1.0)
            elif notum == "F":
                grade.append(0.0)
            else:
                break
            
    
    print("Toplam not sayısı:", len(grade_7_core_subjects))
    print()
    print("Notlar: ", note)
    print()
    
    for i in range(len(note)):
        toplam1 += çarp[i]
        toplam2 += çarp[i] * grade[i]
        
    ort1 = toplam2 / toplam1
    print('Ortalama: ', ort1)
    
    
    
    
    
if clas == 8:
    grade_8_core_subjects = [
    "English Language Arts (ELA 8)",
    "8th Grade Mathematics / Algebra I",
    "Physical Science",
    "U.S. History & Civics",
    "Physical Education (PE 8) & Health",
    "Custom / Other"                 
]


    print()
    
    print("Please finish writing when you've completed your elective courses!!")
    
    print()
    
    while True:
        electives = input("Please enter your elective course: ")
        print()
        
        if electives == "finish":
            break
        
        grade_8_core_subjects.append(electives)
        
    print()
    
    for zmn in grade_8_core_subjects:
        time = int(input(f"{zmn} class time: "))
        çarp.append(time)
        
        print()
        
        
    
    for ders in grade_8_core_subjects:
        notum = input(f"{ders} Letter Grade: ")
        note.append(notum)
        
        try:
            sayı = float(notum)
        
            if sayı >= 97:
                grade.append(4.0)
            elif sayı >= 93:
                grade.append(4.0)
            elif sayı >= 90:
                grade.append(3.7)
            elif sayı >= 87:
                grade.append(3.3)
            elif sayı >= 83:
                grade.append(3.0)
            elif sayı >= 80:
                grade.append(2.7)
            elif sayı >= 77:
                grade.append(2.3)
            elif sayı >= 73:
                grade.append(2.0)
            elif sayı >= 70:
                grade.append(1.7)
            elif sayı >= 67:
                grade.append(1.3)
            elif sayı == 65:
                grade.append(1.0)
            elif sayı == 0:
                grade.append(0.0)
            else:
                break
            
        except ValueError:
            if notum == "A" or notum == "A+":
                grade.append(4.0)
            elif notum == "A-":
                grade.append(3.7)
            elif notum == "B+":
                grade.append(3.3)
            elif notum == "B":
                grade.append(3.0)
            elif notum == "B-":
                grade.append(2.7)
            elif notum == "C+":
                grade.append(2.3)
            elif notum == "C":
                grade.append(2.0)
            elif notum == "C-":
                grade.append(1.7)
            elif notum == "D+":
                grade.append(1.3)
            elif notum == "D":
                grade.append(1.0)
            elif notum == "F":
                grade.append(0.0)
            else:
                break
            
    
    print("Toplam not sayısı:", len(grade_8_core_subjects))
    print()
    print("Notlar: ", note)
    print()
    
    for i in range(len(note)):
        toplam1 += çarp[i]
        toplam2 += çarp[i] * grade[i]
        
    ort1 = toplam2 / toplam1
    print('Ortalama: ', ort1)
