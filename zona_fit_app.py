from cliente import Cliente
from cliente_dao import ClienteDao
print('*** Clientes de Zona Fit (GYM) ***')

opcion = None

while opcion != 5:
    print(f'''Menú
        1- Listar usuarios
        2- Agregar nuevo usuario
        3- Modificar usuario
        4- Eliminar usuario
        5- Salir''')
    
    opcion = int(input('Ingrese una opción(1-5): '))

    if opcion == 1:
        print(f'Lista de usuarios'.center(50,'-'))
        clientes = ClienteDao.selecciones()
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        print(f'Agregar nuevo usuario'.center(50,'-'))
        nombre_var = input('Ingrese el nombre de usuario: ')
        apellido_var = input('Ingrese el apellido del usuario: ')
        membresia_var = int(input('Ingrese el N° de membresia del usuario: '))
        cliente_nuevo = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        agregar_usuario = ClienteDao.insertar(cliente_nuevo)
        print(f'Clientes agregados: {agregar_usuario}')
    elif opcion == 3:
        print(f'Modificar usuario'.center(50,'-'))
        id_mod = int(input('Ingrese el ID del usuario a modificar: '))
        nombre_mod = input('Ingrese el nuevo nombre: ')
        apellido_mod = input('Ingrese el nuevo apellido: ')
        membresia_mod = int(input('Ingrese el nuevo N° de membresia: '))
        cliente_modificado = Cliente(id_mod, nombre_mod, apellido_mod, membresia_mod)
        actualizar_usuario = ClienteDao.actualizar(cliente_modificado)
        print(f'Se han actualizado {actualizar_usuario} usuarios')
    elif opcion == 4:
        print(f'Eliminar usuario'.center(50,'-'))
        id_eliminar = int(input('Ingrese el ID del usuario a eliminar: '))
        usuario_eliminar = Cliente(id=id_eliminar)
        usuario_eliminado = ClienteDao.eliminar(usuario_eliminar)
        print(f'Se han eliminado {usuario_eliminado} usuarios')
 
else:
    print('Salimos del programa')