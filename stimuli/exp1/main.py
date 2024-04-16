# -*- coding: utf-8 -*-
  
from psychopy import visual, core, event, data, prefs #import some libraries from PsychoPy
import pandas as pd

import numpy as np

import conditions as cond # creating conditions
import stimuli as st # monitor and constant stimulus features
import instructions as instr # Instructions for each phase
import responses as rsp # Functions for gathering participant info, responses and RTs

# setting PTB as preferred sound lib
prefs.hardware['audioLib']=['pyo'] 
from psychopy.sound import Sound

subject_info = rsp.subject_info()
filepath = "behav_analyses/data/" + subject_info["Nombre"] + ".csv"
#============================= SETTING MONITOR ================================
# choosing monitor
monitor = st.monitor_def()[0]
mon = st.define_monitor(monitor) # select the correct monitor 

# Creating the window
win = visual.Window(size = mon.getSizePix(), monitor = mon , units="deg", screen=0, fullscr=True)
win.mouseVisible = False
ifi = 1000/monitor['Hz']
#=========================== Some general presets =============================

event.globalKeys.clear() # implementing a global event to quit the program at any time by pressing ctrl+q
event.globalKeys.add(key='q', modifiers=['ctrl'], func= win.close)

timer = core.Clock() # Multi-purpose clock
RT = None # Without this, if first trial is catch and participant doesn't respond in time,
          # the experiment will crash when trying to save variable RT          
#============================== DESIGN PRESETS ================================
#Blocks
learning_n = 1 #per modality, so it's x2
test_n = 1 # 5x2 
mod_map = [0,1] 
np.random.shuffle(mod_map) # Random starting modality
blocks_learning = np.concatenate([mod_map] * learning_n)  # 0 = VISUAL / 1 AUDITORY // Alternate them
blocks_test = np.concatenate([mod_map] * test_n) # Same but for test phase
blocks_explicit = mod_map

# Item type counts (for pair generation)
n_items = 4 # number of different items
n_leading = 2 # Number of leading items
n_trailing = 2 # Number of trailing items

# Pair type frequencies
nEXP_learn = 12
nVP_learn = 4
nEXP_test = 24 # n of presentations of expected pairs
nVP_test = 8 # violations

# Loading constant stimuli information
stim = st.stim_config(ifi, n_items)
basic_stim = st.draw_basic(win, stim) 

# Creating stimuli pairs
v_leading = [0,90]
v_trailing = [45,135]
a_leading = [1000,1600]
a_trailing = [100,160]
np.random.shuffle(v_leading)
np.random.shuffle(a_leading)

vpairs_learn = cond.stimlist_reduced(v_leading, v_trailing, "v", nEXP_learn, nVP_learn, n_leading) # visual modality
apairs_learn = cond.stimlist_reduced(a_leading, a_trailing, "a", nEXP_learn, nVP_learn, n_leading) # auditory modality

vpairs_test = cond.stimlist_reduced(v_leading, v_trailing, "v", nEXP_test, nVP_test, n_leading) # visual modality
apairs_test = cond.stimlist_reduced(a_leading, a_trailing, "a", nEXP_test, nVP_test, n_leading) # auditory modality


# Random response mapping for each participant
resp_map = np.random.choice([0,1]) # if 0 z = familiar & m = unfamiliar

# Initial values for each separate adaptive staircase 
# Visual 
v_diff = 20; v_hist = 1; v_inv = 0; v_lastdir = "down"
vstep = [6, 4, 2, 1]
vstep_update = [2, 4, 8] 
# Auditory 
a_diff = 20; a_hist = 1; a_inv = 0; a_lastdir = "down"
astep = [6, 4, 2, 1]
astep_update = [2, 4, 8] 

diff = None # Not updated until test phase. 
#========================== EXPERIMENT STARTS =================================

instr.main_instructions(win, basic_stim['grating_instr'], basic_stim['fixation_instr'], basic_stim['eye'], basic_stim['speaker_cross'])   

header = ['id', 'age', 'gender', 'hand', 'phase', 'block', 'modality', 'ntrial', 'v_pred', 'v_leading', 'v_trailing', 'a_pred', 'a_leading', 'a_trailing', 'catch', 'target', 'resp', 'RT', 'correct', 'diff']   # saving conditions here

basic_stim['eye'].setPos([0,-12]) # Resetting position of visual reminders before starting experiment
basic_stim['speaker'].setPos([0,-12]) # Different placement than during instructions

for phase in [0,1,2]:
    if phase == 0: 
        # Creating trials list (block)
        trial_list = cond.rand_conditions(vpairs_learn, apairs_learn, nEXP_learn, nVP_learn, phase) 
        # Initializing corresponding phase instructions
        instr.learning_starts(win, basic_stim['grating'], basic_stim['fixation_point'], basic_stim['fixation_red']) # Learning phase instr
        instr.training_learn(win, basic_stim, stim) # 2 training trials 
        blocks = blocks_learning # Assigning number of blocks desired for each phase to variable "blocks" 
        
    elif phase == 1: 
        # Creating trials list (block)
        trial_list = cond.rand_conditions(vpairs_test, apairs_test, nEXP_test, nVP_test, phase) 
        # Initializing corresponding phase instructions
        instr.test_starts(win)
        instr.training_test(win, basic_stim, stim, monitor) # 2 training trials
        blocks = blocks_test
    
    else: # Explicit test phase
        # Creating trials list (block)
        vpairs_explicit, apairs_explicit = cond.explicit_test_trials(vpairs_learn, apairs_learn)
        # Initializing corresponding phase instructions
        instr.explicit_starts(win)
        blocks = blocks_explicit
        diff = None
        
    block_n = 0 # counter to keep track of blocks within phase
    for thisBlock in blocks:  #thisBlock == 0 VISUAL / thisBlock == 1 AUDITORY
        vars_stored = [] #for pandas
        # Tracking block's modality
        thisMod = "visual" if thisBlock == 0 else 'auditory'
        basic_stim["fixation_point"].color = [1,1,1] # Just to clean feedback color from a previous test block
        reminder = basic_stim["eye"] if thisMod == "visual" else basic_stim["speaker"]   # Reminder: symbol of an eye or a speaker to appear on screen during trials,            
                                                                                         # So that participant doesn't forget which is the attended modality         
        if phase == 2:
            if thisMod == "visual": trial_list = vpairs_explicit
            else: trial_list = apairs_explicit
            
        # Randomizing order of conditions
        np.random.shuffle(trial_list) 
        trials = data.TrialHandler(trial_list, 1, method='random') # Random method here doesn't randomize our trials, 
                                                                     # as each entry counts as a separate condition which appears just once   
        
        # Instructions for this block            
        if phase == 0:
            instr.learning_visual(win) if thisMod == "visual" else instr.learning_auditory(win)
        else: # Same for test and explicit phase
            instr.test_visual(win) if thisMod == "visual" else instr.test_auditory(win)

#============================== TRIAL STARTS ==================================
       
        for thisTrial in trials:        
            thisResp = None
            basic_stim['grating'].contrast = stim['grating_contrast'] # Restore after catch
            
            if "a_expect" in thisTrial: # Visual block in explicit phase doesn't contain this key
                leading_sound = Sound(thisTrial['a_leading'], sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.2) # Generating corresponding tones for the trails
                trailing_sound = Sound(thisTrial['a_trailing'], sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.9) # Lower tones need more volume to make them isophonic
            
            SOA_frames = int(np.round(np.random.uniform(750, 1500)/ifi)) # add random jitter to itner-trial interval
            for frame in range(SOA_frames): # inter-trial interval
                basic_stim["fixation_point"].draw() 
                reminder.draw()
                win.flip()
            
            basic_stim["fixation_point"].color = [1,1,1] # Restore to white after test phase feedback
            if "v_expect" in thisTrial: basic_stim['grating'].ori = thisTrial['v_leading']  # updating leading grating ori
            #leading_sound.play() 
            for frame in range(stim['leading_frames']): # Leading stimulus presentation
                if frame == 0 and "a_expect" in thisTrial: leading_sound.play() #Start playing tone on first frame
                basic_stim["fixation_point"].draw()
                if "v_expect" in thisTrial: basic_stim['grating'].draw()
                reminder.draw()
                win.flip()
                
            for frame in range(stim['isi_frames']):  # Inter stimulus interval
                basic_stim["fixation_point"].draw()
                reminder.draw()
                win.flip()

#=============================== LEARNING ===================================== 
            if phase == 0:          
                basic_stim['grating'].ori = thisTrial['v_trailing']  #updating trailing grating ori
                
                # CATCH
                if thisTrial['catch'] == 1: # Visual catch
                    basic_stim["grating"].contrast = .3
                elif thisTrial['catch'] == 2: # Auditory catch 
                    trailing_sound.volume = 0.05
                 
                event.clearEvents() # Key presses are to be registered from here      
                for frame in range(stim['trailing_frames']): # Trailing stimulus presentation
                    if frame == 0: trailing_sound.play() #Start playing tone on first frame
                    basic_stim['grating'].draw()
                    basic_stim["fixation_point"].draw()
                    reminder.draw()
                    win.flip() 

                timer.reset(0) # Reset timer when response screen is presented
                while thisResp == None:
                    thisResp, fix_color, outcome = rsp.learning_Response(win, thisTrial, resp_map, thisMod) 
                RT = timer.getTime() # And get RT when a response is given
                basic_stim["fixation_point"].color = fix_color # Update feedback color
                     
 #=============================== TESTING =====================================             
            elif phase == 1: # phase 1     
                if thisTrial['target'] == 1: 
                    if thisMod == "visual": # If target, manipulate stim according to staircase value
                        basic_stim['grating'].ori = thisTrial['v_trailing'] + v_diff * np.random.choice([1,-1])
                        diff = v_diff
                    else:
                        trailing_sound = Sound(thisTrial['a_trailing'] + a_diff * np.random.choice([1,-1]), sampleRate=44100, secs=0.5, stereo=True ,loops=0, volume=0.9)
                        diff = a_diff
                        basic_stim['grating'].ori = thisTrial['v_trailing'] # Also update grating ori
                else: # STANDARD TRIAL
                    basic_stim['grating'].ori = thisTrial['v_trailing'] # Simply set ori to standard and don't change trailing sound                      
                              
                # CATCH    
                if thisTrial['catch'] == 1: # Visual catch
                    basic_stim["grating"].contrast = .3
                elif thisTrial['catch'] == 2: # Auditory catch 
                    trailing_sound.volume = 0.05 
                
                event.clearEvents() # Key presses are to be registered from here   
                for frame in range(stim['trailing_frames']):  
                    if frame == 0: trailing_sound.play() #Start playing tone on first frame
                    basic_stim['grating'].draw()
                    basic_stim["fixation_point"].draw() 
                    reminder.draw()
                    win.flip()  
                                                        
                timer.reset(0) # Reset timer when response screen is presented
                while thisResp == None:
                    thisResp, fix_color, outcome = rsp.test_feedback(win, thisTrial, resp_map) 
                basic_stim["fixation_point"].color = fix_color
                RT = timer.getTime() # And get RT when a response is given
                
                # UPDATING STAIRCASES
                if thisTrial['target'] == 1:
                    if thisMod == 'visual': # Update visual staircase
                        if thisTrial["v_expect"] == "EXP": # Only updating in target, attended-expect trials                 
                            v_last = outcome
                            v_diff, v_hist, v_lastdir, v_inv = rsp.staircase_test(v_last, v_diff, 2, v_hist, v_lastdir, v_inv, vstep, vstep_update)
    
                    else: # Update auditory staircase
                        if thisTrial["a_expect"] == "EXP":
                            a_last = outcome
                            a_diff, a_hist, a_lastdir, a_inv = rsp.staircase_test(a_last, a_diff, 3, a_hist, a_lastdir, a_inv, astep, astep_update)
                else: 
                    if thisMod == 'visual': 
                        diff = v_diff #Save last stc value of this modality
                    else: 
                        diff = a_diff
                        
 #=============================== EXPLICIT =====================================             
            else:  
                if "v_expect" in thisTrial: basic_stim['grating'].ori = thisTrial['v_trailing']  #updating trailing grating ori
                    
                event.clearEvents() # Key presses are to be registered from here      
                for frame in range(stim['trailing_frames']): # Trailing stimulus presentation
                    if frame == 0 and "a_expect" in thisTrial: trailing_sound.play() #Start playing tone on first frame
                    if "v_expect" in thisTrial: basic_stim['grating'].draw()
                    basic_stim["fixation_point"].draw()
                    reminder.draw()
                    win.flip() 

                timer.reset(0) # Reset timer when response screen is presented
                while thisResp == None:
                    thisResp, outcome = rsp.expl_Response(win, thisTrial, resp_map, thisMod) 
                RT = timer.getTime() # And get RT when a response is given     
                if "v_expect" in thisTrial:
                    thisTrial["a_expect"] = None; thisTrial["a_leading"] = None; thisTrial["a_trailing"] = None; thisTrial["catch"] = None; thisTrial["target"] = None;
                else:
                    thisTrial["v_expect"] = None; thisTrial["v_leading"] = None; thisTrial["v_trailing"] = None; thisTrial["catch"] = None; thisTrial["target"] = None;
                    
###############################################################################
                
            # After each trial append variables to this list
            vars_stored.append([subject_info["Nombre"], subject_info["Edad"], subject_info["Género"], subject_info["Mano dominante"], phase, block_n, thisMod, trials.thisN,
                                thisTrial['v_expect'],thisTrial['v_leading'],thisTrial['v_trailing'],thisTrial['a_expect'],thisTrial['a_leading'],thisTrial['a_trailing'], thisTrial['catch'], thisTrial['target'], thisResp, RT, outcome, diff])# saving conditions here


#======================== SHOW LEARNING BLOCK ACCURACY =========================                               
        block_n += 1 # Updating block count at the end of each block
        if phase == 0: # At the end of learning blocks, calculate accucaracy to show on screen
            block_results = vars_stored[-len(trial_list):] # Slicing trials pertaining to this block
            block_df = pd.DataFrame(block_results, columns = header) # df them
            this_accuracy = rsp.block_accuracy(block_df, thisMod)
            instr.show_accuracy(win, this_accuracy)
        
        rsp.save_csv(vars_stored, filepath, header) #Update output file with each block results
        
#============================= EXPERIMENT ENDS ================================            

instr.end_exp(win)
        
win.close()
core.quit()
