def menu_ingreso():
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

opcion = 0
nombres = 0
sexo = 0
seña = 0
datos = {}
m_f = {}
contra = {}
salir = False

while not salir:
    menu_ingreso()
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Por favor eliga una opcion valida")        
        
    if opcion == 1:
        while not salir:
            try:
                nombre = input("ingrese el nombre: ")
                if nombre == datos.get(nombres):
                    print("no se puede repetir nombre")
                else:
                    nombres += 1
                    datos[nombres] = nombre
                    salir = True
                    print(datos)
                    
            except ValueError:
                print("ingrese un dato valido")
                
        salir = False
        while not salir:
            try:
                genero = input("ingrese su sexo(M o F): ")
                if genero != "M" and genero != "F" and genero != "m" and genero != "f":
                    print("solo se puede elegir M o F")
                else:
                    sexo += 1
                    m_f[sexo] = genero
                    print(m_f)
                    salir = True
                    
            except ValueError:
                print("Eliga una opcion valida ")
        
        salir = False
        
        print("ingrese su contraseña")
        print("La contraseña debe de tener")
        print("1 letra")
        print("1 numero")
        print("sin espacios")
        while not salir:
            try:
                contraseña = str(input())

                if len(contraseña) < 8:
                    print("contraseña es corta")
                else:
                    seña += 1
                    contra[seña] = contraseña
                    print(contra)
                    salir = True
            except ValueError:
                print("dato ingresado incorrecto")
            
        salir = False
    elif opcion ==  2:
        busca = input("ingrese el nombre que desea buscar")
        
    elif opcion ==  3:
        eleminar = input("ingrese el usuario que quiere eliminar")
        
    elif opcion ==  4:
        salir = True
    else:
        print("Eliga una opcion valida ")
        