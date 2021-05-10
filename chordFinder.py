

import os

from music21 import *
from mido import MidiFile

staysMajor1 = 0
staysMinor1 = 0
minorToMajor = 0
majorToMinor = 0
endsOnDominant = 0
endsOnOther = 0
listLengths = []

def getLastChord(score):
    lastPitches = []

    for part in score.parts:
        lastPitch = part.pitches[-1]
        lastPitches.append(lastPitch)

    c = chord.Chord(lastPitches)
    c.duration.type = 'whole'

    cClosed = c.closedPosition()
    return cClosed

def getSecondToLastChord(score):
    lastPitches = []

    for part in score.parts:
        lastPitch = part.pitches[-2]
        lastPitches.append(lastPitch)

    c = chord.Chord(lastPitches)
    c.duration.type = 'whole'

    cClosed = c.closedPosition()
    return cClosed

def checkKeyChord(chord, key):
    if key.mode == 'minor':
        if chord.isMinorTriad() is True :
            return True
        else:
            return False
    else:
        if chord.isMajorTriad() is True:
            return True
        else:
            return False


def finalChordIs1(lastChord, key):
    if lastChord.root().name == key.tonic.name:
        return True
    else:
        return False

def checkLength(stream):
    i = 0
    while i < len(listLengths) - 1:
        if len(stream) == listLengths[i]:
            listLengths[i+1] += 1
            return
        i += 2
    listLengths.append(len(stream))
    listLengths.append(1)
    return

#def intervalInvesigation(score):
#    s = score.parts[0]
#    e = s.measures(1, len(s))
#    i = 0
#    while i < len(e)-1:
#        print(e[i].nameWithOctave, e[i+1].nameWithOctave)
#        i += 1

chorales = corpus.search('bach', fileExtensions='xml')
for i, chorale in enumerate(chorales[:10]):
    cScore = chorale.parse()
    stream = cScore.parts[0]
    checkLength(stream)
    key = cScore.analyze('key')
    checkKeySig(key)
    lastChord = getSecondToLastChord(cScore)
    if finalChordIs1(lastChord, key) is True :
        if checkKeyChord(lastChord, key) is True:
            if key.mode == 'minor':
                staysMinor1 += 1
            else:
                staysMajor1 += 1
        else:
            if key.mode == 'minor':
                minorToMajor += 1
            else:
                majorToMinor += 1
    else:
        if lastChord.root().name == key.getDominant().name:
            endsOnDominant += 1
        else:
            endsOnOther += 1


print(staysMajor1, staysMinor1, minorToMajor, majorToMinor, endsOnDominant, endsOnOther)
#print(note2.getOffsetBySite(stream1)) # safer version of .offset
