# Importar el logo ASCII desde el módulo art
from art import logo
print(logo)

# Función para encontrar al ganador con la oferta más alta
def find_highest_bidder(bidding_record):
    # Inicializar la oferta más alta en 0 (cualquier oferta será mayor)
    highest_bid = 0
    # String vacío para guardar el nombre del ganador
    winner = ""
    
    # Iterar sobre cada nombre (clave) en el diccionario
    for bidder in bidding_record:
        # Obtener el valor (oferta) asociado a cada nombre
        bid_amount = bidding_record[bidder]
        
        # Comparar si esta oferta es mayor que la más alta registrada
        if bid_amount > highest_bid:
            # Actualizar la oferta más alta
            highest_bid = bid_amount
            # Actualizar el nombre del ganador
            winner = bidder
    
    # Imprimir el resultado final
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Crear un diccionario VACÍO para guardar todas las ofertas
# Estructura: {"nombre": oferta, "nombre2": oferta2, ...}
bids = {}

# Variable booleana para controlar el bucle principal
continue_bidding = True

# Bucle que se repite mientras continue_bidding sea True
while continue_bidding:
    # Pedir el nombre del participante
    name = input("What is your name?: ")
    
    # Pedir la oferta y convertirla a entero (int)
    # Sin int(), sería un string y no podríamos comparar numéricamente
    price = int(input("What is your bid?: $"))
    
    # AGREGAR la oferta al diccionario
    # Esto NO usa +=, simplemente asigna: diccionario[clave] = valor
    bids[name] = price
    
    # Preguntar si hay más participantes
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    
    # Si no hay más participantes
    if should_continue == "no":
        # Cambiar la variable a False para SALIR del bucle
        continue_bidding = False
        # Llamar a la función para encontrar y anunciar al ganador
        find_highest_bidder(bids)
    
    # Si hay más participantes
    elif should_continue == "yes":
        # "Limpiar" la pantalla imprimiendo 20 líneas vacías
        # Esto oculta la oferta anterior para mantener la subasta ciega
        print("\n" * 20)
