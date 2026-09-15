/********************** 
 * Game_C_Ver2.0 Test *
 **********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.1.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Game_C_ver2.0';  // from the Builder filename that created this script
let expInfo = {
    'session': '001',
    'participant': 'FBVAL-',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from initializeVars
//import {shuffle} from 'random';
var key_list = ["1", "2"];
var x 
var y
var ratingkey_list = ["1", "2", "3", "4", "5", "6"];
var key_1allowed = ["1"];
var key_2allowed = ["2"];
var instruc_list = ["t"];
var background_color = "black";
var targetword_offset = 0.3;
var topword_offset = 0.1;
var bottomword_offset = (- 0.05);
var showrespdur = 4;
var errormsg_offset = 0.2;
var confscale_yoffset = (- 0.25);
var confnumbers_yoffset = (- 0.3285);
var fbkyes_xoffset = (- 0.3);
var fbkyes_yoffset = (- 0.05);
var fbkno_xoffset = 0.1;
var fbkno_yoffset = 0.1;
var fbkcost_xoffset = (- 0.3);
var fbkcost_yoffset = (- 0.15);
var totalcorrect_offset = 0.02;
var bonus_offset = (- 0.04);
var instructword_height = 0.15;
var instruct_width = 0.03;
var targetword_height = 0.1;
var word_height = 0.1;
var respbox_width = (0.1 * 8);
var respbox_height = (0.1 * 1.25);
var selectbox_color = "white";
var errormsg_height = 0.075;
var question_height = 1;
var confscale_height = 0.75;
var studyviewwindow = 4;
var fbk_dur = 2;
var study2dur = 300;
var maxconffbkchoice_dur = 300;
var respbox_y = 0.1;
var slowrespmessage_delay = 4;
var slowrespmessage_dur = (maxconffbkchoice_dur - slowrespmessage_delay);
const r1correct_list = Array.apply(null, Array(60)).map(function () {})
const r2correct_list = Array.apply(null, Array(60)).map(function () {})
const r3correct_list = Array.apply(null, Array(60)).map(function () {})
const correctword_list = Array.apply(null, Array(60)).map(function () {})
const correctword_list2 = Array.apply(null, Array(60)).map(function () {})
const correctword_list3 = Array.apply(null, Array(60)).map(function () {})
var responseiscorrect2;
var responseside2;
var correctside2;
var correctword2;
var correctwordindex2;
var correctwordindex;
var responseiscorrect3;
var responseside3;
var correctside3;
var correctword3;
var correctwordindex3;
var responseside4;
var correctside4;
var correctword4;
var chosenword4;
var totalcorrect = 0;
var totalspent = 0;
var trialbonus = 10;
var fbkcostlevels = [(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0,(- 6), (- 4), (- 2), 0];
var trialspercostlevel = [15, 15, 15, 15];
var fbkcost_list = [];
var idx = 0;
for (var fbkcost, _pj_c = 0, _pj_a = fbkcostlevels, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
    fbkcost = _pj_a[_pj_c];
    fbkcost_list = (fbkcost_list + ([fbkcost] * trialspercostlevel[idx]));
    idx = (idx + 1);
}
util.shuffle(fbkcost_list);
util.shuffle(fbkcostlevels);
console.log(fbkcostlevels)

var idy;
idy = 0;
console.log(idy)
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(SetupConstantsRoutineBegin());
flowScheduler.add(SetupConstantsRoutineEachFrame());
flowScheduler.add(SetupConstantsRoutineEnd());
flowScheduler.add(Instruct1aRoutineBegin());
flowScheduler.add(Instruct1aRoutineEachFrame());
flowScheduler.add(Instruct1aRoutineEnd());
flowScheduler.add(Instruct1bRoutineBegin());
flowScheduler.add(Instruct1bRoutineEachFrame());
flowScheduler.add(Instruct1bRoutineEnd());
flowScheduler.add(GetReadyRoutineBegin());
flowScheduler.add(GetReadyRoutineEachFrame());
flowScheduler.add(GetReadyRoutineEnd());
const Study1LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Study1LoopLoopBegin(Study1LoopLoopScheduler));
flowScheduler.add(Study1LoopLoopScheduler);
flowScheduler.add(Study1LoopLoopEnd);
flowScheduler.add(EndPart1RoutineBegin());
flowScheduler.add(EndPart1RoutineEachFrame());
flowScheduler.add(EndPart1RoutineEnd());
flowScheduler.add(Instruct4RoutineBegin());
flowScheduler.add(Instruct4RoutineEachFrame());
flowScheduler.add(Instruct4RoutineEnd());
flowScheduler.add(Instruct4_2RoutineBegin());
flowScheduler.add(Instruct4_2RoutineEachFrame());
flowScheduler.add(Instruct4_2RoutineEnd());
flowScheduler.add(GetReadyRoutineBegin());
flowScheduler.add(GetReadyRoutineEachFrame());
flowScheduler.add(GetReadyRoutineEnd());
const Study2LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Study2LoopLoopBegin(Study2LoopLoopScheduler));
flowScheduler.add(Study2LoopLoopScheduler);
flowScheduler.add(Study2LoopLoopEnd);
flowScheduler.add(EndPart2RoutineBegin());
flowScheduler.add(EndPart2RoutineEachFrame());
flowScheduler.add(EndPart2RoutineEnd());
flowScheduler.add(Instruct3aRoutineBegin());
flowScheduler.add(Instruct3aRoutineEachFrame());
flowScheduler.add(Instruct3aRoutineEnd());
flowScheduler.add(GetReadyRoutineBegin());
flowScheduler.add(GetReadyRoutineEachFrame());
flowScheduler.add(GetReadyRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(AdditupRoutineBegin());
flowScheduler.add(AdditupRoutineEachFrame());
flowScheduler.add(AdditupRoutineEnd());
flowScheduler.add(EndPart3RoutineBegin());
flowScheduler.add(EndPart3RoutineEachFrame());
flowScheduler.add(EndPart3RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'StimFile_A.xlsx', 'path': 'StimFile_A.xlsx'},
    {'name': 'StimFile_A.xlsx', 'path': 'StimFile_A.xlsx'},
    {'name': 'StimFile_A.xlsx', 'path': 'StimFile_A.xlsx'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'StimFile_TEST.xlsx', 'path': 'StimFile_TEST.xlsx'},
    {'name': 'checkmark.png', 'path': 'checkmark.png'},
    {'name': 'nofeedback.png', 'path': 'nofeedback.png'},
    {'name': 'poundkey.png', 'path': 'poundkey.png'},
    {'name': 'X_mark.png', 'path': 'X_mark.png'},
    {'name': 'StimFile_A.xlsx', 'path': 'StimFile_A.xlsx'},
    {'name': 'StimFile_B.xlsx', 'path': 'StimFile_B.xlsx'},
    {'name': 'StimFile_TEST_reallyshort.xlsx', 'path': 'StimFile_TEST_reallyshort.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://rutgers.ca1.qualtrics.com/jfe/form/SV_0fzhcLGgQrq08Vo', '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var SetupConstantsClock;
var Instruct1aClock;
var text_5;
var Instructresp;
var Instruct1bClock;
var Instruct1b_text;
var Instructresp_2;
var GetReadyClock;
var fixation;
var text_4;
var StudyView1Clock;
var topword_offset;
var bottomword_offset;
var StudyView1_target;
var Study1Response;
var StudyView_topsideword;
var StudyView1_bottomsideword;
var ShowRespClock;
var highlightbox_showresp;
var Fbk_target_showresp;
var Fbk_topsideword_showresp;
var Fbk_bottomsideword_showresp;
var Fbk1Clock;
var resp_highlightbox;
var Fbk_target;
var Fbk_topsideword;
var Fbk_bottomsideword;
var FbkImage;
var Error_message;
var EndPart1Clock;
var text;
var contpart2;
var Instruct4Clock;
var Instruct2a_text;
var Instructresp_3;
var Instruct4_2Clock;
var Instruct2b_text;
var Instructresp_4;
var StudyView4Clock;
var StudyView1_target_2;
var StudyView_topsideword_2;
var StudyView1_bottomsideword_2;
var Study2Response;
var slowrespmessage_conf_2;
var ConfidenceClock;
var R2_highlightbox_conf;
var R2_target_conf;
var R2_word1_conf;
var R2_word2_conf;
var conf_question;
var confscale_numbers;
var confresp;
var slowrespmessage_conf;
var ChooseFbkClock;
var R2_FbkQuestion;
var fbkchoice_resp;
var fbkcosttext;
var R2_fbkyes;
var R2_fbkno;
var slowrespmessage_fbk;
var fbknocosttext;
var Fbk2Clock;
var R2_resp_highlightbox;
var R2_Fbk_target;
var R2_Fbk_topsideword;
var R2_Fbk_bottomsideword;
var R2_FbkImage;
var R2_Error_message;
var EndPart2Clock;
var text_2;
var contpart2_2;
var Instruct3aClock;
var Instruct2a_text_3;
var Instructresp_6;
var Test3Clock;
var StudyView1_target_3;
var StudyView_topsideword_3;
var StudyView1_bottomsideword_3;
var Test3response;
var ShowResp_3Clock;
var highlightbox_showresp_2;
var Fbk_target_showresp_2;
var b_Fbk_topsideword_showresp_2;
var b_Fbk_bottomsideword_showresp_2;
var AdditupClock;
var EndPart3Clock;
var text_3;
var Lastresp;
var totalcorrect_text;
var bonus_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "SetupConstants"
  SetupConstantsClock = new util.Clock();
  // Initialize components for Routine "Instruct1a"
  Instruct1aClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: "Part #1\n\nYou will learn word matches in this first part. \n\nFirst, you will see a target word at the top of the screen, with two possible matches below it. Your job is to guess which word matches the top word. You will then get feedback about the accuracy of your choice and will try to remember the correct word match based on that feedback.\n\nIn the last round, you will earn a cash bonus for each word you remember correctly.\n\nFor example: \n\nABSTRACT\n\n1) DOG\n\n2) PLATE\n\nTo guess Option 1 – press the '1' key.\nTo guess Option 2 – press the '2' key.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Instructresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruct1b"
  Instruct1bClock = new util.Clock();
  Instruct1b_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruct1b_text',
    text: "After you make your choice, you will see feedback indicating whether you were correct (a green checkmark) or incorrect (a red X). The matches are random, so you will not know which choice matches with each target word, but you should try to remember the feedback because you will see these word matches again.\n\nA potentially useful strategy is to create sentences in your head that will help you remember which word matches with the target word, but you can use your own strategy if you wish. Your cash bonus will depend on how many word pairs you remember correctly during the last round. You will earn 10 cents per correct answer and can earn up to 6 dollars.\n\nTry to respond as quickly as possible and learn from the feedback. You will have 4 seconds to respond during each set of words.\n\nAny questions? \n\nPress the '2' key to begin.\n ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Instructresp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "GetReady"
  GetReadyClock = new util.Clock();
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Get ready to begin...',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.05)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "StudyView1"
  StudyView1Clock = new util.Clock();
  // Run 'Begin Experiment' code from PlaceWords
  topword_offset = 0;
  bottomword_offset = 0;
  
  StudyView1_target = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView1_target',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  Study1Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  StudyView_topsideword = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView_topsideword',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  StudyView1_bottomsideword = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView1_bottomsideword',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "ShowResp"
  ShowRespClock = new util.Clock();
  highlightbox_showresp = new visual.Rect ({
    win: psychoJS.window, name: 'highlightbox_showresp', 
    width: [respbox_width, respbox_height][0], height: [respbox_width, respbox_height][1],
    ori: 0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 12, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  Fbk_target_showresp = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_target_showresp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  Fbk_topsideword_showresp = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_topsideword_showresp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  Fbk_bottomsideword_showresp = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_bottomsideword_showresp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Fbk1"
  Fbk1Clock = new util.Clock();
  resp_highlightbox = new visual.Rect ({
    win: psychoJS.window, name: 'resp_highlightbox', 
    width: [respbox_width, respbox_height][0], height: [respbox_width, respbox_height][1],
    ori: 0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 12, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  Fbk_target = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_target',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  Fbk_topsideword = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_topsideword',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  Fbk_bottomsideword = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_bottomsideword',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  FbkImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'FbkImage', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  Error_message = new visual.TextStim({
    win: psychoJS.window,
    name: 'Error_message',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.075,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "EndPart1"
  EndPart1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'That was the end of Part #1.\n\nPlease ring the bell to alert the experimenter, who will set you up on Part #2.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  contpart2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruct4"
  Instruct4Clock = new util.Clock();
  Instruct2a_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruct2a_text',
    text: "Part #2 \n\nNow you will see the words from Part #1 again. Your task is to remember the correct match for the top word, based on what you learned in Part #1. First, press '1' or '2' to select the correct word. The sets of words may not be in the same order as when you saw them the first time. \n\nNext, you will be asked to rate how confident you are that your answer is correct. Press a number key from '1' through '6' to indicate your confidence.\n\n1 = ~50% confidence (LOW: ~50/50 guess)\n2 = ~60% confidence\n3 = ~70% confidence\n4 = ~80% confidence\n5 = ~90% confidence\n6 = ~100% confidence (HIGH: ~100% sure)",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Instructresp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruct4_2"
  Instruct4_2Clock = new util.Clock();
  Instruct2b_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruct2b_text',
    text: 'After you rate your confidence, you will have an opportunity to get feedback again about whether you selected the correct word. The screen will say: "Do you want feedback?"and you can press \'1\' to get feedback, or \'2\' to ignore the feedback.\n\nSometimes, you will see that it will cost a few cents to get feedback. This means if you choose \'YES\' for feedback, you will have the cost deducted from your final cash bonus. Sometimes the cost will be zero cents so you can get feedback for free.  If you choose to ignore the feedback, no money will be deducted  from your bonus.\n\nKeep in mind that you will be rewarded with 10 cents for every correct response you make during the final bonus round. You can be rewarded up to 6 dollars, depending on how well you perform. Since your final cash bonus will depend on your performance during the final round, it may be worthwhile to accept the cost of the feedback so that you can learn the word pairs well.\n\nAny questions? \n\nPress the \'2\' key to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Instructresp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "StudyView4"
  StudyView4Clock = new util.Clock();
  StudyView1_target_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView1_target_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  StudyView_topsideword_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView_topsideword_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: word_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  StudyView1_bottomsideword_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView1_bottomsideword_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: word_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  Study2Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  slowrespmessage_conf_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'slowrespmessage_conf_2',
    text: 'please respond faster',
    font: 'Arial',
    units: undefined, 
    pos: [0, errormsg_offset], height: errormsg_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "Confidence"
  ConfidenceClock = new util.Clock();
  R2_highlightbox_conf = new visual.Rect ({
    win: psychoJS.window, name: 'R2_highlightbox_conf', 
    width: [respbox_width, respbox_height][0], height: [respbox_width, respbox_height][1],
    ori: 0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 12, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color(undefined),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  R2_target_conf = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_target_conf',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: targetword_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  R2_word1_conf = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_word1_conf',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  R2_word2_conf = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_word2_conf',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  conf_question = new visual.TextStim({
    win: psychoJS.window,
    name: 'conf_question',
    text: 'How confident are you in your answer?',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.055,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  confscale_numbers = new visual.TextStim({
    win: psychoJS.window,
    name: 'confscale_numbers',
    text: '(1)   (2)   (3)   (4)   (5)   (6)\n\nlow                            high\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.06,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  confresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  slowrespmessage_conf = new visual.TextStim({
    win: psychoJS.window,
    name: 'slowrespmessage_conf',
    text: 'please respond faster',
    font: 'Arial',
    units: undefined, 
    pos: [0, errormsg_offset], height: errormsg_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "ChooseFbk"
  ChooseFbkClock = new util.Clock();
  R2_FbkQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_FbkQuestion',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: 0.075,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  fbkchoice_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fbkcosttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'fbkcosttext',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [fbkcost_xoffset, fbkcost_yoffset], height: 0.075,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  R2_fbkyes = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_fbkyes',
    text: '1) YES',
    font: 'Arial',
    units: undefined, 
    pos: [fbkyes_xoffset, fbkyes_yoffset], height: 0.075,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  R2_fbkno = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_fbkno',
    text: '2) NO',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, (- 0.05)], height: 0.075,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slowrespmessage_fbk = new visual.TextStim({
    win: psychoJS.window,
    name: 'slowrespmessage_fbk',
    text: 'please respond faster',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: 1,
    depth: -5.0 
  });
  
  fbknocosttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'fbknocosttext',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, fbkcost_yoffset], height: 0.075,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "Fbk2"
  Fbk2Clock = new util.Clock();
  R2_resp_highlightbox = new visual.Rect ({
    win: psychoJS.window, name: 'R2_resp_highlightbox', 
    width: [respbox_width, respbox_height][0], height: [respbox_width, respbox_height][1],
    ori: 0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 12, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  R2_Fbk_target = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_Fbk_target',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  R2_Fbk_topsideword = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_Fbk_topsideword',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  R2_Fbk_bottomsideword = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_Fbk_bottomsideword',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: word_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  R2_FbkImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R2_FbkImage', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  R2_Error_message = new visual.TextStim({
    win: psychoJS.window,
    name: 'R2_Error_message',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, errormsg_offset], height: errormsg_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "EndPart2"
  EndPart2Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'That was the end of Part #2.\n\nPlease ring the bell to alert the experimenter, who will set you up on the final part.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  contpart2_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruct3a"
  Instruct3aClock = new util.Clock();
  Instruct2a_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruct2a_text_3',
    text: "Part #3\n\nIn this last part, you will see the same sets of words from earlier. Your task is to remember the correct match for the top word, based on what you learned earlier.\n\nPress '1' or '2' to select the correct word. \nYou will see your cash bonus total at the end of the round.\n\nAny questions? \n\nPress the '2' key to begin.\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Instructresp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Test3"
  Test3Clock = new util.Clock();
  StudyView1_target_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView1_target_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: targetword_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  StudyView_topsideword_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView_topsideword_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: word_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  StudyView1_bottomsideword_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView1_bottomsideword_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: word_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  Test3response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ShowResp_3"
  ShowResp_3Clock = new util.Clock();
  highlightbox_showresp_2 = new visual.Rect ({
    win: psychoJS.window, name: 'highlightbox_showresp_2', 
    width: [respbox_width, respbox_height][0], height: [respbox_width, respbox_height][1],
    ori: 0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 12, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color(undefined),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  Fbk_target_showresp_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_target_showresp_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, targetword_offset], height: targetword_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  b_Fbk_topsideword_showresp_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'b_Fbk_topsideword_showresp_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: word_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  b_Fbk_bottomsideword_showresp_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'b_Fbk_bottomsideword_showresp_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: word_height,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Additup"
  AdditupClock = new util.Clock();
  // Initialize components for Routine "EndPart3"
  EndPart3Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'That was the end of Part #3. \n\nPlease alert the experimenter. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Lastresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  totalcorrect_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'totalcorrect_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.15)], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  bonus_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'bonus_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.033,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var SetupConstantsComponents;
function SetupConstantsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SetupConstants' ---
    t = 0;
    SetupConstantsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    SetupConstantsComponents = [];
    
    for (const thisComponent of SetupConstantsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SetupConstantsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SetupConstants' ---
    // get current time
    t = SetupConstantsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SetupConstantsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SetupConstantsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SetupConstants' ---
    for (const thisComponent of SetupConstantsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "SetupConstants" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Instructresp_allKeys;
var Instruct1aComponents;
function Instruct1aRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruct1a' ---
    t = 0;
    Instruct1aClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Instructresp.keys = undefined;
    Instructresp.rt = undefined;
    _Instructresp_allKeys = [];
    // keep track of which components have finished
    Instruct1aComponents = [];
    Instruct1aComponents.push(text_5);
    Instruct1aComponents.push(Instructresp);
    
    for (const thisComponent of Instruct1aComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruct1aRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruct1a' ---
    // get current time
    t = Instruct1aClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *Instructresp* updates
    if (t >= 0.0 && Instructresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructresp.tStart = t;  // (not accounting for frame time here)
      Instructresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instructresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instructresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instructresp.clearEvents(); });
    }

    if (Instructresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instructresp.getKeys({keyList: ['t'], waitRelease: false});
      _Instructresp_allKeys = _Instructresp_allKeys.concat(theseKeys);
      if (_Instructresp_allKeys.length > 0) {
        Instructresp.keys = _Instructresp_allKeys.map((key) => key.name);  // storing all keys
        Instructresp.rt = _Instructresp_allKeys.map((key) => key.rt);
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruct1aComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruct1aRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruct1a' ---
    for (const thisComponent of Instruct1aComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Instructresp.corr, level);
    }
    psychoJS.experiment.addData('Instructresp.keys', Instructresp.keys);
    if (typeof Instructresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Instructresp.rt', Instructresp.rt);
        routineTimer.reset();
        }
    
    Instructresp.stop();
    // the Routine "Instruct1a" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Instructresp_2_allKeys;
var Instruct1bComponents;
function Instruct1bRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruct1b' ---
    t = 0;
    Instruct1bClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Instructresp_2.keys = undefined;
    Instructresp_2.rt = undefined;
    _Instructresp_2_allKeys = [];
    // keep track of which components have finished
    Instruct1bComponents = [];
    Instruct1bComponents.push(Instruct1b_text);
    Instruct1bComponents.push(Instructresp_2);
    
    for (const thisComponent of Instruct1bComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruct1bRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruct1b' ---
    // get current time
    t = Instruct1bClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruct1b_text* updates
    if (t >= 0.0 && Instruct1b_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruct1b_text.tStart = t;  // (not accounting for frame time here)
      Instruct1b_text.frameNStart = frameN;  // exact frame index
      
      Instruct1b_text.setAutoDraw(true);
    }

    
    // *Instructresp_2* updates
    if (t >= 0.0 && Instructresp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructresp_2.tStart = t;  // (not accounting for frame time here)
      Instructresp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instructresp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instructresp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instructresp_2.clearEvents(); });
    }

    if (Instructresp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instructresp_2.getKeys({keyList: ['2'], waitRelease: false});
      _Instructresp_2_allKeys = _Instructresp_2_allKeys.concat(theseKeys);
      if (_Instructresp_2_allKeys.length > 0) {
        Instructresp_2.keys = _Instructresp_2_allKeys[_Instructresp_2_allKeys.length - 1].name;  // just the last key pressed
        Instructresp_2.rt = _Instructresp_2_allKeys[_Instructresp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruct1bComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruct1bRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruct1b' ---
    for (const thisComponent of Instruct1bComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Instructresp_2.stop();
    // the Routine "Instruct1b" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GetReadyComponents;
function GetReadyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'GetReady' ---
    t = 0;
    GetReadyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    GetReadyComponents = [];
    GetReadyComponents.push(fixation);
    GetReadyComponents.push(text_4);
    
    for (const thisComponent of GetReadyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function GetReadyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'GetReady' ---
    // get current time
    t = GetReadyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of GetReadyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GetReadyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'GetReady' ---
    for (const thisComponent of GetReadyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Study1Loop;
function Study1LoopLoopBegin(Study1LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Study1Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'StimFile_A.xlsx',
      seed: undefined, name: 'Study1Loop'
    });
    psychoJS.experiment.addLoop(Study1Loop); // add the loop to the experiment
    currentLoop = Study1Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStudy1Loop of Study1Loop) {
      snapshot = Study1Loop.getSnapshot();
      Study1LoopLoopScheduler.add(importConditions(snapshot));
      Study1LoopLoopScheduler.add(StudyView1RoutineBegin(snapshot));
      Study1LoopLoopScheduler.add(StudyView1RoutineEachFrame());
      Study1LoopLoopScheduler.add(StudyView1RoutineEnd(snapshot));
      Study1LoopLoopScheduler.add(ShowRespRoutineBegin(snapshot));
      Study1LoopLoopScheduler.add(ShowRespRoutineEachFrame());
      Study1LoopLoopScheduler.add(ShowRespRoutineEnd(snapshot));
      Study1LoopLoopScheduler.add(Fbk1RoutineBegin(snapshot));
      Study1LoopLoopScheduler.add(Fbk1RoutineEachFrame());
      Study1LoopLoopScheduler.add(Fbk1RoutineEnd(snapshot));
      Study1LoopLoopScheduler.add(Study1LoopLoopEndIteration(Study1LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function Study1LoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Study1Loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Study1LoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Study2Loop;
function Study2LoopLoopBegin(Study2LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Study2Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'StimFile_A.xlsx',
      seed: undefined, name: 'Study2Loop'
    });
    psychoJS.experiment.addLoop(Study2Loop); // add the loop to the experiment
    currentLoop = Study2Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStudy2Loop of Study2Loop) {
      snapshot = Study2Loop.getSnapshot();
      Study2LoopLoopScheduler.add(importConditions(snapshot));
      Study2LoopLoopScheduler.add(StudyView4RoutineBegin(snapshot));
      Study2LoopLoopScheduler.add(StudyView4RoutineEachFrame());
      Study2LoopLoopScheduler.add(StudyView4RoutineEnd(snapshot));
      Study2LoopLoopScheduler.add(ShowRespRoutineBegin(snapshot));
      Study2LoopLoopScheduler.add(ShowRespRoutineEachFrame());
      Study2LoopLoopScheduler.add(ShowRespRoutineEnd(snapshot));
      Study2LoopLoopScheduler.add(ConfidenceRoutineBegin(snapshot));
      Study2LoopLoopScheduler.add(ConfidenceRoutineEachFrame());
      Study2LoopLoopScheduler.add(ConfidenceRoutineEnd(snapshot));
      Study2LoopLoopScheduler.add(ChooseFbkRoutineBegin(snapshot));
      Study2LoopLoopScheduler.add(ChooseFbkRoutineEachFrame());
      Study2LoopLoopScheduler.add(ChooseFbkRoutineEnd(snapshot));
      Study2LoopLoopScheduler.add(Fbk2RoutineBegin(snapshot));
      Study2LoopLoopScheduler.add(Fbk2RoutineEachFrame());
      Study2LoopLoopScheduler.add(Fbk2RoutineEnd(snapshot));
      Study2LoopLoopScheduler.add(Study2LoopLoopEndIteration(Study2LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function Study2LoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Study2Loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Study2LoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'StimFile_A.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(Test3RoutineBegin(snapshot));
      trialsLoopScheduler.add(Test3RoutineEachFrame());
      trialsLoopScheduler.add(Test3RoutineEnd(snapshot));
      trialsLoopScheduler.add(ShowResp_3RoutineBegin(snapshot));
      trialsLoopScheduler.add(ShowResp_3RoutineEachFrame());
      trialsLoopScheduler.add(ShowResp_3RoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var x;
var y;
var r1reversed;
var _Study1Response_allKeys;
var StudyView1Components;
function StudyView1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'StudyView1' ---
    t = 0;
    StudyView1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from PlaceWords
    x = ["1) "];
    y = ["2) "];
    if ((Math.random() > 0.5)) {
        topword_offset = 0.1;
        bottomword_offset = (- 0.05);
        r1reversed = false;
        x = "1) ";
        y = "2) ";
    } else {
        topword_offset = (- 0.05);
        bottomword_offset = 0.1;
        r1reversed = true;
        x = "2) ";
        y = "1) ";
    }
    console.log(r1reversed);
    console.log(topword_offset);
    
    
    StudyView1_target.setText(targetword);
    Study1Response.keys = undefined;
    Study1Response.rt = undefined;
    _Study1Response_allKeys = [];
    StudyView_topsideword.setPos([0, topword_offset]);
    StudyView_topsideword.setText((x + R1Word1));
    StudyView1_bottomsideword.setPos([0, bottomword_offset]);
    StudyView1_bottomsideword.setText((y + R1Word2));
    // keep track of which components have finished
    StudyView1Components = [];
    StudyView1Components.push(StudyView1_target);
    StudyView1Components.push(Study1Response);
    StudyView1Components.push(StudyView_topsideword);
    StudyView1Components.push(StudyView1_bottomsideword);
    
    for (const thisComponent of StudyView1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StudyView1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'StudyView1' ---
    // get current time
    t = StudyView1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *StudyView1_target* updates
    if (t >= 0.0 && StudyView1_target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView1_target.tStart = t;  // (not accounting for frame time here)
      StudyView1_target.frameNStart = frameN;  // exact frame index
      
      StudyView1_target.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView1_target.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView1_target.setAutoDraw(false);
    }
    
    // *Study1Response* updates
    if (t >= 0 && Study1Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Study1Response.tStart = t;  // (not accounting for frame time here)
      Study1Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Study1Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Study1Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Study1Response.clearEvents(); });
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Study1Response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Study1Response.status = PsychoJS.Status.FINISHED;
  }

    if (Study1Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = Study1Response.getKeys({keyList: ['1', '2'], waitRelease: false});
      _Study1Response_allKeys = _Study1Response_allKeys.concat(theseKeys);
      if (_Study1Response_allKeys.length > 0) {
        Study1Response.keys = _Study1Response_allKeys[_Study1Response_allKeys.length - 1].name;  // just the last key pressed
        Study1Response.rt = _Study1Response_allKeys[_Study1Response_allKeys.length - 1].rt;
        // was this correct?
        if (Study1Response.keys == '') {
            Study1Response.corr = 1;
        } else {
            Study1Response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *StudyView_topsideword* updates
    if (t >= 0.0 && StudyView_topsideword.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView_topsideword.tStart = t;  // (not accounting for frame time here)
      StudyView_topsideword.frameNStart = frameN;  // exact frame index
      
      StudyView_topsideword.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView_topsideword.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView_topsideword.setAutoDraw(false);
    }
    
    // *StudyView1_bottomsideword* updates
    if (t >= 0.0 && StudyView1_bottomsideword.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView1_bottomsideword.tStart = t;  // (not accounting for frame time here)
      StudyView1_bottomsideword.frameNStart = frameN;  // exact frame index
      
      StudyView1_bottomsideword.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView1_bottomsideword.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView1_bottomsideword.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StudyView1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var errormsg;
var responseiscorrect;
var respbox_color;
var fbkimagefile;
var responseside;
var correctside;
var respbox_y;
var correctwordindex;
var correctword;
function StudyView1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'StudyView1' ---
    for (const thisComponent of StudyView1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (Study1Response.keys === undefined) {
      if (['None','none',undefined].includes('')) {
         Study1Response.corr = 1;  // correct non-response
      } else {
         Study1Response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Study1Response.corr, level);
    }
    psychoJS.experiment.addData('Study1Response.keys', Study1Response.keys);
    psychoJS.experiment.addData('Study1Response.corr', Study1Response.corr);
    if (typeof Study1Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Study1Response.rt', Study1Response.rt);
        routineTimer.reset();
        }
    
    Study1Response.stop();
    // Run 'End Routine' code from test_3
    errormsg = "";
    WordIndex;
    if (((Math.random() > 0.5) && Study1Response.keys)) {
        responseiscorrect = true;
        respbox_color = "green";
        fbkimagefile = "checkmark.png";
        r1correct_list[(WordIndex - 1)] = true;
        if ((Study1Response.keys === key_list[0])) {
            responseside = "top";
            correctside = "top";
            respbox_y = 0.1;
            if ((r1reversed === true)) {
                correctwordindex = 2;
                correctword = R1Word2;
            } else {
                correctwordindex = 1;
                correctword = R1Word1;
            }
        } else {
            responseside = "bottom";
            correctside = "bottom";
            respbox_y = (- 0.05);
            if ((r1reversed === true)) {
                correctwordindex = 1;
                correctword = R1Word1;
            } else {
                correctwordindex = 2;
                correctword = R1Word2;
            }
        }
    } else {
        if (Study1Response.keys) {
            responseiscorrect = false;
            fbkimagefile = "X_mark.png";
            respbox_color = "red";
            r1correct_list[(WordIndex - 1)] = false;
            if ((Study1Response.keys === key_list[0])) {
                responseside = "top";
                correctside = "bottom";
                respbox_y = 0.1;
                if (r1reversed) {
                    correctwordindex = 1;
                    correctword = R1Word1;
                } else {
                    correctwordindex = 2;
                    correctword = R1Word2;
                }
            } else {
                responseside = "bottom";
                correctside = "top";
                respbox_y = (- 0.05);
                if (r1reversed) {
                    correctwordindex = 2;
                    correctword = R1Word2;
                } else {
                    correctwordindex = 1;
                    correctword = R1Word1;
                }
            }
        } else {
            responseiscorrect = false;
            r1correct_list[(WordIndex - 1)] = false;
            responseside = "miss";
            fbkimagefile = "poundkey.png";
            respbox_color = background_color;
            respbox_y = 1;
            errormsg = "no response";
            if ((Math.random() > 0.5)) {
                correctside = "top";
                if (r1reversed) {
                    correctwordindex = 2;
                    correctword = R1Word2;
                } else {
                    correctwordindex = 1;
                    correctword = R1Word1;
                }
            } else {
                correctside = "bottom";
                if (r1reversed) {
                    correctwordindex = 1;
                    correctword = R1Word1;
                } else {
                    correctwordindex = 2;
                    correctword = R1Word2;
                }
            }
        }
    }
    if ((correctside === responseside)) {
        responseiscorrect = true;
    } else {
        responseiscorrect = false;
    }
    correctword_list[(WordIndex - 1)] = correctwordindex;
    psychoJS.experiment.addData("r1reversed", r1reversed);
    psychoJS.experiment.addData("responseiscorrect", responseiscorrect);
    psychoJS.experiment.addData("responseside", responseside);
    psychoJS.experiment.addData("correctside", correctside);
    psychoJS.experiment.addData("correctword", correctword);
    psychoJS.experiment.addData("correctwordindex", correctwordindex);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ShowRespComponents;
function ShowRespRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ShowResp' ---
    t = 0;
    ShowRespClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    highlightbox_showresp.setPos([0, respbox_y]);
    highlightbox_showresp.setLineColor(new util.Color(selectbox_color));
    Fbk_target_showresp.setText(targetword);
    Fbk_topsideword_showresp.setPos([0, topword_offset]);
    Fbk_topsideword_showresp.setText((x + R1Word1));
    Fbk_bottomsideword_showresp.setPos([0, bottomword_offset]);
    Fbk_bottomsideword_showresp.setText((y + R1Word2));
    // keep track of which components have finished
    ShowRespComponents = [];
    ShowRespComponents.push(highlightbox_showresp);
    ShowRespComponents.push(Fbk_target_showresp);
    ShowRespComponents.push(Fbk_topsideword_showresp);
    ShowRespComponents.push(Fbk_bottomsideword_showresp);
    
    for (const thisComponent of ShowRespComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ShowRespRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ShowResp' ---
    // get current time
    t = ShowRespClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *highlightbox_showresp* updates
    if (t >= 0.0 && highlightbox_showresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      highlightbox_showresp.tStart = t;  // (not accounting for frame time here)
      highlightbox_showresp.frameNStart = frameN;  // exact frame index
      
      highlightbox_showresp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (highlightbox_showresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      highlightbox_showresp.setAutoDraw(false);
    }
    
    // *Fbk_target_showresp* updates
    if (t >= 0.0 && Fbk_target_showresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_target_showresp.tStart = t;  // (not accounting for frame time here)
      Fbk_target_showresp.frameNStart = frameN;  // exact frame index
      
      Fbk_target_showresp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_target_showresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_target_showresp.setAutoDraw(false);
    }
    
    // *Fbk_topsideword_showresp* updates
    if (t >= 0.0 && Fbk_topsideword_showresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_topsideword_showresp.tStart = t;  // (not accounting for frame time here)
      Fbk_topsideword_showresp.frameNStart = frameN;  // exact frame index
      
      Fbk_topsideword_showresp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_topsideword_showresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_topsideword_showresp.setAutoDraw(false);
    }
    
    // *Fbk_bottomsideword_showresp* updates
    if (t >= 0.0 && Fbk_bottomsideword_showresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_bottomsideword_showresp.tStart = t;  // (not accounting for frame time here)
      Fbk_bottomsideword_showresp.frameNStart = frameN;  // exact frame index
      
      Fbk_bottomsideword_showresp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_bottomsideword_showresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_bottomsideword_showresp.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ShowRespComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ShowRespRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ShowResp' ---
    for (const thisComponent of ShowRespComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Fbk1Components;
function Fbk1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Fbk1' ---
    t = 0;
    Fbk1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    resp_highlightbox.setPos([0, respbox_y]);
    resp_highlightbox.setLineColor(new util.Color(respbox_color));
    Fbk_target.setText(targetword);
    Fbk_topsideword.setPos([0, topword_offset]);
    Fbk_topsideword.setText((x + R1Word1));
    Fbk_bottomsideword.setPos([0, bottomword_offset]);
    Fbk_bottomsideword.setText((y + R1Word2));
    FbkImage.setPos([0, (- 0.285)]);
    FbkImage.setImage(fbkimagefile);
    Error_message.setText(errormsg);
    // keep track of which components have finished
    Fbk1Components = [];
    Fbk1Components.push(resp_highlightbox);
    Fbk1Components.push(Fbk_target);
    Fbk1Components.push(Fbk_topsideword);
    Fbk1Components.push(Fbk_bottomsideword);
    Fbk1Components.push(FbkImage);
    Fbk1Components.push(Error_message);
    
    for (const thisComponent of Fbk1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Fbk1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Fbk1' ---
    // get current time
    t = Fbk1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *resp_highlightbox* updates
    if (t >= 0.0 && resp_highlightbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_highlightbox.tStart = t;  // (not accounting for frame time here)
      resp_highlightbox.frameNStart = frameN;  // exact frame index
      
      resp_highlightbox.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_highlightbox.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_highlightbox.setAutoDraw(false);
    }
    
    // *Fbk_target* updates
    if (t >= 0.0 && Fbk_target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_target.tStart = t;  // (not accounting for frame time here)
      Fbk_target.frameNStart = frameN;  // exact frame index
      
      Fbk_target.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_target.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_target.setAutoDraw(false);
    }
    
    // *Fbk_topsideword* updates
    if (t >= 0.0 && Fbk_topsideword.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_topsideword.tStart = t;  // (not accounting for frame time here)
      Fbk_topsideword.frameNStart = frameN;  // exact frame index
      
      Fbk_topsideword.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_topsideword.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_topsideword.setAutoDraw(false);
    }
    
    // *Fbk_bottomsideword* updates
    if (t >= 0.0 && Fbk_bottomsideword.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_bottomsideword.tStart = t;  // (not accounting for frame time here)
      Fbk_bottomsideword.frameNStart = frameN;  // exact frame index
      
      Fbk_bottomsideword.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_bottomsideword.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_bottomsideword.setAutoDraw(false);
    }
    
    // *FbkImage* updates
    if (t >= 0.0 && FbkImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FbkImage.tStart = t;  // (not accounting for frame time here)
      FbkImage.frameNStart = frameN;  // exact frame index
      
      FbkImage.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (FbkImage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      FbkImage.setAutoDraw(false);
    }
    
    // *Error_message* updates
    if (t >= 0.0 && Error_message.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Error_message.tStart = t;  // (not accounting for frame time here)
      Error_message.frameNStart = frameN;  // exact frame index
      
      Error_message.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Error_message.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Error_message.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Fbk1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Fbk1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Fbk1' ---
    for (const thisComponent of Fbk1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Fbk1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _contpart2_allKeys;
var EndPart1Components;
function EndPart1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndPart1' ---
    t = 0;
    EndPart1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    contpart2.keys = undefined;
    contpart2.rt = undefined;
    _contpart2_allKeys = [];
    // keep track of which components have finished
    EndPart1Components = [];
    EndPart1Components.push(text);
    EndPart1Components.push(contpart2);
    
    for (const thisComponent of EndPart1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndPart1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndPart1' ---
    // get current time
    t = EndPart1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *contpart2* updates
    if (t >= 0.0 && contpart2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contpart2.tStart = t;  // (not accounting for frame time here)
      contpart2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { contpart2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { contpart2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { contpart2.clearEvents(); });
    }

    if (contpart2.status === PsychoJS.Status.STARTED) {
      let theseKeys = contpart2.getKeys({keyList: ['t'], waitRelease: false});
      _contpart2_allKeys = _contpart2_allKeys.concat(theseKeys);
      if (_contpart2_allKeys.length > 0) {
        contpart2.keys = _contpart2_allKeys[_contpart2_allKeys.length - 1].name;  // just the last key pressed
        contpart2.rt = _contpart2_allKeys[_contpart2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndPart1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndPart1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndPart1' ---
    for (const thisComponent of EndPart1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(contpart2.corr, level);
    }
    psychoJS.experiment.addData('contpart2.keys', contpart2.keys);
    if (typeof contpart2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('contpart2.rt', contpart2.rt);
        routineTimer.reset();
        }
    
    contpart2.stop();
    // the Routine "EndPart1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Instructresp_3_allKeys;
var Instruct4Components;
function Instruct4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruct4' ---
    t = 0;
    Instruct4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Instructresp_3.keys = undefined;
    Instructresp_3.rt = undefined;
    _Instructresp_3_allKeys = [];
    // keep track of which components have finished
    Instruct4Components = [];
    Instruct4Components.push(Instruct2a_text);
    Instruct4Components.push(Instructresp_3);
    
    for (const thisComponent of Instruct4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruct4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruct4' ---
    // get current time
    t = Instruct4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruct2a_text* updates
    if (t >= 0.0 && Instruct2a_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruct2a_text.tStart = t;  // (not accounting for frame time here)
      Instruct2a_text.frameNStart = frameN;  // exact frame index
      
      Instruct2a_text.setAutoDraw(true);
    }

    
    // *Instructresp_3* updates
    if (t >= 0.0 && Instructresp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructresp_3.tStart = t;  // (not accounting for frame time here)
      Instructresp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instructresp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instructresp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instructresp_3.clearEvents(); });
    }

    if (Instructresp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instructresp_3.getKeys({keyList: ['t'], waitRelease: false});
      _Instructresp_3_allKeys = _Instructresp_3_allKeys.concat(theseKeys);
      if (_Instructresp_3_allKeys.length > 0) {
        Instructresp_3.keys = _Instructresp_3_allKeys[_Instructresp_3_allKeys.length - 1].name;  // just the last key pressed
        Instructresp_3.rt = _Instructresp_3_allKeys[_Instructresp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruct4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruct4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruct4' ---
    for (const thisComponent of Instruct4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Instructresp_3.stop();
    // the Routine "Instruct4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Instructresp_4_allKeys;
var Instruct4_2Components;
function Instruct4_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruct4_2' ---
    t = 0;
    Instruct4_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Instructresp_4.keys = undefined;
    Instructresp_4.rt = undefined;
    _Instructresp_4_allKeys = [];
    // keep track of which components have finished
    Instruct4_2Components = [];
    Instruct4_2Components.push(Instruct2b_text);
    Instruct4_2Components.push(Instructresp_4);
    
    for (const thisComponent of Instruct4_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruct4_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruct4_2' ---
    // get current time
    t = Instruct4_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruct2b_text* updates
    if (t >= 0.0 && Instruct2b_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruct2b_text.tStart = t;  // (not accounting for frame time here)
      Instruct2b_text.frameNStart = frameN;  // exact frame index
      
      Instruct2b_text.setAutoDraw(true);
    }

    
    // *Instructresp_4* updates
    if (t >= 0.0 && Instructresp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructresp_4.tStart = t;  // (not accounting for frame time here)
      Instructresp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instructresp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instructresp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instructresp_4.clearEvents(); });
    }

    if (Instructresp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instructresp_4.getKeys({keyList: ['2'], waitRelease: false});
      _Instructresp_4_allKeys = _Instructresp_4_allKeys.concat(theseKeys);
      if (_Instructresp_4_allKeys.length > 0) {
        Instructresp_4.keys = _Instructresp_4_allKeys[_Instructresp_4_allKeys.length - 1].name;  // just the last key pressed
        Instructresp_4.rt = _Instructresp_4_allKeys[_Instructresp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruct4_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruct4_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruct4_2' ---
    for (const thisComponent of Instruct4_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Instructresp_4.stop();
    // the Routine "Instruct4_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var r2reversed;
var _Study2Response_allKeys;
var StudyView4Components;
function StudyView4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'StudyView4' ---
    t = 0;
    StudyView4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from PlaceWords_2
    if ((Math.random() > 0.5)) {
        topword_offset = 0.1;
        bottomword_offset = (- 0.05);
        r2reversed = false;
        x = "1) ";
        y = "2) ";
    } else {
        topword_offset = (- 0.05);
        bottomword_offset = 0.1;
        r2reversed = true;
        x = "2) ";
        y = "1) ";
    }
    psychoJS.experiment.addData("r2reversed", r2reversed);
    
    StudyView1_target_2.setText(targetword);
    StudyView_topsideword_2.setPos([0, topword_offset]);
    StudyView_topsideword_2.setText((x + R1Word1));
    StudyView1_bottomsideword_2.setPos([0, bottomword_offset]);
    StudyView1_bottomsideword_2.setText((y + R1Word2));
    Study2Response.keys = undefined;
    Study2Response.rt = undefined;
    _Study2Response_allKeys = [];
    // keep track of which components have finished
    StudyView4Components = [];
    StudyView4Components.push(StudyView1_target_2);
    StudyView4Components.push(StudyView_topsideword_2);
    StudyView4Components.push(StudyView1_bottomsideword_2);
    StudyView4Components.push(Study2Response);
    StudyView4Components.push(slowrespmessage_conf_2);
    
    for (const thisComponent of StudyView4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StudyView4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'StudyView4' ---
    // get current time
    t = StudyView4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *StudyView1_target_2* updates
    if (t >= 0.0 && StudyView1_target_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView1_target_2.tStart = t;  // (not accounting for frame time here)
      StudyView1_target_2.frameNStart = frameN;  // exact frame index
      
      StudyView1_target_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + study2dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView1_target_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView1_target_2.setAutoDraw(false);
    }
    
    // *StudyView_topsideword_2* updates
    if (t >= 0.0 && StudyView_topsideword_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView_topsideword_2.tStart = t;  // (not accounting for frame time here)
      StudyView_topsideword_2.frameNStart = frameN;  // exact frame index
      
      StudyView_topsideword_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + study2dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView_topsideword_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView_topsideword_2.setAutoDraw(false);
    }
    
    // *StudyView1_bottomsideword_2* updates
    if (t >= 0.0 && StudyView1_bottomsideword_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView1_bottomsideword_2.tStart = t;  // (not accounting for frame time here)
      StudyView1_bottomsideword_2.frameNStart = frameN;  // exact frame index
      
      StudyView1_bottomsideword_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + study2dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView1_bottomsideword_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView1_bottomsideword_2.setAutoDraw(false);
    }
    
    // *Study2Response* updates
    if (t >= 0 && Study2Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Study2Response.tStart = t;  // (not accounting for frame time here)
      Study2Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Study2Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Study2Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Study2Response.clearEvents(); });
    }

    if (Study2Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = Study2Response.getKeys({keyList: ['1', '2'], waitRelease: false});
      _Study2Response_allKeys = _Study2Response_allKeys.concat(theseKeys);
      if (_Study2Response_allKeys.length > 0) {
        Study2Response.keys = _Study2Response_allKeys[_Study2Response_allKeys.length - 1].name;  // just the last key pressed
        Study2Response.rt = _Study2Response_allKeys[_Study2Response_allKeys.length - 1].rt;
        // was this correct?
        if (Study2Response.keys == correctkey) {
            Study2Response.corr = 1;
        } else {
            Study2Response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *slowrespmessage_conf_2* updates
    if (t >= 4 && slowrespmessage_conf_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slowrespmessage_conf_2.tStart = t;  // (not accounting for frame time here)
      slowrespmessage_conf_2.frameNStart = frameN;  // exact frame index
      
      slowrespmessage_conf_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StudyView4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correctkey;
var r2responseiscorrect;
var r2chosenword;
var responseside2;
var correctside2;
var correctwordindex2;
var correctword2;
var responseiscorrect2;
var trialfbkcost;
var costnum;
var fbk_question;
var costsign;
function StudyView4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'StudyView4' ---
    for (const thisComponent of StudyView4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (Study2Response.keys === undefined) {
      if (['None','none',undefined].includes(correctkey)) {
         Study2Response.corr = 1;  // correct non-response
      } else {
         Study2Response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Study2Response.corr, level);
    }
    psychoJS.experiment.addData('Study2Response.keys', Study2Response.keys);
    psychoJS.experiment.addData('Study2Response.corr', Study2Response.corr);
    if (typeof Study2Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Study2Response.rt', Study2Response.rt);
        routineTimer.reset();
        }
    
    Study2Response.stop();
    errormsg = "";
    WordIndex;
    if (r2reversed === true) {
        correctkey = key_list[(2 - correctword_list[(WordIndex - 1)])];
    } else {
        correctkey = key_list[(correctword_list[(WordIndex - 1)] - 1)];
    }
    if ((Study2Response.keys === correctkey)) {
        r2responseiscorrect = true;
        respbox_color = "green";
        fbkimagefile = "checkmark.png";
        r2correct_list[(WordIndex - 1)] = true;
        r2chosenword = correctword_list2[(WordIndex - 1)];
        if ((Study2Response.keys === key_list[0])) {
            responseside2 = "top";
            correctside2 = "top";
    //        correctword2 = R1Word1;
            respbox_y = 0.1;
            if (r2reversed === true) {
                correctwordindex2 = 2;
                correctword2 = R1Word2;
            } else {
                correctwordindex2 = 1;
                correctword2 = R1Word1;
            }
        } else {
            responseside2 = "bottom";
            correctside2 = "bottom";
    //        correctword2 = R1Word2;
            respbox_y = (- 0.05);
            if (r2reversed) {
                correctwordindex2 = 1;
                correctword2 = R1Word1;
            } else {
                correctwordindex2 = 2;
                correctword2 = R1Word2;
            }
        }
    } else {
        if (Study2Response.keys) {
            responseiscorrect2 = false;
            fbkimagefile = "X_mark.png";
            respbox_color = "red";
            r2correct_list[(WordIndex - 1)] = false;
            if ((Study2Response.keys === key_list[0])) {
                responseside2 = "top";
                correctside2 = "bottom";
    //            correctword2 = R1Word2;
                respbox_y = 0.1;
                if (r2reversed) {
                    correctwordindex2 = 1;
                    correctword2 = R1Word1;
                } else {
                    correctwordindex2 = 2;
                    correctword2 = R1Word2;
                }
            } else {
                responseside2 = "bottom";
                correctside2 = "top";
    //            correctword2 = R1Word1;
                respbox_y = (- 0.05);
                if (r2reversed) {
                    correctwordindex2 = 2;
                    correctword2 = R1Word2;
                } else {
                    correctwordindex2 = 1;
                    correctword2 = R1Word1;
                }
            }
        } else {
            responseiscorrect2 = false;
            r2correct_list[(WordIndex - 1)] = false;
            responseside2 = "miss";
            fbkimagefile = "poundkey.png";
            respbox_color = background_color;
            respbox_y = 0.3;
            errormsg = "no response";
            if ((Study2Response.keys === correctkey)) {
                correctside2 = "top";
    //            correctword2 = R1Word1;
                if (r2reversed) {
                    correctwordindex2 = 2;
                    correctword2 = R1Word2;
                } else {
                    correctwordindex2 = 1;
                    correctword2 = R1Word1;
                }
            } else {
                correctside2 = "bottom";
    //            correctword2 = R1Word2;
                if (r2reversed) {
                    correctwordindex2 = 1;
                    correctword2 = R1Word1;
                } else {
                    correctwordindex2 = 2;
                    correctword2 = R1Word2;
                }
            }
        }
    }
    if ((correctside2 === responseside2)) {
        responseiscorrect2 = true;
    } else {
        responseiscorrect2 = false;
    }
    
    
    trialfbkcost = fbkcost_list[(WordIndex - 1)];
    costnum = fbkcostlevels[idy];
    console.log(costnum);
    if ((trialfbkcost > 0)) {
        fbk_question = `Do you want feedback?
    (${costnum} cents)`
    ;
        costsign = "";
    } else {
        fbk_question = `Do you want feedback?
    (${costnum} cents)`
    ;
        costsign = "";
    }
    correctword_list2[(WordIndex - 1)] = correctwordindex2;
    psychoJS.experiment.addData("responseiscorrect2", responseiscorrect2);
    psychoJS.experiment.addData("responseside2", responseside2);
    psychoJS.experiment.addData("correctside2", correctside2);
    psychoJS.experiment.addData("correctword2", correctword2);
    psychoJS.experiment.addData("correctwordindex2", correctwordindex2);
    psychoJS.experiment.addData("correctkey", correctkey);
    psychoJS.experiment.addData("costnum", costnum);
    psychoJS.experiment.addData("r2chosenword", r2chosenword);
    
    // the Routine "StudyView4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _confresp_allKeys;
var ConfidenceComponents;
function ConfidenceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Confidence' ---
    t = 0;
    ConfidenceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    R2_highlightbox_conf.setPos([0, respbox_y]);
    R2_highlightbox_conf.setLineColor(new util.Color(selectbox_color));
    R2_target_conf.setText(targetword);
    R2_word1_conf.setPos([0, topword_offset]);
    R2_word1_conf.setText((x + R1Word1));
    R2_word2_conf.setPos([0, bottomword_offset]);
    R2_word2_conf.setText((y + R1Word2));
    confresp.keys = undefined;
    confresp.rt = undefined;
    _confresp_allKeys = [];
    // keep track of which components have finished
    ConfidenceComponents = [];
    ConfidenceComponents.push(R2_highlightbox_conf);
    ConfidenceComponents.push(R2_target_conf);
    ConfidenceComponents.push(R2_word1_conf);
    ConfidenceComponents.push(R2_word2_conf);
    ConfidenceComponents.push(conf_question);
    ConfidenceComponents.push(confscale_numbers);
    ConfidenceComponents.push(confresp);
    ConfidenceComponents.push(slowrespmessage_conf);
    
    for (const thisComponent of ConfidenceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ConfidenceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Confidence' ---
    // get current time
    t = ConfidenceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *R2_highlightbox_conf* updates
    if (t >= 0.0 && R2_highlightbox_conf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_highlightbox_conf.tStart = t;  // (not accounting for frame time here)
      R2_highlightbox_conf.frameNStart = frameN;  // exact frame index
      
      R2_highlightbox_conf.setAutoDraw(true);
    }

    
    // *R2_target_conf* updates
    if (t >= 0.0 && R2_target_conf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_target_conf.tStart = t;  // (not accounting for frame time here)
      R2_target_conf.frameNStart = frameN;  // exact frame index
      
      R2_target_conf.setAutoDraw(true);
    }

    
    // *R2_word1_conf* updates
    if (t >= 0.0 && R2_word1_conf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_word1_conf.tStart = t;  // (not accounting for frame time here)
      R2_word1_conf.frameNStart = frameN;  // exact frame index
      
      R2_word1_conf.setAutoDraw(true);
    }

    
    // *R2_word2_conf* updates
    if (t >= 0.0 && R2_word2_conf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_word2_conf.tStart = t;  // (not accounting for frame time here)
      R2_word2_conf.frameNStart = frameN;  // exact frame index
      
      R2_word2_conf.setAutoDraw(true);
    }

    
    // *conf_question* updates
    if (t >= 0.0 && conf_question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      conf_question.tStart = t;  // (not accounting for frame time here)
      conf_question.frameNStart = frameN;  // exact frame index
      
      conf_question.setAutoDraw(true);
    }

    
    // *confscale_numbers* updates
    if (t >= 0.0 && confscale_numbers.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confscale_numbers.tStart = t;  // (not accounting for frame time here)
      confscale_numbers.frameNStart = frameN;  // exact frame index
      
      confscale_numbers.setAutoDraw(true);
    }

    
    // *confresp* updates
    if (t >= 0.0 && confresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confresp.tStart = t;  // (not accounting for frame time here)
      confresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { confresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { confresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { confresp.clearEvents(); });
    }

    if (confresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = confresp.getKeys({keyList: ['1', '2', '3', '4', '5', '6'], waitRelease: false});
      _confresp_allKeys = _confresp_allKeys.concat(theseKeys);
      if (_confresp_allKeys.length > 0) {
        confresp.keys = _confresp_allKeys[_confresp_allKeys.length - 1].name;  // just the last key pressed
        confresp.rt = _confresp_allKeys[_confresp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *slowrespmessage_conf* updates
    if (t >= 4 && slowrespmessage_conf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slowrespmessage_conf.tStart = t;  // (not accounting for frame time here)
      slowrespmessage_conf.frameNStart = frameN;  // exact frame index
      
      slowrespmessage_conf.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ConfidenceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ConfidenceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Confidence' ---
    for (const thisComponent of ConfidenceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(confresp.corr, level);
    }
    psychoJS.experiment.addData('confresp.keys', confresp.keys);
    if (typeof confresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('confresp.rt', confresp.rt);
        routineTimer.reset();
        }
    
    confresp.stop();
    // the Routine "Confidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _fbkchoice_resp_allKeys;
var ChooseFbkComponents;
function ChooseFbkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ChooseFbk' ---
    t = 0;
    ChooseFbkClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    R2_FbkQuestion.setText(fbk_question);
    fbkchoice_resp.keys = undefined;
    fbkchoice_resp.rt = undefined;
    _fbkchoice_resp_allKeys = [];
    fbkcosttext.setText(fbkcostlevels[idy]);
    fbknocosttext.setText('  0');
    // keep track of which components have finished
    ChooseFbkComponents = [];
    ChooseFbkComponents.push(R2_FbkQuestion);
    ChooseFbkComponents.push(fbkchoice_resp);
    ChooseFbkComponents.push(fbkcosttext);
    ChooseFbkComponents.push(R2_fbkyes);
    ChooseFbkComponents.push(R2_fbkno);
    ChooseFbkComponents.push(slowrespmessage_fbk);
    ChooseFbkComponents.push(fbknocosttext);
    
    for (const thisComponent of ChooseFbkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ChooseFbkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ChooseFbk' ---
    // get current time
    t = ChooseFbkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *R2_FbkQuestion* updates
    if (t >= 0.0 && R2_FbkQuestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_FbkQuestion.tStart = t;  // (not accounting for frame time here)
      R2_FbkQuestion.frameNStart = frameN;  // exact frame index
      
      R2_FbkQuestion.setAutoDraw(true);
    }

    
    // *fbkchoice_resp* updates
    if (t >= 0.0 && fbkchoice_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fbkchoice_resp.tStart = t;  // (not accounting for frame time here)
      fbkchoice_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fbkchoice_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fbkchoice_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fbkchoice_resp.clearEvents(); });
    }

    if (fbkchoice_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = fbkchoice_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _fbkchoice_resp_allKeys = _fbkchoice_resp_allKeys.concat(theseKeys);
      if (_fbkchoice_resp_allKeys.length > 0) {
        fbkchoice_resp.keys = _fbkchoice_resp_allKeys[_fbkchoice_resp_allKeys.length - 1].name;  // just the last key pressed
        fbkchoice_resp.rt = _fbkchoice_resp_allKeys[_fbkchoice_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fbkcosttext* updates
    if (t >= 0.0 && fbkcosttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fbkcosttext.tStart = t;  // (not accounting for frame time here)
      fbkcosttext.frameNStart = frameN;  // exact frame index
      
      fbkcosttext.setAutoDraw(true);
    }

    
    // *R2_fbkyes* updates
    if (t >= 0.0 && R2_fbkyes.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_fbkyes.tStart = t;  // (not accounting for frame time here)
      R2_fbkyes.frameNStart = frameN;  // exact frame index
      
      R2_fbkyes.setAutoDraw(true);
    }

    
    // *R2_fbkno* updates
    if (t >= 0.0 && R2_fbkno.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_fbkno.tStart = t;  // (not accounting for frame time here)
      R2_fbkno.frameNStart = frameN;  // exact frame index
      
      R2_fbkno.setAutoDraw(true);
    }

    
    // *slowrespmessage_fbk* updates
    if (t >= 4 && slowrespmessage_fbk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slowrespmessage_fbk.tStart = t;  // (not accounting for frame time here)
      slowrespmessage_fbk.frameNStart = frameN;  // exact frame index
      
      slowrespmessage_fbk.setAutoDraw(true);
    }

    
    // *fbknocosttext* updates
    if (t >= 0.0 && fbknocosttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fbknocosttext.tStart = t;  // (not accounting for frame time here)
      fbknocosttext.frameNStart = frameN;  // exact frame index
      
      fbknocosttext.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ChooseFbkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var feedback_chosen;
var feedback_chosen2;
var idy;
function ChooseFbkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ChooseFbk' ---
    for (const thisComponent of ChooseFbkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(fbkchoice_resp.corr, level);
    }
    psychoJS.experiment.addData('fbkchoice_resp.keys', fbkchoice_resp.keys);
    if (typeof fbkchoice_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fbkchoice_resp.rt', fbkchoice_resp.rt);
        routineTimer.reset();
        }
    
    fbkchoice_resp.stop();
    // Run 'End Routine' code from setfbkchoice
    var feedback_chosen2 = [];
    if ((fbkchoice_resp.keys === key_list[1])) {
        fbkimagefile = "nofeedback.png";
        respbox_color = selectbox_color;
        feedback_chosen = 0;
        feedback_chosen2 = false;
    } else {
        if ((fbkchoice_resp.keys === key_list[0])) {
            totalspent = (totalspent + fbkcostlevels[(idy)]);
            feedback_chosen = 1;
            feedback_chosen2 = true;
        } else {
            fbkimagefile = "nofeedback.png";
            respbox_color = background_color;
            feedback_chosen = (- 99);
        }
    }
    
    idy = (idy + 1)
    console.log(idy)
    psychoJS.experiment.addData("feedbackchoice", feedback_chosen);
    psychoJS.experiment.addData("feedbackchoice2", feedback_chosen2);
    
    // the Routine "ChooseFbk" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Fbk2Components;
function Fbk2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Fbk2' ---
    t = 0;
    Fbk2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    R2_resp_highlightbox.setPos([0, respbox_y]);
    R2_resp_highlightbox.setLineColor(new util.Color(respbox_color));
    R2_Fbk_target.setText(targetword);
    R2_Fbk_topsideword.setPos([0, topword_offset]);
    R2_Fbk_topsideword.setText((x + R1Word1));
    R2_Fbk_bottomsideword.setPos([0, bottomword_offset]);
    R2_Fbk_bottomsideword.setText((y + R1Word2));
    R2_FbkImage.setPos([0, (- 0.285)]);
    R2_FbkImage.setImage(fbkimagefile);
    R2_Error_message.setText(errormsg);
    // keep track of which components have finished
    Fbk2Components = [];
    Fbk2Components.push(R2_resp_highlightbox);
    Fbk2Components.push(R2_Fbk_target);
    Fbk2Components.push(R2_Fbk_topsideword);
    Fbk2Components.push(R2_Fbk_bottomsideword);
    Fbk2Components.push(R2_FbkImage);
    Fbk2Components.push(R2_Error_message);
    
    for (const thisComponent of Fbk2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Fbk2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Fbk2' ---
    // get current time
    t = Fbk2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *R2_resp_highlightbox* updates
    if (t >= 0.0 && R2_resp_highlightbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_resp_highlightbox.tStart = t;  // (not accounting for frame time here)
      R2_resp_highlightbox.frameNStart = frameN;  // exact frame index
      
      R2_resp_highlightbox.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_resp_highlightbox.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_resp_highlightbox.setAutoDraw(false);
    }
    
    // *R2_Fbk_target* updates
    if (t >= 0.0 && R2_Fbk_target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_Fbk_target.tStart = t;  // (not accounting for frame time here)
      R2_Fbk_target.frameNStart = frameN;  // exact frame index
      
      R2_Fbk_target.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_Fbk_target.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_Fbk_target.setAutoDraw(false);
    }
    
    // *R2_Fbk_topsideword* updates
    if (t >= 0.0 && R2_Fbk_topsideword.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_Fbk_topsideword.tStart = t;  // (not accounting for frame time here)
      R2_Fbk_topsideword.frameNStart = frameN;  // exact frame index
      
      R2_Fbk_topsideword.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_Fbk_topsideword.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_Fbk_topsideword.setAutoDraw(false);
    }
    
    // *R2_Fbk_bottomsideword* updates
    if (t >= 0.0 && R2_Fbk_bottomsideword.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_Fbk_bottomsideword.tStart = t;  // (not accounting for frame time here)
      R2_Fbk_bottomsideword.frameNStart = frameN;  // exact frame index
      
      R2_Fbk_bottomsideword.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_Fbk_bottomsideword.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_Fbk_bottomsideword.setAutoDraw(false);
    }
    
    // *R2_FbkImage* updates
    if (t >= 0.0 && R2_FbkImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_FbkImage.tStart = t;  // (not accounting for frame time here)
      R2_FbkImage.frameNStart = frameN;  // exact frame index
      
      R2_FbkImage.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_FbkImage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_FbkImage.setAutoDraw(false);
    }
    
    // *R2_Error_message* updates
    if (t >= 0.0 && R2_Error_message.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_Error_message.tStart = t;  // (not accounting for frame time here)
      R2_Error_message.frameNStart = frameN;  // exact frame index
      
      R2_Error_message.setAutoDraw(true);
    }

    frameRemains = 0.0 + fbk_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_Error_message.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_Error_message.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Fbk2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Fbk2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Fbk2' ---
    for (const thisComponent of Fbk2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Fbk2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _contpart2_2_allKeys;
var EndPart2Components;
function EndPart2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndPart2' ---
    t = 0;
    EndPart2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    contpart2_2.keys = undefined;
    contpart2_2.rt = undefined;
    _contpart2_2_allKeys = [];
    // keep track of which components have finished
    EndPart2Components = [];
    EndPart2Components.push(text_2);
    EndPart2Components.push(contpart2_2);
    
    for (const thisComponent of EndPart2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndPart2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndPart2' ---
    // get current time
    t = EndPart2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *contpart2_2* updates
    if (t >= 0.0 && contpart2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contpart2_2.tStart = t;  // (not accounting for frame time here)
      contpart2_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { contpart2_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { contpart2_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { contpart2_2.clearEvents(); });
    }

    if (contpart2_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = contpart2_2.getKeys({keyList: ['t'], waitRelease: false});
      _contpart2_2_allKeys = _contpart2_2_allKeys.concat(theseKeys);
      if (_contpart2_2_allKeys.length > 0) {
        contpart2_2.keys = _contpart2_2_allKeys[_contpart2_2_allKeys.length - 1].name;  // just the last key pressed
        contpart2_2.rt = _contpart2_2_allKeys[_contpart2_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndPart2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndPart2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndPart2' ---
    for (const thisComponent of EndPart2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(contpart2_2.corr, level);
    }
    psychoJS.experiment.addData('contpart2_2.keys', contpart2_2.keys);
    if (typeof contpart2_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('contpart2_2.rt', contpart2_2.rt);
        routineTimer.reset();
        }
    
    contpart2_2.stop();
    // the Routine "EndPart2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Instructresp_6_allKeys;
var Instruct3aComponents;
function Instruct3aRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruct3a' ---
    t = 0;
    Instruct3aClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Instructresp_6.keys = undefined;
    Instructresp_6.rt = undefined;
    _Instructresp_6_allKeys = [];
    // keep track of which components have finished
    Instruct3aComponents = [];
    Instruct3aComponents.push(Instruct2a_text_3);
    Instruct3aComponents.push(Instructresp_6);
    
    for (const thisComponent of Instruct3aComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruct3aRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruct3a' ---
    // get current time
    t = Instruct3aClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruct2a_text_3* updates
    if (t >= 0.0 && Instruct2a_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruct2a_text_3.tStart = t;  // (not accounting for frame time here)
      Instruct2a_text_3.frameNStart = frameN;  // exact frame index
      
      Instruct2a_text_3.setAutoDraw(true);
    }

    
    // *Instructresp_6* updates
    if (t >= 0.0 && Instructresp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructresp_6.tStart = t;  // (not accounting for frame time here)
      Instructresp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instructresp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instructresp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instructresp_6.clearEvents(); });
    }

    if (Instructresp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instructresp_6.getKeys({keyList: ['2'], waitRelease: false});
      _Instructresp_6_allKeys = _Instructresp_6_allKeys.concat(theseKeys);
      if (_Instructresp_6_allKeys.length > 0) {
        Instructresp_6.keys = _Instructresp_6_allKeys[_Instructresp_6_allKeys.length - 1].name;  // just the last key pressed
        Instructresp_6.rt = _Instructresp_6_allKeys[_Instructresp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruct3aComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruct3aRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruct3a' ---
    for (const thisComponent of Instruct3aComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Instructresp_6.stop();
    // the Routine "Instruct3a" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var r3reversed;
var _Test3response_allKeys;
var Test3Components;
function Test3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Test3' ---
    t = 0;
    Test3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from PlaceWords_3
    var r3reversed
    r3reversed = [];
    if ((Math.random() > 0.5)) {
        topword_offset = 0.1;
        bottomword_offset = (- 0.05);
        r3reversed = false;
        x = "1) ";
        y = "2) ";
    } else {
        topword_offset = (- 0.05);
        bottomword_offset = 0.1;
        r3reversed = true;
        x = "2) ";
        y = "1) ";
    }
    if ((r3reversed === true)) {
        correctkey = key_list[(2 - correctword_list[(WordIndex - 1)])];
    } else {
        correctkey = key_list[(correctword_list[(WordIndex - 1)] - 1)];
    }
    psychoJS.experiment.addData("r3reversed", r3reversed);
    
    StudyView1_target_3.setText(targetword);
    StudyView_topsideword_3.setPos([0, topword_offset]);
    StudyView_topsideword_3.setText((x + R1Word1));
    StudyView1_bottomsideword_3.setPos([0, bottomword_offset]);
    StudyView1_bottomsideword_3.setText((y + R1Word2));
    Test3response.keys = undefined;
    Test3response.rt = undefined;
    _Test3response_allKeys = [];
    // keep track of which components have finished
    Test3Components = [];
    Test3Components.push(StudyView1_target_3);
    Test3Components.push(StudyView_topsideword_3);
    Test3Components.push(StudyView1_bottomsideword_3);
    Test3Components.push(Test3response);
    
    for (const thisComponent of Test3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Test3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Test3' ---
    // get current time
    t = Test3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *StudyView1_target_3* updates
    if (t >= 0.0 && StudyView1_target_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView1_target_3.tStart = t;  // (not accounting for frame time here)
      StudyView1_target_3.frameNStart = frameN;  // exact frame index
      
      StudyView1_target_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView1_target_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView1_target_3.setAutoDraw(false);
    }
    
    // *StudyView_topsideword_3* updates
    if (t >= 0.0 && StudyView_topsideword_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView_topsideword_3.tStart = t;  // (not accounting for frame time here)
      StudyView_topsideword_3.frameNStart = frameN;  // exact frame index
      
      StudyView_topsideword_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView_topsideword_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView_topsideword_3.setAutoDraw(false);
    }
    
    // *StudyView1_bottomsideword_3* updates
    if (t >= 0.0 && StudyView1_bottomsideword_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView1_bottomsideword_3.tStart = t;  // (not accounting for frame time here)
      StudyView1_bottomsideword_3.frameNStart = frameN;  // exact frame index
      
      StudyView1_bottomsideword_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView1_bottomsideword_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView1_bottomsideword_3.setAutoDraw(false);
    }
    
    // *Test3response* updates
    if (t >= 0 && Test3response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Test3response.tStart = t;  // (not accounting for frame time here)
      Test3response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Test3response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Test3response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Test3response.clearEvents(); });
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Test3response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Test3response.status = PsychoJS.Status.FINISHED;
  }

    if (Test3response.status === PsychoJS.Status.STARTED) {
      let theseKeys = Test3response.getKeys({keyList: ['1', '2'], waitRelease: false});
      _Test3response_allKeys = _Test3response_allKeys.concat(theseKeys);
      if (_Test3response_allKeys.length > 0) {
        Test3response.keys = _Test3response_allKeys[_Test3response_allKeys.length - 1].name;  // just the last key pressed
        Test3response.rt = _Test3response_allKeys[_Test3response_allKeys.length - 1].rt;
        // was this correct?
        if (Test3response.keys == correctkey) {
            Test3response.corr = 1;
        } else {
            Test3response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Test3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var responseiscorrect3;
var totalcorrect;
var responseside3;
var correctside3;
var chosenword3;
var correctword3;
var correctwordindex3;
function Test3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Test3' ---
    for (const thisComponent of Test3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (Test3response.keys === undefined) {
      if (['None','none',undefined].includes(correctkey)) {
         Test3response.corr = 1;  // correct non-response
      } else {
         Test3response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Test3response.corr, level);
    }
    psychoJS.experiment.addData('Test3response.keys', Test3response.keys);
    psychoJS.experiment.addData('Test3response.corr', Test3response.corr);
    if (typeof Test3response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Test3response.rt', Test3response.rt);
        routineTimer.reset();
        }
    
    Test3response.stop();
    // Run 'End Routine' code from test_2
    if ((Test3response.keys === correctkey)) {
        responseiscorrect3 = true;
        respbox_color = "green";
        fbkimagefile = "checkmark.png";
        totalcorrect = (totalcorrect + 1);
        r3correct_list[(WordIndex - 1)] = true;
        if ((Test3response.keys === key_list[0])) {
            responseside3 = "top";
            correctside3 = "top";
            chosenword3 = R1Word1;
            correctword3 = R1Word1;
            correctwordindex3 = 1;
            respbox_y = 0.1;
        } else {
            responseside3 = "bottom";
            correctside3 = "bottom";
            correctword3 = R1Word2;
            chosenword3 = R1Word2;
            respbox_y = (- 0.05);
            correctwordindex3 = 2;
        }
    } else {
        if (Test3response.keys) {
            responseiscorrect3 = false;
            fbkimagefile = "X_mark.png";
            respbox_color = "red";
            r3correct_list[(WordIndex - 1)] = false;
            if ((Test3response.keys === key_list[0])) {
                responseside3 = "top";
                correctside3 = "bottom";
                correctword3 = R1Word2;
                chosenword3 = R1Word1;
                respbox_y = 0.1;
            } else {
                responseside3 = "bottom";
                chosenword3 = R1Word2;
                correctside3 = "top";
                correctword3 = R1Word1;
                respbox_y = (- 0.05);
            }
        } else {
            responseiscorrect3 = false;
            r3correct_list[(WordIndex - 1)] = false;
            responseside3 = "miss";
            fbkimagefile = "poundkey.png";
            respbox_color = background_color;
            respbox_y = 0.3;
            errormsg = "no response";
        }
    }
    psychoJS.experiment.addData("responseiscorrect3", responseiscorrect3);
    psychoJS.experiment.addData("responseside3", responseside3);
    psychoJS.experiment.addData("correctside3", correctside3);
    psychoJS.experiment.addData("correctword3", correctword3);
    psychoJS.experiment.addData("correctwordindex3", correctwordindex3);
    psychoJS.experiment.addData("chosenword3", chosenword3);
    psychoJS.experiment.addData("correctword4", correctword4);
    psychoJS.experiment.addData("responseside4", responseside4);
    psychoJS.experiment.addData("correctside4", correctside4);
    psychoJS.experiment.addData("chosenword4", chosenword4);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ShowResp_3Components;
function ShowResp_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ShowResp_3' ---
    t = 0;
    ShowResp_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    highlightbox_showresp_2.setPos([0, respbox_y]);
    highlightbox_showresp_2.setLineColor(new util.Color(selectbox_color));
    Fbk_target_showresp_2.setText(targetword);
    b_Fbk_topsideword_showresp_2.setPos([0, topword_offset]);
    b_Fbk_topsideword_showresp_2.setText((x + R1Word1));
    b_Fbk_bottomsideword_showresp_2.setPos([0, bottomword_offset]);
    b_Fbk_bottomsideword_showresp_2.setText((y + R1Word2));
    // keep track of which components have finished
    ShowResp_3Components = [];
    ShowResp_3Components.push(highlightbox_showresp_2);
    ShowResp_3Components.push(Fbk_target_showresp_2);
    ShowResp_3Components.push(b_Fbk_topsideword_showresp_2);
    ShowResp_3Components.push(b_Fbk_bottomsideword_showresp_2);
    
    for (const thisComponent of ShowResp_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ShowResp_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ShowResp_3' ---
    // get current time
    t = ShowResp_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *highlightbox_showresp_2* updates
    if (t >= 0.0 && highlightbox_showresp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      highlightbox_showresp_2.tStart = t;  // (not accounting for frame time here)
      highlightbox_showresp_2.frameNStart = frameN;  // exact frame index
      
      highlightbox_showresp_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (highlightbox_showresp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      highlightbox_showresp_2.setAutoDraw(false);
    }
    
    // *Fbk_target_showresp_2* updates
    if (t >= 0.0 && Fbk_target_showresp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_target_showresp_2.tStart = t;  // (not accounting for frame time here)
      Fbk_target_showresp_2.frameNStart = frameN;  // exact frame index
      
      Fbk_target_showresp_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_target_showresp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_target_showresp_2.setAutoDraw(false);
    }
    
    // *b_Fbk_topsideword_showresp_2* updates
    if (t >= 0.0 && b_Fbk_topsideword_showresp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      b_Fbk_topsideword_showresp_2.tStart = t;  // (not accounting for frame time here)
      b_Fbk_topsideword_showresp_2.frameNStart = frameN;  // exact frame index
      
      b_Fbk_topsideword_showresp_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (b_Fbk_topsideword_showresp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      b_Fbk_topsideword_showresp_2.setAutoDraw(false);
    }
    
    // *b_Fbk_bottomsideword_showresp_2* updates
    if (t >= 0.0 && b_Fbk_bottomsideword_showresp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      b_Fbk_bottomsideword_showresp_2.tStart = t;  // (not accounting for frame time here)
      b_Fbk_bottomsideword_showresp_2.frameNStart = frameN;  // exact frame index
      
      b_Fbk_bottomsideword_showresp_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (b_Fbk_bottomsideword_showresp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      b_Fbk_bottomsideword_showresp_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ShowResp_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ShowResp_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ShowResp_3' ---
    for (const thisComponent of ShowResp_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var bonus;
var bonusmessage;
var totalcorrectmessage;
var AdditupComponents;
function AdditupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Additup' ---
    t = 0;
    AdditupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from calctotalsfinal
    bonus;
    totalcorrect;
    totalspent;
    trialbonus;
    bonusmessage;
    totalcorrectmessage;
    bonus = ((totalcorrect * 10) + totalspent);
    console.log(bonus);
    console.log(totalcorrect);
    console.log(totalspent);
    psychoJS.experiment.addData("totalcorrect", totalcorrect);
    psychoJS.experiment.addData("totalspent", totalspent);
    psychoJS.experiment.addData("bonus", bonus);
    bonusmessage = `Total Bonus: ${bonus}`;
    totalcorrectmessage = `Total Correct: ${totalcorrect}`;
    psychoJS.experiment.addData("bonusmessage", bonusmessage);
    
    // keep track of which components have finished
    AdditupComponents = [];
    
    for (const thisComponent of AdditupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AdditupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Additup' ---
    // get current time
    t = AdditupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AdditupComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AdditupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Additup' ---
    for (const thisComponent of AdditupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Additup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Lastresp_allKeys;
var EndPart3Components;
function EndPart3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndPart3' ---
    t = 0;
    EndPart3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Lastresp.keys = undefined;
    Lastresp.rt = undefined;
    _Lastresp_allKeys = [];
    totalcorrect_text.setText(totalcorrectmessage);
    bonus_text.setText((bonusmessage + " cents "));
    // keep track of which components have finished
    EndPart3Components = [];
    EndPart3Components.push(text_3);
    EndPart3Components.push(Lastresp);
    EndPart3Components.push(totalcorrect_text);
    EndPart3Components.push(bonus_text);
    
    for (const thisComponent of EndPart3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndPart3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndPart3' ---
    // get current time
    t = EndPart3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *Lastresp* updates
    if (t >= 0.0 && Lastresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Lastresp.tStart = t;  // (not accounting for frame time here)
      Lastresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Lastresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Lastresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Lastresp.clearEvents(); });
    }

    if (Lastresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Lastresp.getKeys({keyList: ['t'], waitRelease: false});
      _Lastresp_allKeys = _Lastresp_allKeys.concat(theseKeys);
      if (_Lastresp_allKeys.length > 0) {
        Lastresp.keys = _Lastresp_allKeys[_Lastresp_allKeys.length - 1].name;  // just the last key pressed
        Lastresp.rt = _Lastresp_allKeys[_Lastresp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *totalcorrect_text* updates
    if (t >= 0.0 && totalcorrect_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      totalcorrect_text.tStart = t;  // (not accounting for frame time here)
      totalcorrect_text.frameNStart = frameN;  // exact frame index
      
      totalcorrect_text.setAutoDraw(true);
    }

    
    // *bonus_text* updates
    if (t >= 0.0 && bonus_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bonus_text.tStart = t;  // (not accounting for frame time here)
      bonus_text.frameNStart = frameN;  // exact frame index
      
      bonus_text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndPart3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndPart3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndPart3' ---
    for (const thisComponent of EndPart3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Lastresp.corr, level);
    }
    psychoJS.experiment.addData('Lastresp.keys', Lastresp.keys);
    if (typeof Lastresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Lastresp.rt', Lastresp.rt);
        routineTimer.reset();
        }
    
    Lastresp.stop();
    // the Routine "EndPart3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
