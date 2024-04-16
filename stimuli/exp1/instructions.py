# -*- coding: utf-8 -*-

from psychopy import visual, event, core
from psychopy.sound import Sound
import numpy as np


# Experiment instructions
def main_instructions(win, grating, fixation, eye, speaker):
# Instrucciones generales del experimento       
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.text = "¡Bienvenid@ a este experimento! Durante la sesión te vamos a presentar pares de estímulos visuales, y pares de estímulos auditivos." 
    

    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.wrapWidth = 25
    nextt.height = 0.9
    nextt.color = 'black'
    nextt.text = "Pulsa spacio para continuar"
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    inst.text = "En cada bloque te pediremos que atiendas a unos u otros.\
    Dicho de otro modo, si te pedimos que atiendas a los estímulos visuales, tendrás que ignorar a los auditivos, y viceversa." 
    inst.draw()
    nextt.draw()
    eye.draw()
    speaker.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    inst.text = "Los estímulos visuales consisten en enrejados con distintas orientaciones, como el que ves arriba. En cada trial aparecerá el primer enrejado, \
            y a la vez escucharás un suave pitido. Este pitido será el primer estímulo de la pareja auditiva. Asimismo, el segundo pitido se reproducirá a la vez que aparezca el segundo enrejado.\
            Cuando pulses espacio escucharás un tono similar a los del experimento."
    inst.setPos([0,-2])
    nextt.setPos([0,-8])
    grating.draw()
    fixation.draw()
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    sample_sound = Sound(415, sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.2)
    sample_sound.play()
    core.wait(1)
    
    
    return

# PHASE START MESSAGES
# Learning instructions
def learning_starts(win, grating, fixation, red):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Durante esta primera fase tendrás que aprender cuáles son las parejas correctas. Estas van a aparecer con mayor frecuencia que las demás.\
                Tras la presentación del segundo estímulo, tu tarea consistirá en indicar si los dos estímulos que has percibido son una pareja frecuente o infrecuente (según se indique en la pantalla de respuesta)."                 
    nextt.text = "Pulsa espacio para continuar"

    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])
    
    inst.text = "Lógicamente, al principio te costará distinguir qué parejas son las frecuentes y cuáles no. Pero a la larga ciertas parejas te resultarán familiares y acertarás con mayor frecuencia.\
                Además, después de cada respuesta, el punto central cambiará de color: Verde = respuesta correcta / Rojo = incorrecta. \
                En cada bloque te indicaremos qué modalidad sensorial tienes que atender, y siempre habrá un recordatorio visual en pantalla que te lo indicará. Ojo = responde a visuales  /  Altavoz = responde a auditivos."
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    inst.text = "Por último, te pedimos que en todo momento fijes la mirada en el punto central de color blanco.\
                Esto es importante ya que en ciertas ocasiones, el segundo estímulo se presentará con menor intensidad. Independientmente si estás atendiendo a los visuales o los auditivos, \
                si el enrejado aparece con menor contraste, o el tono se escucha más flojo, deberás indicarlo en la pantalla de respuesta, sin tener que responder a la pregunta de si la pareja era frecuente o rara."
    nextt.text = "Pulsa espacio para realizar un par de ejemplos"
    inst.wrapWidth = 40
    inst.setPos([0,13])
    nextt.setPos([0,-12])
    
    
    for i in range(1000):
        keys = event.getKeys(['space'])
        if len(keys) > 0: break
        grating.contrast = 0.7
        for frame in range(60):
            inst.draw()
            nextt.draw()
            grating.draw()
            fixation.draw()
            win.flip()
            if len(keys) > 0: break
        grating.contrast = 0.3
        for frame in range(30):
            inst.draw()
            nextt.draw()
            grating.draw()
            fixation.draw()
            win.flip()
            if len(keys) > 0: break
        
# Learning phase training        
def training_learn(win, basic_stim, stim):
    basic_stim['grating'].contrast = 0.7
    for thisTrial in range(2):        
        leading_ori = np.random.choice([0, 90])
        trailing_ori = np.random.choice([45, 135])
        leading_sound = Sound( np.random.choice([1000, 1600]), sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.2)
        trailing_sound = Sound( np.random.choice([100, 160]), sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.9)
        reminder = basic_stim["eye"] if thisTrial == 0 else basic_stim["speaker"]
        for frame in range(stim['fixation_pre']):
            basic_stim["fixation_point"].draw() 
            reminder.draw()
            win.flip()
            
        basic_stim["fixation_point"].color = [1,1,1]
        basic_stim['grating'].ori = leading_ori  #updating leading grating ori
        leading_sound.play()
        for frame in range(stim['leading_frames']):       
            basic_stim["fixation_point"].draw()
            basic_stim['grating'].draw()
            reminder.draw()
            win.flip()
                
        for frame in range(stim['isi_frames']): 
            basic_stim["fixation_point"].draw()
            reminder.draw()
            win.flip()

        basic_stim['grating'].ori = trailing_ori  #updating trailing grating ori
        trailing_sound.play() 
        event.clearEvents() # Key presses are to be registered from here      
        for frame in range(stim['trailing_frames']):
            basic_stim['grating'].draw()
            basic_stim["fixation_point"].draw()
            reminder.draw()
            win.flip() 

        inst = visual.TextStim(win, pos = [0,0])
        inst.wrapWidth = 40
        inst.height = 1
        inst.text = "z = frecuente          espacio = débil          m = raro"
        inst.draw()
        win.flip()          
        allKeys = event.waitKeys(keyList = ["z", "m", "space"])        
        fix_color = [-1,1,-1] if allKeys[0]=='z' else [1,-1,-1]
        basic_stim["fixation_point"].color = fix_color



# Test phase training
def training_test(win, basic_stim, stim, monitor):

    for thisTrial in range(2):        
        leading_ori = np.random.choice([0, 90])
        trailing_ori = np.random.choice([45, 135])
        #leading_sound = Sound(np.random.choice([1000, 1300]), sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.2)
        leading_sound = Sound(1000, sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.2)
        trailing_freq = np.random.choice([100, 135])
        #trailing_sound = Sound(np.random.choice([100, 135]), sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.2)
        trailing_sound = Sound(100, sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.9)
        basic_stim['grating'].setOpacity(0.7)
        reminder = basic_stim["eye"] if thisTrial == 0 else basic_stim["speaker"]
        for frame in range(stim['fixation_pre']):
            basic_stim["fixation_point"].draw()
            reminder.draw()
            win.flip()
        
        basic_stim["fixation_point"].color = [1,1,1]
        basic_stim['grating'].ori = leading_ori  #updating leading grating ori
        leading_sound.play()
        for frame in range(stim['leading_frames']):       
            basic_stim["fixation_point"].draw()
            basic_stim['grating'].draw()
            reminder.draw()
            win.flip()
            
        for frame in range(stim['isi_frames']): 
            basic_stim["fixation_point"].draw()
            reminder.draw()
            win.flip()
        
        basic_stim['grating'].ori = trailing_ori  #updating trailing grating ori
        if thisTrial == 0: #First we will show a visual target
            basic_stim['grating'].ori += np.random.choice([20, -20])
            trailing_sound.play()
        else: # and then an auditory target
            trailing_sound = Sound(trailing_freq + np.random.choice([15, -15]), sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.9)    
            trailing_sound.play()
        event.clearEvents() # Key presses are to be registered from here                
        for frame in range(stim['trailing_frames']):                            
            basic_stim['grating'].draw()
            basic_stim["fixation_point"].draw() 
            reminder.draw()
            win.flip()  
            
        inst = visual.TextStim(win, pos = [0,0])
        inst.wrapWidth = 40
        inst.height = 1
        inst.text = "z = diferente         espacio = débil           m = normal"
        inst.draw()
        win.flip()          
        allKeys=event.waitKeys(keyList = ["z", "space", "m"])
        fix_color = [-1,1,-1] if allKeys[0]=='z' else [1,-1,-1]
        basic_stim["fixation_point"].color = fix_color

    
def test_starts(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Durante esta segunda fase van a ir apareciendo los mismos pares de estímulos que ya conoces. Pero ahora ya no te tienes que preocupar de si la pareja es correcta o no.\
                Tu tarea ahora será indicar si el segundo estímulo es ligeramente distinto a lo habitual: en el caso de los enrejados si la orientación está un poco desviada respecto a\
                los enrejados diagonales que has ido viendo hasta ahora; En el caso de los tonos, si lo percibes ligeramente más agudo o grave de lo habitual."
    nextt.text = "Pulsa espacio para continuar"
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])
    
    inst.text = "Igual que antes deberás atender a los visuales o a los auditivos, lo cuál se indicará mediante el recordatorio visual.\
                Ojo = responde a visuales  /  Altavoz = responde a auditivos. Sólo los estímulos a los que tengas que atender podrán aparecer distintos a lo habitual."    
    inst.draw()
    nextt.draw()
    win.flip()
    
    event.waitKeys( keyList=['space'])
    
    inst.text = "Igual que antes, si el estímulo es notablemente más débil tendrás que indicarlo en la pantalla de respuesta. Esta pantalla es similar a la fase anterior: aparecerá después de la presentación del segundo estímulo\
                y se te indicará qué botón corresponde a cada opción (diferente, débil o normal). Tras tu respuesta verás que el color del punto central también cambia.\
                Verde = respuesta correcta / Rojo = incorrecta. "
                
    nextt.text = "Pulsa espacio para realizar un par de ejemplos"    
    inst.draw()
    nextt.draw()
    win.flip()
    
    event.waitKeys( keyList=['space'])
    
def explicit_starts(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Esta fase final es similar a la primera, solo que mucho más corta. Aquí comprobaremos si recuerdas cuáles son las parejas de estímulos correctas. \
                Recuerda: tu objetivo es indicar si el par que acabas de percibir es frecuente o raro."
    nextt.text = "Pulsa espacio para continuar"
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])
    
    inst.text = "Ahora los estímulos visuales y auditivos no aparecerán simultáneamente, así que sencillamente responderás en función de la pareja que se presente. \
                Tampoco aparecerán estímulos débiles, así que solo deberás responder ""frecuente"" o ""raro""."
    nextt.text = "Pulsa espacio para realizar un par de ejemplos"
    inst.draw()
    nextt.draw()
    win.flip()
    
    event.waitKeys( keyList=['space'])
                
    
    
# BLOCK START MESSAGES

def learning_visual(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Aprende los pares visuales. En la pantalla de respuesta se te indicará con qué teclas responder. ¡Recuerda: fija la mirada en el punto central! "
    nextt.text = "Cuando estes listo/a, pulsa espacio para comenzar "
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])


def learning_auditory(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Aprende los pares auditivos. En la pantalla de respuesta se te indicará con qué teclas responder. ¡Recuerda: fija la mirada en el punto central! "
    nextt.text = "Cuando estes listo/a, pulsa espacio para comenzar "
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])

def test_visual(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Responde a los estímulos visuales. Coloca los dedos sobre botones de respuesta"
    nextt.text = "Cuando estes listo/a, pulsa espacio para comenzar "
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])

def test_auditory(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Responde a los estímulos auditivos. Coloca los dedos sobre botones de respuesta"
    nextt.text = "Cuando estes listo/a, pulsa espacio para comenzar "
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])

def show_accuracy(win, acc):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 1
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "En este bloque has acertado un " + acc + "% de las parejas"
    nextt.text = "Pulsa espacio para empezar el siguiente bloque "
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])

                

def end_exp(win):
# Instrucciones generales del experimento       
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    inst.text = "Has terminado el experimento. Gracias por tu participación. Avisa al investigador."         
    inst.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
