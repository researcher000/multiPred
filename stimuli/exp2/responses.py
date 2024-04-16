# -*- coding: utf-8 -*-

from psychopy import visual, event, gui
import os
import pandas as pd


def subject_info(): # loading staircase subject data
    
    info = {'Nombre':'', 
            'Edad': '', 
            'Mano dominante': ['izquierda', 'derecha'],
            'Género': ['Mujer', 'Hombre', 'Otro']}
    
    dictDlg = gui.DlgFromDict(dictionary=info,
            title='TestExperiment', fixed=['ExpVersion'])
    if dictDlg.OK:
        print(info)
    else:
        print('User Cancelled')
    
    return info
    
    
def learning_Response(win, thisTrial, this_respmap, modality):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 40
    inst.height = 1
        
    inst.text = "espacio = débil          -> = normal"
    
    inst.draw()
    win.flip()          
    allKeys=event.waitKeys(keyList = ["right", "space"])
                    
    if allKeys[0]=='space':
        thisResp = "catch"
        if thisTrial['catch'] == 1 or thisTrial['catch'] == 2:
            outcome = 1
            fix_color = [-1,1,-1]
        else:
            outcome = 0
            fix_color = [1,-1,-1]
                        
    else: 
        thisResp = "normal"
        if thisTrial['catch'] == 0:
            outcome = 1
            fix_color = [-1,1,-1]
        else:
            outcome = 0
            fix_color = [1,-1,-1]
                            
    return thisResp, fix_color, outcome




def test_feedback(win, thisTrial, this_respmap):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 40
    inst.height = 1
    if this_respmap == 0: inst.text = "z = diferente         espacio = débil           m = normal"
    else: inst.text = "z = normal        espacio = débil         m = diferente"
    inst.draw()
    win.flip()          
    allKeys=event.waitKeys(keyList = ["z", "m", "space"])
    if this_respmap == 0: 

        if allKeys[0]=='z': 
            thisResp = "diferente"
            if thisTrial['target'] == 1 and thisTrial['catch'] == 0:
                outcome = 1
                fix_color = [-1,1,-1]
            else:
                outcome = 0
                fix_color = [1,-1,-1]
                
        elif allKeys[0]=='space':
            thisResp = "catch"
            if thisTrial['catch'] == 1 or thisTrial['catch'] == 2:
                outcome = 1
                fix_color = [-1,1,-1]
            else:
                outcome = 0
                fix_color = [1,-1,-1]
                        
        else: 
            thisResp = "normal"
            if thisTrial['target'] == 0 and thisTrial['catch'] == 0:
                outcome = 1
                fix_color = [-1,1,-1]
            else:
                outcome = 0
                fix_color = [1,-1,-1]
            
    else:

        if allKeys[0]=='z': 
            thisResp = "normal"
            if thisTrial['target'] == 0 and thisTrial['catch'] == 0:
                outcome = 1
                fix_color = [-1,1,-1]
            else:
                outcome = 0
                fix_color = [1,-1,-1]
                
        elif allKeys[0]=='space':
            thisResp = "catch"
            if thisTrial['catch'] == 1 or thisTrial['catch'] == 2:
                outcome = 1
                fix_color = [-1,1,-1]
            else:
                outcome = 0
                fix_color = [1,-1,-1]
                
        else: 
            thisResp = "diferente"
            if thisTrial['target'] == 1 and thisTrial['catch'] == 0:
                outcome = 1
                fix_color = [-1,1,-1]
            else:
                outcome = 0
                fix_color = [1,-1,-1]
 
    return thisResp, fix_color, outcome


def expl_Response(win, thisTrial, this_respmap, modality):
    inst = visual.TextStim(win, pos = [0,0])
    inst.wrapWidth = 40
    inst.height = 1
    
    if modality == "visual": expect = thisTrial["v_expect"]
    else: expect = thisTrial["a_expect"]
    
    if this_respmap == 0: inst.text = "z = frecuente                 m = raro"
    else: inst.text = "z = raro              m = frecuente"
    inst.draw()
    win.flip()          
    allKeys=event.waitKeys(keyList = ["z", "m"])
    
    
    if this_respmap == 0: 

        if allKeys[0]=='z': 
            thisResp = "frecuente"
            if expect == "EXP":
                outcome = 1
            else:
                outcome = 0    
                        
        else: 
            thisResp = "raro"
            if expect == "VP":
                outcome = 1
            else:
                outcome = 0
            
    else:
        if allKeys[0]=='z': 
            thisResp = "raro"
            if expect == "VP":
                outcome = 1
            else:
                outcome = 0            
                
        else: 
            thisResp = "frecuente"
            if expect == "EXP":
                outcome = 1
            else:
                outcome = 0
                
    return thisResp, outcome


def block_accuracy(df, modality):
    if modality == "visual":
        hits = len(df[(df.iloc[:,8] == "EXP") & (df.iloc[:,16] == "frecuente")]) + len(df[(df.iloc[:,8] == "VP") & (df.iloc[:,16] == "raro")]) + len(df[(df.iloc[:,14] == 1) & (df.iloc[:,16] == "catch")])
               #len(df[(df.iloc[:,8] == "N") & (df.iloc[:,15] == "unfamiliar")]) + \
    else:
        hits = len(df[(df.iloc[:,11] == "EXP") & (df.iloc[:,16] == "frecuente")]) + len(df[(df.iloc[:,11] == "VP") & (df.iloc[:,16] == "raro")]) + len(df[(df.iloc[:,14] == 1) & (df.iloc[:,16] == "catch")])
               #len(df[(df.iloc[:,11] == "N") & (df.iloc[:,15] == "unfamiliar")]) + \
                                 
    accuracy = str(round(((hits / len(df)) * 100), 2))    
    
    return accuracy



def staircase_test(last_outcome, diff, stepsize, history, last_dir, n_inv, step, step_update):
    #diff = how much target stimuli deviate from standard
    #stepsize = by how much diff has to increase or decrease
    #history = outcome of last trial. 0: incorrect / 1: n-1 correct / 2: n-1,n-2 correct and so on
    if n_inv < step_update[0]: stepsize = step[0]
    elif n_inv >=step_update[0] and n_inv < step_update[1]: stepsize = step[1]
    elif n_inv >= step_update[1] and n_inv < step_update[2]: stepsize = step[2]
    else: stepsize = step[3]
        
    if last_outcome == 0: 
        if diff + stepsize <= 20: 
            diff += stepsize #If last target was incorrect increase diff
            history = 0
            if last_dir == "down": n_inv += 1
            last_dir = "up"
        else:
            diff = diff
    else:
        history += 1
        if history == 3:
            history = 0 # If 3 consecutive correct response restart count
            diff -= stepsize # and drecrease diff
            if last_dir == "up": n_inv += 1 
            last_dir = "down"
        else: # history == 1 or 2
            history = history  
            diff = diff #remains the same
            last_dir = last_dir
        
    return diff, history, last_dir, n_inv

    
def save_csv(results, filepath, header):
    if not os.path.isfile(filepath):
        df = pd.DataFrame(results, columns=header)
        df.to_csv(filepath, index = False)
    else:
        df = pd.DataFrame(results)
        df.to_csv(filepath, mode='a', header=False, index = False)
