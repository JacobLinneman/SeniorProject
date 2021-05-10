# Author: Jacob Linneman
# chordFinder.py is a file that finds for me the last two chords within the 300
# Bach chorales

import os

from music21 import *
from mido import MidiFile

# our values to keep track of
staysMajor1 = 0
staysMinor1 = 0
minorToMajor = 0
majorToMinor = 0
endsOnDominant = 0
endsOnOther = 0
listLengths = []

# finds the last chord in a given score
def getLastChord(score):
    lastPitches = []

    for part in score.parts:
        lastPitch = part.pitches[-1]
        lastPitches.append(lastPitch)

    c = chord.Chord(lastPitches)
    c.duration.type = 'whole'

    cClosed = c.closedPosition()
    return cClosed

# finds the second to last chord in a given score
def getSecondToLastChord(score):
    lastPitches = []

    for part in score.parts:
        lastPitch = part.pitches[-2]
        lastPitches.append(lastPitch)

    c = chord.Chord(lastPitches)
    c.duration.type = 'whole'

    cClosed = c.closedPosition()
    return cClosed

# Checks to see if a major more minor chord within given key
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

# Checks to see if a final chord is a tonic chord
def finalChordIs1(lastChord, key):
    if lastChord.root().name == key.tonic.name:
        return True
    else:
        return False

# Check the length of a given stream
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

# Defines all of the 300 bach chorales we are using and finds either the last
# chord or second to last chord. Then returns all of the values of those chords
chorales = corpus.search('bach', fileExtensions='xml')
for i, chorale in enumerate(chorales[:10]):
    cScore = chorale.parse()
    stream = cScore.parts[0]
    checkLength(stream)
    key = cScore.analyze('key')
    checkKeySig(key)
    # lastChord = getLastChord(cScore)
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
