# ProyectoCoderGrupo1
A Django of cinema proyect.

Para el proyecto, se genero una app llamada cineproyecto.
La misma tiene el path derivado desde el principal /cineproyecto/
Tiene una index principal de html (index.html) con herencia de (padre.html)

Se crearon dos modelos principales para la BD:

Cines (Cinemas)
Peliculas (Movies)
- Penddiente: Actores (Actors)

Se agrego un modelo para usuarios
Usuarios (Users)

Todos los modelos creados tiene un API en .forms
Estos están renderizados en html, con un path especifico.
Desde el nav bar se puede ingresar a cargar por formulario, los diferentes datos.

Se agrego la opción de búsqueda por nombre de películas (tambien con link en nav bar)

-- Proximos pasos:

Esta es la base para proximas mejoras.
Pasar los datos de formulario a español
Mejorar CSS, y tratar de incluir una plantilla
Generar las relaciones entre tablas
Lanzar la funcionalidad de admin
Generar formulario de publicacion de post noticias en inicio
Permitir que usuarios comenten en esas publicaciones

