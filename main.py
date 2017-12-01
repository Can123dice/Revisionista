import sys
#sys.path.append('/home/candice/Documents/xxx/music21-1.9.3/music21')
#Alternative: Terminal: cd <path of the folder> then sudo setup.py install


# import PyQt4 QtCore module
from PyQt4.QtCore import * 
from music21 import *

#Import and parse an XML file (Example from http://web.mit.edu/music21/)
#sBach = converter.parse('/home/candice/Documents/xxx/Concept Elbums/Archive/Sarisiphirilla/noAbsolution/NoAbsolution.mscz.xml') 
#sBach.show('text') 

#show melody in musical notation, also works with a MIDI file or XML file as shown above
#converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#").show()

#Converting a file from whatever notation to XML
#converter.parse('/users/.../docs/composition.etc').write('musicxml')
converter.parse("lilypond: c' e' g' a' c'").write('musicxml')

#FileDump = 

converter.parse('/home/candice/Documents/xxx/Concept Elbums/Archive/Sarisiphirilla/noAbsolution/NoAbsolution.mscz.xml')


