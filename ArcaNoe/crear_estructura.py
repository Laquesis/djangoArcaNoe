import os

def crear_estructura_app(app_name):
    # Ruta de la carpeta de la aplicación
    app_path = os.path.join(os.getcwd(), app_name)

    # Estructura de carpetas que queremos crear
    estructura = [
        os.path.join(app_path, 'models'),
        os.path.join(app_path, 'views'),
        os.path.join(app_path, 'templates', app_name),
        os.path.join(app_path, 'tests')
    ]

    # Crear las carpetas de la estructura
    for folder in estructura:
        os.makedirs(folder, exist_ok=True)
        init_file = os.path.join(folder, '__init__.py')
        open(init_file, 'a').close()  # Crea un archivo __init__.py vacío

    # Crear archivos adicionales como urls.py en la app
    urls_file = os.path.join(app_path, 'urls.py')
    with open(urls_file, 'w') as f:
        f.write("from django.urls import path\n\nurlpatterns = []\n")

    print(f"Estructura creada exitosamente en la app '{app_name}'.")

# Solicitar el nombre de la aplicación
if __name__ == "__main__":
    app_name = input("Introduce el nombre de la aplicación (e.g., 'app_ejemplo'): ")
    crear_estructura_app(app_name)
