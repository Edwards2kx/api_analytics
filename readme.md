// dentro del folder contenedor del proyecto ejecutar  source ./env/bin/activate 
// para listar las librerias instaladas usar pip list
// para actualizar pip usar pip install --upgrade pip
// para instalar 

web de ayuda de ambientes virtuales de python
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

1. Crea un entorno virtual: `python3 -m venv .venv`
2. Activa el entorno virtual: `source .venv/bin/activate` (o `. venv/bin/activate` en Windows)
3. Instala las dependencias: `pip install -r requirements.txt`

4. desactivar el entorno virtual `deactivate`
5. instalar fastapi pip install fastapi
6. instalar uvicorn como servidor pip install "uvicorn[standard]"
instalar fastapi y uvicorn al juntos pip install "fastapi[all]"

instalar openpyxl para generar archivo xls "pip install openpyxl"


para correr el proyecto con uvicorn usar `uvicorn main:app --reload`
eso activa en localhost el proyecto

instalar SQLAlchemy usar comando `pip install sqlalchemy`
instalar psycopg2 usar comando `pip install psycopg2`

para usar con ngRok usar `ngrok http 8000`

conexion con supabase postgresql database

1. crear proyecto en supabase

nombre proyecto : comodo_api
password de la base de datos :  ~s*56K(!Pb-X5Nt

2. revisar la info de la conexion

host: aws-0-us-west-1.pooler.supabase.com
database name: postgres
port: 6543
user: postgres.wnsnlwsxdwoeetabejez
password: ~s*56K(!Pb-X5Nt




averiguar que es opt in y opt out en analitica




