# asistencias
sistema automatico de registro de asistencias

Idea.
Este proyecto busca solucionar problemas en cuantoal registro de asistencias en medianas y grandes instituciones que hagan 
uso intensivo de computadoras como es el caso del propio IPF.

Observacion del problema.

Vemos que en una institución que cuenta con muchos alumnos la tarea de tomar asistencias de manera manual se vuelve tediosa 
incluso hasta un poco insalubre ya que generalmente se hace uso del "voceo" que es utilizar un tono de voz elevado nombrando uno 
por uno los nombres de cada estudiante y esperando que estos respondan tambien con cierta elevacion del tono de voz. A una persona 
con problemas en las cuerdas vocales esto le podria resultar muy perjudicial y doloroso, y ademas podria darse el caso que por alguna 
razón el alumno no escuchara o no estuviera presente en el momento del relevamiento lo cual resultaria en una falta injusta.
Por tal manera hemos ideado un sistema que automatice el registro de asistencias aprovechando que en particular en nuestra carrera se 
hace uso intensivo del computador y por lo tanto la totalidad del aula posee un hardware o bien el instituto le provee uno.

Aprovechando que en nuestra carrera y en muchas otras, y que ademas el estado proveyó netbooks a los estudiantes de niveles polimodales 
lo que garantiza el acceso a un hardware para todos los estudiantes es que hemos ideado solucionar el problema mediante una API de tipo 
REST montada en una red WLAN (wireless local area network). Un cliente que haga uso del servicio bajará una pequeña aplicación la cual 
extraerá del sistema operativo datos únicos del hardware o del SO como por ejemplo podrian ser el número de MAC, el Id de producto o los 
números de serie. El cliente enviará estos datos a un servidor que guardará estos en una base de datos mediante un protocolo similar a 
REST API para mas tarde cuando al conectarse a la red wifi de la institución se envie nuevamente estos datos únicos por cada alumno. El 
sistema registrará la asistencia automáticamente para ese alumno. Este mismo servicio tambien le proveerá al usuario la posibilidad de 
observar mediante el navegador web o la aplicación de escritorio si realmente el sistema lo ha registrado exitosamente mediante una 
lista de los presentes, ademas de poder ver datos históricos de sus asistencias y faltas.
Ademas el sistema le notificará automáticamente si el registro de asistencia se logró con éxito, o si por ejemplo ya tiene demasiadas 
faltas le advertirá que esta llegando al limite de las faltas, incluso podria notificarle otros datos como notas de trabajos, examenes, 
mensajes personalizados del preceptor o profesor, etc.
Lo ideal es que el proceso esté lo mas automatizado posible, al detectar el sistema que se ha conectado a la red wifi de la institucion registrará todo y recibirá las notificaciones que sean pertinentes con la menor intervencion del usuario o profesores o preceptores posible.
