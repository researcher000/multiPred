# -*- coding: utf-8 -*-

from psychopy import visual, event, core
from psychopy.sound import Sound
import numpy as np


# Experiment instructions
def main_instructions_v(win, grating, fixation, eye, speaker):
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

def main_instructions_a(win, grating, fixation, eye, speaker):
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

# PHASE START MESSAGES
# Learning instructions
def learning_starts(win, grating, fixation, red):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    
    inst.text = "Durante esta primera fase solo tienes que fijar la mirada en el punto central de color blanco.\
                En ciertas ocasiones, el segundo estímulo se presentará con menor intensidad: \
                si el enrejado aparece con menor contraste, o el tono se escucha más flojo, deberás pulsar la barra espaciadora en la pantalla de respuesta."
    nextt.text = "Pulsa espacio para realizar unos cuantos ejemplos"
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

def learning_starts_a(win, grating, fixation, red):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Durante esta primera fase tendrás que aprender cuáles son las parejas auditivas correctas. Estas van a aparecer con mayor frecuencia que las demás.\
                Tras la presentación del segundo pitido, tu tarea consistirá en indicar si los dos pitidos que has percibido forman una pareja frecuente o infrecuente (según se indique en la pantalla de respuesta)."                 
    nextt.text = "Pulsa espacio para continuar"

    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])
    
    inst.text = "Lógicamente, al principio te costará distinguir qué pares de pitidos son los frecuentes y cuáles no. Pero a la larga ciertos pares te resultarán familiares y acertarás con mayor frecuencia.\
                Además, después de cada respuesta, el punto central cambiará de color: Verde = respuesta correcta / Rojo = incorrecta."
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    inst.text = "Por último, te pedimos que en todo momento fijes la mirada en el punto central de color blanco.\
                Esto es importante ya que en ciertas ocasiones, el segundo estímulo se presentará con menor intensidad: \
                si el enrejado aparece con menor contraste, o el tono se escucha más flojo, deberás indicarlo en la pantalla de respuesta, sin tener que responder a la pregunta de si el par de pitidos era frecuente o raro."
    nextt.text = "Pulsa espacio para realizar unos cuantos ejemplos"
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
def training_learn(win, basic_stim, stim, mod, trial_list, this_respmap):
    training_trials = np.hstack([np.random.choice(trial_list[:len(trial_list)-8], 6),np.random.choice(trial_list[-8:], 4)])
    np.random.shuffle(training_trials)
    basic_stim['grating'].contrast = 0.7
    fix_color = [1,1,1]
    for tr in range(10):
        basic_stim["fixation_point"].color = fix_color
        basic_stim['grating'].contrast = 0.7
        thisTrial = training_trials[tr]        
        leading_sound = Sound(thisTrial['a_leading'], sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.2) # Generating corresponding tones for the trails
        trailing_sound = Sound(thisTrial['a_trailing'], sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.9) # Lower tones need more volume to make them isophonic
        basic_stim['grating'].ori = thisTrial['v_leading']
        
        
        for frame in range(stim['fixation_pre']):
            basic_stim["fixation_point"].draw() 
            win.flip()
            
        basic_stim["fixation_point"].color = [1,1,1]
        basic_stim['grating'].ori = thisTrial['v_leading']  #updating leading grating ori
        leading_sound.play()
        for frame in range(stim['leading_frames']):       
            basic_stim["fixation_point"].draw()
            basic_stim['grating'].draw()
            win.flip()
                
        for frame in range(stim['isi_frames']): 
            basic_stim["fixation_point"].draw()
            win.flip()

        # CATCH
        if thisTrial['catch'] == 1: # Visual catch
            basic_stim["grating"].contrast = .3
        elif thisTrial['catch'] == 2: # Auditory catch 
            trailing_sound.volume = 0.05

        basic_stim['grating'].ori = thisTrial['v_trailing']  #updating trailing grating ori
        trailing_sound.play() 
        event.clearEvents() # Key presses are to be registered from here      
        for frame in range(stim['trailing_frames']):
            basic_stim['grating'].draw()
            basic_stim["fixation_point"].draw()
            win.flip() 
        
        inst = visual.TextStim(win, pos = [0,0])
        inst.wrapWidth = 40
        inst.height = 1
        
        inst.text = "espacio = débil          -> = normal"
    
        inst.draw()
        win.flip()          
        allKeys=event.waitKeys(keyList = ["right", "space"])
                    
        if allKeys[0]=='space':
            if thisTrial['catch'] == 1 or thisTrial['catch'] == 2:
                fix_color = [-1,1,-1]
            else:
                fix_color = [1,-1,-1]
                            
        else: 
            if thisTrial['catch'] == 0:
                fix_color = [-1,1,-1]
            else:
                fix_color = [1,-1,-1]



# Test phase training
def training_test(win, basic_stim, stim, mod, trial_list, this_respmap):
    basic_stim['grating'].contrast = 0.7
    fix_color = [1,1,1]
    np.random.shuffle(trial_list)
    for tr in range(10):  
        basic_stim["fixation_point"].color = fix_color
        thisTrial = trial_list[tr]        
        leading_sound = Sound(thisTrial['a_leading'], sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.2) # Generating corresponding tones for the trails
        trailing_sound = Sound(thisTrial['a_trailing'], sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.9) # Lower tones need more volume to make them isophonic
        basic_stim['grating'].setOpacity(0.7)
        for frame in range(stim['fixation_pre']):
            basic_stim["fixation_point"].draw()
            win.flip()
        
        basic_stim["fixation_point"].color = [1,1,1]
        basic_stim['grating'].ori = thisTrial['v_leading']  #updating leading grating ori
        leading_sound.play()
        for frame in range(stim['leading_frames']):       
            basic_stim["fixation_point"].draw()
            basic_stim['grating'].draw()
            win.flip()
            
        for frame in range(stim['isi_frames']): 
            basic_stim["fixation_point"].draw()
            win.flip()
        
        if thisTrial['target'] == 1: 
            if mod == 0: 
                basic_stim['grating'].ori = thisTrial['v_trailing'] + 25 * np.random.choice([1,-1])
                
            else:
                trailing_sound = Sound(thisTrial['a_trailing'] + 15 * np.random.choice([1,-1]), sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.9)
                basic_stim['grating'].ori = thisTrial['v_trailing'] # Also update grating ori
        else: # STANDARD TRIAL
            basic_stim['grating'].ori = thisTrial['v_trailing'] # Simply set ori to standard and don't change trailing sound                      
                              

        event.clearEvents() # Key presses are to be registered from here   
        for frame in range(stim['trailing_frames']):  
            if frame == 0: trailing_sound.play() #Start playing tone on first frame
            basic_stim['grating'].draw()
            basic_stim["fixation_point"].draw() 
            win.flip()  
                
        inst = visual.TextStim(win, pos = [0,0])
        inst.wrapWidth = 40
        inst.height = 1
        

        
        if this_respmap == 0: inst.text = "z = diferente          espacio = débil          m = normal"
        else: inst.text = "z = normal         espacio = débil        m = diferente"
        inst.draw()
        win.flip()          
        allKeys=event.waitKeys(keyList = ["z", "m", "space"])
        
        
        if this_respmap == 0: 
    
            if allKeys[0]=='z': 
                if thisTrial['target'] == 1:
                    fix_color = [-1,1,-1]
                else:
                    fix_color = [1,-1,-1]
                    
            elif allKeys[0]=='space':
                    fix_color = [1,-1,-1]
                            
            else: 
                if thisTrial['target'] == 0:
                    fix_color = [-1,1,-1]
                else:
                    fix_color = [1,-1,-1]
                
        else:    
            if allKeys[0]=='z': 
                if thisTrial['target'] == 0:
                    fix_color = [-1,1,-1]
                else:
                    fix_color = [1,-1,-1]
                    
            elif allKeys[0]=='space':
                    fix_color = [1,-1,-1]
                    
            else: 
                if thisTrial['target'] == 1:
                    fix_color = [-1,1,-1]
                else:
                    fix_color = [1,-1,-1]

    
def test_starts_v(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Durante esta segunda fase van a ir apareciendo los mismos pares de enrejados que ya conoces. Pero ahora ya no te tienes que preocupar de si la pareja es correcta o no.\
                Tu tarea ahora será indicar si el segundo estímulo es ligeramente distinto a lo habitual, concretamente si la orientación del segundo enrejado está un poco desviada respecto a\
                los enrejados diagonales que has ido viendo hasta ahora."
    nextt.text = "Pulsa espacio para continuar"
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

def test_starts_a(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Durante esta segunda fase van a ir apareciendo los mismos pares de pitidos que ya conoces. Pero ahora ya no te tienes que preocupar de si la pareja es correcta o no.\
                Tu tarea ahora será indicar si el segundo estímulo es ligeramente distinto a lo habitual, concretamente si el segundo tono es ligeramente más grave o agudo\
                los que has ido escuchando hasta ahora."
    nextt.text = "Pulsa espacio para continuar"
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
    inst.text = "Esta fase final es mucho más corta que las dos anteriores. Aquí comprobaremos si te has dado cuenta de que algunas transiciones eran más frecuentes que otras. \
                Aunque no estés del todo segur@, intenta responder de forma intuitiva si el par es frecuente o infrecuente."
    nextt.text = "Pulsa espacio para continuar"
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])
    
    inst.text = "Ahora solo vas a ver los enrejados, sin escuchar los pitidos, o al revés: escucharás los pitidos sin ver los enrjados. \
                Tampoco aparecerán estímulos débiles, así que solo deberás responder ""frecuente"" o ""raro""."
    nextt.text = "Pulsa espacio para empezar"
    inst.draw()
    nextt.draw()
    win.flip()
    
    event.waitKeys( keyList=['space'])
                

    

# BLOCK START MESSAGES

def learning_block(win):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 25
    inst.height = 0.9
    nextt = visual.TextStim(win, pos = [0,-6])
    nextt.height = 0.7
    nextt.color = "black"
    inst.text = "Detecta los estímulos débiles. En la pantalla de respuesta se te indicará con qué teclas responder. ¡Recuerda: fija la mirada en el punto central! "
    nextt.text = "Cuando estes listo/a, pulsa espacio para comenzar "
    inst.draw()
    nextt.draw()
    win.flip()
    event.waitKeys( keyList=['space'])

# def learning_visual(win):
#     inst = visual.TextStim(win, pos = [0,0])
#     inst.wrapWidth = 25
#     inst.height = 0.9
#     nextt = visual.TextStim(win, pos = [0,-6])
#     nextt.height = 0.7
#     nextt.color = "black"
#     inst.text = "Aprende los pares visuales. En la pantalla de respuesta se te indicará con qué teclas responder. ¡Recuerda: fija la mirada en el punto central! "
#     nextt.text = "Cuando estes listo/a, pulsa espacio para comenzar "
#     inst.draw()
#     nextt.draw()
#     win.flip()
#     event.waitKeys( keyList=['space'])


# def learning_auditory(win):
#     inst = visual.TextStim(win, pos = [0,0])
#     inst.wrapWidth = 25
#     inst.height = 0.9
#     nextt = visual.TextStim(win, pos = [0,-6])
#     nextt.height = 0.7
#     nextt.color = "black"
#     inst.text = "Aprende los pares auditivos. En la pantalla de respuesta se te indicará con qué teclas responder. ¡Recuerda: fija la mirada en el punto central! "
#     nextt.text = "Cuando estes listo/a, pulsa espacio para comenzar "
#     inst.draw()
#     nextt.draw()
#     win.flip()
#     event.waitKeys( keyList=['space'])

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
    
