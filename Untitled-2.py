# Nombre del estudiante: [NOMBRE COMPLETO]
# Grupo: [NÚMERO DE GRUPO]
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia
 
# Constantes
IVA = 0.19
RECARGO_LUJO = 0.05
 
print("=== CÁLCULO DEL VALOR FINAL DEL PRODUCTO ===")
 
# R2: captura y validación del precio base
precio_base = float(input("Ingrese el precio base del producto: "))
 
if precio_base <= 0:
    print("Error: el precio base debe ser mayor a cero.")
else:
    # R3: captura y validación de la categoría
    print("\nCategorías disponibles:")
    print("1. Producto básico (sin IVA)")
    print("2. Producto estándar (IVA 19%)")
    print("3. Producto de lujo (IVA 19% + recargo 5%)")
    codigo = int(input("Ingrese el código de categoría: "))
 
    # R4: cálculo del valor final según la categoría
    if codigo == 1:
        categoria = "Básico"
        valor_final = precio_base
    elif codigo == 2:
        categoria = "Estándar"
        valor_final = precio_base + precio_base * IVA
    elif codigo == 3:
        categoria = "Lujo"
        valor_final = precio_base + precio_base * IVA + precio_base * RECARGO_LUJO
    else:
        categoria = None
 
    # R5: salida del resultado
    if categoria is None:
        print("Error: código de categoría inválido.")
    else:
        print(f"\nCategoría: {categoria}")
        print(f"Precio base: ${precio_base:,.2f}")
        print(f"Valor final a pagar: ${valor_final:,.2f}")
        
