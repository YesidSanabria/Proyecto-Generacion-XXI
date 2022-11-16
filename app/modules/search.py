import modules.crud as crud

def searchInData(user, text):
    if str(text.upper()) in str(user['Nombres'].upper()):
        return True
    if str(text.upper()) in str(user['Apellidos'].upper()):
        return True
    return False

def searchStudent(text):
    allStudents = crud.getAllStudents()
    studentList = []
    for student in allStudents.keys():
        data = allStudents[student]
        if searchInData(data, text):
            studentList.append(student)
    return studentList
