# MPK261-MIDI-Remote-Script
Custom midi remote script for using the MPK261 in Ableton Live 10.x <br/>
Fixes some issues with the default one that comes with Ableton.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I was trying to resolve 3 problems mainly: <br/>
1: Actually using the encoder knobs in RELATIVE mode as they were intended. Makes them much smoother to use. <br/>
2: Automap the 8 knobs to devices instead of being fixed as Pan controls. <br/>
3: Make the B and C bank usable to cover more than 8 channels

All 3 problems are solved as of 2020-10-04 6:27 PM 

How to Install<br/>
1: Find the "MIDI Remote Scripts" folder for your installation of Ableton (Usually: C:\Program Files\Ableton\Resources\MIDI Remote Scripts)<br/>
2: Copy the MPK261MX folder there<br/>
3: Open Ableton and got to Option/Preferences .. Then the Link MIDI tab. Select MPK261MX in the Control Surface selector. Set Input/Output as your MPK261<br/>

Setting on the MPK261 to support the Relative Encoders<br/>
1: Load the "LiveLite" default Preset<br/>
2: Save it on another slot (there are empty ones from 25 to 30), I name mine MPK261MX to keep it simple<br/>
3: With your new Preset loaded go to edit mode<br/>
4: Move the first knob and change the "Type" from "MIDI CC" to "INC/DEC2". Do the same for all 8 knobs<br/>
5: Save your preset<br/>

You should be good to go!<br/>
Clicking on a device you should now see the blue hand and it should automap if you click on another device<br/>
Enjoy the super smooth movement of the relative knobs!<br/>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
v1.0 - 2020-10-04 10:43 AM <br/>
Limitations:<br/>
This is my first time messing with midi remote script so bear with me<br/>
~~Only Bank A of the sliders/arm works right now.<br/>~~
Sometimes it doesn't get the blue hand on the first device you open, selecting a second one usually makes it work.<br/>

TODO:<br/>
~~Fix bank B+C so it controls tracks 9-16 and 16-24 fluidly<br/>~~
~~Switch device (blue hand) automatically when selecting another channel<br/>~~
Set up my Preset so it can be dumped directly to the mpk from Ableton (Sysex?)<br/>

v1.1 fixed the autoswitch device when selecting another channel  

v1.2 - 2020-10-04 6:27 PM  
Bank B and C entirely functionnal with the arm buttons and sliders activating channels 9-15 and 16-24 as would be expected  

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- KUDOS --<br/>
Gluon (Julien Bayle) for the unofficial repository: https://github.com/gluon/AbletonLive10.1_MIDIRemoteScripts<br/>
and API documentation: https://julienbayle.studio/AbletonLiveRemoteScripts_Docs/_Framework/_Framework-module.html<br/>
mLegore (Michael LeGore) for his MPK249 automap fix: https://gist.github.com/mlegore/477741b6b6a2c8f658d81d2c02de0974<br/>
Richard Medek for his Endless encoders fix: https://richardmedek.com/2016/01/13/ableton-live-and-akais-endless-encoders/<br/>
Ableton for making this possible at all<br/>
NOT Ableton for making this information so freaking hard to find and figure out<br/>
NOT Akai for putting out a half-assed default script. The super old MPK61 script didn't have the same limitations. So weird.<br/>

Some links on how to mess with MIDI remote scripts:<br/>
https://djtechtools.com/2014/07/06/the-basics-of-ableton-live-midi-controller-scripts-auto-mapping/<br/>
Max 8 Documentation (translates a lot to what you can do in the scripts: https://docs.cycling74.com/max8<br/>
http://remotescripts.blogspot.com/2010_03_01_archive.html<br/>
 

