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


UPDATE 13 04 2022
1) Se aplican correcciones/sugerencias del tutor:
    - Mejorar visualización de búsqueda
    - Listado completo de cines y peliculas
    - Contraseña protegida
2) Se agregan las siguientes mejoras:
    - Homogeneidad en nombre de views, urls y patters para mejorar el flow
    - Homogeneidad en idioma, salvo los Forms (para que se vea en español (queda pendiente mejorar esto)
    - Ordenamiento por alfabeto de listados y búsquedas.
    - Se quitanon todos los HttpResponse y se cambian por renders con sus hrefs para no perder el track dentro del site.
3) El modelo User, será eliminado en los próximos commits, dado que al momento de crearlo (y entregarlo) no habíamos visto la gestion de usuarios que tiene Django. De todas formas, se deja en este commit para mostrar la mejora en la contraseña.
4) Hay views y urls comentarizadas, forman parte de nuevas features que no estaban en el commit original y están siendo desarrolladas. Los templates correspondientes a estos, se pueden identificar por no tener el formato std.
5) Para testear el site, se debe ingresar a la 127.0.0.1:8000/cineproyecto/ como en le commit original. La navegación es intuitiva.

