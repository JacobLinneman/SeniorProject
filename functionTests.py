from music21 import *


perfect1 = 0
m2D = 0
m2U = 0
mj2D = 0
mj2U = 0
m3D = 0
m3U = 0
mj3U = 0
mj3D = 0
p4U = 0
p4D = 0
p5U = 0
p5D = 0
m6U = 0
m6D = 0
mj6U = 0
mj6D = 0
m7U = 0
m7D = 0
mj7U = 0
mj7D = 0
p8U = 0
p8D = 0
otherNotes = 0

def checkInterval(int):
    global perfect1
    global m2D
    global m2U
    global mj2D
    global mj2U
    global m3D
    global m3U
    global mj3U
    global mj3D
    global p4U
    global p4D
    global p5U
    global p5D
    global m6U
    global m6D
    global mj6U
    global mj6D
    global m7U
    global m7D
    global mj7U
    global mj7D
    global p8U
    global p8D
    global otherNotes

    if(int.name == 'P1'):
        perfect1 += 1
    elif(int.name == 'M2'):
        if(int.directedSimpleName == 'M2'):
            mj2U += 1
        else:
            mj2D += 1
    elif(int.name == 'm2'):
        if(int.directedSimpleName == 'm2'):
            m2U += 1
        else:
            m2D += 1
    elif(int.name == 'm3'):
        if(int.directedSimpleName == 'm3'):
            m3U += 1
        else:
            m3D += 1
    elif(int.name == 'M3'):
        if(int.directedSimpleName == 'M3'):
            mj3U += 1
        else:
            mj3D += 1
    elif(int.name == 'P4'):
        if(int.directedSimpleName == 'P4'):
            p4U += 1
        else:
            p4D += 1
    elif(int.name == 'P5'):
        if(int.directedSimpleName == 'P5'):
            p5U += 1
        else:
            p5D += 1
    elif(int.name == 'm6'):
        if(int.directedSimpleName == 'm6'):
            m6U += 1
        else:
            m6D += 1
    elif(int.name == 'M6'):
        if(int.directedSimpleName == 'M6'):
            mj6U += 1
        else:
            mj6D += 1
    elif(int.name == 'm7'):
        if(int.directedSimpleName == 'm7'):
            m7U += 1
        else:
            m7D += 1
    elif(int.name == 'M7'):
        if(int.directedSimpleName == 'M7'):
            mj7U += 1
        else:
            mj7D += 1
    elif(int.name == 'P8'):
        if(int.directedSimpleName == 'P8'):
            p8U += 1
        else:
            p8D += 1
    else:
        otherNotes += 1

q = 0
i = 0
measure = 0
tonicNotes = 0
totalNotes = 0
chorales = corpus.search('bach', fileExtensions='xml')
for p, chorale in enumerate(chorales[:169]):
    c = chorale.parse()
    key = c.analyze('key')
    while q < len(c.parts):
        part = c.getElementsByClass(stream.Part)[q]
        noteList = stream.Stream()
        while measure < len(part)-1:
            notes = part.getElementsByClass(stream.Measure)[measure].getElementsByClass(note.Note)
            for thisNote in notes:
                noteList.append(thisNote)
            measure += 1
        while i < len(noteList)-1:
            if(noteList[i].name == key.tonic.name):
                tonicNotes += 1
                int = interval.Interval(noteStart = noteList[i], noteEnd = noteList[i+1])
                checkInterval(int)
            i += 1
        measure = 0
        i = 0
        q +=1
        totalNotes += len(noteList)
    q = 0

print(tonicNotes, totalNotes)
print(perfect1, m2D, m2U, mj2D, mj2U, m3D, m3U, mj3D, mj3U, p4D, p4U, p5D, p5U, otherNotes)
(m6D, m6U, mj6D, mj6U, m7D, m7U, mj7D, mj7U, p8U, p8D)
