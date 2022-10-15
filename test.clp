;create a generic program for clips language
defplate alumno "datos de un alumno"
    (slot nombre (type SYMBOL))
    (slot edad (type INTEGER) range (1 99))
    (slot estatura (type FLOAT) range (1.0 2.0))
    (slot sexo (type SYMBOL) range (masculino femenino))
    (slot promedio (type FLOAT) range (0.0 10.0))
    (slot carrera (type SYMBOL) default (ingenieria))

;hechos iniciales
(deffacts hechos_iniciales
(alumno (nombre "Juan") (edad 20) (estatura 1.70) (sexo masculino) (promedio 8.5) (carrera ingenieria))
(alumno (nombre "Maria") (edad 19) (estatura 1.60) (sexo femenino) (promedio 9.0) (carrera ingenieria))
(alumno (nombre "Pedro") (edad 21) (estatura 1.80) (sexo masculino) (promedio 7.5) (carrera ingenieria))
(alumno (nombre "Luis") (edad 20) (estatura 1.75) (sexo masculino) (promedio 8.0) (carrera ingenieria))
(alumno (nombre "Ana") (edad 19) (estatura 1.65) (sexo femenino) (promedio 9.5) (carrera ingenieria))
)

(defrule MENU
    (iniciar)
    =>
    (printout t "1.- INSERTAR" crlf)
    (printout t "2.- ELIMINAR" crlf)
    (printout t "3.- MODIFICAR" crlf)
    (printout t "4.- CONSULTAR" crlf)
    (printout t "5.- SALIR" crlf)
    (printout t "Ingrese una opcion: " crlf)
    (assert (respuesta (read)))
)

(defrule INSERTAR
    ?f <- (respuesta INSERTAR)
    =>
    (printout t "Ingrese el nombre del alumno: " crlf)
    (bind ?nombre (read))
    (printout t "Ingrese la edad del alumno: " crlf)
    (bind ?edad (read))
    (printout t "Ingrese la estatura del alumno: " crlf)
    (bind ?estatura (read))
    (printout t "Ingrese el sexo del alumno: " crlf)
    (bind ?sexo (read))
    (printout t "Ingrese el promedio del alumno: " crlf)
    (bind ?promedio (read))
    (printout t "Ingrese la carrera del alumno: " crlf)
    (bind ?carrera (read))
    (assert (alumno (nombre ?nombre) (edad ?edad) (estatura ?estatura) (sexo ?sexo) (promedio ?promedio) (carrera ?carrera)))
    (printout t "Alumno agregado" crlf)
    (retract ?f)
    (refresh MENU) 

)

(defrule ELIMINAR
    ?f <- (respuesta ELIMINAR)
    =>
    (printout t "Ingrese el nombre del alumno: " crlf)
    (bind ?nombre (read))
    (retract (alumno (nombre ?nombre) (edad ?edad) (estatura ?estatura) (sexo ?sexo) (promedio ?promedio) (carrera ?carrera)))
    (printout t "Alumno eliminado" crlf)
    (retract ?f)
    (refresh MENU) 
)

(defrule CONSULTAR
    ?f <- (respuesta CONSULTAR)
    =>
    (printout t "Ingrese el nombre del alumno: " crlf)
    (bind ?nombre (read))
    (printout t "Nombre: " ?nombre crlf)
    (printout t "Edad: " ?edad crlf)
    (printout t "Estatura: " ?estatura crlf)
    (printout t "Sexo: " ?sexo crlf)
    (printout t "Promedio: " ?promedio crlf)
    (printout t "Carrera: " ?carrera crlf)
    (retract ?f)
    (refresh MENU) 
)

(defrule MODIFICAR
    ?f <- (respuesta MODIFICAR)
    =>
    (printout t "Ingrese el nombre del alumno: " crlf)
    (bind ?nombre (read))
    (printout t "Ingrese la edad del alumno: " crlf)
    (bind ?edad (read))
    (printout t "Ingrese la estatura del alumno: " crlf)
    (bind ?estatura (read))
    (printout t "Ingrese el sexo del alumno: " crlf)
    (bind ?sexo (read))
    (printout t "Ingrese el promedio del alumno: " crlf)
    (bind ?promedio (read))
    (printout t "Ingrese la carrera del alumno: " crlf)
    (bind ?carrera (read))
    (retract (alumno (nombre ?nombre) (edad ?edad) (estatura ?estatura) (sexo ?sexo) (promedio ?promedio) (carrera ?carrera)))
    (assert (alumno (nombre ?nombre) (edad ?edad) (estatura ?estatura) (sexo ?sexo) (promedio ?promedio) (carrera ?carrera)))
    (printout t "Alumno modificado" crlf)
    (retract ?f)
    (refresh MENU) 
)

(defrule SALIR
    ?f <- (respuesta SALIR)
    =>
    (printout t "Saliendo..." crlf)
    (retract ?f)
    (halt)
)


