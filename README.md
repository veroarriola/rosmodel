# rosmodel
Uso de modelos de Django desde ROS2

Para utilizar una base de datos como almacenamiento y administrarla mediante las facilidades de `django` es posible mezclar proyectos de `django` y `ros2`.

Primero se creó el paquete de ros2:
```
ros2 pkg create --build-type ament_python --node-name dbstate rosmodel
```
Para poder crear el paquete de django, es necesario cambiarle el nombre al directorio raíz `rosmodel` temporalmente.  Desde `src` se invoca el comando de django:
```
django-admin startproject rosmodel
```
Ahora se copian los archivos que generó ros2 dentro del directorio `rosmodel` recién creado por django.

Se puede utilizar el script `manage.py` para administrar este proyecto, como siempre:
```
python manage.py startapp state
```
La estructura de directorios y archivos obtenida es la que se comparte en este repositorio.  Se puede ver cómo los archivos del proyecto de django y del paquete de ros2 están entremezclados, afortunadamente los nombres no colisionan, por lo que no hay conflicto entre ellos.

Para instalar el proyecto correctamente, fue necesario agregar la aplicación `state` a la opción `packages` en `setup.py` y el archivo de sqlite a los `data_files` (este paso no es necesario si se usa otra base de datos).  El archivo `dbstate.py` dentro de `rosmodel` muestra cómo utilizar un modelo, previamente migrado, de la aplicación de django.  El proyecto se compila/instala con:
```
colcon build --packages-select rosmodel
```

**NOTA:** Cuidado, la base de datos que se usa al ejecutar el nodo desde el espacio de trabajo con:
```
ros2 run rosmodel dbstate
```
es la copia que se installa en el directorio `share`, cuidado al modificar y reinstalar, porque se pueden perder datos.
