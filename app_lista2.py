list_name = []
list_id = []
list_email = []
list_contact = []
list_years = []
list_exp = []
list_profession = []
list_city = []
list_sex = []

sw = True

import os

def fnt_limpiar():
    os.system("cls")
    print('Autor: Juan Esteban Aristizabal Suarez')
    print('Fecha: 18 de abril del 2024')
    
def fnt_registar(name, id, email, contact, years, exp, profession, city, sex):
    if id == '' or name == '' or contact == '' or email == '':
        print('Debe ingresar todos los datos')
        enter = ('<ENTER>')
    elif (years >= 25 and years <= 35) and (profession == 'Sistemas' or profession == 'sistemas' or profession == 'ing. sistemas' or profession == 'Ing. Sistemas' or profession == ' Ing. sistemas')and (profession == 'Informatico' or profession == 'informatico' or profession == 'ing. informatico' or profession == 'Ing. Informatico' or profession == ' Ing. informatico') and (exp >= 2 and exp <= 4):
        list_name.append(name)
        list_id.append(id)
        list_email.append(email)
        list_contact.append(contact)
        list_years.append(years)
        list_exp.append(exp)
        list_profession.append(profession)
        list_city.append(city)
        list_sex.append(sex)
        
        enter = input('Registro exitoso\n\n<ENTER>')
    else:
        print('No cumples con lo requerido.')
        enter = input('<ENTER>')

def fnt_selector(op):
    if op == '1':
        fnt_limpiar()
        name = input('\nIngrese el nombre: ')
        id = input('Ingrese el id: ')
        if id in list_id:
            enter = input('\nEl id ya se encuentra registrado\n\n<ENTER>')
        else: 
            email = input('Ingrese el email: ')
            contact = input('Ingrese el contacto: ')
            years = int(input('Ingrese la edad: '))
            exp = int(input('Ingrese los años de experiencia: '))
            profession = input('Ingrese la profesión(Ing. Sistemas/Ing. Informatico): ')
            city = input('Ingrese la ciudad: ')
            sex = input('Ingrese el sexo(M/F): ')
            fnt_registar(name, id, email, contact, years, exp, profession, city, sex)
    elif op == '2':
        fnt_limpiar()
        for i in range(len(list_id)):
            print(f'\n{list_name[i]} {list_id[i]} {list_email[i]} {list_contact[i]} {list_years[i]} {list_exp[i]} {list_profession[i]} {list_city[i]} {list_sex[i]}')
        
        enter = input('\n<ENTER>')
    elif op == '3':
        sw = False
    else:
        print('Opción no válida')
        enter = input('\n<ENTER>')


while sw == True:
    fnt_limpiar()
    op = input('\n\n<<< MENÜ DE OPCIONES >>>\n\n1. Registar\n2. Consultar\n3. SALIR\n\n-> ')
    fnt_selector(op)