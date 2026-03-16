# Coloca el código de tu juego en este archivo.
include "game/recursos.rpy"
# El juego comienza aquí.

label start:

    scene bg_montana #Firts scene, background of the mountain

    show aiden_normal

    # Aiden's dialogue: Here we introduce the character and his backstory.
    aid "Aiden creció en un pequeño pueblo al pie de las montañas. Cuando era niño, su hermana desapareció durante una excursión. Nunca encontraron su cuerpo."

    #Scene transition: We transition to a new background to indicate the passage of time.
    scene bg_fiveyears
    with (fade)
    pause 4.0
    
    return
