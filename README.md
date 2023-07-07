# Se debe ejecutar la siguiente línea para generar el entorno virtual de Python
```
py -m venv env
```

# Se debe ingresar al entorno virtual con el siguiente comando
```
cd env
```

```
cd Scripts
```

```
activate
```

# Luego se debe instalar los paquetes requeridos

```
pip install -r requirements.txt
```

# 


# Deploy en servidor: 

```
uvicorn main:app --host 0.0.0.0 --port 80
```

# 