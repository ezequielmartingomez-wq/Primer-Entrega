"""
Sistema de Registro y Login de Usuarios
Curso de Python - Trabajo Práctico

"""

# ========== DICCIONARIO GLOBAL (BASE DE DATOS) ==========
usuarios = {}  # Diccionario: clave=nombre_usuario, valor=contraseña


# ========== FUNCIÓN DE REGISTRO ==========
def registrar_usuario():

    print("        REGISTRO DE USUARIO")
    
    # INPUT: Solicitar nombre de usuario
    nombre_usuario = input("Ingrese nombre de usuario: ")
    
    # IF: Validar que el usuario no exista
    if nombre_usuario in usuarios:
        print("❌ Error: El usuario ya existe.")
        return False
    
    # IF: Validar que no esté vacío
    if nombre_usuario == "":
        print("❌ Error: El nombre de usuario no puede estar vacío.")
        return False
    
    # INPUT: Solicitar contraseña
    contrasena = input("Ingrese contraseña: ")
    
    # IF: Validar que la contraseña no esté vacía
    if contrasena == "":
        print("❌ Error: La contraseña no puede estar vacía.")
        return False
    
    # IF: Validar longitud mínima de contraseña
    if len(contrasena) < 4:
        print("❌ Error: La contraseña debe tener al menos 4 caracteres.")
        return False
    
    # Llamar a la función de almacenamiento
    almacenar_usuario(nombre_usuario, contrasena)
    
    print(f"✅ Usuario '{nombre_usuario}' registrado exitosamente!")
    return True


# ========== FUNCIÓN DE ALMACENAMIENTO ==========
def almacenar_usuario(nombre_usuario, contrasena):

    # DICCIONARIO: Guardar datos (clave: nombre_usuario, valor: contraseña)
    usuarios[nombre_usuario] = contrasena


# ========== FUNCIÓN DE LOGIN ==========
def login_usuario():

    print("           INICIAR SESIÓN")
    
    # INPUT: Solicitar credenciales
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contrasena = input("Ingrese contraseña: ")
    
    # IF: Verificar si el usuario existe
    if nombre_usuario in usuarios:
        # IF: Verificar si la contraseña es correcta
        if usuarios[nombre_usuario] == contrasena:
            print(f"✅ ¡Bienvenido, {nombre_usuario}!")
            return True
        else:
            print("❌ Contraseña incorrecta.")
            return False
    else:
        print("❌ Usuario no encontrado.")
        return False


# ========== FUNCIÓN DE MOSTRAR USUARIOS ==========
def mostrar_usuarios():

    print("      USUARIOS REGISTRADOS")
    
    # IF: Verificar si hay usuarios registrados
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return
    
    # Variable contador
    contador = 1
    
    # FOR: Recorrer el diccionario de usuarios
    for nombre_usuario, contrasena in usuarios.items():
        # PRINT: Mostrar información
        print(f"{contador}. Usuario: {nombre_usuario}")
        print(f"   Contraseña: {'*' * len(contrasena)} (oculta)")
        contador += 1
    
    # PRINT: Mostrar total
    print(f"\nTotal de usuarios: {len(usuarios)}")


# ========== FUNCIÓN DEL MENÚ ==========
def mostrar_menu():

    print("      MENÚ PRINCIPAL")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar todos los usuarios")
    print("4. Salir")


# ========== FUNCIÓN PRINCIPAL ==========
def main():

    # PRINT: Mensaje de bienvenida
    print("  SISTEMA DE REGISTRO DE USUARIOS")
    print("  ¡Bienvenido al sistema!")
    
    # Variable para controlar el bucle
    ejecutando = True
    
    # WHILE: Bucle principal del programa
    while ejecutando:
        # Mostrar menú
        mostrar_menu()
        
        # INPUT: Solicitar opción
        opcion = input("\nSeleccione una opción (1-4): ")
        
        # IF-ELIF: Validar y ejecutar la opción seleccionada
        if opcion == "1":
            registrar_usuario()
            
        elif opcion == "2":
            login_usuario()
            
        elif opcion == "3":
            mostrar_usuarios()

        elif opcion == "4":
            # Cambiar variable para salir del WHILE
            ejecutando = False
            print("\n¡Gracias por usar el sistema!")
            print("¡Hasta pronto!\n")
            
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
        
        # IF: Pausa solo si el programa sigue ejecutándose
        if ejecutando:
            input("\nPresione Enter para continuar...")


# ========== PUNTO DE ENTRADA ==========
if __name__ == "__main__":
    main()
