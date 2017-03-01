#		python code
#		script_name: darb.py
#
#		author: Maria

#		description: The instruments and melodic patterns are randomized. 
#   Run the script several times and listen to the random re-mixes. 
#   Some may not sound so good, but I hope you enjoy. 
#   Uncomment some of the code to listen to even more crazy patterns.

from earsketch import * 
from random import *

init()

tempo = randint(83, 134) #randomize tempo
setTempo(tempo) #set tempo
print "selected tempo " + str(tempo) #display random tempo

#set up the instruments

#drum sequencer sounds and patterns
kikDrum=OS_KICK06 #kick drum sound
kikString='0-------0-------' #kick drum pattern
hiHat=OS_CLOSEDHAT03 #hiHat Sound
hatString='0-0-0-0-0-0-0-0-' #hiHat pattern
snareDrum=OS_SNARE03 #snare Drum sound
snareString='----0-------0---' #snare drum pattern

#setting up a drum fill
fillIn=[OS_SNARE01, OS_LOWTOM01, OS_LOWTOM02, OS_LOWTOM03, OS_LOWTOM04,OS_KICK06,OS_CLOSEDHAT03] #drum set
fillString='5+6+0+6+0012350-' #drum fill pattern

#base
basses = [HIPHOP_DUSTYBASSLINE_001, RD_EDM_RAZORBASS_2, EIGHT_BIT_ATARI_BASSLINE_004, ELECTRO_ANALOGUE_BASS_007, RD_POP_ARPBASS_7, RD_ROCK_POPELECTRICBASS_9, TECHNO_ACIDBASS_007, RD_TRAP_RAZORBASSWOBBLE_3, RD_UK_HOUSE__SFX_BASSLINEPULSAR_1, RD_WORLD_PERCUSSION_BASSWOODENTONE_2 ] #bass selection
bass=basses[randint(0,len(basses)-1)] # select random base drum sound
print "bass selected " + bass #displays random bass instrument

#pad
pads = [DUBSTEP_PAD_003, DUBSTEP_PAD_001, EIGHT_BIT_ATARI_PAD_003, HIPHOP_FUNKPAD_001, HOUSE_DEEP_DREAMPAD_001, RD_FUTURE_DUBSTEP_PAD_3, RD_RNB_JUPITERPAD_2 , RD_TRAP_DARKPAD_1, TECHNO_SOFTPAD_003, YG_FUNK_STRING_PAD_2,YG_RNB_PAD_2] #pad sounds
pad=pads[randint(0, len(pads) - 1)] #pad sound
print "selected pad sound " + pad #displays selected pad sound

#setting up melodic 8bit sounds
beats=[
    EIGHT_BIT_ATARI_LEAD_002, 
    EIGHT_BIT_ATARI_LEAD_004, 
    EIGHT_BIT_ATARI_LEAD_010, 
    EIGHT_BIT_ATARI_LEAD_012, 
    EIGHT_BIT_ATARI_LEAD_013, 
    EIGHT_BIT_ATARI_LEAD_003
]  #list of 8bit sounds

beats = shuffleList(beats) #shuffle lead melodies

#set up melodic patterns
beatString='0-0-1-1-2+++3+++'
beatString1='4-4-5-5-0+++1+++'
beatString2='2-2-3-3-4+++5+++'
beatString3='0+++1+++2+++3+++'
loopString='3-5-2+++1-0-4+++'
loopString1='35204+--0+1+5-3-'
loopString2='2+5+4+0+1+3+5---'
loopString3='5+++4---2+3+1-0-'  #patterns

#optional: uncomment the following to shuffle the melody rhythm (very random and may not sound so good, but try)

# beatString = shuffleString(beatString)
# beatString1 = shuffleString(beatString1)
# beatString2 = shuffleString(beatString2)
# beatString3 = shuffleString(beatString3)
# loopString = shuffleString(loopString)
# loopString1 = shuffleString(loopString1)
# loopString2 = shuffleString(loopString2)
# loopString3 = shuffleString(loopString3)

#random start and end for pad fx
start=randint(-100,0)
end=randint(0, 100)
print "start " + str(start) + " end " + str(end)

#performance procedures

def sequencer(kick, hat, snare, kstr, hstr, snstr, drum_set, pattern,track, start, end):
  for measure in range(start, end):
    if measure %4 != 0:
      makeBeat(kick, track, measure, kstr)
      makeBeat(hat, track+1, measure, hstr)
      makeBeat(snare, track+2, measure, snstr)
    else:
      makeBeat(drum_set, track, measure, pattern )
        
 
   
def bass_pad(bs, pd, track,start, end):
    fitMedia(bs, track, start, end)
    fitMedia(pd, track+1, start, end)
    
    
def melody(pitches, pat1, pat2, pat3, pat4, loop1, loop2, loop3, loop4, track):
  makeBeat(pitches, track, 3, pat1)
  makeBeat(pitches, track, 5, pat2)    
  makeBeat(pitches, track, 7, pat3)
  makeBeat(pitches, track, 9, pat4)
  for measure in range(11, 13):
    makeBeat(pitches, track, measure, loop1)
  for measure in range(17, 19):
    makeBeat(pitches, track, measure, loop2)
  for measure in range(23, 25):
    makeBeat(pitches, track, measure, loop3)
  for measure in range(29, 31):
    makeBeat(pitches, track, measure, loop4)
    
def darbuka(darbuka, track, start, end):
  fitMedia(darbuka, track, start, end)
    

def effects(track, etype, param, startv, startm=1, endv=-5, endm=37):
  setEffect(track, etype, param, startv, startm, endv, endm)
        
        
#performance execution section
sequencer(kikDrum, hiHat, snareDrum, kikString, hatString, snareString, fillIn, fillString, 1,  1, 37)
bass_pad(bass, pad,4,  3, 33)
melody(beats, beatString, beatString1, beatString2, beatString3, loopString, loopString1, loopString2, loopString3, 6)
darbuka(MARIA_DARBUKA, 7, 4, 8.25 )
darbuka(MARIA_DARBUKA, 7, 12, 16.25 )
darbuka(MARIA_DARBUKA, 7, 20, 24.25 )
darbuka(MARIA_DARBUKA, 7, 28, 32.25 )
effects(4, DISTORTION, DISTO_GAIN, 0, 3, 50, 16)
effects(4, DISTORTION, DISTO_GAIN, 50, 16, 0, 33)
effects(5, PAN, LEFT_RIGHT, start, 3, end, 9)
effects(5, PAN, LEFT_RIGHT, start, 9, end, 17)
effects(5, PAN, LEFT_RIGHT, start, 17, end, 25)
effects(5, PAN, LEFT_RIGHT, start, 25, end, 33)
effects(MASTER_TRACK, COMPRESSOR, COMPRESSOR_THRESHOLD, -5)

finish() 
