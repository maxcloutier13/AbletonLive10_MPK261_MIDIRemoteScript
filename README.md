# MPK261-MIDI-Remote-Script
Custom midi remote script for using the MPK261 in Ableton Live 10.x <br/>
Fixes some issues with the default one that comes with Ableton.<br/>
Alternate script with Live-Looping functionality
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to Install<br/>
1: Find the "MIDI Remote Scripts" folder for your installation of Ableton (Usually: C:\Program Files\Ableton\Resources\MIDI Remote Scripts)<br/>
2: Copy the MPK261MX and MPK261MXLOOP folders there<br/>
3: Open Ableton and got to Option/Preferences .. Then the Link MIDI tab. Select the desired script in the Control Surface selector. Set Input/Output as your MPK261<br/>

Setting on the MPK261 to support the Relative Encoders<br/>
1: Load the "LiveLite" default Preset<br/>
2: Save it on another slot (there are empty ones from 25 to 30), I name mine MPK261MX to keep it simple<br/>
3: With your new Preset loaded go to edit mode<br/>
4: Move the first knob and change the "Type" from "MIDI CC" to "INC/DEC2". Make sure they are on channel 1. Do the same for all 8 knobs<br/>
5: Save your preset<br/>

You should be good to go!<br/>
Clicking on a device you should now see the blue hand and it should automap if you click on another device<br/>
Enjoy the super smooth movement of the relative knobs!<br/>

<b>MPK261MX </b>
"Normal" script mostly meant to live play insttruments

<b>MPK261MXLOOP </b>
Script to be used for LiveLooping<br/>
Sustain pedal 1 (CC64) is a smart Launchtrack button<br/>
-- On empty cell: record<br/>
-- While recording: Stop and play clip<br/>
-- On a playing clip: toggle overdub mode on/off<br/>
-- On an empty clip while another clip is playing: Stop clips and start recording<br/>

Daw Control arrows<br/>
Change your MPK preset so that the arrows send CC instead of keystrokes<br/>
Channel 1<br/>
UP:88 Down:89 Left:20 Right:21<br/>
Those are automapped to track selection Left/Right and clip selection up/down regardless of current focus

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
 

