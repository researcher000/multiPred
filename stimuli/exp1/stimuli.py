# -*- coding: utf-8 -*-

from psychopy import visual, monitors
import numpy as np

#========================== MONITORS and WINDOW ===============================

def monitor_def():
    # lets define the monitor if necessary in a dictionary (you can define other monitors def2, def3)
    monitor_def1 = {}
    monitor_def1['monitor_name'] = 'casa' # monitor to use (make sure to define monitors in exp_monitors center.
    monitor_def1['monitor_pixels']  = (1920, 1080)
    monitor_def1['monitor_width'] = 54
    monitor_def1['distance2monitor'] = 50
    monitor_def1['Hz'] = 60
    
    monitor_def2 = {}
    monitor_def2['monitor_name'] = 'cova' # monitor to use (make sure to define monitors in exp_monitors center.
    monitor_def2['monitor_pixels']  = (1366, 768)
    monitor_def2['monitor_width'] = 54#41
    monitor_def2['distance2monitor'] = 50#23
    monitor_def2['Hz'] = 60
    
    monitor_def3 = {}
    monitor_def3['monitor_name'] = 'multiple' # monitor to use (make sure to define monitors in exp_monitors center.
    monitor_def3['monitor_pixels']  = (1920, 1080)
    monitor_def3['monitor_width'] = 54
    monitor_def3['distance2monitor'] = 50
    monitor_def3['Hz'] = 144
    
    monitors = [monitor_def1, monitor_def2, monitor_def3]
    return monitors

def define_monitor(monitor):
    # Lets define the monitor characteristics
    screen = monitors.Monitor(name=monitor['monitor_name'] )
    screen.setSizePix(monitor['monitor_pixels'])
    screen.setWidth(monitor['monitor_width'] )
    screen.setDistance(monitor['distance2monitor'])
    screen.save()
    #monitors.getAllMonitors()
    print("The monitor " + screen.name  + " has "  + str(screen.getSizePix()) + " pixels, a width of " + str(monitor['monitor_width']) + " cm and subjects seat at " + str(monitor['distance2monitor']) + " cm"   )
    return screen

#================================ STIMULI =====================================

def shuffle_list(some_list):
    # Shuffle without replacement. NOT USED
    randomized_list = some_list.copy()
    while True:
        np.random.shuffle(randomized_list)        
        for i in range(len(some_list)):
            if some_list[i] == randomized_list[i]:
                break            
        else: break
    return randomized_list


def stim_config(ifi, nstim):
    # Experiment timings design
    stim = {}    
    stim['fixation_pre'] = round(1000/ifi)
    stim['leading_frames'] = round(500/ifi) 
    stim['isi_frames'] = round(500/ifi) 
    stim['trailing_frames'] = round(500/ifi)

         
    # Stimuli parameters
    stim['size_stim'] = 20
    stim['grating_contrast'] = 0.7
    stim['SF'] = 0.7

    return stim


def draw_basic(win, stim): # creates a dictionary with basic stimulus features    
    # Fixation point
    basic_stim = {}
    basic_stim['fixation_point'] =  visual.PatchStim(win, color= [1, 1, 1], tex=None,mask='circle', size=0.3, units = "deg")
    basic_stim['fixation_red'] =  visual.PatchStim(win, color= "red", tex=None,mask='circle', size=0.3, units = "deg")
    basic_stim['fixation_instr'] =  visual.PatchStim(win, color= [1, 1, 1], pos=[0,8], tex=None,mask='circle', size=0.3, units = "deg")

          
    # Grating stim
    basic_stim['grating'] = visual.GratingStim(win=win, mask="raisedCos" , size=stim['size_stim'], opacity=0.7, pos=[0,0], sf=stim['SF'],
                                 units = "deg", contrast = stim['grating_contrast'], maskParams = {'sd': 3} ) # , color = [1,0,1]
    basic_stim['grating_instr'] = visual.GratingStim(win=win, mask="raisedCos" , size=10, opacity=0.7, pos=[0,8], sf=stim['SF'],
                                 units = "deg", contrast = stim['grating_contrast'], maskParams = {'sd': 3}) # , color = [1,0,1]
    
    # Reminders
    basic_stim['eye'] = visual.ImageStim(win , "img/eye.png", pos=[-5,7], size=[7,5])
    basic_stim['speaker'] = visual.ImageStim(win , "img/speaker.png", pos=[5,7], size=[5,5])
    basic_stim['speaker_cross'] = visual.ImageStim(win , "img/speakercross.png", pos=[5,7], size=[5,5])

    return basic_stim



    
