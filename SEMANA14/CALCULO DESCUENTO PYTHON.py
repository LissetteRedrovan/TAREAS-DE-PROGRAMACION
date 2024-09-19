# Cálculo de Descuento en Compras
def calcular_descuento(monto_total, porcentaje_descuento = 10):
  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# Llamada a la función
monto1 = 5000
monto2 = 3000
porcentaje_descuento = 25

# Primera llamada, se proporciona solo el monto total de la compra.
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Segunda llamada, se proporciona tanto el monto total de la compra como el porcentaje de descuento.
descuento2 = calcular_descuento(monto2, porcentaje_descuento)
monto_final2 = monto2 - descuento2

# Salida de resultados
print(f"Compra 1: Monto total = ${monto1}, Descuento = ${descuento1}, Monto final = ${monto_final1}")
print(f"Compra 2: Monto total = ${monto2}, Descuento = ${descuento2}, Monto final = ${monto_final2}")
