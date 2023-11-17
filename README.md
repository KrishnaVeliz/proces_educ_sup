## Paso1: Redirigete a la carpeta del proyecto 

## Paso2: Cree el ambiente virtual 
python -m venv myenv 

## Paso3: Activar el entorno virtual 
myenv\Scripts\activate

## Paso4: Instalar las librerias del archivo 
requeriments.txt

## Paso5: Luego descargar el CSV más reciente de la siguiente url:
https://datosabiertos.mineduc.cl/titulados-en-educacion-superior/

## Paso6: Ejecutar la aplicacion 
python get_excel_resumen_es.py 