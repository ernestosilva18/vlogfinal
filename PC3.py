# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu


# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
with st.sidebar:
    opciones = option_menu(None,['Inicio', 'Experiencia', 'Gráficos'] , 
        icons=['spotify','brilliance', 'battery-full'], menu_icon="non", default_index=0)
    # Crea un menú de opciones dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de opciones disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

st.markdown(
    """
    <style>
    /* Cambiar el fondo de la aplicación */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://wallpapers.com/images/hd/christmas-teams-background-qj2j0kqebj8bpb0q.jpg");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Agregar transparencia al contenido principal para que se lea bien */
    .main {
        background-color: rgba(0, 0, 0, 0.8);
    }
    
    """,
    unsafe_allow_html=True  # Permitir que Streamlit interprete el código HTML/CSS
)
# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'

    # Título que aparece antes de las opciones del menú -> menu_title="Selecciona una sección: "
    # Lista de opciones que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "opciones"
if opciones == 'Inicio':
    st.markdown("<h1 style='text-align: center; font-size: 100px; color: #FF1515'>ENTRE PAZ Y DESGRACIA</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("fotoperfil.jpeg", caption='Ernesto o Martín xd', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    Mi nombre es Ernesto (o Martín) Silva, estudiante de la carrera de publicidad en la PUCP. 
    Lo que más me gusta de la carrera es la libertad que tengo para navegar y explotar mi 
    creatividad en función de crear algo que sea útil para una marca o persona. 
    Adoro escuchar música, realmente siento que no podría vivir sin la música. 
    Da igual si estoy dentro o fuera de la universidad, no puedo estar sin mis audífonos 
    escuchando música. Además, me gusta jugar videojuegos de vez en cuando. 
    Antes solía ser mucho más frecuente, pero con el tiempo fui perdiendo más y más 
    interés en ello, y ahora sólo son un pequeño pasatiempo.  
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif opciones == 'Experiencia':
    st.markdown("<h1 style='text-align: center; font-size: 80px; color: #FF1515'>Ey, ¿te llama la atención programar?</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Mi experiencia aprendiendo Python realmente se remonta a épocas de pandemia. Por allá del 2020-21, con comandos simples empleando las funciones: print, if, elif, else, comencé a familiarizarme con el lenguaje de programación. Sin embargo, luego de ello, no volví a adentrarme en algún otro lenguaje en general. Al menos eso creía, hasta que finalmente, en este 2026 volví a interactuar con el lenguaje de Python, donde aprendería muchísimo más de los conocimientos que ya tenía previamente.
    Al inicio realmente pensaba que el lenguaje era bastante simple. No obstante, conforme avanzaba en las clases me daba cuenta que también demanda mucha paciencia y mucho más conocimiento acerca de él conforme vas descubriendo nuevas funciones y/o comandos. Por ello, considero que fue muy enriquecedor ir progresando durante las semanas, pues, así pude no solo aprender a programar una página web, sino que, en general, obtuve muchísimo conocimiento para crear otro tipo de cosas. Por ejemplo, gráficos, listas, juegos, etc. Siento que esta experiencia realmente me servirá a futuro, principalmente para saber ordenar y facilitarme el manejo de datos.
    Además, quisiera dejar adjuntos algunos videos respecto a mi trayectoria dentro del curso: mis 2 PC's y la idea de mi proyecto final, al cual podrán acceder muy pronto :))).
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("💻 Diferencias entre Strings y Listas - Google Drive")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1cw9omQmLY7FFYNi6rlcmzCjqxUiL0wv_/view?usp=drive_link"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presentan las diferencias entre los Strings y las Listas, donde, en términos sencillos, un String es como una palabra escrita con lapicero. Es decir, no puedes cambiar algo sin tener que dañar o hacer algo que interfiera con el papel. Por otro lado, las Listas son como un archivador de carpetas: puedes poner una nueva, cambiar orden, etc. Sin detallar más, dentro de este video conocerán más dieferencias entre ambas."
    
    )

    st.subheader("💡Diferencias entre los bucles For y While - Google Drive")

    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1nd7dc-lQB_Imw_7h2kHjw_GC0kViXqYI/view?usp=drive_link"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presentan las diferencias entre los bucles for y while. Por un lado, en términos sencillos, un buble se encarga de repetir una acción para que nosotros no tengamos que escribir el mismo código una y otra vez. Por otro lado, respecto al for y el while, ambos repiten cosas, pero se usan de formas diferentes. Si te interesa conocer más acerca de estas diferencias, te invito a mirar el video completo. "
    
    )

    st.subheader("🎸 Proyecto Final / Concepto de Página Web - Google Drive")

    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1pyzD2s0PBpEGRAACeUSFanRkdN6OEhB9/view?usp=drive_link"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta lo que será mi proyecto final (o que quizás ya salió al público), el cual consiste en una página web interactiva dedicada a la banda Twenty One Pilots, analizando su discografía, desglosando sus canciones, conociendo el lore construido por la banda a lo largo de los años y demás cosas que, cuando estén listas, los invito cordialmente a visitarla, ya sean fans de la banda o no."
    
    )

elif opciones == 'Gráficos':
    st.markdown("<h1 style='text-align: center; font-size: 80px; color: #FF1515'>ALGUNOS GRÁFICOS HECHOS EN CLASE</h1>", unsafe_allow_html=True)

    graficos = ['Gráfico_1', 'Gráfico_2', 'Gráfico_3','Gráfico_4', 'Mapa_1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("🏃‍♂️💨 Promedio de goles anotados anotados como local por equipo")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Este gráfico analiza principalmente el promedio de goles anotados como local por equipo respecto a las jornadas de la Liga de Francia. Como puede verse en el Gráfico, equipos como el Angers, Auxerre, Nantes, entre otros, tienen un promedio cercano a un gol por partido jugando como locales. Por otro lado, hay equipos como el Marseille y el PSG, quienes tienen casi un promedio de 2.5 goles por partido jugando como local.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "gráfico5.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_2':
        # Título de la sección
        st.subheader("🟥 Promedio de Tarjetas Rojas recibidas por Equipo Local")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Este gráfico analiza principalmente el promedio de tarjetas rojas recibidas por equipo jugando como local respecto a las jornadas de LaLiga Española. Como puede verse en el Gráfico de barras. este está ordenado de mayor promedio de tarjetas rojas por equipo a menor. En este caso, el Girona se posiciona como el equipo con mayor promedio de tarjetas rojdas, seguido por el Real Madrid y el Oviedo; mientras que, por otro lado, equipos como el Celta, el Elche, Villareal, etc., se posicionan con números más bajos; además de los equipos cuyo promedio de tarjetas rojas como local es nulo, como el Barcelona y el Valencia.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "gráfico6.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_3':
        # Título de la sección
        st.subheader("💙❤️ Rendimiento del FCBarcelona jugando como visitante")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Este gráfico analiza principalmente el rendimiento del FCBarcelona durante LaLiga española cuando éste juega de visitante. Para ello, el gráfico de pastel está repartido principalmente en: los partidos ganados, los perdidos y los empatados. De esta manera, es posible notar que, en términos generales, al Barcelona le va relativamente bien, dentro de lo que cabe, habiendo ganado la mayoría de sus partidos, habiendo perdido menos de la mitad y habiendo empatado algunos pocos.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "gráfico7.png",
                width=800
            )
    elif grafico_seleccionado == 'Gráfico_4':
        # Título de la sección
        st.subheader("☁️ Nube de palabras")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Esta nube de palabras fue creada a partir de un diccionario vacío inicial, utilizado para almacenar la cantidad de veces que aparece cada palabra de una lista depurada. Por ello, al imprimirlo, este nos muestra la nube de palabras, habiendo utilizado los datos del diccionario obtenido anteriormente. Además, es posible apreciar los ejes de la nube, y es posible apreciar que la palabra no es la que más se repite.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "gráfico8.png",
                width=800
            )

    elif grafico_seleccionado == 'Mapa_1':
        # Título de la sección
        st.subheader("🗺️ Mapa de los lugares donde se grabaron mis series y película favoritas")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            En este mapa es posible apreciar exactamente las ubicaciones en las que fueron grabadas las series y película que más han sido de mi agrado durante mi vida, las cuales son: Riverdale, Stranger Things, Spiderman No Way Home, Euphoria y Bessos, Kitty. Como es posible apreciar, cada marcador está situado en el lugar original donde se rodó cada material audiovisual.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa_interactivo.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
