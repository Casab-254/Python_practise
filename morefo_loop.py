student_name_1= 'parker'
student_name_2 = 'itika'


records= {'itika': 90, 'aisha':70, 'brad':100}

def marks(student_name):
    for a_student in records:
        if a_student == records:
            return records[a_student]
        break
    else:
        return f'There is no student of name{student_name} in the records'
    
    print(f"Markd of{student_name_1} are:", marks(student_name_1))
    print(f"Marks of{student_name_2}are:", marks(student_name_2))