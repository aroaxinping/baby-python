import art  # Importa el archivo art.py que contiene el logo ASCII de la calculadora


# ============================================================================
# DEFINICIÓN DE FUNCIONES MATEMÁTICAS
# ============================================================================
# Cada función realiza UNA operación matemática específica
# Todas siguen el mismo patrón: reciben 2 números (n1, n2) y RETORNAN el resultado
# El 'return' es CRUCIAL: sin él, la función no devuelve nada (None)

def add(n1, n2):
    """Suma dos números y retorna el resultado"""
    return n1 + n2


def subtract(n1, n2):
    """Resta n2 de n1 y retorna el resultado"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplica dos números y retorna el resultado"""
    return n1 * n2


def divide(n1, n2):
    """Divide n1 entre n2 y retorna el resultado"""
    return n1 / n2
    # NOTA: No maneja división por cero (causaría error si n2 = 0)


# ============================================================================
# DICCIONARIO DE OPERACIONES
# ============================================================================
# Este es el CORAZÓN del programa: un diccionario que guarda FUNCIONES como valores
# 
# Estructura: { "símbolo": función }
# - Clave: El símbolo matemático como string ("+", "-", etc.)
# - Valor: La FUNCIÓN misma (sin paréntesis, no la ejecutamos todavía)
#
# ¿Por qué es poderoso?
# - Podemos elegir qué función ejecutar dinámicamente según input del usuario
# - Evitamos escribir múltiples if/elif/else
# - Es escalable: agregar nuevas operaciones es solo añadir una línea

operations = {
    "+": add,        # Si usuario elige "+", ejecutaremos add()
    "-": subtract,   # Si usuario elige "-", ejecutaremos subtract()
    "*": multiply,   # Si usuario elige "*", ejecutaremos multiply()
    "/": divide,     # Si usuario elige "/", ejecutaremos divide()
}

# EJEMPLO de cómo funciona:
# print(operations["*"](4, 8))
# Esto es equivalente a: multiply(4, 8)
# 1. operations["*"] busca en el diccionario y encuentra la función multiply
# 2. (4, 8) ejecuta esa función con esos argumentos
# 3. Resultado: 32


# ============================================================================
# FUNCIÓN PRINCIPAL: CALCULATOR
# ============================================================================
# Esta función encapsula TODA la lógica de la calculadora
# Ventajas de tenerlo en una función:
# - Podemos llamarla recursivamente para reiniciar
# - El código está organizado y no "suelto"
# - Es reutilizable

def calculator():
    # ========================================================================
    # INICIALIZACIÓN
    # ========================================================================
    print(art.logo)  # Muestra el logo ASCII al inicio
    
    # FLAG de control del bucle principal
    # True = continuar en el loop, False = salir del loop
    # Esta variable controla si seguimos calculando o no
    should_accumulate = True
    
    # Pedimos el PRIMER número al usuario
    # float() permite números decimales (no solo enteros como int())
    # Este será el número inicial con el que empezamos a calcular
    num1 = float(input("What is the first number?: "))

    # ========================================================================
    # BUCLE PRINCIPAL - Aquí ocurre toda la magia de la calculadora
    # ========================================================================
    # Este loop continúa MIENTRAS should_accumulate sea True
    # Permite hacer múltiples operaciones seguidas con el resultado anterior
    
    while should_accumulate:
        
        # ====================================================================
        # PASO 1: Mostrar operaciones disponibles
        # ====================================================================
        # Iteramos sobre las CLAVES del diccionario (los símbolos: +, -, *, /)
        # 'for symbol in operations' recorre cada clave del diccionario
        for symbol in operations:
            print(symbol)  # Imprime cada símbolo en una línea
        # Resultado en pantalla:
        # +
        # -
        # *
        # /
        
        # ====================================================================
        # PASO 2: Obtener inputs del usuario
        # ====================================================================
        # Preguntamos qué operación quiere realizar
        operation_symbol = input("Pick an operation: ")
        # El usuario escribe por ejemplo: "*"
        
        # Preguntamos el segundo número
        num2 = float(input("What is the next number?: "))
        # El usuario escribe por ejemplo: 5
        
        # ====================================================================
        # PASO 3: REALIZAR EL CÁLCULO (la parte más importante)
        # ====================================================================
        # Esta línea es PURA MAGIA y merece explicación detallada:
        
        answer = operations[operation_symbol](num1, num2)
        
        # Desglosemos esto paso a paso con un ejemplo:
        # Si operation_symbol = "*", num1 = 10, num2 = 5
        #
        # 1. operations[operation_symbol]
        #    → operations["*"]
        #    → Busca en el diccionario la clave "*"
        #    → Encuentra la función multiply
        #
        # 2. operations["*"](num1, num2)
        #    → multiply(num1, num2)
        #    → multiply(10, 5)
        #    → Ejecuta la función multiply con argumentos 10 y 5
        #    → Retorna 50
        #
        # 3. answer = 50
        #
        # Es como tener un control remoto donde cada botón ejecuta una función diferente
        
        # ====================================================================
        # PASO 4: Mostrar el resultado
        # ====================================================================
        # f-string para formatear e imprimir: "10.0 * 5.0 = 50.0"
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        # ====================================================================
        # PASO 5: Preguntar si continuar o reiniciar
        # ====================================================================
        # Le preguntamos al usuario si quiere:
        # - Continuar calculando CON el resultado actual (acumular)
        # - O empezar de cero con un nuevo número
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        
        # ====================================================================
        # PASO 6: Decisión - Acumular o Reiniciar
        # ====================================================================
        
        if choice == "y":
            # ================================================================
            # OPCIÓN 1: CONTINUAR (ACUMULAR)
            # ================================================================
            # Esta es LA LÍNEA CLAVE para la acumulación:
            
            num1 = answer
            
            # ¿Qué hace esto?
            # REASIGNA num1 con el valor de answer
            # Ahora num1 ya no es el número original, es el RESULTADO anterior
            #
            # Ejemplo del flujo:
            # Iteración 1:
            #   num1 = 10
            #   num2 = 5
            #   answer = 50
            #   Usuario dice 'y'
            #   num1 = 50  ← REASIGNACIÓN
            #
            # Iteración 2:
            #   num1 = 50  ← ¡Ahora usa el resultado anterior!
            #   num2 = 15 (nuevo input del usuario)
            #   answer = 65
            #
            # Sin esta línea, num1 siempre sería 10 y no acumularíamos
            
            # should_accumulate sigue siendo True, así que el while continúa
            # El bucle vuelve al inicio y permite otra operación
            
        else:
            # ================================================================
            # OPCIÓN 2: REINICIAR
            # ================================================================
            # El usuario escribió 'n' o cualquier cosa que no sea 'y'
            
            # Cambiamos el flag a False para SALIR del bucle while
            should_accumulate = False
            
            # "Limpiamos" la pantalla imprimiendo 20 líneas vacías
            # No borra realmente, pero empuja el contenido anterior fuera de vista
            print("\n" * 20)
            
            # ================================================================
            # RECURSIÓN - La función se llama a sí misma
            # ================================================================
            calculator()
            
            # ¿Qué hace esto?
            # Ejecuta calculator() de nuevo, empezando desde el principio
            # Es como presionar el botón de "reiniciar" del programa
            #
            # Ventajas de la recursión aquí:
            # - No necesitamos duplicar código
            # - Empieza con un estado completamente limpio
            # - Todas las variables se reinician (nuevo num1, nuevo should_accumulate, etc.)
            #
            # Alternativa sin recursión:
            # Podríamos poner TODO dentro de otro while loop gigante
            # Pero la recursión es más elegante en este caso


# ============================================================================
# PUNTO DE ENTRADA - Inicia el programa
# ============================================================================
# Esta línea ejecuta la función calculator() por primera vez
# Todo el programa empieza aquí
calculator()


# ============================================================================
# CONCEPTOS CLAVE PARA RECORDAR
# ============================================================================
#
# 1. FUNCIONES EN DICCIONARIOS:
#    - Se guardan SIN paréntesis: operations = {"+": add}
#    - Se ejecutan CON paréntesis: operations["+"](5, 3)
#
# 2. RETURN:
#    - Sin return, una función devuelve None
#    - Con return, podemos usar el resultado: answer = add(5, 3)
#
# 3. REASIGNACIÓN PARA ACUMULACIÓN:
#    - num1 = answer hace que el resultado se convierta en el nuevo input
#    - Sin esto, no hay acumulación, solo cálculos independientes
#
# 4. FLAGS BOOLEANOS:
#    - should_accumulate = True/False controla el bucle
#    - Más claro que comparar strings directamente
#
# 5. RECURSIÓN:
#    - calculator() llamando a calculator()
#    - Útil para reiniciar con estado limpio
#    - Cuidado: demasiadas llamadas recursivas pueden causar stack overflow
#
# 6. for KEY in DICTIONARY:
#    - Itera sobre las CLAVES del diccionario
#    - Para obtener valores: dictionary[key]
#
# 7. f-strings:
#    - f"{variable}" permite insertar variables en strings
#    - Más limpio que concatenar con +
#
# ============================================================================
