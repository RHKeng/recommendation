from __future__ import division

#return Tanimoto
def Tanimoto_distance(prefs,person1,person2):
    #get the same items of person1 and person2
    si={}
    tanimoto=0
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
            if prefs[person1][item]==prefs[person2][item]:
                tanimoto+=1

    #none same items
    if len(si)==0:
        return 0
    else:
        return tanimoto/len(si)