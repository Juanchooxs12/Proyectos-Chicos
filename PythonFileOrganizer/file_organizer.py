import os 
import shutil

#Definir la ruta de la carpeta a organizar
#raw string para evitar problemas con las barras invertidas en Windows

#Organizer_Path = r"Colocar aquí la ruta de la carpeta a organizar"

#Mapear las extensiones de archivos
FILES_TYPES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".html", ".css", ".js"],
    "Others": [],
}        
    
def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()
    for category, extensions in FILES_TYPES.items():
        if extension in extensions:
            return category
    return "Others"

def organize_files(root_path):

    print(f"Iniciando organización en: {root_path}\n")
    items_found = os.listdir(root_path)
    print(f"Elementos encontrados en el directorio: {items_found}")

    for filename in os.listdir(root_path):
        # 1. Rutas completas
        source_path = os.path.join(root_path, filename)
        # Ignora si es un directorio, el script que se está ejecutando, o la carpeta de prueba.
        if os.path.isfile(source_path):
            # 2. Obtener la categoría
            category_name = get_category(filename)            
            # 3. Construir la ruta de destino (la nueva carpeta)
            destination_dir = os.path.join(root_path, category_name)
            destination_path = os.path.join(destination_dir, filename)
            # 4. CREAR LA CARPETA SI NO EXISTE
            # os.makedirs asegura que la carpeta se crea si no existe. 
            # El argumento exist_ok=True evita errores si ya existe.
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir, exist_ok=True)
                print(f"-> Carpeta creada: {category_name}")           

            # 5. MOVER EL ARCHIVO
            try:
                # shutil.move mueve el archivo a la nueva ubicación
                shutil.move(source_path, destination_path)
                print(f"Movido: {filename} -> {category_name}")
            except Exception as e:
                # Esto maneja errores como "permiso denegado" o si el archivo ya existe
                print(f"Error al mover {filename}: {e}")
                
    print("\nOrganización completada. ¡Revisa tu carpeta de prueba!")


if __name__ == "__main__":
    #Organizer_Path = r"Colocar aquí la ruta de la carpeta a organizar"
    organize_files(Organizer_Path)
