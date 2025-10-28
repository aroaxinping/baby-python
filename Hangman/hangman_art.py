## hangman_art.py
```python
# hangman_art.py
# Este archivo contiene el arte ASCII para el juego

# Logo que se muestra al inicio del juego
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''

# Lista de dibujos del ahorcado
# stages[6] = sin errores (dibujo vacío)
# stages[5] = 1 error (cabeza)
# stages[4] = 2 errores (cabeza + cuerpo)
# stages[3] = 3 errores (cabeza + cuerpo + brazo izquierdo)
# stages[2] = 4 errores (cabeza + cuerpo + ambos brazos)
# stages[1] = 5 errores (cabeza + cuerpo + ambos brazos + pierna izquierda)
# stages[0] = 6 errores (ahorcado completo = GAME OVER)

stages = [
    # Estado final: 6 errores - PERDISTE
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    ''',
    # Estado 5: 5 errores
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    ''',
    # Estado 4: 4 errores
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    ''',
    # Estado 3: 3 errores
    '''
       --------
       |      |
       |      O
       |     \\|
       |      |
       |     
       -
    ''',
    # Estado 2: 2 errores
    '''
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    ''',
    # Estado 1: 1 error
    '''
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    ''',
    # Estado inicial: 0 errores
    '''
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    '''
]
```
