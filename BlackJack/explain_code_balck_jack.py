############################################
# BLACKJACK EN ESPAÑOL
# Proyecto completo con explicaciones
############################################

import random

# El mazo de cartas (ilimitado)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dar_carta():
    """Saca una carta aleatoria del mazo"""
    return random.choice(cards)

def calcular_puntos(lista_cartas):
    """
    Calcula los puntos totales de una mano
    Si el As (11) hace que te pases de 21, se convierte en 1
    """
    total = sum(lista_cartas)
    
    # Si te pasas y tienes un As, conviértelo en 1
    if total > 21 and 11 in lista_cartas:
        lista_cartas.remove(11)
        lista_cartas.append(1)
        total = sum(lista_cartas)
    
    return total

def comparar_resultados(puntos_jugador, puntos_dealer):
    """Determina quién ganó el juego"""
    
    if puntos_jugador > 21:
        return "💥 Te pasaste de 21. Pierdes."
    
    if puntos_dealer > 21:
        return "🎉 ¡El dealer se pasó! Tú ganas."
    
    if puntos_jugador == puntos_dealer:
        return "🤝 Empate."
    
    if puntos_jugador > puntos_dealer:
        return "🎉 ¡Ganaste!"
    else:
        return "😔 Ganó el dealer."

def jugar_blackjack():
    """Función principal del juego"""
    
    print("\n" + "="*40)
    print("🃏  BIENVENIDO AL BLACKJACK  🃏")
    print("="*40 + "\n")
    
    # Dar cartas iniciales
    cartas_jugador = [dar_carta(), dar_carta()]
    cartas_dealer = [dar_carta(), dar_carta()]
    
    juego_terminado = False
    
    # Turno del jugador
    while not juego_terminado:
        puntos_jugador = calcular_puntos(cartas_jugador)
        puntos_dealer = calcular_puntos(cartas_dealer)
        
        print(f"🎴 Tus cartas: {cartas_jugador} → Puntos: {puntos_jugador}")
        print(f"🎴 Carta visible del dealer: [{cartas_dealer[0]}]\n")
        
        # Si el jugador se pasa de 21, pierde automáticamente
        if puntos_jugador > 21:
            juego_terminado = True
        # Si el jugador tiene 21 exacto (Blackjack), se planta automáticamente
        elif puntos_jugador == 21:
            print("🎯 ¡BLACKJACK! Te plantas automáticamente.\n")
            juego_terminado = True
        else:
            # Preguntar si quiere otra carta
            otra_carta = input("¿Quieres otra carta? Escribe 's' (sí) o 'n' (no): ").lower()
            
            if otra_carta == 's':
                cartas_jugador.append(dar_carta())
                print(f"📥 Nueva carta recibida!\n")
            else:
                juego_terminado = True
    
    # Turno del dealer (solo si el jugador no se pasó)
    puntos_jugador = calcular_puntos(cartas_jugador)
    
    if puntos_jugador <= 21:
        print("="*40)
        print("🎰 TURNO DEL DEALER")
        print("="*40)
        print(f"🎴 Cartas del dealer: {cartas_dealer} → Puntos: {puntos_dealer}\n")
        
        # El dealer debe pedir carta si tiene menos de 17
        while puntos_dealer < 17:
            cartas_dealer.append(dar_carta())
            puntos_dealer = calcular_puntos(cartas_dealer)
            print(f"🎴 Dealer recibe carta: {cartas_dealer} → Puntos: {puntos_dealer}")
        
        print()
    
    # Mostrar resultado final
    print("="*40)
    print("📊 RESULTADO FINAL")
    print("="*40)
    print(f"🎴 Tus cartas finales: {cartas_jugador} → {puntos_jugador} puntos")
    print(f"🎴 Cartas del dealer: {cartas_dealer} → {puntos_dealer} puntos\n")
    
    print(comparar_resultados(puntos_jugador, puntos_dealer))
    print("="*40 + "\n")

# Iniciar el juego
if __name__ == "__main__":
    jugar_blackjack()
    
    # Preguntar si quiere jugar otra vez
    while input("¿Quieres jugar otra vez? 's' o 'n': ").lower() == 's':
        jugar_blackjack()
    
    print("\n👋 ¡Gracias por jugar! Hasta pronto.")
