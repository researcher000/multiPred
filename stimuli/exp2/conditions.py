# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd


def stimlist_reduced(leading, trailing, modality, nEXP, nVP, n_leading):
            
    pairs = np.ones([n_leading, n_leading]) * nVP # This is a square matrix which size alway equals n_trailing
    np.fill_diagonal(pairs, nEXP) # Filling diagonal with frequency of expected pairs
    trans_mat = pairs.astype(int)

    stimList = []
    for i in range(trans_mat.shape[0]): # Iter rows
        for j in range(trans_mat.shape[1]): # Iter cols
            if modality == "v": # Different key names for each modality
                for x in range(trans_mat[i,j]): # Append a number of elements defined by values in trans_mat
    
                    if trans_mat[i,j] == nEXP:
                        stimList.append({"v_leading":leading[i], "v_trailing":trailing[j], "v_expect": "EXP"})
                    else:
                        stimList.append({"v_leading":leading[i], "v_trailing":trailing[j], "v_expect": "VP"})
            else:
                for x in range(trans_mat[i,j]):     
                    if trans_mat[i,j] == nEXP:
                        stimList.append({"a_leading":leading[i], "a_trailing":trailing[j], "a_expect": "EXP"})
                    else:
                        stimList.append({"a_leading":leading[i], "a_trailing":trailing[j], "a_expect": "VP"})
                                        
    return stimList   
        

# def rand_conditions_pre(vpairs, apairs, nEXP): # This is for no expectations 
#     ntrials = len(vpairs)
#     #Reordering apairs
#     apairs_re = np.repeat([apairs[0],apairs[nEXP],apairs[nEXP*2], apairs[nEXP*3]]*4,2)
    
#     a_v = []
#     for d in range(ntrials):
#         a_v.append({**vpairs[d], **apairs_re[d]})
#     np.random.shuffle(a_v)
    
#     #Creating catch entry
#     catch_types = [{"catch":0}, {"catch":1}, {"catch":2}]
#     catch_list = np.hstack([[catch_types[0]]*12, [catch_types[1]]*10, [catch_types[2]]*10])
#     np.random.shuffle(catch_list)
    
#     targets = []
#     for i in range(ntrials): targets.append({"target":0})
    
#     out = []
#     for d in range(ntrials):
#         out.append({**a_v[d], **catch_list[d], **targets[d]})
    
#     return out

def rand_conditions(vpairs, apairs, nEXP, nVP, phase):
    #Slicing 4 possible combinations of vpairs
    ntrials = len(vpairs)
    partExp = round((nEXP - nVP/2)/2)
    partVP = round(nVP/4)
    Ve1 = vpairs[0: nEXP]
    Vu1 = vpairs[nEXP:nEXP+nVP]
    Vu2 = vpairs[nEXP+nVP:nEXP+nVP*2]
    Ve2 = vpairs[-nEXP:]

    #Reordering
    newvpairs = Ve1[0:partExp] + Ve2[0:partExp] + Vu1[0:partVP] + Vu2[0:partVP] #AE1
    newvpairs += Ve1[0:partVP] + Ve2[0:partVP] + Vu1[0:partVP] + Vu2[0:partVP] #AU1
    newvpairs += Ve1[0:partVP] + Ve2[0:partVP] + Vu1[0:partVP] + Vu2[0:partVP] #AU2
    newvpairs += Ve1[0:partExp] + Ve2[0:partExp] + Vu1[0:partVP] + Vu2[0:partVP] #AE2
    
    #Creating catch entry
    nocatch = []
    for i in range(ntrials): nocatch.append({"catch":0})
    
    #Allocating targets (50% target therefore allocate in 50% of trials from each cond)
    if phase == 0:
        target_inds = np.zeros(ntrials)
    else:
        Congruent_cond = np.hstack([np.ones(int(np.ceil(partExp/4))), np.zeros(int(np.floor(partExp*(3/4))))])
        V_cond = np.hstack([np.zeros(round(partVP/2)), np.ones(round(partVP/2))])
        target_inds = np.hstack([np.hstack([Congruent_cond]*2), np.hstack([V_cond]*10), np.hstack([Congruent_cond]*2), np.hstack([V_cond]*2)])
    
    target_trials = []
    for i in range(ntrials):
        target_trials.append({"target":int(target_inds[i])})    
    
    out = []
    for d in range(ntrials):
        out.append({**apairs[d], **newvpairs[d], **nocatch[d], **target_trials[d]})
        
    # Generating catch trials
    a1v1 = out[0].copy()
    a1v1["target"] = 0
    a1v2 = out[partExp].copy()
    a1v2["target"] = 0
    a2v1 = out[ntrials-(partVP*2 + 1)].copy()
    a2v1["target"] = 0
    a2v2 = out[ntrials-(partVP*2 + 1 + partExp)].copy()
    a2v2["target"] = 0
    
    aud1, aud2, aud3, aud4 = a1v1.copy(),a1v2.copy(),a2v1.copy(),a2v2.copy()
    catch_visual = list((a1v1,a1v2,a2v1,a2v2))
    catch_auditory = list((aud1, aud2, aud3, aud4))
    for dic in catch_visual: dic["catch"] = 1
    for dic in catch_auditory: dic["catch"] = 2
        
    output = out + catch_visual + catch_auditory
    
    return output

def explicit_test_trials(vpairs, apairs):
    visual_df = pd.DataFrame(vpairs)
    visualpairs = visual_df.groupby(['v_leading','v_trailing','v_expect']).size().reset_index()
    visualpairs = visualpairs.drop(0, axis=1)
    visualpairs = pd.concat([visualpairs]*2)
    visualpairs = visualpairs.to_dict('records')
    
    auditory_df = pd.DataFrame(apairs)
    auditorypairs = auditory_df.groupby(['a_leading','a_trailing','a_expect']).size().reset_index()
    auditorypairs = auditorypairs.drop(0, axis=1)
    auditorypairs = pd.concat([auditorypairs]*2)
    auditorypairs = auditorypairs.to_dict('records')
    
    return visualpairs, auditorypairs
