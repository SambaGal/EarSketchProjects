#		python code
#
#		script_name:Project B
#
#		author: Maria
#
#		description: Composition
#
#
#

from earsketch import * 
from random import * 

init() 
setTempo(105) 

#drum sequencer sounds and patterns
kikDrum=OS_KICK06 #kick drum sound
kikString='0-------0-------' #kick drum pattern
hiHat=OS_CLOSEDHAT03 #hiHat Sound
hatString='0-0-0-0-0-0-0-0-' #hiHat pattern
snareDrum=OS_SNARE03 #snare Drum sound
snareString='----0-------0---' #snare drum pattern
#base
bass=HIPHOP_DUSTYBASSLINE_001 #base drum sound
#pad
pad=DUBSTEP_PAD_003 #pad sound

#putting drum sequencer in tracks 1-3
for measure in range (1,37):
	makeBeat(kikDrum, 1, measure, kikString)
	
for measure in range (1, 37):
	makeBeat(hiHat, 2, measure, hatString)	
	
for measure in range (1, 37):
	makeBeat(snareDrum, 3, measure, snareString)

#putting base on track 4
fitMedia(bass, 4, 3, 33)
#base effects
setEffect(4, DISTORTION, DISTO_GAIN, 0, 3, 50, 16)
setEffect(4, DISTORTION, DISTO_GAIN, 50, 16, 0, 33)
# putting Base on track 5
fitMedia(pad, 5, 3, 33)

#random effect parameters for the Pad sound
start=randint(-100,0)
end=randint(0, 100)
#setting effect for the pad sound 
setEffect (5, PAN, LEFT_RIGHT, start, 3, end, 9)
setEffect (5, PAN, LEFT_RIGHT, start, 9, end, 17)
setEffect (5, PAN, LEFT_RIGHT, start, 17, end, 25)
setEffect (5, PAN, LEFT_RIGHT, start, 25, end, 33)

#setting up melodic 8bit sounds
beats=[
    EIGHT_BIT_ATARI_LEAD_002, 
    EIGHT_BIT_ATARI_LEAD_004, 
    EIGHT_BIT_ATARI_LEAD_010, 
    EIGHT_BIT_ATARI_LEAD_012, 
    EIGHT_BIT_ATARI_LEAD_013, 
    EIGHT_BIT_ATARI_LEAD_003
]
beatString='0-0-1-1-2+++3+++'
beatString1='4-4-5-5-0+++1+++'
beatString2='2-2-3-3-4+++5+++'
beatString3='0+++1+++2+++3+++'
loopString='3-5-2+++1-0-4+++'
loopString1='35204+--0+1+5-3-'
loopString2='2+5+4+0+1+3+5---'
loopString3='5+++4---2+3+1-0-'
#puttin melody on track 6
makeBeat(beats, 6, 3, beatString)
makeBeat(beats, 6, 5, beatString1)
makeBeat(beats, 6, 7, beatString2)
makeBeat(beats, 6, 9, beatString3)
# putting loops on track 6
for measure in range (11,15):
	makeBeat(beats, 6, measure, loopString)
	
for measure in range (17,21):
	makeBeat(beats, 6, measure, loopString1)

for measure in range (23,27):
	makeBeat(beats, 6, measure, loopString2)

for measure in range (29,33):
	makeBeat(beats, 6, measure, loopString3)
#setting up a drum fill
fillIn=[OS_SNARE01, OS_LOWTOM01, OS_LOWTOM02, OS_LOWTOM03, OS_LOWTOM04,OS_KICK06] #drum set
fillString='--------0012350-' #drum fill pattern
#putting fillin drum on track 7
makeBeat(fillIn, 7, 8, fillString)
makeBeat(fillIn, 7, 16, fillString)
makeBeat(fillIn, 7, 24, fillString)
makeBeat(fillIn, 7, 32, fillString)
makeBeat(fillIn, 7, 36, fillString)
#putting imported Darbuka sound on track
fitMedia(MARIA_DARBUKA, 8, 4, 8.25)
fitMedia(MARIA_DARBUKA, 8, 12, 16.25)
fitMedia(MARIA_DARBUKA, 8, 20, 24.25)
fitMedia(MARIA_DARBUKA, 8, 28, 32.25)
#master track effects
setEffect(MASTER_TRACK, COMPRESSOR, COMPRESSOR_THRESHOLD, -5)
#finish 
finish() 


 




