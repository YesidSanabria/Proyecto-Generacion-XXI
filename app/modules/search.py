import modules.crud as crud

def limpiar_acentos(text):
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'ü': 'u', 'Ü': 'U'}
	for acen in acentos:
		if acen in text:
			text = text.replace(acen, acentos[acen])
	return text

def searchInData(user, text):
    text = limpiar_acentos(text)
    names = limpiar_acentos(user['Nombres'])
    lastnames = limpiar_acentos(user['Apellidos'])
    career = limpiar_acentos(user['Carrera'])
    if text.upper() in names.upper():
        return True
    if text.upper() in lastnames.upper():
        return True
    if text.upper() in career.upper():
        return True    
    return False

def searchInDataC(user, text):
    text = limpiar_acentos(text)
    career = limpiar_acentos(user['Carrera'])
    if text.upper() in career.upper():
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

def searchCareer(text):
    allStudents = crud.getAllStudents()
    studentList = []
    for student in allStudents.keys():
        data = allStudents[student]
        if searchInDataC(data, text):
            studentList.append(student)
    return studentList   
