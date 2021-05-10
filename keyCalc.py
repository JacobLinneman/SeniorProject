# Author: Jacob Linneman

from music21 import *


#key Values
AM = 0
Am = 0
AFM = 0
AFm = 0
ASm = 0

BM = 0
Bm = 0
BFM = 0
BFm = 0

CM = 0
Cm = 0
CSM = 0
CSm = 0
CFM = 0

DM = 0
Dm = 0
DSm = 0
DFM = 0

EM = 0
Em = 0
EFM = 0
EFm = 0

FM = 0
Fm = 0
FSM = 0
FSm = 0

GM = 0
Gm = 0
GSm = 0
GFM = 0

def checkKeySig(givenKey):
    global AM
    global Am
    global AFM
    global AFm
    global ASm

    global BM
    global Bm
    global BFM
    global BFm

    global CM
    global Cm
    global CSM
    global CSm
    global CFM

    global DM
    global Dm
    global DSm
    global DFM

    global EM
    global Em
    global EFM
    global EFm

    global FM
    global Fm
    global FSM
    global FSm

    global GM
    global Gm
    global GSm
    global GFM

    if givenKey.sharps == 0:
        if givenKey.mode == 'minor':
            Am += 1
        else:
            CM += 1
        return
    if givenKey.sharps == -1:
        if givenKey.mode == 'minor':
            Dm += 1
        else:
            FM += 1
        return
    if givenKey.sharps == 1:
        if givenKey.mode == 'minor':
            Em += 1
        else:
            GM += 1
        return
    if givenKey.sharps == -2:
        if givenKey.mode == 'minor':
            Gm += 1
        else:
            BFM += 1
        return
    if givenKey.sharps == 2:
        if givenKey.mode == 'minor':
            Bm += 1
        else:
            DM += 1
        return
    if givenKey.sharps == -3:
        if givenKey.mode == 'minor':
            Cm += 1
        else:
            EFM += 1
        return
    if givenKey.sharps == 3:
        if givenKey.mode == 'minor':
            FSm += 1
        else:
            AM += 1
        return
    if givenKey.sharps == -4:
        if givenKey.mode == 'minor':
            Fm += 1
        else:
            AFM += 1
        return
    if givenKey.sharps == 4:
        if givenKey.mode == 'minor':
            CSm += 1
        else:
            EM += 1
        return
    if givenKey.sharps == -5:
        if givenKey.mode == 'minor':
            BFm += 1
        else:
            DFM += 1
        return
    if givenKey.sharps == 5:
        if givenKey.mode == 'minor':
            GSm += 1
        else:
            BM += 1
        return
    if givenKey.sharps == -6:
        if givenKey.mode == 'minor':
            EFm += 1
        else:
            GFM += 1
        return
    if givenKey.sharps == 6:
        if givenKey.mode == 'minor':
            DSm += 1
        else:
            FSM += 1
        return
    if givenKey.sharps == -7:
        if givenKey.mode == 'minor':
            AFm += 1
        else:
            CFM += 1
        return
    if givenKey.sharps == 7:
        if givenKey.mode == 'minor':
            ASm += 1
        else:
            CSM += 1
        return

chorales = corpus.search('bach', fileExtensions='xml')
for i, chorale in enumerate(chorales[:300]):
    cScore = chorale.parse()
    key = cScore.analyze('key')
    checkKeySig(key)

print(AM, Am, AFM, AFm, ASm)
print(BM, Bm, BFM, BFm)
print(CM, Cm, CSM, CSm, CFM)
print(DM, Dm, DSm, DFM)
print(EM, Em, EFM, EFm)
print(FM, Fm, FSM, FSm)
print(GM, Gm, GSm, GFM)
