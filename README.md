# Proyecto-Sis-Info-III

### Descripción archivos:
- comments: archivo de prueba con 7 comentarios escogidos del dataset principal
- generate_classifier: notebook que clasifica genera el clasificador
- logistic_regression: clasificador generado con el mejor accuracy
- processing_text: archivo que contiene la función que hace la limpieza del texto
- server: el servidor que hace las predicciones
- final_job: el job de pentaho que llama a la transformación clasificador.ktr
- clasificador: transformación que carga el archivo, hace el request y genera otro archivo.

### Pasos:
1. Hacer correr el servidor "server.py" con el comando python server.py
2. Entrar a pentaho hacer correr el job "final_job.kj"
3. Ir al directorio y ver el archivo "result.xls" el cual contiene los resultados.
