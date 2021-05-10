# Author: Jacob Linneman
# MarkovTest.py: A file that takes in all of the data found in both functionTests
# keyCalc and chordFinder and makes a markov chain based on the values given.
# Outputs a piece of music that is viewed within musescore.


import numpy as np
import random as rm
from music21 import *

totalAnalyzed = 300

# Keys, P before means percentages
AM, Am, AFM = 25, 37, 1
PAM, PAm, PAFM =  AM / totalAnalyzed, Am / totalAnalyzed, AFM / totalAnalyzed

Bm, BFM, BFm = 24, 19, 2
PBm, PBFM, PBFm = Bm / totalAnalyzed, BFM / totalAnalyzed, BFm / totalAnalyzed

CM, Cm = 18, 6
PCM, PCm = CM / totalAnalyzed, Cm / totalAnalyzed

DM, Dm = 26, 17
PDM, PDm = DM / totalAnalyzed, Dm / totalAnalyzed

EM, Em, EFM = 5, 16, 6
PEM, PEm, PEFM = EM / totalAnalyzed, Em / totalAnalyzed, EFM / totalAnalyzed

FM, Fm, FSm = 21, 1, 5
PFM, PFm, PFSm =  FM / totalAnalyzed, Fm / totalAnalyzed, FSm / totalAnalyzed

GM, Gm = 42, 29
PGM, PGm = GM / totalAnalyzed, Gm / totalAnalyzed

keyNames = ['A', 'a', 'A-', 'b', 'B-', 'C', 'c', 'D', 'd', 'E', 'e', 'E-', 'F', 'f', 'f#', 'G', 'g']
keyList = [AM, Am, AFM, Bm, BFM, BFm, CM, Cm, DM, Dm, EM, Em, EFM, FM, Fm, FSm, GM, Gm]
keyListPercentages = [PAM, PAm, PAFM, PBm, PBFM, PBFm, PCM, PCm, PDM, PDm, PEM, PEm, PEFM, PFM, PFm, PFSm, PGM, PGm]


#last chord root
fstaysMajor1 = 147
fsmjPerct = fstaysMajor1 / totalAnalyzed

fstaysMinor1 = 10
fsmPerct = fstaysMinor1 / totalAnalyzed

fminorToMajor = 89
fmTm = fminorToMajor / totalAnalyzed

fmajorToMinor = 3
fmjTm = fmajorToMinor / totalAnalyzed

fdominant = 31
fDPerct = fdominant / totalAnalyzed

fother = 20
fOPerct = fother / totalAnalyzed

# second to last chord root
sfMajor1 = 4
sfM1Perct = sfMajor1 / totalAnalyzed

sfMinor1 = 3
sfm1Perct = sfMinor1 / totalAnalyzed

sfMajor1inMinor = 13
sfmjTmPerct = sfMajor1inMinor / totalAnalyzed

sfMinor1inMajor = 8
sfmTmjPerct = sfMinor1inMajor / totalAnalyzed

sfDominant = 219
sfDPerct = sfDominant / totalAnalyzed

sfOther = 53 #assuming these are ii and IV chords
sfOPerct = sfOther / totalAnalyzed

# measure length likelyness
eightToFourteen = 140
eTFP = eightToFourteen / totalAnalyzed
eTFA = [8, 9, 10, 11, 12, 13, 14]
eTFAEvenDis = 1 / len(eTFA)

fifteenToNinteen = 108
fTNP = fifteenToNinteen / totalAnalyzed
fTNA = [15, 16, 17, 18, 19]
fTNAEvenDis = 1 / len(fTNA)

twentyToTwentyNine = 34
tTTNP = twentyToTwentyNine / totalAnalyzed
tTTNA = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
tTTNAEvenDis = 1 / len(tTTNA)

thirtyToSixtyNine = 18
tTSNP = thirtyToSixtyNine / totalAnalyzed # going to use 30, 35, 44, 57, and 69 for easy calc
tTSNA = [30, 35, 44, 57, 69]
tTSNAEvenDis = 1 / len(tTSNA)

measureNames = ['8-14', '15-19', '20-29', '30-69']

measureProbabilities = [eTFP, fTNP, tTTNP, tTSNP]

# note counts for tonicNotes
totalNotes = 31436 + 50471
tonicNotes = 5359 + 9057
tW = totalNotes - tonicNotes # total without tonic= 67491
p1 = 1051 + 2060
m2d = 1773 + 1189
m2u = 25 + 17
mj2d = 739 + 587
mj2u = 1847 + 1228
m3d = 271 + 114
m3u = 81 + 85
mj3d = 61 + 37
mj3u = 232 + 88
p4d = 541 + 218
p4u = 346 + 232
p5d = 168 + 86
p5u = 372 + 195
m6d = 43 + 17
m6u = 15 + 14
mj6d = 6 + 9
mj6u = 56 + 14
m7d = 16 + 2
m7u = 4 + 5
mj7d = 0
mj7u = 12 + 6
p8 = 308 + 127
otherNotes = 81 + 38 # includes A1, A4, d5, d4, M10, d8, P12,
                     # assuming equal distribution

checkNotes = p1+ m2d + m2u + mj2d + mj2u + m3d + m3u + mj3d + mj3u + p4d + p4u + p5d + p5u + m6d + m6u + mj6d + mj6u + m7d + m7u + mj7d + mj7u + p8 + otherNotes

# Defines our range that our measure length can be in, based on the 300 pieces
# analyzed
def pickMeasureRange():
    q = np.random.rand(1)
    temp = 0
    i = 0
    while i < len(measureProbabilities):
        if temp > q:
            return(measureNames[i-1])
        else:
            temp += measureProbabilities[i]
            i += 1
    return(measureNames[-1])

# Helper function for pickMeasureLength, takes an array and an even distribution
# value to pick our measuer length
def pickFromEvenArray(array, evenValue):
    q = np.random.rand(1)
    temp = 0
    i = 0
    while i < len(array):
        if temp > q:
            return array[i - 1]
        else:
            i += 1
            temp += evenValue
    return array[-1]

# Picks a measuer length based on our 300 pieces analyzed
def pickMeasureLength():
    measureRange = pickMeasureRange()
    temp = 0
    i = 0
    chosen = 0
    if measureRange == measureNames[0]:
        chosen = pickFromEvenArray(eTFA, eTFAEvenDis)
    elif measureRange == measureNames[1]:
        chosen = pickFromEvenArray(fTNA, fTNAEvenDis)
    elif measureRange == measureNames[2]:
        chosen = pickFromEvenArray(tTTNA, tTTNAEvenDis)
    else:
        chosen = pickFromEvenArray(tTSNA, tTSNAEvenDis)
    return chosen

# Defines our key based on the list of keys we defined earlier
def defineKey():
    q = np.random.rand(1)
    temp = 0
    i = 0
    while i < len(keyList):
        if temp > q:
            return keyNames[i-1]
        else:
            temp += keyListPercentages[i]
            i += 1
    return keyNames[-1]

# Helper function for tonicJumps that takes a measure, note, and interval and
# appends to the measure the approprate interval
def addNewInterval(newMeasure, currentNote, targetInterval):
    aInterval = interval.Interval(targetInterval)
    aInterval.noteStart = currentNote
    newNote = aInterval.noteEnd
    newNote.duration.type = 'whole'
    newMeasure.append(newNote)
    return newMeasure


# A method that takes in a key, a note, a stream to add to, and a measure number
# to insert it, adds a new note to the stream at the approprate measure.  Picks
# the approprate note from our transition matix and moves accordingly.
def tonicJumps(key, ourStream, currentNote, measureNumber):
    newMeasure = stream.Measure(number = measureNumber)
    newMeasure.keySignature = ourKey
    if currentNote.pitch == key.tonic:
        change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
        if change == "TT":
            newNote = currentNote
            newNote.duration.type = 'whole'
            newMeasure.append(newNote)
            ourStream.append(newMeasure)
            return ourStream
        elif change == "Tm2d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-m2'))
            return ourStream
        elif change == "Tm2u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'm2'))
            return ourStream
        elif change == "TM2d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-M2'))
            return ourStream
        elif change == "TM2u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'M2'))
            return ourStream
        elif change == "Tm3d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-m3'))
            return ourStream
        elif change == "Tm3u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'm3'))
            return ourStream
        elif change == "TM3d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-M3'))
            return ourStream
        elif change == "TM3u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'M3'))
            return ourStream
        elif change == "TP4d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-P4'))
            return ourStream
        elif change == "TP4u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'P4'))
            return ourStream
        elif change == "TP5d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-P5'))
            return ourStream
        elif change == "TP5u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'P5'))
            return ourStream
        elif change == "Tm6d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-m6'))
            return ourStream
        elif change == "Tm6u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'm6'))
            return ourStream
        elif change == "TM6d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-M6'))
            return ourStream
        elif change == "TM6u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'M6'))
            return ourStream
        elif change == "Tm7d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-m7'))
            return ourStream
        elif change == "Tm7u":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-m7'))
            return ourStream
        elif change == "TM7d":
            ourStream.append(addNewInterval(newMeasure, currentNote, '-M7'))
            return ourStream
        elif change == "TM7u":
            ourStream.append(addNewInterval(newMeasure, currentNote, 'M7'))
            return ourStream
        elif change == "TP8":
            q = np.random.randint(0, 5)
            if q <= 1:
                ourStream.append(addNewInterval(newMeasure, currentNote, '-P8'))
            else:
                ourStream.append(addNewInterval(newMeasure, currentNote, 'P8'))
            return ourStream
        else:
            q = np.random.randint(0, 8)
            if q <= 1:
                direction = np.random.randint(0, 2)
                if direction < 1:
                    ourStream.append(addNewInterval(newMeasure, currentNote, '-A1')) # includes A1, A4, d5, d4, M10, d8, P12,
                else:
                    ourStream.append(addNewInterval(newMeasure, currentNote, 'A1'))
            elif q == 2:
                direction = np.random.randint(0, 2)
                if direction < 1:
                    ourStream.append(addNewInterval(newMeasure, currentNote, '-A4'))
                else:
                    ourStream.append(addNewInterval(newMeasure, currentNote, 'A4'))
            elif q == 3:
                direction = np.random.randint(0, 2)
                if direction < 1:
                    ourStream.append(addNewInterval(newMeasure, currentNote, '-d4'))
                else:
                    ourStream.append(addNewInterval(newMeasure, currentNote, 'd4'))
            elif q ==4:
                direction = np.random.randint(0, 2)
                if direction < 1:
                    ourStream.append(addNewInterval(newMeasure, currentNote, '-d5'))
                else:
                    ourStream.append(addNewInterval(newMeasure, currentNote, 'd5'))
            elif q ==5:
                ourStream.append(addNewInterval(newMeasure, currentNote, "M10"))
            elif q ==6:
                ourStream.append(addNewInterval(newMeasure, currentNote, "-d8"))
            else:
                ourStream.append(addNewInterval(newMeasure, currentNote, "P12"))
            return ourStream
    else:
        scaleDegree = key.getScaleDegreeFromPitch(currentNote.pitch)
        scaleAccidental = key.getScaleDegreeAndAccidentalFromPitch(currentNote.pitch)
        if scaleDegree == 7:
            if scaleAccidental == pitch.Accidental('flat'):
                ourStream.append(addNewInterval(newMeasure, currentNote, 'M2'))
            else:
                ourStream.append(addNewInterval(newMeasure, currentNote, 'm2'))
            return ourStream
        elif scaleDegree == 5:
            q = np.random.rand(1)
            if q < .5:
                ourStream.append(addNewInterval(newMeasure, currentNote, '-P5'))
            else:
                ourStream.append(addNewInterval(newMeasure, currentNote, 'P4'))
            return ourStream
        elif scaleDegree == 2:
            ourStream.append(addNewInterval(newMeasure, currentNote, '-M2'))
            return ourStream
        else:
            newNote = note.Note(ourKey.tonic)
            newNote.duration.type = 'whole'
            newNote.octave = np.random.randint(4, 6)
            newMeasure.append(newNote)
            ourStream.append(newMeasure)
            return ourStream
    return

# The statespace
states = ["Tonic","notTonic"]

# Possible sequences of events
transitionName = [["TT","Tm2d","Tm2u","TM2d","TM2u","Tm3d","Tm3u","TM3d","TM3u",
                    "TP4d","TP4u","TP5d","TP5u","Tm6d","Tm6u","TM6d","TM6u",
                    "Tm7d","Tm7u","TM7d","TM7u","TP8", "other"]
                    ,["TT"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[p1/tonicNotes, m2d/tonicNotes, m2u/tonicNotes, mj2d/tonicNotes, mj2u/tonicNotes, m3d/tonicNotes,
                    m3u/tonicNotes, mj3d/tonicNotes, mj3u/tonicNotes, p4d/tonicNotes, p4u/tonicNotes, p5d/tonicNotes, p5u/tonicNotes, m6d/tonicNotes,
                    m6u/tonicNotes, mj6d/tonicNotes, mj6u/tonicNotes, m7d/tonicNotes, m7u/tonicNotes, mj7d/tonicNotes, mj7u/tonicNotes,
                    p8/tonicNotes, otherNotes/tonicNotes],[1.0]]

# definifng our key, starting note, and the final stream we are showing
ourKey = key.Key(defineKey())
measures = stream.Stream()
measures.keySignature = ourKey
pieceLength = pickMeasureLength()
firstMeasure = stream.Measure(number = 1)
firstNote = note.Note(ourKey.tonic)
firstNote.octave = np.random.randint(4, 6)
firstNote.duration.type = 'whole'
firstMeasure.append(firstNote)
measures.append(firstMeasure)
currentNote = firstNote
print(ourKey)
print(firstNote.octave)
print(pieceLength)
index = 0
while index < pieceLength:
    tonicJumps(ourKey, measures, currentNote, index + 1)
    currentNote = measures[-1][-1]
    index += 1
print(measures)
measures.show()
