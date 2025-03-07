DESCRIPCIÓN:

Es un programa que realiza una simulación de movimiento de un número n de partículas en un plano bajo atracción gravitacional mutua en un sistema aislado. La velocidad y posición se hallaron mediante el método de integración 'leapfrog', el cual consiste en hallar la velocidad en la mitad de un intervalo y hallar la posición al final del intervalo con la velocidad en la mitad de dicho intervalo (similar a la integración por regla del punto medio). El tamaño del intervalo, llamado dt, es inicializado a un valor observado apto, pero el usuario puede cambiarlo a su antojo. Para mitigar errores con la integración numérica, observados con aumentos abruptos de velocidad al acercarse  substancialmente dos partículas, el programa contiene un algoritmo de corrección de la longitud del intervalo que el usuario podrá activar a su antojo y deberá desactivar manualmente por conveniencia; el algoritmo consiste en evitar que la diferencia en dos velocidades consecutivas para cualquier partícula en la animación sea mayor a un valor épsilon que también es inicializado a un valor observado apto pero que el usuario tendrá la opción de cambiar a lo largo de la animación. Finalmente, también se podrá descargar un archivo de tipo .xlsx en el tiempo actual de la animación el cual contiene las masas, posiciones, velocidades y colores de la partícula en el instante actual y las posiciones y velocidades en cada tiempo hasta el actual. El usuario podrá ingresar las masas con los parámetros que desee y también podrá ingresar un número que especifique de partículas aleatorias con una masa de 1 a 20, posición entre (-10,-10) y (10,10), velocidad entre el mismo rango y color aleatorio. Una vez habiendo ingresado todas las masas, el usuario deberá comenzar la animación con un botón de la interfaz; habiendo comenzado, podrá pausar y continuar la animación a su gusto, al igual que agregar masas; finalmente, podrá cerrar la ventana con el botón de cerrar (o, en su defecto, con la X en la parte superior derecha).

Todos los parámetros y variables están en unidades de Masa solares para masa, Unidades Astronómicas para distancia y años para tiempo.



ESTRUCTURA:

El programa está divido en dos archivos, uno llamado 'Body_file' en el cual se define la clase 'Body', que representa una partícula en la simulación; esta clase maneja las propiedades físicas de las partículas, incluyendo su masa, posición, velocidad y color, y proporciona métodos para actualizar estas propiedades durante la simulación, dichos métodos están explicados en el docstring de la respectiva clase. El segundo archivo, siendo el 'main.py', es el archivo que debe ser ejecutado, es donde se encuentra el resto del programa; este archivo contiene otras dos clases las cuales no pudieron ser separadas a otros archivos puesto que dentro de dichas clases se cambian variables a lo largo de la ejecución del programa (como el delta t, deshabilitando al usuario de cambiar dicha variable), lo cual no se puede lograr al separarlas ejecutando únicamente el 'main.py'.

El archivo principal (main.py) comienza importando los módulos necesarios y definiendo dos clases: SimulationParameters y ParticleManager. En la primera están definidos los parámetros de la simulación: el deltat, el deltat (dt) ingresado por el usuario, el epsilon del algoritmo de corrección, el intervalo de animación (parámetro de FuncAnimation), y el estado del algoritmo de corrección(activado o desactivo); en la segunda están definidas las funciones que manejan a las partículas durante la simulación, mencionadas y explicadas en el docstring de la clase. Habiéndose creado un objeto de cada una de estas clases, se definen las funciones que crean un color aleatorio y un nombre aleatorio; luego las que cambiarán el dt y el epsilon a petición del usuario, verificando que su entrada fue correcta; luego la encargada de crear una partícula con parámetros especificados por el usuario; luego la encargada de crear un número especificado por el usuario de partículas aleatorias; siguiéndole la función encargada de animar, ejecutándose en cada iteración de la animación; siguiendo con las funciones de comenzar, pausar y continuar la animación, de cerrar la ventana, de activar o desactivar el algoritmo de corrección, para terminar con la función que permite al usuario escoger el color. La ventana se crea a partir de Tkinter y la gráfica a partir de matplotlib. Se crean dos cuadros en la ventana: uno donde se guardan los botones y otro donde se encuentra la gráfica. 



INSTRUCCIONES DE USO:

Instalación:

1. Clona el repositorio:
   bash
   git clone <URL_DEL_REPOSITORIO>
    

2. Navega al directorio del proyecto:
   bash
   cd <NOMBRE_DEL_PROYECTO>
    

3. Crea un entorno virtual (opcional pero recomendado):
   bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    

4. Instala las dependencias:
   bash
   pip install -r requirements.txt
    

Dependencias:

Las siguientes bibliotecas de Python son necesarias para ejecutar el proyecto:

- matplotlib
- openpyxl
- tkinter (incluido en la mayoría de las instalaciones de Python)

Uso:

1. Ejecuta el script principal:
   bash
   python main.py
     

2. Interactúa con la interfaz para agregar partículas, generar partículas aleatorias, y controlar la animación.

