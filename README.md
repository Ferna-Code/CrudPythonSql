# Sistema de Gestión de Clientes en Python y MySQL

Este es un proyecto simple de consola que permite gestionar clientes con operaciones CRUD (Crear, Leer, Actualizar, Eliminar), utilizando Python y una base de datos MySQL.

## 🧰 Tecnologías utilizadas

- Python 3
- MySQL
- MySQL Connector (pooling)
- Programación Orientada a Objetos

## 🧱 Estructura

- `cliente.py`: Define la clase `Cliente` (modelo/entidad).
- `cliente_dao.py`: Contiene las operaciones de base de datos (DAO).
- `conexion.py`: Administra la conexión con MySQL utilizando un pool.
- `zona_fit_app.py`: Gestiona el acceso a las diferentes opciones del programa

## 📦 Funcionalidades

- Insertar nuevos clientes
- Consultar todos los clientes
- Actualizar información de un cliente
- Eliminar un cliente por ID

## 🗃️ Requisitos

- Python 3.x
- MySQL instalado y corriendo
- Base de datos llamada `zona_fit_db` con la siguiente tabla:

```sql
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    membresia INT UNIQUE
);
