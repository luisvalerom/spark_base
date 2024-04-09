# Proyecto base para lanzar una tarea de Spark

Esto es solo con intención de aprendizaje, no recomendado para producción.

Util para lanzar una tarea de *Spark* dentro de un cluster *Hadoop* utilizando *Yarn* como *resource manager*, para este proposito nos apoyamos en el [proyecto Hadoop Base](https://github.com/luisvalerom/hadoop-base)

Debemos crear dentro del directorio *app* nuestra aplicación Python *app.py* con la estructura que mejor nos convenga. Utilizar el archivo *requirements.txt* para gestionar la instalación de dependencias *Python*.

Si necesitamos pasar paramentros a la aplicación debemos editar el archivo *Dockerfile* y asignar valor a la variable de entorno *APP_ARGS*

## Punto de inicio

- Iniciar el cluster Hadoop, para esto seguir las instrucción descritas en el [proyecto Hadoop Base](https://github.com/luisvalerom/hadoop-base)
- Ejecutar el script *run.sh*

## Configuración

#### Para configurar las propiedades de *Spark* tenemos dos opciones:
- Editando el archivo *spark_defaults.conf* ubicado en *base/spark_conf*
- Asignado valor a la variable de entorno *SUBMIT_ARGS* dentro del archivo *Dockerfile*

#### Para configurar la propiedades del *Cluster Hadoop*:
- Utilizamos el archivo *config*
