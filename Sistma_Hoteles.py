#Sistema y gestion de hoteles bien basico

cliente = "Andres Manzilla"
dias_estancia = 6
tarifa_diria = 7500
habitacion_con_mar = False

costo_total = 0
print("**** Sistema de Hoteles ****")
print("Nombre del Cliente:", cliente)
print("Dias de estancia:", dias_estancia)
print("Tarifa diaria:",tarifa_diria)
print("Habitacion con vista al mar: ",habitacion_con_mar)

costo_total = tarifa_diria * dias_estancia

if habitacion_con_mar : costo_total *= 1.59

print("Costo total del servicio: ", costo_total)
print("----------------------------------------------------")


#Nuevos datos

#Sistema y gestion de hoteles bien basico

cliente = "Sofia Caceres"
dias_estancia = 45
tarifa_diria = 7500
habitacion_con_mar = True

costo_total = 0

print("**** Sistema de Hoteles ****")
print("Nombre del Cliente:", cliente)
print("Dias de estancia:", dias_estancia)
print("Tarifa diaria:",tarifa_diria)
print("Habitacion con vista al mar: ",habitacion_con_mar)

costo_total = tarifa_diria * dias_estancia

if habitacion_con_mar : costo_total *= 1.59

print("Costo total del servicio: ", costo_total)
print("----------------------------------------------------")
