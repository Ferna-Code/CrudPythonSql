from conexion import Conexion
from cliente import Cliente

class ClienteDao:
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def selecciones(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []# Almacena todos los objetos de tipo cliente
            # Mapeo de clase-table cliente
            for registro in registros:# Combertimos los registros a objetos y los almacenamos en una lista
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            print('Datos agregados con exito')
            return cursor.rowcount
        except Exception as e:
            print(f'Ha ocurrido un error al insertar los datos: {e}')
        finally:
            cursor.close()
            Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            if cursor.rowcount == 0:
                print('No se encontró ningún cliente con ese ID.')
            else:
                print('Datos actualizados con éxito')
            return cursor.rowcount
        except Exception as e:
            print(f'Ha ocurrido un error al actualizar los datos: {e}')
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
            
    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valor = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valor)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ha ocurrido un error al insertar los datos: {e}')
        finally:
            cursor.close()
            Conexion.liberar_conexion(conexion)

if __name__ == '__main__':

    #Ver tabla
    #  cliente1 = ClienteDao.selecciones()

    #  for cliente in cliente1:
    #      print(cliente)

    #Insertar datos
    #  datos = Cliente(nombre='Umberto', apellido='Cosio', membresia=646)
    #  insertar = ClienteDao.insertar(datos)

    # Actualizacion
    #   cliente_actualizar = Cliente(4, 'Alexa', 'Tellez', 400)
    #   clientes_actualizados = ClienteDao.actualizar(cliente_actualizar)
    #   print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar
    cliente = Cliente(id=5)
    cliente_eliminar = ClienteDao.eliminar(cliente)
    print(f'Se han eliminado: {cliente_eliminar}')

  