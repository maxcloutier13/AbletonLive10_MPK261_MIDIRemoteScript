# MPK261-MIDI-Remote-Script
Custom midi remote script for using the MPK261 in Ableton Live 10.x
Custom script to fix some issues with the default one that comes with Ableton.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I was trying to resolve 2 problems:
1: Actually using the encoder knobs in RELATIVE mode as they were intended. Makes them much smoother to use.
2: Automap the 8 knobs to devices instead of being fixed as Pan controls. 

How to Install
1: Find the "MIDI Remote Scripts" folder for your installation of Ableton (Usually: C:\Program Files\Ableton\Resources\MIDI Remote Scripts)
2: Copy the MPK261MX folder there
3: Open Ableton and got to Option/Preferences .. Then the Link MIDI tab. Select MPK261MX in the Control Surface selector. Set Input/Output as your MPK261

Setting on the MPK261 to support the Relative Encoders
1: Load the "LiveLite" default Preset
2: Save it on another slot (there are empty ones from 25 to 30), I name mine MPK261MX to keep it simple
3: With your new Preset loaded go to edit mode
4: Move the first knob and change the "Type" from "MIDI CC" to "INC/DEC2". Do the same for all 8 knobs
5: Save your preset

You should be good to go!
Clicking on a device you should now see the blue hand and it should automap if you click on another device
Enjoy the super smooth movement of the relative knobs!

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2020-10-04 10:43 AM 
Limitations:
This is my first time messing with midi remote script so bear with me
Only Bank A of the sliders/arm works right now.
Sometimes it doesn't get the blue hand on the first device you open, selecting a second one usually makes it work.

TODO:
Fix bank B+C so it controls tracks 9-16 and 16-24 fluidly
Set up my Preset so it can be dumped directly to the mpk from Ableton.
Switch device (blue hand) automatically when selecting another channel
Implement red box functionality


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- KUDOS --
Gluon (Julien Bayle) for the unofficial repository: https://github.com/gluon/AbletonLive10.1_MIDIRemoteScripts
and API documentation: https://julienbayle.studio/AbletonLiveRemoteScripts_Docs/_Framework/_Framework-module.html
mLegore (Michael LeGore) for his MPK249 automap fix: https://gist.github.com/mlegore/477741b6b6a2c8f658d81d2c02de0974
Richard Medek for his Endless encoders fix: https://richardmedek.com/2016/01/13/ableton-live-and-akais-endless-encoders/
Ableton for making this possible at all
NOT Ableton for making this information so freaking hard to find and figure out
NOT Akai for putting out a half-assed default script. The super old MPK61 script didn't have the same limitations. So weird.

Some links on how to mess with MIDI remote scripts:
https://djtechtools.com/2014/07/06/the-basics-of-ableton-live-midi-controller-scripts-auto-mapping/
Max 8 Documentation (translates a lot to what you can do in the scripts: https://docs.cycling74.com/max8
http://remotescripts.blogspot.com/2010_03_01_archive.html
API Documentation: 

