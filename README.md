EXPLICACIÓN PARA QUE EL PROFESOR PUEDA VER SU CÓDIGO

🔗 Enlace base del repositorio
👉 https://github.com/fabiansmsecu/ASISTEMAS_A2025

🔹 PASO 2 – ¿Dónde hacer el Fork?
Ingresa al enlace anterior.

En la parte superior derecha de la pantalla (cerca de tu foto de perfil), verás un botón que dice “Fork” (o "Bifurcar" si tienes GitHub en español).

Haz clic allí.

Se abrirá una ventana preguntando dónde quieres hacer el fork → selecciona tu cuenta.

GitHub creará una copia del repositorio en tu propia cuenta. El enlace cambiará a algo como:

arduino
Copiar
Editar
https://github.com/tuUsuario/ASISTEMAS_A2025
🔹 PASO 3 – ¿Dónde encontrar el botón "Code" para clonar?
Ve a tu fork, es decir, el repositorio que ahora está en tu cuenta.

Verás un botón verde que dice "Code" justo encima de los archivos.

Haz clic en "Code" → copia el enlace que aparece en la pestaña HTTPS (es algo como https://github.com/tuUsuario/ASISTEMAS_A2025.git).

Abre Git Bash o Terminal y usa ese enlace como en las instrucciones:

bash
Copiar
Editar
git clone https://github.com/tuUsuario/ASISTEMAS_A2025.git
cd ASISTEMAS_A2025
🔹 PASO 4 – Crear una rama
Una vez estés dentro de la carpeta clonada en tu PC, en la terminal:

bash
Copiar
Editar
git checkout -b actividad1-TuApellidoTuNombre
🔹 PASO 6 – ¿Dónde veo si el Push funcionó?
Después de hacer:

bash
Copiar
Editar
git push origin actividad1-TuApellidoTuNombre
Ve otra vez a tu repositorio en GitHub.

Verás una barra amarilla que dice algo como:

vbnet
Copiar
Editar
Compare & pull request
Haz clic allí.

🔹 PASO 7 – ¿Dónde se crea el Pull Request (PR)?
En esa pantalla de “Compare & pull request”, asegúrate de lo siguiente:

Base repository: fabiansmsecu/ASISTEMAS_A2025

Head repository: tuUsuario/ASISTEMAS_A2025

Escribe como título:
Actividad 1 – Apellido Nombre

Haz clic en el botón verde que dice “Create pull request”.

✅ ¡Con eso tu profesor verá tu entrega automáticamente en el siguiente enlace!
📌 https://github.com/fabiansmsecu/ASISTEMAS_A2025/pulls
