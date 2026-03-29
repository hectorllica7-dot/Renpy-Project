# Coloca el código de tu juego en este archivo.
include "game/recursos.rpy"
# El juego comienza aquí.
transform credits_scroll:
    xalign 0.5
    yalign 1.2
    xanchor 0.5
    linear 25.0 yalign -1.0
image ending_movie = Movie(play="images/video/final_malo.webm", loop=True)
image ending_movie_good = Movie(play="images/video/final_bueno.webm", loop=True)

label start:
    default liberar_nino = False

    scene bg_aldea #Firts scene, background of the mountain

    show aiden_nino at center #Aiden as a child, in the center of the screen

    # Aiden's dialogue: Here we introduce the character and his backstory.
    nar "{i}Aiden Vivía en una pequeña aldea junto a su padre, un guerrero retirado que había dejado atrás la violencia.{/i}"
    nar "{i}Su padre no era como los demás hombres del norte: no buscaba batallas ni gloria. Creía que la verdadera fuerza no estaba en la espada, sino en saber cuándo no usarla.{/i}"
         
    scene bg_montana with fade #Second scene, background of the mountain
    show aiden_espada at left #Aiden with his sword, on the left side of the screen
    show eros_normal at right #Eros with his sword, on the right side of the screen
    nar "{i}Aiden lo admiraba. Entrenaban juntos, pero su padre siempre le repetía lo mismo:{/i}"
    ero "Un verdadero guerrero no necesita enemigos."
    nar "{i}Aiden no lo entendía… aún.{/i}"

    scene bg_aldea_quemada with hpunch #Third scene, background of the burned village
    nar "{i}Un día, todo cambió. Un grupo de mercenarios llegó a la aldea. No venían a negociar, ni a hablar. Venían a arrasar.{/i}"
    nar "{i}Los hombres del pueblo intentaron defenderse, pero eran superados. El caos se extendió rápidamente: fuego, gritos, acero chocando.{/i}"
    show eros_serio at right #Eros with a serious expression, on the right side of the screen
    nar "{i}Aiden, escondido, observaba sin poder hacer nada. Su padre salió a enfrentarlos.{/i}"
    nar "{i}Pero no atacó. Bajó el arma e intentó hablar.{/i}"
    show aiden_nino_triste at left: #Aiden with a sad expression, on the left side of the screen
        xzoom -1.0
    aid "Esto no es necesario. Podemos detener esto."
    nar "{i}Por un momento, el tiempo pareció detenerse. Entonces, Kael avanzó.{/i}"
    nar "{i}Sin decir una palabra… levantó su espada. Y lo mató.{/i}"
    hide eros_serio with hpunch #Eros disappears with a hit effect
    hide aiden_nino_triste
    nar "{i}Sin rabia. Sin duda. Solo como parte del trabajo.{/i}"
    nar "{i}El mundo de Aiden se rompió en ese instante. Los mercenarios se marcharon, dejando atrás destrucción… y silencio.{/i}"
    show aiden_nino_triste:
            xzoom -1.0
            xalign -0.5
            yalign 1.0
            linear 0.5 xalign 0.5
    show eros_derrotado at right #Eros with a defeated expression, on the right side of the screen
    nar "{i}Aiden salió de su escondite y corrió hacia el cuerpo de su padre.{/i}"
    nar "{i}Se arrodilló junto a él, temblando.{/i}"
    scene bg_fiveyears with fade #Fourth scene
    pause 4.0

    scene bg_tumba with fade #Fifth scene
    play sound "audio/viento.mp3" loop
    nar "{i}El viento sopla entre las lápidas. El cielo está cubierto, gris, como si el mundo mismo guardara luto.{/i}"
    show aiden_espaldas at left #Aiden with his back turned, in the center of the screen
    nar "{i}Aiden permanece inmóvil frente a una tumba reciente. La tierra aún está fresca.{/i}"
    aid "..."
    aid "No llegué a tiempo"
    nar "{i}Aprieta los puños{/i}"
    aid "Dijeron que luchaste hasta el final"
    aid "Que no retrocediste"
    nar "{i}El viento arrecia. Una hoja cruza frente a él{/i}"
    aid "Kael..."
    nar "{i}El nombre pesa{/i}"
    aid "Voy a encontrarte"
    aid "Y cuando lo haga..."
    nar "{i}Se detiene. Respira hondo. Sus manos tiemblan ligeramente.{/i}"
    nar "{i}El silencio vuelve. Más profundo.{/i}"
    aid "..."
    nar "{i}Mira la tumba. Sus ojos ya no estan llenos solo de dolor... también de duda.{/i}"
    menu:    
        "Juro que lo mataré. Cueste lo que cueste.":
            jump ruta_odio
        
        "No dejaré que el odio me consuma... pero me hare fuerte":
            jump ruta_voluntad
        
label ruta_odio:
    aid "Juro, que no importa cuantó tiempo pase..."
    aid "No importa en que tenga que convertirme."
    nar "{i}Clava la mirada en la tumba{/i}"
    aid "Kael morira por esto"
    nar "{i}El viento sopla con mas fuerza{/i}"
    #musica_viento
    nar "{i}y asi, empieza el odio{/i}"
    jump guerilleros

label ruta_voluntad:
    nar "{i}(voz contenida){/i}"
    aid "No… esto no es lo que querías para mí."
    nar "{i}Cierra los ojos un momento.{/i}"
    aid "Me haré fuerte."
    aid "Pero no para convertirme en alguien como él."
    nar "{i}Apoya suavemente su mano sobre la tumba.{/i}"
    aid "Encontraré mi propio camino."
    #musica fondo
    nar "{i}El viento se calma levemente.{/i}"
    nar "{i}Y así, una duda comienza a crecer… junto con la fuerza.{/i}"
    jump guerilleros

label guerilleros:
    stop sound
    scene bg_guerrilleros with fade
    nar "{i}El sonido del acero chocando resuena a lo lejos.{/i}"
    nar "{i}Aiden avanza entre rocas y árboles secos… hasta que lo ve.{/i}"
    show aiden_serio at left #Aiden in his normal state, on the left side of the screen
    aid "Kael..."
    show kael_normal: #Kael in his normal state, on the right side of the screen
        xalign 0.8
        yalign 1.0
    nar "{i}De pie entre varios guerreros. Imponente. Tranquilo. Como si nada en el mundo pudiera tocarlo.{/i}"
    nar "{i}La sangre de Aiden hierve. Su respiración se vuelve pesada.{/i}"
    nar "{i}Aiden susurra{/i}"
    aid "Por fin..."
    nar "{i}Kael levanta ligeramente la cabeza. Como si ya supiera que alguien lo observa. Sus miradas se cruzan.{/i}"
    menu:
        "Atacar sin pensarlo":
            jump ataque_kael
        
        "Mantener la calma y acercarse":
            jump estrategia
label ataque_kael:
    aid "{b}¡Kael!{/b}"
    hide aiden_serio with hpunch
    show aiden_ataque at left #Aiden in his attack state, on the
    nar "{i}Aiden corre hacia él con todo lo que tiene. Rabia, dolor, años acumulados.{/i}"
    play sound "audio/desenvainar_espada.mp3"
    nar "{i}Aiden desenvaina su arma y ataca sin pensar.{/i}"
    stop sound
    nar "{i}Kael… ni siquiera se mueve al principio.{/i}"
    pause 1.0
    hide kael_normal
    show kael_espada with hpunch: #Kael with his sword, on the right side of the screen
        xalign 0.8
        yalign 1.0
    nar "{i}En el último segundo...{/i}"
    play sound "audio/choque_espadas.mp3"
    nar "{i}Kael bloquea el ataque con facilidad.{/i}"
    nar "{i}Silencio...{/i}"
    pause 1.0
    kae "…"
    kae "Qué decepcionante."
    nar "{i}Con un solo movimiento, golpea a Aiden en el estómago.{/i}"
    hide aiden_ataque with hpunch
    show aiden_herido: #Aiden in his wounded state, on the left side of the screen
        xalign 0.2
        yalign 1.0
        xzoom -1.0
    nar "{i}Aiden cae de rodillas, sin aliento.{/i}"
    nar "{i}Kael lo observa desde arriba.{/i}"
    kae "Vienes con ese fuego en los ojos… y no tienes nada que lo sostenga."
    nar "{i}Aiden intenta levantarse, pero Kael lo empuja de nuevo al suelo.{/i}"
    kae "Si quieres matar a alguien, primero aprende a no morir."
    nar "{i}Se gira, perdiendo el interés.{/i}"
    kae "Déjenlo. No es más que un niño con una espada."
    nar "{i}Uno de los guerreros ríe.{/i}"
    nar "{i}Kael se detiene un segundo… sin mirar atrás.{/i}"
    kae "Si sigue vivo mañana…"
    pause 0.5
    kae "quizá aprenda algo."
    nar "{i}Derrotado, pero no muerto. A veces, sobrevivir es el primer paso.{/i}"
    hide kael_normal
    hide aiden_herido
    jump black
label estrategia:
    hide kael_normal
    nar "{i}Aiden camina hacia ellos. Sin desenvainar. Sin correr.{/i}"
    show aiden_serio at left #Aiden in his normal state, on the left side of the screen
    nar "{i}Cada paso pesa. Los guerreros lo notan enseguida.{/i}"
    show guerrero_normal at right #A warrior in his normal state, on the right side of the screen
    gue "{b}Eh!{/b} Tenemos compañía."
    hide guerrero_normal
    show kael_normal: #Kael in his normal state, on the right side of the screen
        xalign 0.8
        yalign 1.0
    nar "{i}Varias manos se posan sobre armas... Kael levanta una mano. Todos se detienen.{/i}"
    pause 1.0
    nar "{i}Silencio.{/i}"
    nar "{i}Aiden queda frente a él. Kael lo examina. De arriba abajo.{/i}"
    kae "No vienes a luchar."
    aid "No. No vine a eso."
    kae "Entonces habla."
    nar "{i}Aiden sostiene su mirada.{/i}"
    aid "Quiero hacerme más fuerte."
    nar "{i}Un murmullo entre los guerreros.{/i}"
    gue "Otro crío buscando gloria…"
    nar "{i}Kael no sonríe. No se burla. Solo observa.{/i}"
    kae " La fuerza tiene un precio. Y no todos pueden pagarlo."
    aid "Estoy dispuesto a pagar ese precio."
    nar "{i}Un silencio tenso.{/i}"
    pause 1.0
    nar "{i}Kael sussura{/i}"
    kae "¿Incluso si eso significa perder lo que eres?"
    nar "{i}Aiden duda… apenas un segundo.{/i}"
    aid "..."
    pause 0.5
    aid "Si, pagaré ese precio."
    kae "Hmm"
    nar "{i}Se gira.{/i}"
    kae "Puedes venir."
    nar "{i}Los guerreros se miran entre sí, sorprendidos.{/i}"
    gue "¿En serio? ¿Vas a dejar que un niño se una a nosotros?"
    kae "Si estorba, muere."
    nar "{i}Sigue caminando sin mirar atrás. Tras un instante… Aiden lo sigue.{/i}"
    jump black
label black:
    scene bg_black with fade
    nar "{i}A veces, acercarse al enemigo es la forma más peligrosa de guerra.{/i}"
    pause 1.0
    nar "{i}El grupo avanza. Armas, armaduras, risas ásperas.{/i}"
    nar "{i}Aiden camina entre ellos. Ahora… ya no está solo.{/i}"
    jump cuartel
label cuartel:
    scene bg_cuartel_quemado with fade
    nar "{i}Humo y gritos llenan el aire. Casas de madera arden mientras los guerreros avanzan, gritando y golpeando todo a su paso.{/i}"
    nar "{i}Aiden observa desde una colina cercana. El corazón le late rápido.{/i}"
    show guerrero_normal at right #A normal warrior, on the right side of the screen
    gue "¡Vamos! ¡No dejen que nada sobreviva!"
    hide guerrero_normal
    nar "{i}El grupo se dispersa entre los aldeanos aterrados.{/i}"
    menu:
        "Saquear":
            jump Saquear
        "Ayudar":
            jump Ayudar 
label Saquear:
    nar "{i}Aiden se une al caos. Arrebata armas, saquea cofres y golpea a quien se interpone.{/i}"
    show guerrero_normal at right #A normal warrior, on the right side of the screen
    gue "¡Eso es, chico! ¡Así se hace!"
    hide guerrero_normal
    nar "{i}Aiden siente una mezcla de adrenalina y culpa… pero no lo muestra.{/i}"
    show aiden_ataque at left #Aiden in his attack state, on the left side of the screen
    nar "{i}Kael lo observa desde un rincón, evaluando.{/i}"
    show kael_normal: #Kael in his normal state, on the right side of the screen
        xalign 0.8
        yalign 1.0
    kae "Bien. Aprendes rápido."
    nar "{i}La violencia trae respeto… pero también deja cicatrices invisibles.{/i}"
    nar "{i}La aldea queda destruida. Los gritos se desvanecen entre las llamas.{/i}"
    jump black_1
label Ayudar:
    show aiden_normal at left #Aiden in his normal state, on the left side of the screen
    nar "{i}Aiden se mueve entre el caos con cautela. Encuentra a aldeanos escondidos entre escombros y casas en llamas.{/i}"
    show aldeano at right #A villager in his normal state, on the right side of the screen
    aid "Rápido… por aquí."
    hide aiden_normal
    hide aldeano
    nar "{i}Ayuda a algunas familias a escapar por caminos ocultos. Nadie del grupo lo nota.{/i}"
    show guerrero_normal at right #A normal warrior, on the right side of the screen
    gue "¿Qué hace ese crío?"
    hide guerrero_normal
    show kael_espada: #Kael in his normal state, on the right side of the screen
        xalign 0.8
        yalign 1.0
    kae "Déjalo. Si estorba, tarde o temprano aprenderá."
    hide kael_espada
    jump black_1
label black_1:
    nar "{i}Sus manos salvan vidas, pero su corazón se llena de miedo y duda. La guerra es cruel y la compasión es un acto peligroso.{/i}"
    pause 1.0
    nar "{i}La aldea queda destruida, pero algunos inocentes logran escapar gracias a Aiden.{/i}"
    jump carcel
label carcel:
    scene bg_jaula with fade
    nar "{i}Entre sombras y polvo, una joven está encadenada a un poste. Sus ojos reflejan miedo… y una chispa de esperanza al verlo.{/i}"
    show lyra_triste at center #Lyra with a sad expression, in the center of the screen
    lyr "¿Por favor...? "
    nar "{i}Aiden se detiene. El silencio pesa. El sonido de los guerreros que se alejan se mezcla con el crepitar de una pequeña hoguera cercana.{/i}"
    menu:
        "Liberarla":
            $ liberar_lyra = False
            jump liberar_lyra
        "Ignorarla":
            $ liberar_lyra = True
            jump ignorar_lyra
label liberar_lyra:
    nar "{i}Aiden rompe las cadenas con cuidado, tratando de no hacer ruido.{/i}"
    lyr "¡No… no puedo creerlo!"
    show aiden_normal at left #Aiden in his normal state, on the left side of the screen
    aid "Corre. Rápido."
    hide lyra_triste
    show lyra_sonriente at center #Lyra with a smiling expression, in the center of the screen
    nar "{i}Ella lo mira con gratitud, y una pequeña sonrisa rompe la tensión.{/i}"
    hide lyra_sonriente
    show guerrero_normal at right #A normal warrior, on the right side of the screen
    gue "¿Qué haces? ¡Deberias matarla!"
    nar "{i}Kael lo mira, con una mezcla de desaprobación y… curiosidad.{/i}"
    hide guerrero_normal
    show kael_normal at right #Kael in his normal state, on the right side of the screen
    kae "Hmm. Mantienes tu moral… por ahora."
    kae "Pero el mundo no siempre da segundas oportunidades."
    nar "{i}Algunos dudan de ti, pero tu conciencia permanece intacta.{/i}"
    nar "{i}La tensión dentro del grupo aumenta.{/i}"
    nar "{i}Tu decisión deja huellas profundas, visibles solo para los que saben mirar.{/i}"
    jump black_2
label ignorar_lyra:
    show lyra_triste at center #Lyra with a sad expression, in the center of the screen
    nar "{i}Aiden se acerca, con la respiración agitada.{/i}"
    show aiden_serio at left #Aiden in his normal state, on the left side of the screen
    nar "{i}No es mi problema.{/i}"
    hide aiden_serio with hpunch
    hide lyra_triste with hpunch #Lyra disappears with a hit effect
    nar "{i}Aiden se aleja, dejando a la joven atrás.{/i}"
    nar "{i}Algunas decisiones son más fáciles… pero pesan más de lo que parece.{/i}"
    nar "{i}Te vuelves más duro, y la tensión con algunos guerreros disminuye…{/i}"
    nar "{i}pero algo dentro de ti cambia para siempre.{/i}"
    jump black_2
label black_2:
    scene bg_colina with fade
    nar "{i}El grupo sigue avanzando, cada vez más lejos de la aldea que una vez llamaste hogar.{/i}"
    nar "{i}Las decisiones que tomaste te han marcado, y el camino por delante es incierto.{/i}"
    nar "{i}Pero una cosa es segura: el viaje apenas ha comenzado.{/i}"
    jump bosque
label bosque:
    scene bg_bosque with fade
    nar "{i}Se hace la noche, Kael y los suyos contiunan a un camino sin rumbo fijo, sin un destino claro.{/i}"
    show niño_atado: #A tied child, in the center of the screen
        xalign 0.8
        yalign 1.0
    nar "{i}De repente en un arbol, se puede ver un niño de apenas diez años está atado de pies y manos, temblando.{/i}"
    show guerrero_normal at left #A normal warrior, on the left side of the screen
    nar "{i}Un guerrero se acerca, con una sonrisa fría.{/i}"
    gue "Mira lo que tenemos aquí. Este pequeño no sirve para nada más que para… enseñarle a temer."
    nar "{i}Kael observa, imperturbable.{/i}"
    nar "{i}Aiden siente que todo se tensa a su alrededor.{/i}"
    hide guerrero_normal
    menu:
        "Matarlo sin dudar":
            $ liberar_nino = False
            jump matar_niño
        "Liberarlo":
            $ liberar_nino = True
            jump liberar_niño
label matar_niño:
    show niño_atado: #A tied child, on the right side of the screen
        xalign 0.8
        yalign 1.0
    nar "{i}Aiden se acerca, con la respiración agitada.{/i}"
    show aiden_ataque at left #Aiden in his attack state, on the left side of the screen
    nar "{i}Sin dudarlo, levanta el arma y termina con el niño.{/i}"
    play sound "audio/desenvainar_espada.mp3"
    hide niño_atado with hpunch #The tied child disappears with a hit effect
    show guerrero_normal at right #A normal warrior, on the right side of the screen
    gue "¡Eso es! ¡Así se hace! Finalmente entiendes lo que significa sobrevivir aquí."
    nar "{i}Kael asiente, sin emoción, pero con aprobación tácita.{/i}"
    hide guerrero_normal
    nar "{i}La sangre endurece el corazón. Respeto ganado, humanidad perdida.{/i}"
    nar "{i}Te vuelves más duro, y la tensión con algunos guerreros disminuye…{/i}"
    nar "{i}pero algo dentro de ti cambia para siempre.{/i}"
    jump la_verdad
label liberar_niño:
    nar "{i}Aiden corta las cuerdas y empuja al niño hacia el bosque, susurrándole:{/i}"
    show niño_atado:#A tied child, on the right side of the screen
        xalign 0.8
        yalign 1.0
    show aiden_normal at left #Aiden in his normal state, on the left side of the screen
    play sound "audio/desenvainar_espada.mp3"
    aid "Corre. Rápido."
    nar "{i}El niño desaparece entre los árboles, llorando y temblando, pero vivo.{/i}"
    hide niño_atado
    show guerrero_normal at right #A normal warrior, on the right side of the screen
    gue "Qué haces? ¡Deberias matarlo!"
    nar "{i}Kael lo mira, con una mezcla de desaprobación y… curiosidad.{/i}"
    hide guerrero_normal
    show kael_normal at right #Kael in his normal state, on the right side
    kae "Hmm. Mantienes tu moral… por ahora."
    kae "Pero el mundo no siempre da segundas oportunidades."
    hide kael_normal
    nar "{i}Algunos dudan de ti, pero tu conciencia permanece intacta.{/i}"
    nar "{i}La tensión dentro del grupo aumenta.{/i}"
    nar "{i}Tu decisión deja huellas profundas, visibles solo para los que saben mirar.{/i}"
    jump la_verdad
label la_verdad:
    scene bosque_amanecer with fade
    nar "{i}La noche da paso al amanecer.{/i}"
    show aiden_serio at center #Aiden in his normal state, on the left side of the screen
    nar "{i}Aiden junto a uno de los carruajes, encuentra documentos antiguos y relatos de sobrevivientes{/i}"
    nar "{i}Aiden finalmente descubre la verdad...{/i}"
    hide aiden_serio
    show aiden_punos at center #Aiden with his fists clenched, in
    nar "{i}Kael no mató a su padre por odio." 
    nar "{i}Solo seguía órdenes.{/i}"
    nar "{i}El corazón de Aiden se tensa y sus manos aprietan los puños, temblando ligeramente.{/i}"
    aid "Entonces… todo este tiempo… ¿he estado equivocado?"
    show kael_normal at left #Kael in his normal state, on the right side of the screen
    nar "{i}Kael aparece detrás de él, en silencio, observando cómo procesa la información.{/i}"
    kae "La verdad no cambia el pasado, Aiden. Solo cambia cómo decides vivir con él."
    menu:
        "Odiar":
            jump odiar
        "Dudar":
            jump dudar
label odiar:
    aid "No importa. Lo que hiciste destruyó a mi familia."
    aid "Mi venganza sigue siendo mia"
    nar "{i}Kael asiente levemente, sin sorpresa ni reproche.{/i}"
    kae "Entonces sigue adelante. Pero recuerda… el odio es un fuego que consume a quien lo sostiene."
    nar "{i}La revelación no cambia tu rumbo. Tu odio permanece, y con él, tu destino.{/i}"
    jump campamento_noche_1
label dudar:
    hide aiden_punos
    show aiden_sentado at center: #Aiden sitting, in the center of the screen
        xzoom -1.0
    nar "{i}Aiden se sienta, apoyando los codos sobre las rodillas, la mirada perdida.{/i}"
    aid "Entonces… ¿todo lo que sentí… era por nada?"
    kae "No es nada. Es solo… parte de tu viaje. Parte de lo que te hizo quien eres."
    kae "Pero ahora lo sabes. Y eso cambia tu camino."
    nar "{i}Dudar abre puertas que el odio cerraba. Tu mente se vuelve un campo de batalla, mientras tu corazón intenta encontrar su lugar.{/i}"
    jump campamento_noche_1
label campamento_noche_1:
    scene bg_campamento_noche with fade
    nar "{i}El grupo acampa bajo las estrellas. El fuego crepita, lanzando sombras danzantes sobre los rostros cansados.{/i}"
    nar "{i}Pero una cosa sorprtendente sucede esa noche. Aiden no está solo.{/i}"
    if liberar_lyra:
        scene black with fade
        nar "{i}Una cosa ocurrio la noche anterior, la noche que Aiden decidió ignorar a Lyra{/i}"
        nar "{i}Realmente Aiden no ignoró a Lyra, cuando el grupo se durmio...{/i}"
        nar "{i}Aiden tiro la llave de la celda de Lyra a pies de ella, y ella se liberó por sí misma, sin que nadie lo notara.{/i}"
        jump campamento_noche
    else:
        jump campamento_noche
label campamento_noche:
    scene bg_campamento_noche with fade
    nar "{i}Lyra quien estuvo siguiendo a Aiden desde la distancia...{/i}"
    nar "{i}Aparece silenciosamente desde los arboles, con una sonrisa tímida.{/i}"
    show lyra_normal at left: #Lyra in her normal state, on the right side of the screen
        xzoom -1.0
    lyr "Aiden… hay un lugar lejos de todo esto."
    aid "Que? Quien me llama?"
    show aiden_serio at center #Aiden in his normal state, on the left side of the screen
    nar "{i}Aiden se sorprende al escuchar su nombre, pero no ve a nadie.{/i}"
    lyr "Aquí… en el bosque. Hay un lugar donde podemos estar a salvo."
    aid "Lyra? Eres tú?"
    hide aiden_serio
    show aiden_normal at center #Aiden in his normal state, on the left side of the screen
    lyr "Sí. He estado siguiéndote. Quería ayudarte, pero no sabía cómo acercarme."
    lyr "Conozco un lugar sin guerra, sin cadenas... solo nosotros"
    lyr "Si quieres, puedo llevarte allí. Pero ha de ser esta noche."
    nar "{i}Aiden siente la gravedad de la propuesta. Su corazón late con fuerza.{/i}"
    menu:
        "Huir con Lyra":
            jump aceptar_lyra
        "Quedarte con los guerreros":
            jump quedar_con_guerreros
label aceptar_lyra:
    hide aiden_normal
    hide lyra_normal
    scene bg_campamento_noche with fade
    show aiden_normal at center #Aiden in his normal state, on the left side of the screen
    aid "Está bien… vamos."
    nar "{i}Lyra sonríe suavemente y toma su mano.{/i}"
    show lyra_sonriente at left #Lyra with a smiling expression, in the center of the screen
    nar "{i}Juntos, se deslizan entre las sombras, evitando las patrullas del campamento.{/i}"
    nar "{i}El viento nocturno los acompaña mientras desaparecen en el horizonte.{/i}"
    hide lyra_sonriente
    hide aiden_normal
    nar "{i}La libertad tiene un precio… pero también un comienzo.{/i}"
    nar "{i}Aunque ellos aun no lo saben, su peor pesadilla apenas ha comenzado.{/i}"
    jump black_3
label quedar_con_guerreros:
    scene bg_campamento_noche with fade
    show aiden_serio at center #Aiden in his serious state, on the left side of the screen
    aid "No… debo quedarme."
    nar "{i}Lyra asiente, aunque su sonrisa se desvanece un poco.{/i}"
    show lyra_triste at left #Lyra with a sad expression, in the center of the screen
    lyr "Está bien… lo entiendo."
    nar "{i}Lo que Aiden y Lyra es que alguien los observa.{/i}"
    nar "{i}Detras de ellos esta Kael{/i}"
    show kael_normal: #Kael in his normal state, on the right side of the screen
        xalign 0.8
        yalign 1.0
    kae "Anda si la niña se preocupa por ti."
    kae "No es tan débil como pensaba."
    hide lyra_triste
    show lyra_triste at right #Lyra with a sad expression, in the center of the screen
    nar "{i}Kael rapta a Lyra en ese momento, sin darle a Aiden la oportunidad de reaccionar.{/i}"
    kae "Mañana veremos si me tienes tanta lealtad..."
    hide lyra_triste with hpunch #Lyra disappears with a hit effect
    hide kael_normal with hpunch #Kael disappears with a hit effect
    hide aiden_serio with hpunch #Aiden disappears with a hit effect
    jump claro_bosque
label claro_bosque:
    scene bg_claro_bosque with fade
    play sound "audio/pajaros.mp3" loop
    nar "{i}El dia se abre, y con el, el peor dia de Aiden.{/i}"
    nar "{i}Kael se acerca, la mirada gélida.{/i}"
    kae "Es hora de probar tu lealtad."
    kae "Acaba con ella. Ahora."
    nar "{i}Lyra te mira, confusa y aterrada.{/i}"
    menu:
        "Obedecer a Kael y atacar a Lyra":
            jump atacar_lyra
        
        "Negarse a atacar a Lyra":
            jump proteger_lyra
label atacar_lyra:
    show aiden_ataque at left #Aiden in his attack state, on the left side of the screen
    show lyra_atada at right #Lyra in her tied state, on the right side of the screen
    nar "{i}Aiden levanta el arma, la apunta{/i}"
    aid "Lo siento, Lyra..."
    play sound "audio/desenvainar_espada.mp3"
    hide lyra_atada with hpunch #Lyra disappears with a hit effect
    show kael_normal at right #Kael in his normal state, on the right side of the screen
    kae "Bien. Has demostrado tu lealtad..."
    kae "Ahora puedo confiar totalmente en ti."
    hide kael_normal
    nar "{i}Te has ganado el respeto del maestro… pero a un costo que pesa en tu alma.{/i}"
    stop sound
    jump final_1
label proteger_lyra:
    nar "{i}Aiden baja el arma, la mirada fija en Kael.{/i}"
    aid "No. No puedo hacer eso."
    nar "{i}Kael frunce el ceño, la tensión explota.{/i}"
    kae "¡Insensato!"
    kae "Cómo te atreves a desafiarme?"
    nar "{i}Se desata un enfrentamiento; los guerreros observan en silencio.{/i}"
    nar "{i}Kael ataca con furia, pero Aiden se defiende con determinación, impulsado por la necesidad de proteger a Lyra.{/i}"
    nar "{i}Sabes que revelarte contra Kael es peligroso, pero afirma que aún conservas algo de ti mismo.{/i}"
    nar "{i}Aiden desenvaina su espada, de un golpe seco y rapido, para el ataque de Kael, y contraataca con un movimiento inesperado.{/i}"
    play sound "audio/choque_espadas.mp3"
    nar "{i}Kael cae al suelo, sorprendido por la resistencia de Aiden.{/i}"
    nar "{i}Los guerreros se quedan en silencio, sin saber cómo reaccionar.{/i}"
    nar "{i}Aiden y Lyra aprovechan la confusión para escapar, corriendo hacia el bosque mientras Kael se recupera lentamente.{/i}"
    stop sound
    jump final_2
label black_3:
    scene bg_black with fade
    nar "{i}Aiden y Lyra recorren varios cientos de metros juntos{/i}"
    nar "{i}Cuando de repente, en un claro del bosque...{/i}"
    jump claro_bosque_1
label claro_bosque_1:
    scene bg_claro_bosque with fade
    play sound "audio/pajaros.mp3" loop
    nar "{i}Se encuentran a Kael{/i}"
    kae "¿Pensaste que podrías escapar tan fácilmente?"
    nar "{i}Lyra se esconde detrás de Aiden, temblando.{/i}"
    menu:
        "Luchar contra Kael":
            jump luchar_kael
        "Rendirse":
            jump rendirse_kael
label luchar_kael:
    show aiden_ataque at left #Aiden in his attack state, on the left side of the screen
    nar "{i}Aiden empuña el arma.{/i}"
    play sound "audio/desenvainar_espada.mp3"
    show kael_normal:
        xalign 0.7
        yalign 1.0
    nar "{i}Kael responde con rapidez, ambos chocan en un duelo intenso.{/i}"
    hide kael_normal
    show kael_espada:
        xalign 0.7
        yalign 1.0
    play sound "audio/choque_espadas.mp3"
    nar "{i}Aiden lucha con todo lo que tiene, pero Kael es un oponente despiadado.{/i}"
    nar "{i}Aiden esta entre la vida y la muerte.{/i}"
    if liberar_nino == True:
        nar "{i}Justo cuando Kael está a punto de dar el golpe final...{/i}"
        nar "{i}El niño que Aiden liberó aparece de repente, lanzándose sobre Kael.{/i}"
        show niño_saltando at right with vpunch #The tied child, now jumping, on the right side of the screen
        nar "{i}Kael se tambalea, sorprendido por la aparición inesperada.{/i}"
        hide kael_espada with hpunch
        show kael_espada with hpunch: #Kael with his sword, on the right side of the screen
            xalign 0.7
            yalign 1.0
        nar "{i}Aiden aprovecha la distracción para contraatacar, logrando degollar a Kael.{/i}"
        play sound "audio/cortar_cabeza.mp3"
        hide kael_espada
        nar "{i}Kael, una vez ya muerto, permite a Aiden y Lyra escapar.{/i}"
        stop sound
        jump final_2
    else:
        nar "{i}Kael con un movimiento brutal, deja a Aiden herido.{/i}"
        hide aiden_ataque with hpunch
        show aiden_herido at left #Aiden in his wounded state, on the
        show lyra_herida at right #Lyra in her wounded state, on the right side of the screen
        nar "{i}Permitiendo a Kael, matar a Lyra.{/i}"
        hide lyra_herida with hpunch #Lyra disappears with a hit effect
        aid "¡No!"
        show aiden_espada_herido at left #Aiden with his sword, in his wounded state, on the left side of the screen
        nar "{i}Aiden, herido y exhausto, se levanta y mata a Kael.{/i}"
        sound "audio/corta_cabeza.mp3"
        hide kael_espada
        stop sound
        jump final_1
label rendirse_kael:
    show aiden_ataque at left #Aiden in his attack state, on the left side of the screen
    nar "{i}Aiden baja el arma, resignado.{/i}"
    hide aiden_ataque with hpunch
    show aiden_serio at left #Aiden in his normal state, on the left side of the screen
    aid "No... no más."
    nar "{i}Kael se acerca lentamente, con una sonrisa fría.{/i}"
    show kael_normal:
        xalign 0.7
        yalign 1.0
    kae "¿Es miedo o locura...?"
    kae "De cualquier manera, has perdido."
    hide kael_normal
    show kael_espada:
        xalign 0.7
        yalign 1.0
    play sound "audio/desenvainar_espada.mp3"
    nar "{i}Kael levanta su arma...{/i}"
    kae "Aiden... Vas a perder todo lo que tienes."
    nar "{i}Kael ataca a Lyra.{/i}"
    show lyra_herida at right: #Lyra in her wounded state, on the right side of the screen
        yalign 0.3
        linear 0.3 yalign 0.9
        linear 0.2 rotate 82
    with vpunch
    pause 2.0
    nar "{i}Lyra cae al suelo, muerta.{/i}"
    hide lyra_herida with hpunch #Lyra disappears with a hit effect
    hide aiden_serio with hpunch
    aid "¡No!"
    nar "{i}Aiden, devastado, se levanta y enfrenta a Kael{/i}"
    show aiden_espada_herido at left #Aiden with his sword, in his wounded state, on the left side of the screen
    play sound "audio/desenvainar_espada.mp3"
    nar "{i}De rabia, Aiden mata a Kael{/i}"
    play sound "audio/cortar_cabeza.mp3"
    hide kael_espada
    nar "{i}Pero Aiden ya ha perdido todo lo que tenía...{/i}"
    nar "{i}La familia y el amor{/i}"
    jump final_1
label final_1:
    scene black with fade
    nar "{i}Aiden se queda solo, con el peso de sus decisiones y la pérdida de todo lo que amaba.{/i}"
    nar "{i}El odio lo consume, y su destino se sella en la oscuridad.{/i}"
    nar "{i}Se vuelve en lo que nunca quiso ser.{/i}"
    scene bg_final_devastado with fade
    show aiden_malo at center #Aiden in his evil state, in the center of the screen
    nar "{i}El mundo se convierte en un lugar más oscuro, y Aiden se convierte en una leyenda temida por todos.{/i}"
    nar "{i}El niño que una vez buscó venganza, ahora es el monstruo que temía convertirse.{/i}"
    scene black with fade
    scene ending_movie
    show text """{size=50}{color=#FFFFFF}ASHES OF THE UNBOUND{/color}{/size}\n\n
    {size=30}{color=#CCCCCC}
    Un juego de OIH

    PROGRAMACIÓN: Hector Galindo

    ARTE: Omar e Izan

    MÚSICA: Hector Galindo

    AGRADECIMIENTOS: A todas las IA que ayudaron

    Gracias por jugar
    {/color}{/size}
    """ at credits_scroll
    pause 25.0
    hide movie
    return
label final_2:
    scene black with fade
    nar "{i}Aiden y Lyra encuentran un nuevo camino, lejos de la guerra y el odio.{/i}"
    nar "{i}COMIENZA UNA NUEVA VIDA{/i}"
    nar "{i}Una vida un poco mas afrodisiaca{/i}"
    scene bg_final_playa with fade
    show lyra_playa at right #Lyra in her beach state, on the right side of the screen
    show aiden_playa at left #Aiden in his beach state, on the left side of the screen
    nar "{i}Juntos, encuentran la paz en un mundo que aún tiene esperanza.{/i}"
    scene black with fade
    scene ending_movie_good
    show text """{size=50}{color=#FFFFFF}ASHES OF THE UNBOUND{/color}{/size}\n\n
    {size=30}{color=#CCCCCC}
    Un juego de OIH

    PROGRAMACIÓN: Hector Galindo

    ARTE: Omar e Izan

    MÚSICA: Hector Galindo

    AGRADECIMIENTOS: A todas las IA que ayudaron

    Gracias por jugar
    {/color}{/size}
    """ at credits_scroll
    pause 25.0
    hide movie
    return



    

        



    


        




    return



    



        