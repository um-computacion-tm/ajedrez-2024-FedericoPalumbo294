
# Como crear/comentar y subir en github
<!-- 
1_echo "# ajedrez-2024-fedepaljumbo294" >> README.md ---Crea un archivo README.md
2_git init ---Inicializa un nuevo repositorio Git en el directorio actual
3_git add README.md ---Aquí estás añadiendo README.md para que sea incluido en el próximo commit
4_git add . ---aca estas añadiendo todo en el proximo commit
5_git commit -m "cambios realizados" ---aca creas un commit mencionando los cambios que hiciste
6_git branch -M main ---Cambia el nombre de la rama actual a main
7_git remote add origin git@github.com:um-computacion-tm/ajedrez-2024-fedepaljumbo294.git ---establece la conexión entre tu repositorio local y el repositorio remoto en GitHub
8_git push -u origin main ---Sube los commits de tu repositorio local a la rama main en el repositorio remoto llamado origin.
-->

# Como crear un entorno virtual
<!-- 
python3 -m venv venv ---Creamos el entorno virtual
source venv/bin/activate ---Activamos el entorno virtual
-->

# Como cambiar de rama
<!--
git branch ---Veo en que rama estoy
git checkout develop ---Me cambio a la rama develop
git checkout main ---Me cambio a la rama main
-->

# Pasos a seguir para crear el juego
<!--
Primero: Clases de las piezas en archivo.py diferentes y despues la estructura del tablero en board.py.
Segundo: Una vez terminado seguire con la lógica del juego en chess.py.
Tercero: Terminado la lógica del juego ya puedes trabajar en la interfaz de usuario en main.py
Cuarto: Por ultimo necesito utilizar Docker para ejecutar mi juego: 
1.Crea un Dockerfile: Creo Dockerfile en la raíz de tu proyecto para configurar el entorno de Docker.
2.Construye la imagen: Ejecutar "docker build -t AJEDREZ ." en la terminal para construir la imagen de Docker basada en tu Dockerfile.
3.Ejecuta el contenedor: Ejecuar "docker run -it AJEDREZ" para ejecutar el juego dentro de un contenedor Docker.
-->

# Pasos para coverage
<!--
coverage run -m unittest && coverage xml && coverage report -m
pip install -r requirements.txt
-->