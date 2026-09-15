#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on January 12, 2024, at 12:21
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.2')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from initializeVars
#response key constants
responseiscorrect2;
key_list = ['1','2'] #['num_1','num_2']  #num_1 means '1' on the number pad
ratingkey_list = ['1','2','3','4','5','6'] #['num_1','num_2']  #num_1 means '1' on the number pad
key_1allowed = ['1'] #['num_1']
key_2allowed = ['2'] #['num_2']
instruc_list = ['t'] #['t' key for passing through instructions]
responseiscorrect2;
responseside2;
correctside2;
correctword2;
correctwordindex2;
#screen appearance constants 
background_color = 'black' #used for setting colors of objects, but the actual background color is set in monitor settings
targetword_offset = .3 #show target X cm above center
#topword_offset = .1  #show word1 X cm above(+)/below(-) center
#bottomword_offset = -.05 #show word1 X cm above(+)/below(-) center
#fbkimage_offset = .07
showrespdur = 4 #seconds
errormsg_offset = .2
confscale_yoffset = -.25
confnumbers_yoffset = -0.3285
fbkyes_xoffset = -.3
fbkyes_yoffset = -.05
fbkno_xoffset = .1
fbkno_yoffset = .1
fbkcost_xoffset = -.3
fbkcost_yoffset = -.15
totalcorrect_offset = .02
bonus_offset = -.04

instructword_height = .15  #instruct word size (cm)
instruct_width = .030  #instruct text width (cm)
targetword_height = .1  #target word size cm
word_height = .1  #word options size cm
respbox_width = .1 * 8
respbox_height = .1 * 1.25
selectbox_color = 'white'
errormsg_height = .075
question_height = 1
confscale_height = .75
respbox_y = .1
#timing constants
studyviewwindow = 4 #R1 study duration in seconds
fbk_dur = 2 #feedback duration in seconds
study2dur = 300 #R2 study duration in seconds
maxconffbkchoice_dur = 300 #max time for confidence rating/ fbk choice (seconds)
slowrespmessage_delay = 4 #message for slow confidence/fbk choice responses
slowrespmessage_dur = maxconffbkchoice_dur - slowrespmessage_delay

#lists for tracking performance
r1correct_list = [None] * 60 #(True or False in each slot indexed by WordIndex-1)
r2correct_list = [None] * 60 #(True or False in each slot indexed by WordIndex-1)
r3correct_list = [None] * 60 #(True or False in each slot indexed by WordIndex-1)
correctword_list = [None] * 60 #(1 or 2 in each slot indexed by WordIndex-1)
totalcorrect = 0
totalspent = 0
trialbonus = 10
r1reversed = []
r2reversed = []
r3reversed = []
#feedback cost list
fbkcostlevels = [ -6, -4, -2, 0 ] #possible costs per trial
trialspercostlevel = [ 15, 15, 15, 15 ] #how many trials of each cost level?
fbkcost_list = []
idx = 0
for fbkcost in fbkcostlevels:
    fbkcost_list = fbkcost_list + ([fbkcost] * trialspercostlevel[idx])
    idx = idx + 1
from random import shuffle
shuffle(fbkcost_list)



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'Game_C_ver2.0'  # from the Builder filename that created this script
expInfo = {
    'session': '001',
    'participant': 'FBVAL-',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\daria\\OneDrive\\Documents\\Psychopy\\Game_C_ver2.0\\Game_C_ver2.0_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 960], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "SetupConstants" ---

# --- Initialize components for Routine "Instruct1a" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text="Part #1\n\nYou will learn word matches in this first part. \n\nFirst, you will see a target word at the top of the screen, with two possible matches below it. Your job is to guess which word matches the top word. You will then get feedback about the accuracy of your choice and will try to remember the correct word match based on that feedback.\n\nIn the last round, you will earn a cash bonus for each word you remember correctly.\n\nFor example: \n\nABSTRACT\n\n1) DOG\n\n2) PLATE\n\nTo guess Option 1 – press the '1' key.\nTo guess Option 2 – press the '2' key.",
    font='Arial',
    pos=(0, 0), height=0.033, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Instructresp = keyboard.Keyboard()

# --- Initialize components for Routine "Instruct1b" ---
Instruct1b_text = visual.TextStim(win=win, name='Instruct1b_text',
    text="After you make your choice, you will see feedback indicating whether you were correct (a green checkmark) or incorrect (a red X). The matches are random, so you will not know which choice matches with each target word, but you should try to remember the feedback because you will see these word matches again.\n\nA potentially useful strategy is to create sentences in your head that will help you remember which word matches with the target word, but you can use your own strategy if you wish. Your cash bonus will depend on how many word pairs you remember correctly during the last round. You will earn 10 cents per correct answer and can earn up to 6 dollars.\n\nTry to respond as quickly as possible and learn from the feedback. You will have 4 seconds to respond during each set of words.\n\nAny questions? \n\nPress the '2' key to begin.\n ",
    font='Arial',
    pos=(0, 0), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instructresp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "GetReady" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, .05), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Get ready to begin...',
    font='Arial',
    pos=(0, -.05), height=.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "StudyView1" ---
# Run 'Begin Experiment' code from PlaceWords
topword_offset = 0
bottomword_offset = 0
StudyView1_target = visual.TextStim(win=win, name='StudyView1_target',
    text='',
    font='Arial',
    pos=(0,targetword_offset), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Study1Response = keyboard.Keyboard()
StudyView_topsideword = visual.TextStim(win=win, name='StudyView_topsideword',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
StudyView1_bottomsideword = visual.TextStim(win=win, name='StudyView1_bottomsideword',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "ShowResp" ---
highlightbox_showresp = visual.Rect(
    win=win, name='highlightbox_showresp',
    width=(respbox_width, respbox_height)[0], height=(respbox_width, respbox_height)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=12,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1, depth=0.0, interpolate=True)
Fbk_target_showresp = visual.TextStim(win=win, name='Fbk_target_showresp',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Fbk_topsideword_showresp = visual.TextStim(win=win, name='Fbk_topsideword_showresp',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Fbk_bottomsideword_showresp = visual.TextStim(win=win, name='Fbk_bottomsideword_showresp',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Fbk1" ---
resp_highlightbox = visual.Rect(
    win=win, name='resp_highlightbox',
    width=(respbox_width, respbox_height)[0], height=(respbox_width, respbox_height)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=12,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1, depth=0.0, interpolate=True)
Fbk_target = visual.TextStim(win=win, name='Fbk_target',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Fbk_topsideword = visual.TextStim(win=win, name='Fbk_topsideword',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Fbk_bottomsideword = visual.TextStim(win=win, name='Fbk_bottomsideword',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
FbkImage = visual.ImageStim(
    win=win,
    name='FbkImage', 
    image='default.png', mask=None, anchor='center',
    ori=0, pos=[0,0], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Error_message = visual.TextStim(win=win, name='Error_message',
    text='',
    font='Arial',
    pos=(0, .2), height=.075, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "EndPart1" ---
text = visual.TextStim(win=win, name='text',
    text='That was the end of Part #1.\n\nPlease ring the bell to alert the experimenter, who will set you up on Part #2.',
    font='Arial',
    pos=(0, 0), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
contpart2 = keyboard.Keyboard()

# --- Initialize components for Routine "Instruct4" ---
Instruct2a_text = visual.TextStim(win=win, name='Instruct2a_text',
    text="Part #2 \n\nNow you will see the words from Part #1 again. Your task is to remember the correct match for the top word, based on what you learned in Part #1. First, press '1' or '2' to select the correct word. The sets of words may not be in the same order as when you saw them the first time. \n\nNext, you will be asked to rate how confident you are that your answer is correct. Press a number key from '1' through '6' to indicate your confidence.\n\n1 = ~50% confidence (LOW: ~50/50 guess)\n2 = ~60% confidence\n3 = ~70% confidence\n4 = ~80% confidence\n5 = ~90% confidence\n6 = ~100% confidence (HIGH: ~100% sure)",
    font='Arial',
    pos=(0, 0), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instructresp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "Instruct4_2" ---
Instruct2b_text = visual.TextStim(win=win, name='Instruct2b_text',
    text='After you rate your confidence, you will have an opportunity to get feedback again about whether you selected the correct word. The screen will say: "Do you want feedback?"and you can press \'1\' to get feedback, or \'2\' to ignore the feedback.\n\nSometimes, you will see that it will cost a few cents to get feedback. This means if you choose \'YES\' for feedback, you will have the cost deducted from your final cash bonus. Sometimes the cost will be zero cents so you can get feedback for free.  If you choose to ignore the feedback, no money will be deducted  from your bonus.\n\nKeep in mind that you will be rewarded with 10 cents for every correct response you make during the final bonus round. You can be rewarded up to 6 dollars, depending on how well you perform. Since your final cash bonus will depend on your performance during the final round, it may be worthwhile to accept the cost of the feedback so that you can learn the word pairs well.\n\nAny questions? \n\nPress the \'2\' key to begin.',
    font='Arial',
    pos=(0, 0), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instructresp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "GetReady" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, .05), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Get ready to begin...',
    font='Arial',
    pos=(0, -.05), height=.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "StudyView4" ---
StudyView1_target_2 = visual.TextStim(win=win, name='StudyView1_target_2',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
StudyView_topsideword_2 = visual.TextStim(win=win, name='StudyView_topsideword_2',
    text='',
    font='Arial',
    pos=[0,0], height=word_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
StudyView1_bottomsideword_2 = visual.TextStim(win=win, name='StudyView1_bottomsideword_2',
    text='',
    font='Arial',
    pos=[0,0], height=word_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Study2Response = keyboard.Keyboard()
slowrespmessage_conf_2 = visual.TextStim(win=win, name='slowrespmessage_conf_2',
    text='please respond faster',
    font='Arial',
    pos=(0, errormsg_offset), height=errormsg_height, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "ShowResp" ---
highlightbox_showresp = visual.Rect(
    win=win, name='highlightbox_showresp',
    width=(respbox_width, respbox_height)[0], height=(respbox_width, respbox_height)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=12,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1, depth=0.0, interpolate=True)
Fbk_target_showresp = visual.TextStim(win=win, name='Fbk_target_showresp',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Fbk_topsideword_showresp = visual.TextStim(win=win, name='Fbk_topsideword_showresp',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Fbk_bottomsideword_showresp = visual.TextStim(win=win, name='Fbk_bottomsideword_showresp',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Confidence" ---
R2_highlightbox_conf = visual.Rect(
    win=win, name='R2_highlightbox_conf',
    width=(respbox_width, respbox_height)[0], height=(respbox_width, respbox_height)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=12,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=0.0, interpolate=True)
R2_target_conf = visual.TextStim(win=win, name='R2_target_conf',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=targetword_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
R2_word1_conf = visual.TextStim(win=win, name='R2_word1_conf',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
R2_word2_conf = visual.TextStim(win=win, name='R2_word2_conf',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
conf_question = visual.TextStim(win=win, name='conf_question',
    text='How confident are you in your answer?',
    font='Arial',
    pos=(0, -.2), height=.055, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
confscale_numbers = visual.TextStim(win=win, name='confscale_numbers',
    text='(1)   (2)   (3)   (4)   (5)   (6)\n\nlow                            high\n',
    font='Arial',
    pos=(0, -.4), height=.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
confresp = keyboard.Keyboard()
slowrespmessage_conf = visual.TextStim(win=win, name='slowrespmessage_conf',
    text='please respond faster',
    font='Arial',
    pos=(0, errormsg_offset), height=errormsg_height, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "ChooseFbk" ---
R2_FbkQuestion = visual.TextStim(win=win, name='R2_FbkQuestion',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fbkchoice_resp = keyboard.Keyboard()
fbkcosttext = visual.TextStim(win=win, name='fbkcosttext',
    text='',
    font='Arial',
    pos=(fbkcost_xoffset,fbkcost_yoffset), height=.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
R2_fbkyes = visual.TextStim(win=win, name='R2_fbkyes',
    text='1) YES',
    font='Arial',
    pos=(fbkyes_xoffset, fbkyes_yoffset), height=.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
R2_fbkno = visual.TextStim(win=win, name='R2_fbkno',
    text='2) NO',
    font='Arial',
    pos=(.3, -.05), height=.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
slowrespmessage_fbk = visual.TextStim(win=win, name='slowrespmessage_fbk',
    text='please respond faster',
    font='Arial',
    pos=(0, .15), height=.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
fbknocosttext = visual.TextStim(win=win, name='fbknocosttext',
    text='',
    font='Arial',
    pos=(.3,fbkcost_yoffset), height=.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "Fbk2" ---
R2_resp_highlightbox = visual.Rect(
    win=win, name='R2_resp_highlightbox',
    width=(respbox_width, respbox_height)[0], height=(respbox_width, respbox_height)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=12,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1, depth=0.0, interpolate=True)
R2_Fbk_target = visual.TextStim(win=win, name='R2_Fbk_target',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
R2_Fbk_topsideword = visual.TextStim(win=win, name='R2_Fbk_topsideword',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
R2_Fbk_bottomsideword = visual.TextStim(win=win, name='R2_Fbk_bottomsideword',
    text='',
    font='Arial',
    pos=[0,0], height=word_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
R2_FbkImage = visual.ImageStim(
    win=win,
    name='R2_FbkImage', 
    image='default.png', mask=None, anchor='center',
    ori=0, pos=[0,0], size=[.3, .3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
R2_Error_message = visual.TextStim(win=win, name='R2_Error_message',
    text='',
    font='Arial',
    pos=(0, errormsg_offset), height=errormsg_height, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "EndPart2" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='That was the end of Part #2.\n\nPlease ring the bell to alert the experimenter, who will set you up on the final part.',
    font='Arial',
    pos=(0, 0), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
contpart2_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Instruct3a" ---
Instruct2a_text_3 = visual.TextStim(win=win, name='Instruct2a_text_3',
    text="Part #3\n\nIn this last part, you will see the same sets of words from earlier. Your task is to remember the correct match for the top word, based on what you learned earlier.\n\nPress '1' or '2' to select the correct word. \nYou will see your cash bonus total at the end of the round.\n\nAny questions? \n\nPress the '2' key to begin.\n",
    font='Arial',
    pos=(0, 0), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instructresp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "GetReady" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, .05), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Get ready to begin...',
    font='Arial',
    pos=(0, -.05), height=.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Test3" ---
StudyView1_target_3 = visual.TextStim(win=win, name='StudyView1_target_3',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=targetword_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
StudyView_topsideword_3 = visual.TextStim(win=win, name='StudyView_topsideword_3',
    text='',
    font='Arial',
    pos=[0,0], height=word_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
StudyView1_bottomsideword_3 = visual.TextStim(win=win, name='StudyView1_bottomsideword_3',
    text='',
    font='Arial',
    pos=[0,0], height=word_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Test3response = keyboard.Keyboard()

# --- Initialize components for Routine "ShowResp_3" ---
highlightbox_showresp_2 = visual.Rect(
    win=win, name='highlightbox_showresp_2',
    width=(respbox_width, respbox_height)[0], height=(respbox_width, respbox_height)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=12,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=0.0, interpolate=True)
Fbk_target_showresp_2 = visual.TextStim(win=win, name='Fbk_target_showresp_2',
    text='',
    font='Arial',
    pos=(0, targetword_offset), height=targetword_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
b_Fbk_topsideword_showresp_2_ = visual.TextStim(win=win, name='b_Fbk_topsideword_showresp_2_',
    text='',
    font='Arial',
    pos=[0,0], height=word_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
b_Fbk_bottomsideword_showresp_2_ = visual.TextStim(win=win, name='b_Fbk_bottomsideword_showresp_2_',
    text='',
    font='Arial',
    pos=[0,0], height=word_height, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Additup" ---

# --- Initialize components for Routine "EndPart3" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='That was the end of Part #3. \n\nPlease alert the experimenter. ',
    font='Arial',
    pos=(0, 0), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Lastresp = keyboard.Keyboard()
totalcorrect_text = visual.TextStim(win=win, name='totalcorrect_text',
    text='',
    font='Arial',
    pos=(0, -0.15), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
bonus_text = visual.TextStim(win=win, name='bonus_text',
    text='',
    font='Arial',
    pos=(0, -.25), height=.033, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "SetupConstants" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
SetupConstantsComponents = []
for thisComponent in SetupConstantsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "SetupConstants" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SetupConstantsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SetupConstants" ---
for thisComponent in SetupConstantsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "SetupConstants" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instruct1a" ---
continueRoutine = True
# update component parameters for each repeat
Instructresp.keys = []
Instructresp.rt = []
_Instructresp_allKeys = []
# keep track of which components have finished
Instruct1aComponents = [text_5, Instructresp]
for thisComponent in Instruct1aComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruct1a" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    
    # if text_5 is starting this frame...
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_5.started')
        # update status
        text_5.status = STARTED
        text_5.setAutoDraw(True)
    
    # if text_5 is active this frame...
    if text_5.status == STARTED:
        # update params
        pass
    
    # *Instructresp* updates
    waitOnFlip = False
    
    # if Instructresp is starting this frame...
    if Instructresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructresp.frameNStart = frameN  # exact frame index
        Instructresp.tStart = t  # local t and not account for scr refresh
        Instructresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructresp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructresp.started')
        # update status
        Instructresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instructresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instructresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instructresp.status == STARTED and not waitOnFlip:
        theseKeys = Instructresp.getKeys(keyList=['t'], waitRelease=False)
        _Instructresp_allKeys.extend(theseKeys)
        if len(_Instructresp_allKeys):
            Instructresp.keys = [key.name for key in _Instructresp_allKeys]  # storing all keys
            Instructresp.rt = [key.rt for key in _Instructresp_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct1aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruct1a" ---
for thisComponent in Instruct1aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instructresp.keys in ['', [], None]:  # No response was made
    Instructresp.keys = None
thisExp.addData('Instructresp.keys',Instructresp.keys)
if Instructresp.keys != None:  # we had a response
    thisExp.addData('Instructresp.rt', Instructresp.rt)
thisExp.nextEntry()
# the Routine "Instruct1a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instruct1b" ---
continueRoutine = True
# update component parameters for each repeat
Instructresp_2.keys = []
Instructresp_2.rt = []
_Instructresp_2_allKeys = []
# keep track of which components have finished
Instruct1bComponents = [Instruct1b_text, Instructresp_2]
for thisComponent in Instruct1bComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruct1b" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct1b_text* updates
    
    # if Instruct1b_text is starting this frame...
    if Instruct1b_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct1b_text.frameNStart = frameN  # exact frame index
        Instruct1b_text.tStart = t  # local t and not account for scr refresh
        Instruct1b_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct1b_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instruct1b_text.started')
        # update status
        Instruct1b_text.status = STARTED
        Instruct1b_text.setAutoDraw(True)
    
    # if Instruct1b_text is active this frame...
    if Instruct1b_text.status == STARTED:
        # update params
        pass
    
    # *Instructresp_2* updates
    waitOnFlip = False
    
    # if Instructresp_2 is starting this frame...
    if Instructresp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructresp_2.frameNStart = frameN  # exact frame index
        Instructresp_2.tStart = t  # local t and not account for scr refresh
        Instructresp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructresp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructresp_2.started')
        # update status
        Instructresp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instructresp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instructresp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instructresp_2.status == STARTED and not waitOnFlip:
        theseKeys = Instructresp_2.getKeys(keyList=['2'], waitRelease=False)
        _Instructresp_2_allKeys.extend(theseKeys)
        if len(_Instructresp_2_allKeys):
            Instructresp_2.keys = _Instructresp_2_allKeys[-1].name  # just the last key pressed
            Instructresp_2.rt = _Instructresp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct1bComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruct1b" ---
for thisComponent in Instruct1bComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruct1b" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GetReady" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GetReadyComponents = [fixation, text_4]
for thisComponent in GetReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GetReady" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation* updates
    
    # if fixation is starting this frame...
    if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation.frameNStart = frameN  # exact frame index
        fixation.tStart = t  # local t and not account for scr refresh
        fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation.started')
        # update status
        fixation.status = STARTED
        fixation.setAutoDraw(True)
    
    # if fixation is active this frame...
    if fixation.status == STARTED:
        # update params
        pass
    
    # if fixation is stopping this frame...
    if fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.stopped')
            # update status
            fixation.status = FINISHED
            fixation.setAutoDraw(False)
    
    # *text_4* updates
    
    # if text_4 is starting this frame...
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        # update status
        text_4.status = STARTED
        text_4.setAutoDraw(True)
    
    # if text_4 is active this frame...
    if text_4.status == STARTED:
        # update params
        pass
    
    # if text_4 is stopping this frame...
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            # update status
            text_4.status = FINISHED
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GetReady" ---
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# set up handler to look after randomisation of conditions etc
Study1Loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StimFile_A.xlsx'),
    seed=None, name='Study1Loop')
thisExp.addLoop(Study1Loop)  # add the loop to the experiment
thisStudy1Loop = Study1Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy1Loop.rgb)
if thisStudy1Loop != None:
    for paramName in thisStudy1Loop:
        exec('{} = thisStudy1Loop[paramName]'.format(paramName))

for thisStudy1Loop in Study1Loop:
    currentLoop = Study1Loop
    # abbreviate parameter names if possible (e.g. rgb = thisStudy1Loop.rgb)
    if thisStudy1Loop != None:
        for paramName in thisStudy1Loop:
            exec('{} = thisStudy1Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "StudyView1" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from PlaceWords
    x = ['1) ']
    y = ['2) ']
    if random()>.5:
        topword_offset = (.1)
        bottomword_offset = (-0.05)
        r1reversed = False
        x = '1) ' 
        y = '2) '
    else:
        topword_offset = -0.05
        bottomword_offset = .1
        r1reversed = True
        x = '2) ' 
        y = '1) ' 
    
    print(r1reversed)
    print(topword_offset)
    
    StudyView1_target.setText(targetword)
    Study1Response.keys = []
    Study1Response.rt = []
    _Study1Response_allKeys = []
    StudyView_topsideword.setPos((0, topword_offset))
    StudyView_topsideword.setText(x + R1Word1)
    StudyView1_bottomsideword.setPos((0,bottomword_offset))
    StudyView1_bottomsideword.setText(y + R1Word2)
    # keep track of which components have finished
    StudyView1Components = [StudyView1_target, Study1Response, StudyView_topsideword, StudyView1_bottomsideword]
    for thisComponent in StudyView1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "StudyView1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StudyView1_target* updates
        
        # if StudyView1_target is starting this frame...
        if StudyView1_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView1_target.frameNStart = frameN  # exact frame index
            StudyView1_target.tStart = t  # local t and not account for scr refresh
            StudyView1_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView1_target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView1_target.started')
            # update status
            StudyView1_target.status = STARTED
            StudyView1_target.setAutoDraw(True)
        
        # if StudyView1_target is active this frame...
        if StudyView1_target.status == STARTED:
            # update params
            pass
        
        # if StudyView1_target is stopping this frame...
        if StudyView1_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView1_target.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                StudyView1_target.tStop = t  # not accounting for scr refresh
                StudyView1_target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView1_target.stopped')
                # update status
                StudyView1_target.status = FINISHED
                StudyView1_target.setAutoDraw(False)
        
        # *Study1Response* updates
        waitOnFlip = False
        
        # if Study1Response is starting this frame...
        if Study1Response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Study1Response.frameNStart = frameN  # exact frame index
            Study1Response.tStart = t  # local t and not account for scr refresh
            Study1Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Study1Response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Study1Response.started')
            # update status
            Study1Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Study1Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Study1Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if Study1Response is stopping this frame...
        if Study1Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Study1Response.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Study1Response.tStop = t  # not accounting for scr refresh
                Study1Response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Study1Response.stopped')
                # update status
                Study1Response.status = FINISHED
                Study1Response.status = FINISHED
        if Study1Response.status == STARTED and not waitOnFlip:
            theseKeys = Study1Response.getKeys(keyList=['1','2'], waitRelease=False)
            _Study1Response_allKeys.extend(theseKeys)
            if len(_Study1Response_allKeys):
                Study1Response.keys = _Study1Response_allKeys[-1].name  # just the last key pressed
                Study1Response.rt = _Study1Response_allKeys[-1].rt
                # was this correct?
                if (Study1Response.keys == str('')) or (Study1Response.keys == ''):
                    Study1Response.corr = 1
                else:
                    Study1Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *StudyView_topsideword* updates
        
        # if StudyView_topsideword is starting this frame...
        if StudyView_topsideword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView_topsideword.frameNStart = frameN  # exact frame index
            StudyView_topsideword.tStart = t  # local t and not account for scr refresh
            StudyView_topsideword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView_topsideword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView_topsideword.started')
            # update status
            StudyView_topsideword.status = STARTED
            StudyView_topsideword.setAutoDraw(True)
        
        # if StudyView_topsideword is active this frame...
        if StudyView_topsideword.status == STARTED:
            # update params
            pass
        
        # if StudyView_topsideword is stopping this frame...
        if StudyView_topsideword.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView_topsideword.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                StudyView_topsideword.tStop = t  # not accounting for scr refresh
                StudyView_topsideword.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView_topsideword.stopped')
                # update status
                StudyView_topsideword.status = FINISHED
                StudyView_topsideword.setAutoDraw(False)
        
        # *StudyView1_bottomsideword* updates
        
        # if StudyView1_bottomsideword is starting this frame...
        if StudyView1_bottomsideword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView1_bottomsideword.frameNStart = frameN  # exact frame index
            StudyView1_bottomsideword.tStart = t  # local t and not account for scr refresh
            StudyView1_bottomsideword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView1_bottomsideword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword.started')
            # update status
            StudyView1_bottomsideword.status = STARTED
            StudyView1_bottomsideword.setAutoDraw(True)
        
        # if StudyView1_bottomsideword is active this frame...
        if StudyView1_bottomsideword.status == STARTED:
            # update params
            pass
        
        # if StudyView1_bottomsideword is stopping this frame...
        if StudyView1_bottomsideword.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView1_bottomsideword.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                StudyView1_bottomsideword.tStop = t  # not accounting for scr refresh
                StudyView1_bottomsideword.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword.stopped')
                # update status
                StudyView1_bottomsideword.status = FINISHED
                StudyView1_bottomsideword.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyView1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "StudyView1" ---
    for thisComponent in StudyView1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Study1Response.keys in ['', [], None]:  # No response was made
        Study1Response.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           Study1Response.corr = 1;  # correct non-response
        else:
           Study1Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Study1Loop (TrialHandler)
    Study1Loop.addData('Study1Response.keys',Study1Response.keys)
    Study1Loop.addData('Study1Response.corr', Study1Response.corr)
    if Study1Response.keys != None:  # we had a response
        Study1Loop.addData('Study1Response.rt', Study1Response.rt)
    # Run 'End Routine' code from test_3
    errormsg=''
    #fbkimagefile = ''
    
    WordIndex
    
    if random()>.5 and Study1Response.keys : # coin flip to determine if response was correct
        responseiscorrect = True
        respbox_color = 'green'
        fbkimagefile = 'checkmark.png'
        r1correct_list[WordIndex-1] = True
        if Study1Response.keys == key_list[0]: #first word selected, response is last key pressed
            responseside = 'top'
            correctside = 'top'
    #        correctword = R1Word1
            respbox_y = 0.1
            if r1reversed == True:
                correctwordindex=2
                correctword = R1Word2
            else:
                correctwordindex=1
                correctword = R1Word1
        else: #second word selected
            responseside = 'bottom'
            correctside = 'bottom'
    #        correctword = R1Word2
            respbox_y = -.05
            if r1reversed == True:
                correctwordindex=1
                correctword = R1Word1
            else:
                correctwordindex=2
                correctword = R1Word2
    elif Study1Response.keys : #response is made but incorrect (by coin flip above)
        responseiscorrect = False
        fbkimagefile = 'X_mark.png'
        respbox_color = 'red'
        r1correct_list[WordIndex-1] = False
        if Study1Response.keys == key_list[0]: #first word selected
            responseside = 'top'
            correctside = 'bottom'
    #        correctword = R1Word2
            respbox_y = 0.1
            if r1reversed:
                correctwordindex=1
                correctword = R1Word1
            else:
                correctwordindex=2
                correctword = R1Word2
        else:
            responseside = 'bottom'
            correctside = 'top'
    #        correctword = R1Word1
            respbox_y = -0.05
            if r1reversed:
                correctwordindex=2
                correctword = R1Word2
            else:
                correctwordindex=1
                correctword = R1Word1
    else:
        #no response
        responseiscorrect = False
        r1correct_list[WordIndex-1] = False
        responseside = 'miss'
        fbkimagefile = 'poundkey.png'
        respbox_color = background_color
        respbox_y = 1
        errormsg = 'no response'
        if random()>.5:
            correctside = 'top'
    #        correctword = R1Word1
            if r1reversed:
                correctwordindex=2
                correctword = R1Word2
            else:
                correctwordindex=1
                correctword = R1Word1
        else:
            correctside = 'bottom'
    #        correctword = R1Word2
            if r1reversed:
                correctwordindex=1
                correctword = R1Word1
            else:
                correctwordindex=2
                correctword = R1Word2
    #if Study1Response.keys:
    #    showrespdur = studyviewwindow - Study1Response.rt
    #else:
    #    showrespdur = 0
    if correctside == responseside:
        responseiscorrect = True
    else: 
        responseiscorrect = False
    correctword_list[WordIndex-1] = correctwordindex
    thisExp.addData('r1reversed',r1reversed)
    #thisExp.addData('topsideword', topsideword)
    #thisExp.addData('bottomsideword', bottomsideword)
    thisExp.addData('responseiscorrect', responseiscorrect)
    thisExp.addData('responseside', responseside)
    thisExp.addData('correctside',correctside)
    thisExp.addData('correctword',correctword)
    thisExp.addData('correctwordindex',correctwordindex)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ShowResp" ---
    continueRoutine = True
    # update component parameters for each repeat
    highlightbox_showresp.setPos((0, respbox_y))
    highlightbox_showresp.setLineColor(selectbox_color)
    Fbk_target_showresp.setText(targetword)
    Fbk_topsideword_showresp.setPos((0, topword_offset))
    Fbk_topsideword_showresp.setText(x + R1Word1)
    Fbk_bottomsideword_showresp.setPos((0, bottomword_offset))
    Fbk_bottomsideword_showresp.setText(y + R1Word2)
    # keep track of which components have finished
    ShowRespComponents = [highlightbox_showresp, Fbk_target_showresp, Fbk_topsideword_showresp, Fbk_bottomsideword_showresp]
    for thisComponent in ShowRespComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ShowResp" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *highlightbox_showresp* updates
        
        # if highlightbox_showresp is starting this frame...
        if highlightbox_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            highlightbox_showresp.frameNStart = frameN  # exact frame index
            highlightbox_showresp.tStart = t  # local t and not account for scr refresh
            highlightbox_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(highlightbox_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'highlightbox_showresp.started')
            # update status
            highlightbox_showresp.status = STARTED
            highlightbox_showresp.setAutoDraw(True)
        
        # if highlightbox_showresp is active this frame...
        if highlightbox_showresp.status == STARTED:
            # update params
            pass
        
        # if highlightbox_showresp is stopping this frame...
        if highlightbox_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > highlightbox_showresp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                highlightbox_showresp.tStop = t  # not accounting for scr refresh
                highlightbox_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'highlightbox_showresp.stopped')
                # update status
                highlightbox_showresp.status = FINISHED
                highlightbox_showresp.setAutoDraw(False)
        
        # *Fbk_target_showresp* updates
        
        # if Fbk_target_showresp is starting this frame...
        if Fbk_target_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_target_showresp.frameNStart = frameN  # exact frame index
            Fbk_target_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_target_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_target_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_target_showresp.started')
            # update status
            Fbk_target_showresp.status = STARTED
            Fbk_target_showresp.setAutoDraw(True)
        
        # if Fbk_target_showresp is active this frame...
        if Fbk_target_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_target_showresp is stopping this frame...
        if Fbk_target_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_target_showresp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_target_showresp.tStop = t  # not accounting for scr refresh
                Fbk_target_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_target_showresp.stopped')
                # update status
                Fbk_target_showresp.status = FINISHED
                Fbk_target_showresp.setAutoDraw(False)
        
        # *Fbk_topsideword_showresp* updates
        
        # if Fbk_topsideword_showresp is starting this frame...
        if Fbk_topsideword_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_topsideword_showresp.frameNStart = frameN  # exact frame index
            Fbk_topsideword_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_topsideword_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_topsideword_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_topsideword_showresp.started')
            # update status
            Fbk_topsideword_showresp.status = STARTED
            Fbk_topsideword_showresp.setAutoDraw(True)
        
        # if Fbk_topsideword_showresp is active this frame...
        if Fbk_topsideword_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_topsideword_showresp is stopping this frame...
        if Fbk_topsideword_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_topsideword_showresp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_topsideword_showresp.tStop = t  # not accounting for scr refresh
                Fbk_topsideword_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_topsideword_showresp.stopped')
                # update status
                Fbk_topsideword_showresp.status = FINISHED
                Fbk_topsideword_showresp.setAutoDraw(False)
        
        # *Fbk_bottomsideword_showresp* updates
        
        # if Fbk_bottomsideword_showresp is starting this frame...
        if Fbk_bottomsideword_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_bottomsideword_showresp.frameNStart = frameN  # exact frame index
            Fbk_bottomsideword_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_bottomsideword_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_bottomsideword_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_bottomsideword_showresp.started')
            # update status
            Fbk_bottomsideword_showresp.status = STARTED
            Fbk_bottomsideword_showresp.setAutoDraw(True)
        
        # if Fbk_bottomsideword_showresp is active this frame...
        if Fbk_bottomsideword_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_bottomsideword_showresp is stopping this frame...
        if Fbk_bottomsideword_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_bottomsideword_showresp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_bottomsideword_showresp.tStop = t  # not accounting for scr refresh
                Fbk_bottomsideword_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_bottomsideword_showresp.stopped')
                # update status
                Fbk_bottomsideword_showresp.status = FINISHED
                Fbk_bottomsideword_showresp.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ShowRespComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ShowResp" ---
    for thisComponent in ShowRespComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Fbk1" ---
    continueRoutine = True
    # update component parameters for each repeat
    resp_highlightbox.setPos((0, respbox_y))
    resp_highlightbox.setLineColor(respbox_color)
    Fbk_target.setText(targetword)
    Fbk_topsideword.setPos((0,topword_offset))
    Fbk_topsideword.setText(x + R1Word1)
    Fbk_bottomsideword.setPos((0, bottomword_offset))
    Fbk_bottomsideword.setText(y + R1Word2)
    FbkImage.setPos([0, -.285])
    FbkImage.setImage(fbkimagefile)
    Error_message.setText(errormsg)
    # keep track of which components have finished
    Fbk1Components = [resp_highlightbox, Fbk_target, Fbk_topsideword, Fbk_bottomsideword, FbkImage, Error_message]
    for thisComponent in Fbk1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fbk1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_highlightbox* updates
        
        # if resp_highlightbox is starting this frame...
        if resp_highlightbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_highlightbox.frameNStart = frameN  # exact frame index
            resp_highlightbox.tStart = t  # local t and not account for scr refresh
            resp_highlightbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_highlightbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_highlightbox.started')
            # update status
            resp_highlightbox.status = STARTED
            resp_highlightbox.setAutoDraw(True)
        
        # if resp_highlightbox is active this frame...
        if resp_highlightbox.status == STARTED:
            # update params
            pass
        
        # if resp_highlightbox is stopping this frame...
        if resp_highlightbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_highlightbox.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                resp_highlightbox.tStop = t  # not accounting for scr refresh
                resp_highlightbox.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp_highlightbox.stopped')
                # update status
                resp_highlightbox.status = FINISHED
                resp_highlightbox.setAutoDraw(False)
        
        # *Fbk_target* updates
        
        # if Fbk_target is starting this frame...
        if Fbk_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_target.frameNStart = frameN  # exact frame index
            Fbk_target.tStart = t  # local t and not account for scr refresh
            Fbk_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_target.started')
            # update status
            Fbk_target.status = STARTED
            Fbk_target.setAutoDraw(True)
        
        # if Fbk_target is active this frame...
        if Fbk_target.status == STARTED:
            # update params
            pass
        
        # if Fbk_target is stopping this frame...
        if Fbk_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_target.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_target.tStop = t  # not accounting for scr refresh
                Fbk_target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_target.stopped')
                # update status
                Fbk_target.status = FINISHED
                Fbk_target.setAutoDraw(False)
        
        # *Fbk_topsideword* updates
        
        # if Fbk_topsideword is starting this frame...
        if Fbk_topsideword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_topsideword.frameNStart = frameN  # exact frame index
            Fbk_topsideword.tStart = t  # local t and not account for scr refresh
            Fbk_topsideword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_topsideword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_topsideword.started')
            # update status
            Fbk_topsideword.status = STARTED
            Fbk_topsideword.setAutoDraw(True)
        
        # if Fbk_topsideword is active this frame...
        if Fbk_topsideword.status == STARTED:
            # update params
            pass
        
        # if Fbk_topsideword is stopping this frame...
        if Fbk_topsideword.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_topsideword.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_topsideword.tStop = t  # not accounting for scr refresh
                Fbk_topsideword.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_topsideword.stopped')
                # update status
                Fbk_topsideword.status = FINISHED
                Fbk_topsideword.setAutoDraw(False)
        
        # *Fbk_bottomsideword* updates
        
        # if Fbk_bottomsideword is starting this frame...
        if Fbk_bottomsideword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_bottomsideword.frameNStart = frameN  # exact frame index
            Fbk_bottomsideword.tStart = t  # local t and not account for scr refresh
            Fbk_bottomsideword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_bottomsideword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_bottomsideword.started')
            # update status
            Fbk_bottomsideword.status = STARTED
            Fbk_bottomsideword.setAutoDraw(True)
        
        # if Fbk_bottomsideword is active this frame...
        if Fbk_bottomsideword.status == STARTED:
            # update params
            pass
        
        # if Fbk_bottomsideword is stopping this frame...
        if Fbk_bottomsideword.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_bottomsideword.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_bottomsideword.tStop = t  # not accounting for scr refresh
                Fbk_bottomsideword.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_bottomsideword.stopped')
                # update status
                Fbk_bottomsideword.status = FINISHED
                Fbk_bottomsideword.setAutoDraw(False)
        
        # *FbkImage* updates
        
        # if FbkImage is starting this frame...
        if FbkImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FbkImage.frameNStart = frameN  # exact frame index
            FbkImage.tStart = t  # local t and not account for scr refresh
            FbkImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FbkImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FbkImage.started')
            # update status
            FbkImage.status = STARTED
            FbkImage.setAutoDraw(True)
        
        # if FbkImage is active this frame...
        if FbkImage.status == STARTED:
            # update params
            pass
        
        # if FbkImage is stopping this frame...
        if FbkImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FbkImage.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                FbkImage.tStop = t  # not accounting for scr refresh
                FbkImage.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FbkImage.stopped')
                # update status
                FbkImage.status = FINISHED
                FbkImage.setAutoDraw(False)
        
        # *Error_message* updates
        
        # if Error_message is starting this frame...
        if Error_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Error_message.frameNStart = frameN  # exact frame index
            Error_message.tStart = t  # local t and not account for scr refresh
            Error_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Error_message, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Error_message.started')
            # update status
            Error_message.status = STARTED
            Error_message.setAutoDraw(True)
        
        # if Error_message is active this frame...
        if Error_message.status == STARTED:
            # update params
            pass
        
        # if Error_message is stopping this frame...
        if Error_message.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Error_message.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                Error_message.tStop = t  # not accounting for scr refresh
                Error_message.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Error_message.stopped')
                # update status
                Error_message.status = FINISHED
                Error_message.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fbk1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fbk1" ---
    for thisComponent in Fbk1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Fbk1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Study1Loop'


# --- Prepare to start Routine "EndPart1" ---
continueRoutine = True
# update component parameters for each repeat
contpart2.keys = []
contpart2.rt = []
_contpart2_allKeys = []
# keep track of which components have finished
EndPart1Components = [text, contpart2]
for thisComponent in EndPart1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndPart1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # *contpart2* updates
    waitOnFlip = False
    
    # if contpart2 is starting this frame...
    if contpart2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contpart2.frameNStart = frameN  # exact frame index
        contpart2.tStart = t  # local t and not account for scr refresh
        contpart2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contpart2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'contpart2.started')
        # update status
        contpart2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(contpart2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(contpart2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if contpart2.status == STARTED and not waitOnFlip:
        theseKeys = contpart2.getKeys(keyList=['t'], waitRelease=False)
        _contpart2_allKeys.extend(theseKeys)
        if len(_contpart2_allKeys):
            contpart2.keys = _contpart2_allKeys[-1].name  # just the last key pressed
            contpart2.rt = _contpart2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndPart1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndPart1" ---
for thisComponent in EndPart1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if contpart2.keys in ['', [], None]:  # No response was made
    contpart2.keys = None
thisExp.addData('contpart2.keys',contpart2.keys)
if contpart2.keys != None:  # we had a response
    thisExp.addData('contpart2.rt', contpart2.rt)
thisExp.nextEntry()
# the Routine "EndPart1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instruct4" ---
continueRoutine = True
# update component parameters for each repeat
Instructresp_3.keys = []
Instructresp_3.rt = []
_Instructresp_3_allKeys = []
# keep track of which components have finished
Instruct4Components = [Instruct2a_text, Instructresp_3]
for thisComponent in Instruct4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruct4" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct2a_text* updates
    
    # if Instruct2a_text is starting this frame...
    if Instruct2a_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct2a_text.frameNStart = frameN  # exact frame index
        Instruct2a_text.tStart = t  # local t and not account for scr refresh
        Instruct2a_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct2a_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instruct2a_text.started')
        # update status
        Instruct2a_text.status = STARTED
        Instruct2a_text.setAutoDraw(True)
    
    # if Instruct2a_text is active this frame...
    if Instruct2a_text.status == STARTED:
        # update params
        pass
    
    # *Instructresp_3* updates
    waitOnFlip = False
    
    # if Instructresp_3 is starting this frame...
    if Instructresp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructresp_3.frameNStart = frameN  # exact frame index
        Instructresp_3.tStart = t  # local t and not account for scr refresh
        Instructresp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructresp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructresp_3.started')
        # update status
        Instructresp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instructresp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instructresp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instructresp_3.status == STARTED and not waitOnFlip:
        theseKeys = Instructresp_3.getKeys(keyList=['t'], waitRelease=False)
        _Instructresp_3_allKeys.extend(theseKeys)
        if len(_Instructresp_3_allKeys):
            Instructresp_3.keys = _Instructresp_3_allKeys[-1].name  # just the last key pressed
            Instructresp_3.rt = _Instructresp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruct4" ---
for thisComponent in Instruct4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruct4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instruct4_2" ---
continueRoutine = True
# update component parameters for each repeat
Instructresp_4.keys = []
Instructresp_4.rt = []
_Instructresp_4_allKeys = []
# keep track of which components have finished
Instruct4_2Components = [Instruct2b_text, Instructresp_4]
for thisComponent in Instruct4_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruct4_2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct2b_text* updates
    
    # if Instruct2b_text is starting this frame...
    if Instruct2b_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct2b_text.frameNStart = frameN  # exact frame index
        Instruct2b_text.tStart = t  # local t and not account for scr refresh
        Instruct2b_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct2b_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instruct2b_text.started')
        # update status
        Instruct2b_text.status = STARTED
        Instruct2b_text.setAutoDraw(True)
    
    # if Instruct2b_text is active this frame...
    if Instruct2b_text.status == STARTED:
        # update params
        pass
    
    # *Instructresp_4* updates
    waitOnFlip = False
    
    # if Instructresp_4 is starting this frame...
    if Instructresp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructresp_4.frameNStart = frameN  # exact frame index
        Instructresp_4.tStart = t  # local t and not account for scr refresh
        Instructresp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructresp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructresp_4.started')
        # update status
        Instructresp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instructresp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instructresp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instructresp_4.status == STARTED and not waitOnFlip:
        theseKeys = Instructresp_4.getKeys(keyList=['2'], waitRelease=False)
        _Instructresp_4_allKeys.extend(theseKeys)
        if len(_Instructresp_4_allKeys):
            Instructresp_4.keys = _Instructresp_4_allKeys[-1].name  # just the last key pressed
            Instructresp_4.rt = _Instructresp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct4_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruct4_2" ---
for thisComponent in Instruct4_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruct4_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GetReady" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GetReadyComponents = [fixation, text_4]
for thisComponent in GetReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GetReady" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation* updates
    
    # if fixation is starting this frame...
    if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation.frameNStart = frameN  # exact frame index
        fixation.tStart = t  # local t and not account for scr refresh
        fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation.started')
        # update status
        fixation.status = STARTED
        fixation.setAutoDraw(True)
    
    # if fixation is active this frame...
    if fixation.status == STARTED:
        # update params
        pass
    
    # if fixation is stopping this frame...
    if fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.stopped')
            # update status
            fixation.status = FINISHED
            fixation.setAutoDraw(False)
    
    # *text_4* updates
    
    # if text_4 is starting this frame...
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        # update status
        text_4.status = STARTED
        text_4.setAutoDraw(True)
    
    # if text_4 is active this frame...
    if text_4.status == STARTED:
        # update params
        pass
    
    # if text_4 is stopping this frame...
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            # update status
            text_4.status = FINISHED
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GetReady" ---
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# set up handler to look after randomisation of conditions etc
Study2Loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StimFile_A.xlsx'),
    seed=None, name='Study2Loop')
thisExp.addLoop(Study2Loop)  # add the loop to the experiment
thisStudy2Loop = Study2Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy2Loop.rgb)
if thisStudy2Loop != None:
    for paramName in thisStudy2Loop:
        exec('{} = thisStudy2Loop[paramName]'.format(paramName))

for thisStudy2Loop in Study2Loop:
    currentLoop = Study2Loop
    # abbreviate parameter names if possible (e.g. rgb = thisStudy2Loop.rgb)
    if thisStudy2Loop != None:
        for paramName in thisStudy2Loop:
            exec('{} = thisStudy2Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "StudyView4" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from PlaceWords_2
    
    
    if random()>.5:
        topword_offset = .1
        bottomword_offset = -.05
        r2reversed = False
        x = '1) ' 
        y = '2) '
    else:
        topword_offset = -.05
        bottomword_offset = .1
        r2reversed = True
        x = '2) ' 
        y = '1) '
    thisExp.addData('r2reversed',r2reversed)
    
    
    #trialfbkcost = fbkcost_list[WordIndex-1]
    #costnum = fbkcostlevels[idy]
    #print(costnum)
    #costnum = str(abs(trialfbkcost))
    #if trialfbkcost > 0:
    #    fbk_question = "Do you want feedback?\n (+%s cents if you choose YES)" % costnum
    #    costsign = '+'
    #else:
    #    fbk_question = "Do you want feedback?\n (-%s cents if you choose YES)" % costnum
    #    costsign = '-'
    
    StudyView1_target_2.setText(targetword)
    StudyView_topsideword_2.setPos((0, topword_offset))
    StudyView_topsideword_2.setText(x + R1Word1)
    StudyView1_bottomsideword_2.setPos((0, bottomword_offset))
    StudyView1_bottomsideword_2.setText(y + R1Word2)
    Study2Response.keys = []
    Study2Response.rt = []
    _Study2Response_allKeys = []
    # keep track of which components have finished
    StudyView4Components = [StudyView1_target_2, StudyView_topsideword_2, StudyView1_bottomsideword_2, Study2Response, slowrespmessage_conf_2]
    for thisComponent in StudyView4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "StudyView4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StudyView1_target_2* updates
        
        # if StudyView1_target_2 is starting this frame...
        if StudyView1_target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView1_target_2.frameNStart = frameN  # exact frame index
            StudyView1_target_2.tStart = t  # local t and not account for scr refresh
            StudyView1_target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView1_target_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView1_target_2.started')
            # update status
            StudyView1_target_2.status = STARTED
            StudyView1_target_2.setAutoDraw(True)
        
        # if StudyView1_target_2 is active this frame...
        if StudyView1_target_2.status == STARTED:
            # update params
            pass
        
        # if StudyView1_target_2 is stopping this frame...
        if StudyView1_target_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView1_target_2.tStartRefresh + study2dur-frameTolerance:
                # keep track of stop time/frame for later
                StudyView1_target_2.tStop = t  # not accounting for scr refresh
                StudyView1_target_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView1_target_2.stopped')
                # update status
                StudyView1_target_2.status = FINISHED
                StudyView1_target_2.setAutoDraw(False)
        
        # *StudyView_topsideword_2* updates
        
        # if StudyView_topsideword_2 is starting this frame...
        if StudyView_topsideword_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView_topsideword_2.frameNStart = frameN  # exact frame index
            StudyView_topsideword_2.tStart = t  # local t and not account for scr refresh
            StudyView_topsideword_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView_topsideword_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView_topsideword_2.started')
            # update status
            StudyView_topsideword_2.status = STARTED
            StudyView_topsideword_2.setAutoDraw(True)
        
        # if StudyView_topsideword_2 is active this frame...
        if StudyView_topsideword_2.status == STARTED:
            # update params
            pass
        
        # if StudyView_topsideword_2 is stopping this frame...
        if StudyView_topsideword_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView_topsideword_2.tStartRefresh + study2dur-frameTolerance:
                # keep track of stop time/frame for later
                StudyView_topsideword_2.tStop = t  # not accounting for scr refresh
                StudyView_topsideword_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView_topsideword_2.stopped')
                # update status
                StudyView_topsideword_2.status = FINISHED
                StudyView_topsideword_2.setAutoDraw(False)
        
        # *StudyView1_bottomsideword_2* updates
        
        # if StudyView1_bottomsideword_2 is starting this frame...
        if StudyView1_bottomsideword_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView1_bottomsideword_2.frameNStart = frameN  # exact frame index
            StudyView1_bottomsideword_2.tStart = t  # local t and not account for scr refresh
            StudyView1_bottomsideword_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView1_bottomsideword_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword_2.started')
            # update status
            StudyView1_bottomsideword_2.status = STARTED
            StudyView1_bottomsideword_2.setAutoDraw(True)
        
        # if StudyView1_bottomsideword_2 is active this frame...
        if StudyView1_bottomsideword_2.status == STARTED:
            # update params
            pass
        
        # if StudyView1_bottomsideword_2 is stopping this frame...
        if StudyView1_bottomsideword_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView1_bottomsideword_2.tStartRefresh + study2dur-frameTolerance:
                # keep track of stop time/frame for later
                StudyView1_bottomsideword_2.tStop = t  # not accounting for scr refresh
                StudyView1_bottomsideword_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword_2.stopped')
                # update status
                StudyView1_bottomsideword_2.status = FINISHED
                StudyView1_bottomsideword_2.setAutoDraw(False)
        
        # *Study2Response* updates
        waitOnFlip = False
        
        # if Study2Response is starting this frame...
        if Study2Response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Study2Response.frameNStart = frameN  # exact frame index
            Study2Response.tStart = t  # local t and not account for scr refresh
            Study2Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Study2Response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Study2Response.started')
            # update status
            Study2Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Study2Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Study2Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Study2Response.status == STARTED and not waitOnFlip:
            theseKeys = Study2Response.getKeys(keyList=['1','2'], waitRelease=False)
            _Study2Response_allKeys.extend(theseKeys)
            if len(_Study2Response_allKeys):
                Study2Response.keys = _Study2Response_allKeys[-1].name  # just the last key pressed
                Study2Response.rt = _Study2Response_allKeys[-1].rt
                # was this correct?
                if (Study2Response.keys == str(correctkey)) or (Study2Response.keys == correctkey):
                    Study2Response.corr = 1
                else:
                    Study2Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *slowrespmessage_conf_2* updates
        
        # if slowrespmessage_conf_2 is starting this frame...
        if slowrespmessage_conf_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            slowrespmessage_conf_2.frameNStart = frameN  # exact frame index
            slowrespmessage_conf_2.tStart = t  # local t and not account for scr refresh
            slowrespmessage_conf_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slowrespmessage_conf_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slowrespmessage_conf_2.started')
            # update status
            slowrespmessage_conf_2.status = STARTED
            slowrespmessage_conf_2.setAutoDraw(True)
        
        # if slowrespmessage_conf_2 is active this frame...
        if slowrespmessage_conf_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyView4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "StudyView4" ---
    for thisComponent in StudyView4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Study2Response.keys in ['', [], None]:  # No response was made
        Study2Response.keys = None
        # was no response the correct answer?!
        if str(correctkey).lower() == 'none':
           Study2Response.corr = 1;  # correct non-response
        else:
           Study2Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Study2Loop (TrialHandler)
    Study2Loop.addData('Study2Response.keys',Study2Response.keys)
    Study2Loop.addData('Study2Response.corr', Study2Response.corr)
    if Study2Response.keys != None:  # we had a response
        Study2Loop.addData('Study2Response.rt', Study2Response.rt)
    # the Routine "StudyView4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ShowResp" ---
    continueRoutine = True
    # update component parameters for each repeat
    highlightbox_showresp.setPos((0, respbox_y))
    highlightbox_showresp.setLineColor(selectbox_color)
    Fbk_target_showresp.setText(targetword)
    Fbk_topsideword_showresp.setPos((0, topword_offset))
    Fbk_topsideword_showresp.setText(x + R1Word1)
    Fbk_bottomsideword_showresp.setPos((0, bottomword_offset))
    Fbk_bottomsideword_showresp.setText(y + R1Word2)
    # keep track of which components have finished
    ShowRespComponents = [highlightbox_showresp, Fbk_target_showresp, Fbk_topsideword_showresp, Fbk_bottomsideword_showresp]
    for thisComponent in ShowRespComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ShowResp" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *highlightbox_showresp* updates
        
        # if highlightbox_showresp is starting this frame...
        if highlightbox_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            highlightbox_showresp.frameNStart = frameN  # exact frame index
            highlightbox_showresp.tStart = t  # local t and not account for scr refresh
            highlightbox_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(highlightbox_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'highlightbox_showresp.started')
            # update status
            highlightbox_showresp.status = STARTED
            highlightbox_showresp.setAutoDraw(True)
        
        # if highlightbox_showresp is active this frame...
        if highlightbox_showresp.status == STARTED:
            # update params
            pass
        
        # if highlightbox_showresp is stopping this frame...
        if highlightbox_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > highlightbox_showresp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                highlightbox_showresp.tStop = t  # not accounting for scr refresh
                highlightbox_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'highlightbox_showresp.stopped')
                # update status
                highlightbox_showresp.status = FINISHED
                highlightbox_showresp.setAutoDraw(False)
        
        # *Fbk_target_showresp* updates
        
        # if Fbk_target_showresp is starting this frame...
        if Fbk_target_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_target_showresp.frameNStart = frameN  # exact frame index
            Fbk_target_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_target_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_target_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_target_showresp.started')
            # update status
            Fbk_target_showresp.status = STARTED
            Fbk_target_showresp.setAutoDraw(True)
        
        # if Fbk_target_showresp is active this frame...
        if Fbk_target_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_target_showresp is stopping this frame...
        if Fbk_target_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_target_showresp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_target_showresp.tStop = t  # not accounting for scr refresh
                Fbk_target_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_target_showresp.stopped')
                # update status
                Fbk_target_showresp.status = FINISHED
                Fbk_target_showresp.setAutoDraw(False)
        
        # *Fbk_topsideword_showresp* updates
        
        # if Fbk_topsideword_showresp is starting this frame...
        if Fbk_topsideword_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_topsideword_showresp.frameNStart = frameN  # exact frame index
            Fbk_topsideword_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_topsideword_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_topsideword_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_topsideword_showresp.started')
            # update status
            Fbk_topsideword_showresp.status = STARTED
            Fbk_topsideword_showresp.setAutoDraw(True)
        
        # if Fbk_topsideword_showresp is active this frame...
        if Fbk_topsideword_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_topsideword_showresp is stopping this frame...
        if Fbk_topsideword_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_topsideword_showresp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_topsideword_showresp.tStop = t  # not accounting for scr refresh
                Fbk_topsideword_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_topsideword_showresp.stopped')
                # update status
                Fbk_topsideword_showresp.status = FINISHED
                Fbk_topsideword_showresp.setAutoDraw(False)
        
        # *Fbk_bottomsideword_showresp* updates
        
        # if Fbk_bottomsideword_showresp is starting this frame...
        if Fbk_bottomsideword_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_bottomsideword_showresp.frameNStart = frameN  # exact frame index
            Fbk_bottomsideword_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_bottomsideword_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_bottomsideword_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_bottomsideword_showresp.started')
            # update status
            Fbk_bottomsideword_showresp.status = STARTED
            Fbk_bottomsideword_showresp.setAutoDraw(True)
        
        # if Fbk_bottomsideword_showresp is active this frame...
        if Fbk_bottomsideword_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_bottomsideword_showresp is stopping this frame...
        if Fbk_bottomsideword_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_bottomsideword_showresp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_bottomsideword_showresp.tStop = t  # not accounting for scr refresh
                Fbk_bottomsideword_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_bottomsideword_showresp.stopped')
                # update status
                Fbk_bottomsideword_showresp.status = FINISHED
                Fbk_bottomsideword_showresp.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ShowRespComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ShowResp" ---
    for thisComponent in ShowRespComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Confidence" ---
    continueRoutine = True
    # update component parameters for each repeat
    R2_highlightbox_conf.setPos((0, respbox_y))
    R2_highlightbox_conf.setLineColor(selectbox_color)
    R2_target_conf.setText(targetword)
    R2_word1_conf.setPos((0, topword_offset))
    R2_word1_conf.setText(x + R1Word1)
    R2_word2_conf.setPos((0, bottomword_offset))
    R2_word2_conf.setText(y + R1Word2)
    confresp.keys = []
    confresp.rt = []
    _confresp_allKeys = []
    # keep track of which components have finished
    ConfidenceComponents = [R2_highlightbox_conf, R2_target_conf, R2_word1_conf, R2_word2_conf, conf_question, confscale_numbers, confresp, slowrespmessage_conf]
    for thisComponent in ConfidenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Confidence" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *R2_highlightbox_conf* updates
        
        # if R2_highlightbox_conf is starting this frame...
        if R2_highlightbox_conf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_highlightbox_conf.frameNStart = frameN  # exact frame index
            R2_highlightbox_conf.tStart = t  # local t and not account for scr refresh
            R2_highlightbox_conf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_highlightbox_conf, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_highlightbox_conf.started')
            # update status
            R2_highlightbox_conf.status = STARTED
            R2_highlightbox_conf.setAutoDraw(True)
        
        # if R2_highlightbox_conf is active this frame...
        if R2_highlightbox_conf.status == STARTED:
            # update params
            pass
        
        # *R2_target_conf* updates
        
        # if R2_target_conf is starting this frame...
        if R2_target_conf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_target_conf.frameNStart = frameN  # exact frame index
            R2_target_conf.tStart = t  # local t and not account for scr refresh
            R2_target_conf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_target_conf, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_target_conf.started')
            # update status
            R2_target_conf.status = STARTED
            R2_target_conf.setAutoDraw(True)
        
        # if R2_target_conf is active this frame...
        if R2_target_conf.status == STARTED:
            # update params
            pass
        
        # *R2_word1_conf* updates
        
        # if R2_word1_conf is starting this frame...
        if R2_word1_conf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_word1_conf.frameNStart = frameN  # exact frame index
            R2_word1_conf.tStart = t  # local t and not account for scr refresh
            R2_word1_conf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_word1_conf, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_word1_conf.started')
            # update status
            R2_word1_conf.status = STARTED
            R2_word1_conf.setAutoDraw(True)
        
        # if R2_word1_conf is active this frame...
        if R2_word1_conf.status == STARTED:
            # update params
            pass
        
        # *R2_word2_conf* updates
        
        # if R2_word2_conf is starting this frame...
        if R2_word2_conf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_word2_conf.frameNStart = frameN  # exact frame index
            R2_word2_conf.tStart = t  # local t and not account for scr refresh
            R2_word2_conf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_word2_conf, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_word2_conf.started')
            # update status
            R2_word2_conf.status = STARTED
            R2_word2_conf.setAutoDraw(True)
        
        # if R2_word2_conf is active this frame...
        if R2_word2_conf.status == STARTED:
            # update params
            pass
        
        # *conf_question* updates
        
        # if conf_question is starting this frame...
        if conf_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            conf_question.frameNStart = frameN  # exact frame index
            conf_question.tStart = t  # local t and not account for scr refresh
            conf_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(conf_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'conf_question.started')
            # update status
            conf_question.status = STARTED
            conf_question.setAutoDraw(True)
        
        # if conf_question is active this frame...
        if conf_question.status == STARTED:
            # update params
            pass
        
        # *confscale_numbers* updates
        
        # if confscale_numbers is starting this frame...
        if confscale_numbers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confscale_numbers.frameNStart = frameN  # exact frame index
            confscale_numbers.tStart = t  # local t and not account for scr refresh
            confscale_numbers.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confscale_numbers, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confscale_numbers.started')
            # update status
            confscale_numbers.status = STARTED
            confscale_numbers.setAutoDraw(True)
        
        # if confscale_numbers is active this frame...
        if confscale_numbers.status == STARTED:
            # update params
            pass
        
        # *confresp* updates
        waitOnFlip = False
        
        # if confresp is starting this frame...
        if confresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confresp.frameNStart = frameN  # exact frame index
            confresp.tStart = t  # local t and not account for scr refresh
            confresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confresp.started')
            # update status
            confresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(confresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(confresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if confresp.status == STARTED and not waitOnFlip:
            theseKeys = confresp.getKeys(keyList=['1','2','3','4','5','6'], waitRelease=False)
            _confresp_allKeys.extend(theseKeys)
            if len(_confresp_allKeys):
                confresp.keys = _confresp_allKeys[-1].name  # just the last key pressed
                confresp.rt = _confresp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *slowrespmessage_conf* updates
        
        # if slowrespmessage_conf is starting this frame...
        if slowrespmessage_conf.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            slowrespmessage_conf.frameNStart = frameN  # exact frame index
            slowrespmessage_conf.tStart = t  # local t and not account for scr refresh
            slowrespmessage_conf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slowrespmessage_conf, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slowrespmessage_conf.started')
            # update status
            slowrespmessage_conf.status = STARTED
            slowrespmessage_conf.setAutoDraw(True)
        
        # if slowrespmessage_conf is active this frame...
        if slowrespmessage_conf.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConfidenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Confidence" ---
    for thisComponent in ConfidenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if confresp.keys in ['', [], None]:  # No response was made
        confresp.keys = None
    Study2Loop.addData('confresp.keys',confresp.keys)
    if confresp.keys != None:  # we had a response
        Study2Loop.addData('confresp.rt', confresp.rt)
    # the Routine "Confidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ChooseFbk" ---
    continueRoutine = True
    # update component parameters for each repeat
    R2_FbkQuestion.setText(fbk_question)
    fbkchoice_resp.keys = []
    fbkchoice_resp.rt = []
    _fbkchoice_resp_allKeys = []
    fbkcosttext.setText(fbkcostlevels[idy])
    fbknocosttext.setText('  0')
    # keep track of which components have finished
    ChooseFbkComponents = [R2_FbkQuestion, fbkchoice_resp, fbkcosttext, R2_fbkyes, R2_fbkno, slowrespmessage_fbk, fbknocosttext]
    for thisComponent in ChooseFbkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ChooseFbk" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *R2_FbkQuestion* updates
        
        # if R2_FbkQuestion is starting this frame...
        if R2_FbkQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_FbkQuestion.frameNStart = frameN  # exact frame index
            R2_FbkQuestion.tStart = t  # local t and not account for scr refresh
            R2_FbkQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_FbkQuestion, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_FbkQuestion.started')
            # update status
            R2_FbkQuestion.status = STARTED
            R2_FbkQuestion.setAutoDraw(True)
        
        # if R2_FbkQuestion is active this frame...
        if R2_FbkQuestion.status == STARTED:
            # update params
            pass
        
        # *fbkchoice_resp* updates
        waitOnFlip = False
        
        # if fbkchoice_resp is starting this frame...
        if fbkchoice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fbkchoice_resp.frameNStart = frameN  # exact frame index
            fbkchoice_resp.tStart = t  # local t and not account for scr refresh
            fbkchoice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fbkchoice_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fbkchoice_resp.started')
            # update status
            fbkchoice_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fbkchoice_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fbkchoice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fbkchoice_resp.status == STARTED and not waitOnFlip:
            theseKeys = fbkchoice_resp.getKeys(keyList=['1','2'], waitRelease=False)
            _fbkchoice_resp_allKeys.extend(theseKeys)
            if len(_fbkchoice_resp_allKeys):
                fbkchoice_resp.keys = _fbkchoice_resp_allKeys[-1].name  # just the last key pressed
                fbkchoice_resp.rt = _fbkchoice_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fbkcosttext* updates
        
        # if fbkcosttext is starting this frame...
        if fbkcosttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fbkcosttext.frameNStart = frameN  # exact frame index
            fbkcosttext.tStart = t  # local t and not account for scr refresh
            fbkcosttext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fbkcosttext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fbkcosttext.started')
            # update status
            fbkcosttext.status = STARTED
            fbkcosttext.setAutoDraw(True)
        
        # if fbkcosttext is active this frame...
        if fbkcosttext.status == STARTED:
            # update params
            pass
        
        # *R2_fbkyes* updates
        
        # if R2_fbkyes is starting this frame...
        if R2_fbkyes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_fbkyes.frameNStart = frameN  # exact frame index
            R2_fbkyes.tStart = t  # local t and not account for scr refresh
            R2_fbkyes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_fbkyes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_fbkyes.started')
            # update status
            R2_fbkyes.status = STARTED
            R2_fbkyes.setAutoDraw(True)
        
        # if R2_fbkyes is active this frame...
        if R2_fbkyes.status == STARTED:
            # update params
            pass
        
        # *R2_fbkno* updates
        
        # if R2_fbkno is starting this frame...
        if R2_fbkno.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_fbkno.frameNStart = frameN  # exact frame index
            R2_fbkno.tStart = t  # local t and not account for scr refresh
            R2_fbkno.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_fbkno, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_fbkno.started')
            # update status
            R2_fbkno.status = STARTED
            R2_fbkno.setAutoDraw(True)
        
        # if R2_fbkno is active this frame...
        if R2_fbkno.status == STARTED:
            # update params
            pass
        
        # *slowrespmessage_fbk* updates
        
        # if slowrespmessage_fbk is starting this frame...
        if slowrespmessage_fbk.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            slowrespmessage_fbk.frameNStart = frameN  # exact frame index
            slowrespmessage_fbk.tStart = t  # local t and not account for scr refresh
            slowrespmessage_fbk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slowrespmessage_fbk, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slowrespmessage_fbk.started')
            # update status
            slowrespmessage_fbk.status = STARTED
            slowrespmessage_fbk.setAutoDraw(True)
        
        # if slowrespmessage_fbk is active this frame...
        if slowrespmessage_fbk.status == STARTED:
            # update params
            pass
        
        # *fbknocosttext* updates
        
        # if fbknocosttext is starting this frame...
        if fbknocosttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fbknocosttext.frameNStart = frameN  # exact frame index
            fbknocosttext.tStart = t  # local t and not account for scr refresh
            fbknocosttext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fbknocosttext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fbknocosttext.started')
            # update status
            fbknocosttext.status = STARTED
            fbknocosttext.setAutoDraw(True)
        
        # if fbknocosttext is active this frame...
        if fbknocosttext.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChooseFbkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ChooseFbk" ---
    for thisComponent in ChooseFbkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if fbkchoice_resp.keys in ['', [], None]:  # No response was made
        fbkchoice_resp.keys = None
    Study2Loop.addData('fbkchoice_resp.keys',fbkchoice_resp.keys)
    if fbkchoice_resp.keys != None:  # we had a response
        Study2Loop.addData('fbkchoice_resp.rt', fbkchoice_resp.rt)
    # Run 'End Routine' code from setfbkchoice
    if fbkchoice_resp.keys == key_list[1]:
        fbkimagefile = 'nofeedback.png'
        respbox_color = selectbox_color
        feedback_chosen = 0
    elif fbkchoice_resp.keys == key_list[0]:
        totalspent = totalspent + trialfbkcost
        feedback_chosen = 1
    else:
        fbkimagefile = 'nofeedback.png'
        respbox_color = background_color
        feedback_chosen = -99
    
    console.log(fbkcostlevels[idy+1])
    thisExp.addData('feedbackchoice',feedback_chosen)
    thisExp.addData('feedbackcost',trialfbkcost)
    # the Routine "ChooseFbk" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Fbk2" ---
    continueRoutine = True
    # update component parameters for each repeat
    R2_resp_highlightbox.setPos((0, respbox_y))
    R2_resp_highlightbox.setLineColor(respbox_color)
    R2_Fbk_target.setText(targetword)
    R2_Fbk_topsideword.setPos((0, topword_offset))
    R2_Fbk_topsideword.setText(x + R1Word1)
    R2_Fbk_bottomsideword.setPos((0, bottomword_offset))
    R2_Fbk_bottomsideword.setText(y + R1Word2)
    R2_FbkImage.setPos([0, -.285])
    R2_FbkImage.setImage(fbkimagefile)
    R2_Error_message.setText(errormsg)
    # keep track of which components have finished
    Fbk2Components = [R2_resp_highlightbox, R2_Fbk_target, R2_Fbk_topsideword, R2_Fbk_bottomsideword, R2_FbkImage, R2_Error_message]
    for thisComponent in Fbk2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fbk2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *R2_resp_highlightbox* updates
        
        # if R2_resp_highlightbox is starting this frame...
        if R2_resp_highlightbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_resp_highlightbox.frameNStart = frameN  # exact frame index
            R2_resp_highlightbox.tStart = t  # local t and not account for scr refresh
            R2_resp_highlightbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_resp_highlightbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_resp_highlightbox.started')
            # update status
            R2_resp_highlightbox.status = STARTED
            R2_resp_highlightbox.setAutoDraw(True)
        
        # if R2_resp_highlightbox is active this frame...
        if R2_resp_highlightbox.status == STARTED:
            # update params
            pass
        
        # if R2_resp_highlightbox is stopping this frame...
        if R2_resp_highlightbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R2_resp_highlightbox.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                R2_resp_highlightbox.tStop = t  # not accounting for scr refresh
                R2_resp_highlightbox.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R2_resp_highlightbox.stopped')
                # update status
                R2_resp_highlightbox.status = FINISHED
                R2_resp_highlightbox.setAutoDraw(False)
        
        # *R2_Fbk_target* updates
        
        # if R2_Fbk_target is starting this frame...
        if R2_Fbk_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_Fbk_target.frameNStart = frameN  # exact frame index
            R2_Fbk_target.tStart = t  # local t and not account for scr refresh
            R2_Fbk_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_Fbk_target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_Fbk_target.started')
            # update status
            R2_Fbk_target.status = STARTED
            R2_Fbk_target.setAutoDraw(True)
        
        # if R2_Fbk_target is active this frame...
        if R2_Fbk_target.status == STARTED:
            # update params
            pass
        
        # if R2_Fbk_target is stopping this frame...
        if R2_Fbk_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R2_Fbk_target.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                R2_Fbk_target.tStop = t  # not accounting for scr refresh
                R2_Fbk_target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R2_Fbk_target.stopped')
                # update status
                R2_Fbk_target.status = FINISHED
                R2_Fbk_target.setAutoDraw(False)
        
        # *R2_Fbk_topsideword* updates
        
        # if R2_Fbk_topsideword is starting this frame...
        if R2_Fbk_topsideword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_Fbk_topsideword.frameNStart = frameN  # exact frame index
            R2_Fbk_topsideword.tStart = t  # local t and not account for scr refresh
            R2_Fbk_topsideword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_Fbk_topsideword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_Fbk_topsideword.started')
            # update status
            R2_Fbk_topsideword.status = STARTED
            R2_Fbk_topsideword.setAutoDraw(True)
        
        # if R2_Fbk_topsideword is active this frame...
        if R2_Fbk_topsideword.status == STARTED:
            # update params
            pass
        
        # if R2_Fbk_topsideword is stopping this frame...
        if R2_Fbk_topsideword.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R2_Fbk_topsideword.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                R2_Fbk_topsideword.tStop = t  # not accounting for scr refresh
                R2_Fbk_topsideword.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R2_Fbk_topsideword.stopped')
                # update status
                R2_Fbk_topsideword.status = FINISHED
                R2_Fbk_topsideword.setAutoDraw(False)
        
        # *R2_Fbk_bottomsideword* updates
        
        # if R2_Fbk_bottomsideword is starting this frame...
        if R2_Fbk_bottomsideword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_Fbk_bottomsideword.frameNStart = frameN  # exact frame index
            R2_Fbk_bottomsideword.tStart = t  # local t and not account for scr refresh
            R2_Fbk_bottomsideword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_Fbk_bottomsideword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_Fbk_bottomsideword.started')
            # update status
            R2_Fbk_bottomsideword.status = STARTED
            R2_Fbk_bottomsideword.setAutoDraw(True)
        
        # if R2_Fbk_bottomsideword is active this frame...
        if R2_Fbk_bottomsideword.status == STARTED:
            # update params
            pass
        
        # if R2_Fbk_bottomsideword is stopping this frame...
        if R2_Fbk_bottomsideword.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R2_Fbk_bottomsideword.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                R2_Fbk_bottomsideword.tStop = t  # not accounting for scr refresh
                R2_Fbk_bottomsideword.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R2_Fbk_bottomsideword.stopped')
                # update status
                R2_Fbk_bottomsideword.status = FINISHED
                R2_Fbk_bottomsideword.setAutoDraw(False)
        
        # *R2_FbkImage* updates
        
        # if R2_FbkImage is starting this frame...
        if R2_FbkImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_FbkImage.frameNStart = frameN  # exact frame index
            R2_FbkImage.tStart = t  # local t and not account for scr refresh
            R2_FbkImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_FbkImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_FbkImage.started')
            # update status
            R2_FbkImage.status = STARTED
            R2_FbkImage.setAutoDraw(True)
        
        # if R2_FbkImage is active this frame...
        if R2_FbkImage.status == STARTED:
            # update params
            pass
        
        # if R2_FbkImage is stopping this frame...
        if R2_FbkImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R2_FbkImage.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                R2_FbkImage.tStop = t  # not accounting for scr refresh
                R2_FbkImage.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R2_FbkImage.stopped')
                # update status
                R2_FbkImage.status = FINISHED
                R2_FbkImage.setAutoDraw(False)
        
        # *R2_Error_message* updates
        
        # if R2_Error_message is starting this frame...
        if R2_Error_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R2_Error_message.frameNStart = frameN  # exact frame index
            R2_Error_message.tStart = t  # local t and not account for scr refresh
            R2_Error_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R2_Error_message, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R2_Error_message.started')
            # update status
            R2_Error_message.status = STARTED
            R2_Error_message.setAutoDraw(True)
        
        # if R2_Error_message is active this frame...
        if R2_Error_message.status == STARTED:
            # update params
            pass
        
        # if R2_Error_message is stopping this frame...
        if R2_Error_message.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R2_Error_message.tStartRefresh + fbk_dur-frameTolerance:
                # keep track of stop time/frame for later
                R2_Error_message.tStop = t  # not accounting for scr refresh
                R2_Error_message.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R2_Error_message.stopped')
                # update status
                R2_Error_message.status = FINISHED
                R2_Error_message.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fbk2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fbk2" ---
    for thisComponent in Fbk2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Fbk2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Study2Loop'


# --- Prepare to start Routine "EndPart2" ---
continueRoutine = True
# update component parameters for each repeat
contpart2_2.keys = []
contpart2_2.rt = []
_contpart2_2_allKeys = []
# keep track of which components have finished
EndPart2Components = [text_2, contpart2_2]
for thisComponent in EndPart2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndPart2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    
    # if text_2 is starting this frame...
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        # update status
        text_2.status = STARTED
        text_2.setAutoDraw(True)
    
    # if text_2 is active this frame...
    if text_2.status == STARTED:
        # update params
        pass
    
    # *contpart2_2* updates
    waitOnFlip = False
    
    # if contpart2_2 is starting this frame...
    if contpart2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contpart2_2.frameNStart = frameN  # exact frame index
        contpart2_2.tStart = t  # local t and not account for scr refresh
        contpart2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contpart2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'contpart2_2.started')
        # update status
        contpart2_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(contpart2_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(contpart2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if contpart2_2.status == STARTED and not waitOnFlip:
        theseKeys = contpart2_2.getKeys(keyList=['t'], waitRelease=False)
        _contpart2_2_allKeys.extend(theseKeys)
        if len(_contpart2_2_allKeys):
            contpart2_2.keys = _contpart2_2_allKeys[-1].name  # just the last key pressed
            contpart2_2.rt = _contpart2_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndPart2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndPart2" ---
for thisComponent in EndPart2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if contpart2_2.keys in ['', [], None]:  # No response was made
    contpart2_2.keys = None
thisExp.addData('contpart2_2.keys',contpart2_2.keys)
if contpart2_2.keys != None:  # we had a response
    thisExp.addData('contpart2_2.rt', contpart2_2.rt)
thisExp.nextEntry()
# the Routine "EndPart2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instruct3a" ---
continueRoutine = True
# update component parameters for each repeat
Instructresp_6.keys = []
Instructresp_6.rt = []
_Instructresp_6_allKeys = []
# keep track of which components have finished
Instruct3aComponents = [Instruct2a_text_3, Instructresp_6]
for thisComponent in Instruct3aComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruct3a" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct2a_text_3* updates
    
    # if Instruct2a_text_3 is starting this frame...
    if Instruct2a_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct2a_text_3.frameNStart = frameN  # exact frame index
        Instruct2a_text_3.tStart = t  # local t and not account for scr refresh
        Instruct2a_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct2a_text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instruct2a_text_3.started')
        # update status
        Instruct2a_text_3.status = STARTED
        Instruct2a_text_3.setAutoDraw(True)
    
    # if Instruct2a_text_3 is active this frame...
    if Instruct2a_text_3.status == STARTED:
        # update params
        pass
    
    # *Instructresp_6* updates
    waitOnFlip = False
    
    # if Instructresp_6 is starting this frame...
    if Instructresp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructresp_6.frameNStart = frameN  # exact frame index
        Instructresp_6.tStart = t  # local t and not account for scr refresh
        Instructresp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructresp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructresp_6.started')
        # update status
        Instructresp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instructresp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instructresp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instructresp_6.status == STARTED and not waitOnFlip:
        theseKeys = Instructresp_6.getKeys(keyList=['2'], waitRelease=False)
        _Instructresp_6_allKeys.extend(theseKeys)
        if len(_Instructresp_6_allKeys):
            Instructresp_6.keys = _Instructresp_6_allKeys[-1].name  # just the last key pressed
            Instructresp_6.rt = _Instructresp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct3aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruct3a" ---
for thisComponent in Instruct3aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruct3a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GetReady" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GetReadyComponents = [fixation, text_4]
for thisComponent in GetReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GetReady" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation* updates
    
    # if fixation is starting this frame...
    if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation.frameNStart = frameN  # exact frame index
        fixation.tStart = t  # local t and not account for scr refresh
        fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation.started')
        # update status
        fixation.status = STARTED
        fixation.setAutoDraw(True)
    
    # if fixation is active this frame...
    if fixation.status == STARTED:
        # update params
        pass
    
    # if fixation is stopping this frame...
    if fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.stopped')
            # update status
            fixation.status = FINISHED
            fixation.setAutoDraw(False)
    
    # *text_4* updates
    
    # if text_4 is starting this frame...
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        # update status
        text_4.status = STARTED
        text_4.setAutoDraw(True)
    
    # if text_4 is active this frame...
    if text_4.status == STARTED:
        # update params
        pass
    
    # if text_4 is stopping this frame...
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            # update status
            text_4.status = FINISHED
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GetReady" ---
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StimFile_A.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Test3" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from PlaceWords_3
    r3reversed = []
    if random()>.5:
        topword_offset = .1
        bottomword_offset = -.05
        r3reversed = False
        x = '1) ' 
        y = '2) '
    else:
        topword_offset = -.05
        bottomword_offset = .1
        r3reversed = True
        x = '2) ' 
        y = '1) '
    
    
    if r3reversed == True:
        correctkey = key_list[2-correctword_list[WordIndex-1]]
    else:
        correctkey = key_list[correctword_list[WordIndex-1]-1]
    
    
    thisExp.addData('r3reversed',r3reversed)
    
    
    StudyView1_target_3.setText(targetword)
    StudyView_topsideword_3.setPos((0, topword_offset))
    StudyView_topsideword_3.setText(x + R1Word1)
    StudyView1_bottomsideword_3.setPos((0, bottomword_offset))
    StudyView1_bottomsideword_3.setText(y + R1Word2)
    Test3response.keys = []
    Test3response.rt = []
    _Test3response_allKeys = []
    # keep track of which components have finished
    Test3Components = [StudyView1_target_3, StudyView_topsideword_3, StudyView1_bottomsideword_3, Test3response]
    for thisComponent in Test3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StudyView1_target_3* updates
        
        # if StudyView1_target_3 is starting this frame...
        if StudyView1_target_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView1_target_3.frameNStart = frameN  # exact frame index
            StudyView1_target_3.tStart = t  # local t and not account for scr refresh
            StudyView1_target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView1_target_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView1_target_3.started')
            # update status
            StudyView1_target_3.status = STARTED
            StudyView1_target_3.setAutoDraw(True)
        
        # if StudyView1_target_3 is active this frame...
        if StudyView1_target_3.status == STARTED:
            # update params
            pass
        
        # if StudyView1_target_3 is stopping this frame...
        if StudyView1_target_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView1_target_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                StudyView1_target_3.tStop = t  # not accounting for scr refresh
                StudyView1_target_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView1_target_3.stopped')
                # update status
                StudyView1_target_3.status = FINISHED
                StudyView1_target_3.setAutoDraw(False)
        
        # *StudyView_topsideword_3* updates
        
        # if StudyView_topsideword_3 is starting this frame...
        if StudyView_topsideword_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView_topsideword_3.frameNStart = frameN  # exact frame index
            StudyView_topsideword_3.tStart = t  # local t and not account for scr refresh
            StudyView_topsideword_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView_topsideword_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView_topsideword_3.started')
            # update status
            StudyView_topsideword_3.status = STARTED
            StudyView_topsideword_3.setAutoDraw(True)
        
        # if StudyView_topsideword_3 is active this frame...
        if StudyView_topsideword_3.status == STARTED:
            # update params
            pass
        
        # if StudyView_topsideword_3 is stopping this frame...
        if StudyView_topsideword_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView_topsideword_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                StudyView_topsideword_3.tStop = t  # not accounting for scr refresh
                StudyView_topsideword_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView_topsideword_3.stopped')
                # update status
                StudyView_topsideword_3.status = FINISHED
                StudyView_topsideword_3.setAutoDraw(False)
        
        # *StudyView1_bottomsideword_3* updates
        
        # if StudyView1_bottomsideword_3 is starting this frame...
        if StudyView1_bottomsideword_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView1_bottomsideword_3.frameNStart = frameN  # exact frame index
            StudyView1_bottomsideword_3.tStart = t  # local t and not account for scr refresh
            StudyView1_bottomsideword_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView1_bottomsideword_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword_3.started')
            # update status
            StudyView1_bottomsideword_3.status = STARTED
            StudyView1_bottomsideword_3.setAutoDraw(True)
        
        # if StudyView1_bottomsideword_3 is active this frame...
        if StudyView1_bottomsideword_3.status == STARTED:
            # update params
            pass
        
        # if StudyView1_bottomsideword_3 is stopping this frame...
        if StudyView1_bottomsideword_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView1_bottomsideword_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                StudyView1_bottomsideword_3.tStop = t  # not accounting for scr refresh
                StudyView1_bottomsideword_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword_3.stopped')
                # update status
                StudyView1_bottomsideword_3.status = FINISHED
                StudyView1_bottomsideword_3.setAutoDraw(False)
        
        # *Test3response* updates
        waitOnFlip = False
        
        # if Test3response is starting this frame...
        if Test3response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Test3response.frameNStart = frameN  # exact frame index
            Test3response.tStart = t  # local t and not account for scr refresh
            Test3response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Test3response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Test3response.started')
            # update status
            Test3response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Test3response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Test3response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if Test3response is stopping this frame...
        if Test3response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Test3response.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Test3response.tStop = t  # not accounting for scr refresh
                Test3response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Test3response.stopped')
                # update status
                Test3response.status = FINISHED
                Test3response.status = FINISHED
        if Test3response.status == STARTED and not waitOnFlip:
            theseKeys = Test3response.getKeys(keyList=['1','2'], waitRelease=False)
            _Test3response_allKeys.extend(theseKeys)
            if len(_Test3response_allKeys):
                Test3response.keys = _Test3response_allKeys[-1].name  # just the last key pressed
                Test3response.rt = _Test3response_allKeys[-1].rt
                # was this correct?
                if (Test3response.keys == str(correctkey)) or (Test3response.keys == correctkey):
                    Test3response.corr = 1
                else:
                    Test3response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test3" ---
    for thisComponent in Test3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Test3response.keys in ['', [], None]:  # No response was made
        Test3response.keys = None
        # was no response the correct answer?!
        if str(correctkey).lower() == 'none':
           Test3response.corr = 1;  # correct non-response
        else:
           Test3response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('Test3response.keys',Test3response.keys)
    trials.addData('Test3response.corr', Test3response.corr)
    if Test3response.keys != None:  # we had a response
        trials.addData('Test3response.rt', Test3response.rt)
    # Run 'End Routine' code from test_2
    
    if Test3response.keys == correctkey: # coin flip to determine if response was correct
        responseiscorrect3 = True
        respbox_color = 'green'
        fbkimagefile = 'checkmark.png'
        totalcorrect = (totalcorrect + 1)
        r3correct_list[WordIndex-1] = True
        if Test3response.keys == key_list[0]: #first word selected, response is last key pressed
            responseside3 = 'top'
            correctside3 = 'top'
            chosenword3 = R1Word1
            correctword3 = R1Word1
            correctwordindex3 =1
            respbox_y = 0.1
        else: #second word selected
            responseside3 = 'bottom'
            correctside3 = 'bottom'
            correctword3 = R1Word2
            chosenword3 = R1Word2
            respbox_y = -.05
            correctwordindex3 = 2
    elif Test3response.keys : #response is made but incorrect (by coin flip above)
        responseiscorrect3 = False
        fbkimagefile = 'X_mark.png'
        respbox_color = 'red'
        r3correct_list[WordIndex-1] = False
        if Test3response.keys == key_list[0]: #first word selected
            responseside3 = 'top'
            correctside3 = 'bottom'
            correctword3 = R1Word2
            chosenword3 = R1Word1
            respbox_y = 0.1
        else:
            responseside3 = 'bottom'
            chosenword3 = R1Word2
            correctside3 = 'top'
            correctword3 = R1Word1
            respbox_y = -0.05
    else:
        #no response
        responseiscorrect3 = False
        r3correct_list[WordIndex-1] = False
        responseside3 = 'miss'
        fbkimagefile = 'poundkey.png'
        respbox_color = background_color
        respbox_y = .3
        errormsg = 'no response'
    
    
    #if Study1Response.keys:
    #    showrespdur = studyviewwindow - Study1Response.rt
    #else:
    #    showrespdur = 0
    
    #correctword_list[WordIndex-1] = correctwordindex3
    #thisExp.addData('r3reversed',r3reversed)
    #thisExp.addData('topsideword', topsideword)
    #thisExp.addData('bottomsideword', bottomsideword)
    thisExp.addData('responseiscorrect3', responseiscorrect3)
    thisExp.addData('responseside3', responseside3)
    thisExp.addData('correctside3',correctside3)
    thisExp.addData('correctword3',correctword3)
    thisExp.addData('correctwordindex3',correctwordindex3)
    #thisExp.addData('correctkey2',correctkey2)
    thisExp.addData('chosenword3',chosenword3)
    thisExp.addData('correctword4',correctword4)
    thisExp.addData('responseside4', responseside4)
    thisExp.addData('correctside4',correctside4)
    thisExp.addData('chosenword4',chosenword4)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ShowResp_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    highlightbox_showresp_2.setPos((0, respbox_y))
    highlightbox_showresp_2.setLineColor(selectbox_color)
    Fbk_target_showresp_2.setText(targetword)
    b_Fbk_topsideword_showresp_2_.setPos((0, topword_offset))
    b_Fbk_topsideword_showresp_2_.setText(x + R1Word1)
    b_Fbk_bottomsideword_showresp_2_.setPos((0, bottomword_offset))
    b_Fbk_bottomsideword_showresp_2_.setText(y + R1Word2)
    # keep track of which components have finished
    ShowResp_3Components = [highlightbox_showresp_2, Fbk_target_showresp_2, b_Fbk_topsideword_showresp_2_, b_Fbk_bottomsideword_showresp_2_]
    for thisComponent in ShowResp_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ShowResp_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *highlightbox_showresp_2* updates
        
        # if highlightbox_showresp_2 is starting this frame...
        if highlightbox_showresp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            highlightbox_showresp_2.frameNStart = frameN  # exact frame index
            highlightbox_showresp_2.tStart = t  # local t and not account for scr refresh
            highlightbox_showresp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(highlightbox_showresp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'highlightbox_showresp_2.started')
            # update status
            highlightbox_showresp_2.status = STARTED
            highlightbox_showresp_2.setAutoDraw(True)
        
        # if highlightbox_showresp_2 is active this frame...
        if highlightbox_showresp_2.status == STARTED:
            # update params
            pass
        
        # if highlightbox_showresp_2 is stopping this frame...
        if highlightbox_showresp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > highlightbox_showresp_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                highlightbox_showresp_2.tStop = t  # not accounting for scr refresh
                highlightbox_showresp_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'highlightbox_showresp_2.stopped')
                # update status
                highlightbox_showresp_2.status = FINISHED
                highlightbox_showresp_2.setAutoDraw(False)
        
        # *Fbk_target_showresp_2* updates
        
        # if Fbk_target_showresp_2 is starting this frame...
        if Fbk_target_showresp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_target_showresp_2.frameNStart = frameN  # exact frame index
            Fbk_target_showresp_2.tStart = t  # local t and not account for scr refresh
            Fbk_target_showresp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_target_showresp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_target_showresp_2.started')
            # update status
            Fbk_target_showresp_2.status = STARTED
            Fbk_target_showresp_2.setAutoDraw(True)
        
        # if Fbk_target_showresp_2 is active this frame...
        if Fbk_target_showresp_2.status == STARTED:
            # update params
            pass
        
        # if Fbk_target_showresp_2 is stopping this frame...
        if Fbk_target_showresp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_target_showresp_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_target_showresp_2.tStop = t  # not accounting for scr refresh
                Fbk_target_showresp_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_target_showresp_2.stopped')
                # update status
                Fbk_target_showresp_2.status = FINISHED
                Fbk_target_showresp_2.setAutoDraw(False)
        
        # *b_Fbk_topsideword_showresp_2_* updates
        
        # if b_Fbk_topsideword_showresp_2_ is starting this frame...
        if b_Fbk_topsideword_showresp_2_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Fbk_topsideword_showresp_2_.frameNStart = frameN  # exact frame index
            b_Fbk_topsideword_showresp_2_.tStart = t  # local t and not account for scr refresh
            b_Fbk_topsideword_showresp_2_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_Fbk_topsideword_showresp_2_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'b_Fbk_topsideword_showresp_2_.started')
            # update status
            b_Fbk_topsideword_showresp_2_.status = STARTED
            b_Fbk_topsideword_showresp_2_.setAutoDraw(True)
        
        # if b_Fbk_topsideword_showresp_2_ is active this frame...
        if b_Fbk_topsideword_showresp_2_.status == STARTED:
            # update params
            pass
        
        # if b_Fbk_topsideword_showresp_2_ is stopping this frame...
        if b_Fbk_topsideword_showresp_2_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Fbk_topsideword_showresp_2_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                b_Fbk_topsideword_showresp_2_.tStop = t  # not accounting for scr refresh
                b_Fbk_topsideword_showresp_2_.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'b_Fbk_topsideword_showresp_2_.stopped')
                # update status
                b_Fbk_topsideword_showresp_2_.status = FINISHED
                b_Fbk_topsideword_showresp_2_.setAutoDraw(False)
        
        # *b_Fbk_bottomsideword_showresp_2_* updates
        
        # if b_Fbk_bottomsideword_showresp_2_ is starting this frame...
        if b_Fbk_bottomsideword_showresp_2_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Fbk_bottomsideword_showresp_2_.frameNStart = frameN  # exact frame index
            b_Fbk_bottomsideword_showresp_2_.tStart = t  # local t and not account for scr refresh
            b_Fbk_bottomsideword_showresp_2_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_Fbk_bottomsideword_showresp_2_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'b_Fbk_bottomsideword_showresp_2_.started')
            # update status
            b_Fbk_bottomsideword_showresp_2_.status = STARTED
            b_Fbk_bottomsideword_showresp_2_.setAutoDraw(True)
        
        # if b_Fbk_bottomsideword_showresp_2_ is active this frame...
        if b_Fbk_bottomsideword_showresp_2_.status == STARTED:
            # update params
            pass
        
        # if b_Fbk_bottomsideword_showresp_2_ is stopping this frame...
        if b_Fbk_bottomsideword_showresp_2_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Fbk_bottomsideword_showresp_2_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                b_Fbk_bottomsideword_showresp_2_.tStop = t  # not accounting for scr refresh
                b_Fbk_bottomsideword_showresp_2_.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'b_Fbk_bottomsideword_showresp_2_.stopped')
                # update status
                b_Fbk_bottomsideword_showresp_2_.status = FINISHED
                b_Fbk_bottomsideword_showresp_2_.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ShowResp_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ShowResp_3" ---
    for thisComponent in ShowResp_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# --- Prepare to start Routine "Additup" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from calctotalsfinal
bonus
totalcorrect
totalspent
trialbonus
bonusmessage
totalcorrectmessage
bonus = (totalcorrect * 10) + totalspent
print(bonus)
print(totalcorrect)
print(totalspent)
thisExp.addData('totalcorrect',totalcorrect)
thisExp.addData('totalspent',totalspent)
thisExp.addData('bonus',bonus)
bonusmessage = "Total Bonus: %d cents" % bonus
totalcorrectmessage = "Total Correct: %d" % totalcorrect
thisExp.addData('bonusmessage',bonusmessage)
# keep track of which components have finished
AdditupComponents = []
for thisComponent in AdditupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Additup" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AdditupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Additup" ---
for thisComponent in AdditupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Additup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EndPart3" ---
continueRoutine = True
# update component parameters for each repeat
Lastresp.keys = []
Lastresp.rt = []
_Lastresp_allKeys = []
totalcorrect_text.setText(totalcorrectmessage)
bonus_text.setText(bonusmessage + ' cents ')
# keep track of which components have finished
EndPart3Components = [text_3, Lastresp, totalcorrect_text, bonus_text]
for thisComponent in EndPart3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndPart3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    
    # if text_3 is starting this frame...
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        # update status
        text_3.status = STARTED
        text_3.setAutoDraw(True)
    
    # if text_3 is active this frame...
    if text_3.status == STARTED:
        # update params
        pass
    
    # *Lastresp* updates
    waitOnFlip = False
    
    # if Lastresp is starting this frame...
    if Lastresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Lastresp.frameNStart = frameN  # exact frame index
        Lastresp.tStart = t  # local t and not account for scr refresh
        Lastresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Lastresp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Lastresp.started')
        # update status
        Lastresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Lastresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Lastresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Lastresp.status == STARTED and not waitOnFlip:
        theseKeys = Lastresp.getKeys(keyList=['t'], waitRelease=False)
        _Lastresp_allKeys.extend(theseKeys)
        if len(_Lastresp_allKeys):
            Lastresp.keys = _Lastresp_allKeys[-1].name  # just the last key pressed
            Lastresp.rt = _Lastresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *totalcorrect_text* updates
    
    # if totalcorrect_text is starting this frame...
    if totalcorrect_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        totalcorrect_text.frameNStart = frameN  # exact frame index
        totalcorrect_text.tStart = t  # local t and not account for scr refresh
        totalcorrect_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(totalcorrect_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'totalcorrect_text.started')
        # update status
        totalcorrect_text.status = STARTED
        totalcorrect_text.setAutoDraw(True)
    
    # if totalcorrect_text is active this frame...
    if totalcorrect_text.status == STARTED:
        # update params
        pass
    
    # *bonus_text* updates
    
    # if bonus_text is starting this frame...
    if bonus_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bonus_text.frameNStart = frameN  # exact frame index
        bonus_text.tStart = t  # local t and not account for scr refresh
        bonus_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bonus_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bonus_text.started')
        # update status
        bonus_text.status = STARTED
        bonus_text.setAutoDraw(True)
    
    # if bonus_text is active this frame...
    if bonus_text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndPart3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndPart3" ---
for thisComponent in EndPart3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Lastresp.keys in ['', [], None]:  # No response was made
    Lastresp.keys = None
thisExp.addData('Lastresp.keys',Lastresp.keys)
if Lastresp.keys != None:  # we had a response
    thisExp.addData('Lastresp.rt', Lastresp.rt)
thisExp.nextEntry()
# the Routine "EndPart3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
