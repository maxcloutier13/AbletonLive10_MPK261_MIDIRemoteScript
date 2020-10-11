# Custom script for the Akai MPK261 in AbletonLive
# Fixes some of the limitations of the stock script

from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.SliderElement import SliderElement
from _Framework.EncoderElement import EncoderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.MixerComponent import MixerComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.TransportComponent import TransportComponent
from _Framework.DrumRackComponent import DrumRackComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.MidiMap import MidiMap as MidiMapBase
from _Framework.MidiMap import make_button, make_encoder, make_slider
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE

_overdub_flag = 0
_color = [0,0,0]
_last_color = []

#Custom make_encoder function to use RELATIVE knobs instead of the default absolute
def make_encoder(name, channel, number, midi_message_type):
 return EncoderElement(midi_message_type, channel, number, Live.MidiMap.MapMode.relative_two_compliment, name=name)

class MidiMap(MidiMapBase):

    def __init__(self, *a, **k):
        super(MidiMap, self).__init__(*a, **k)
        self.add_button('Play', 0, 118, MIDI_CC_TYPE)
        self.add_button('Record', 0, 119, MIDI_CC_TYPE)
        self.add_button('Stop', 0, 117, MIDI_CC_TYPE)
        self.add_button('Loop', 0, 114, MIDI_CC_TYPE)
        self.add_matrix('Encoders', make_encoder, 0, [[22, 23, 24, 25, 26,  27, 28, 29]], MIDI_CC_TYPE)
        #self.add_matrix('Drum_Pads', make_button, 1, [[81, 83, 84, 86],[74, 76, 77, 79], [67, 69, 71, 72],[60, 62, 64, 65]], MIDI_NOTE_TYPE)

class MPK261MXLOOP(ControlSurface):

    def __init__(self, *a, **k):
        super(MPK261MXLOOP, self).__init__(*a, **k)
        self.show_message("-----------------------= MPK261MXLOOP LOADING - maxcloutier13 says hi =----------------------------------------------------------")
        self.log_message("-----------------------= MPK261MXLOOP LOADING - maxcloutier13 says hi =----------------------------------------------------------")
        with self.component_guard():
            midimap = MidiMap()
            #Sustain pedal 1 = Play/Record/Overdub switch for live looping
            self._LoopRecordButton = ButtonElement(True, MIDI_CC_TYPE, 0, 64)
            self._LoopRecordButton.add_value_listener(self._launch_clip, False)
            #Sustain pedal 2 = Sustain pour l'instant ;o)
            #self._LoopRecordButton = ButtonElement(True, MIDI_CC_TYPE, 0, 65)            
            #Control up/down/left/right using the daw controls            
            self._UpButton = ButtonElement(False, MIDI_CC_TYPE, 0, 88, name='UpButton')
            self._DownButton = ButtonElement(False, MIDI_CC_TYPE, 0, 89, name='DownButton')
            self._LeftButton = ButtonElement(False, MIDI_CC_TYPE, 0, 20, name='LeftButton')
            self._RightButton = ButtonElement(False, MIDI_CC_TYPE, 0, 21, name='RightButton')
            #Listeners for the functions
            self._UpButton.add_value_listener(self._move_up, False)
            self._DownButton.add_value_listener(self._move_down, False)
            self._LeftButton.add_value_listener(self._move_left, False)
            self._RightButton.add_value_listener(self._move_right, False)
            #Super crude manual init for the custom buttons and faders 
            #Control Bank A - Channel 1 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            self._Encoder0 = EncoderElement(MIDI_CC_TYPE,1,22, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder0')
            self._Encoder1 = EncoderElement(MIDI_CC_TYPE,1,23, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder1')
            self._Encoder2 = EncoderElement(MIDI_CC_TYPE,1,24, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder2')
            self._Encoder3 = EncoderElement(MIDI_CC_TYPE,1,25, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder3')
            self._Encoder4 = EncoderElement(MIDI_CC_TYPE,1,26, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder4')
            self._Encoder5 = EncoderElement(MIDI_CC_TYPE,1,27, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder5')
            self._Encoder6 = EncoderElement(MIDI_CC_TYPE,1,28, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder6')
            self._Encoder7 = EncoderElement(MIDI_CC_TYPE,1,29, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder7')
            self._ArmButton0 = ButtonElement(False, MIDI_CC_TYPE, 0, 32, name='ArmButton0')
            self._ArmButton1 = ButtonElement(False, MIDI_CC_TYPE, 0, 33, name='ArmButton1')
            self._ArmButton2 = ButtonElement(False, MIDI_CC_TYPE, 0, 34, name='ArmButton2')
            self._ArmButton3 = ButtonElement(False, MIDI_CC_TYPE, 0, 35, name='ArmButton3')
            self._ArmButton4 = ButtonElement(False, MIDI_CC_TYPE, 0, 36, name='ArmButton4')
            self._ArmButton5 = ButtonElement(False, MIDI_CC_TYPE, 0, 37, name='ArmButton5')
            self._ArmButton6 = ButtonElement(False, MIDI_CC_TYPE, 0, 38, name='ArmButton6')
            self._ArmButton7 = ButtonElement(False, MIDI_CC_TYPE, 0, 39, name='ArmButton7')
            self._VolumeSlider0 = SliderElement(MIDI_CC_TYPE, 0, 12, name='VolumeSlider0')
            self._VolumeSlider1 = SliderElement(MIDI_CC_TYPE, 0, 13, name='VolumeSlider1')
            self._VolumeSlider2 = SliderElement(MIDI_CC_TYPE, 0, 14, name='VolumeSlider2')
            self._VolumeSlider3 = SliderElement(MIDI_CC_TYPE, 0, 15, name='VolumeSlider3')
            self._VolumeSlider4 = SliderElement(MIDI_CC_TYPE, 0, 16, name='VolumeSlider4')
            self._VolumeSlider5 = SliderElement(MIDI_CC_TYPE, 0, 17, name='VolumeSlider5')
            self._VolumeSlider6 = SliderElement(MIDI_CC_TYPE, 0, 18, name='VolumeSlider6')
            self._VolumeSlider7 = SliderElement(MIDI_CC_TYPE, 0, 19, name='VolumeSlider7')
            #Control Bank B - Channel 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            self._Encoder8 = EncoderElement(MIDI_CC_TYPE,2,22, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder8')
            self._Encoder9 = EncoderElement(MIDI_CC_TYPE,2,23, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder9')
            self._Encoder10 = EncoderElement(MIDI_CC_TYPE,2,24, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder10')
            self._Encoder11 = EncoderElement(MIDI_CC_TYPE,2,25, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder11')
            self._Encoder12 = EncoderElement(MIDI_CC_TYPE,2,26, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder12')
            self._Encoder13 = EncoderElement(MIDI_CC_TYPE,2,27, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder13')
            self._Encoder14 = EncoderElement(MIDI_CC_TYPE,2,28, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder14')
            self._Encoder15 = EncoderElement(MIDI_CC_TYPE,2,29, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder15')
            self._ArmButton8 = ButtonElement(False, MIDI_CC_TYPE, 1, 32, name='ArmButton8')
            self._ArmButton9 = ButtonElement(False, MIDI_CC_TYPE, 1, 33, name='ArmButton9')
            self._ArmButton10 = ButtonElement(False, MIDI_CC_TYPE, 1, 34, name='ArmButton10')
            self._ArmButton11 = ButtonElement(False, MIDI_CC_TYPE, 1, 35, name='ArmButton11')
            self._ArmButton12 = ButtonElement(False, MIDI_CC_TYPE, 1, 36, name='ArmButton12')
            self._ArmButton13 = ButtonElement(False, MIDI_CC_TYPE, 1, 37, name='ArmButton13')
            self._ArmButton14 = ButtonElement(False, MIDI_CC_TYPE, 1, 38, name='ArmButton14')
            self._ArmButton15 = ButtonElement(False, MIDI_CC_TYPE, 1, 39, name='ArmButton15')
            self._VolumeSlider8 = SliderElement(MIDI_CC_TYPE, 1, 12, name='VolumeSlider8')
            self._VolumeSlider9 = SliderElement(MIDI_CC_TYPE, 1, 13, name='VolumeSlider9')
            self._VolumeSlider10 = SliderElement(MIDI_CC_TYPE, 1, 14, name='VolumeSlider10')
            self._VolumeSlider11 = SliderElement(MIDI_CC_TYPE, 1, 15, name='VolumeSlider11')
            self._VolumeSlider12 = SliderElement(MIDI_CC_TYPE, 1, 16, name='VolumeSlider12')
            self._VolumeSlider13 = SliderElement(MIDI_CC_TYPE, 1, 17, name='VolumeSlider13')
            self._VolumeSlider14 = SliderElement(MIDI_CC_TYPE, 1, 18, name='VolumeSlider14')
            self._VolumeSlider15 = SliderElement(MIDI_CC_TYPE, 1, 19, name='VolumeSlider15')
            #Control Bank C - Channel 3 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            self._Encoder16 = EncoderElement(MIDI_CC_TYPE,3,22, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder16')
            self._Encoder17 = EncoderElement(MIDI_CC_TYPE,3,23, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder17')
            self._Encoder18 = EncoderElement(MIDI_CC_TYPE,3,24, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder18')
            self._Encoder19 = EncoderElement(MIDI_CC_TYPE,3,25, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder19')
            self._Encoder20 = EncoderElement(MIDI_CC_TYPE,3,26, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder20')
            self._Encoder21 = EncoderElement(MIDI_CC_TYPE,3,27, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder21')
            self._Encoder22 = EncoderElement(MIDI_CC_TYPE,3,28, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder22')
            self._Encoder23 = EncoderElement(MIDI_CC_TYPE,3,29, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder23')
            self._ArmButton16 = ButtonElement(False, MIDI_CC_TYPE, 2, 32, name='ArmButton16')
            self._ArmButton17 = ButtonElement(False, MIDI_CC_TYPE, 2, 33, name='ArmButton17')
            self._ArmButton18 = ButtonElement(False, MIDI_CC_TYPE, 2, 34, name='ArmButton18')
            self._ArmButton19 = ButtonElement(False, MIDI_CC_TYPE, 2, 35, name='ArmButton19')
            self._ArmButton20 = ButtonElement(False, MIDI_CC_TYPE, 2, 36, name='ArmButton20')
            self._ArmButton21 = ButtonElement(False, MIDI_CC_TYPE, 2, 37, name='ArmButton21')
            self._ArmButton22 = ButtonElement(False, MIDI_CC_TYPE, 2, 38, name='ArmButton22')
            self._ArmButton23 = ButtonElement(False, MIDI_CC_TYPE, 2, 39, name='ArmButton23')
            self._VolumeSlider16 = SliderElement(MIDI_CC_TYPE, 2, 12, name='VolumeSlider16')
            self._VolumeSlider17 = SliderElement(MIDI_CC_TYPE, 2, 13, name='VolumeSlider17')
            self._VolumeSlider18 = SliderElement(MIDI_CC_TYPE, 2, 14, name='VolumeSlider18')
            self._VolumeSlider19 = SliderElement(MIDI_CC_TYPE, 2, 15, name='VolumeSlider19')
            self._VolumeSlider20 = SliderElement(MIDI_CC_TYPE, 2, 16, name='VolumeSlider20')
            self._VolumeSlider21 = SliderElement(MIDI_CC_TYPE, 2, 17, name='VolumeSlider21')
            self._VolumeSlider22 = SliderElement(MIDI_CC_TYPE, 2, 18, name='VolumeSlider22')
            self._VolumeSlider23 = SliderElement(MIDI_CC_TYPE, 2, 19, name='VolumeSlider23')
            #Drum Bank A - Channel 4--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
            self._Pad0 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 12, name='Pad0')        
            self._Pad1 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 14, name='Pad1')
            self._Pad2 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 16, name='Pad2')
            self._Pad3 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 17, name='Pad3')
            #
            self._Pad4 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 19, name='Pad4')
            self._Pad5 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 21, name='Pad5')
            self._Pad6 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 23, name='Pad6')
            self._Pad7 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 24, name='Pad7')
            #
            self._Pad8 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 26, name='Pad8')
            self._Pad9 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 28, name='Pad9')
            self._Pad10 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 29, name='Pad10')
            self._Pad11 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 31, name='Pad11')
            #
            self._Pad12 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 33, name='Pad12')      
            self._Pad13 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 35, name='Pad13')
            self._Pad14 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 36, name='Pad14')
            self._Pad15 = ButtonElement(True, MIDI_NOTE_TYPE, 5, 38, name='Pad15')
            
            #Listeners on individual pads
            self._Pad0.add_value_listener(self._trig_pad0, False)
            self._Pad1.add_value_listener(self._trig_pad1, False)
            self._Pad2.add_value_listener(self._trig_pad2, False)
            self._Pad3.add_value_listener(self._trig_pad3, False)
            #
            self._Pad4.add_value_listener(self._trig_pad4, False)
            self._Pad5.add_value_listener(self._trig_pad5, False)
            self._Pad6.add_value_listener(self._trig_pad6, False)
            self._Pad7.add_value_listener(self._trig_pad7, False)
            #
            self._Pad8.add_value_listener(self._trig_pad8, False)
            self._Pad9.add_value_listener(self._trig_pad9, False)
            self._Pad10.add_value_listener(self._trig_pad10, False)
            self._Pad11.add_value_listener(self._trig_pad11, False)
            #
            self._Pad12.add_value_listener(self._trig_pad12, False)
            self._Pad13.add_value_listener(self._trig_pad13, False)
            self._Pad14.add_value_listener(self._trig_pad14, False)
            self._Pad15.add_value_listener(self._trig_pad15, False)
            
            self._Pads0 = ButtonMatrixElement(rows=[[self._Pad0, self._Pad1, self._Pad2, self._Pad3],
                                                   [self._Pad4, self._Pad5, self._Pad6, self._Pad7], 
                                                   [self._Pad8, self._Pad9, self._Pad10, self._Pad11],
                                                   [self._Pad12, self._Pad13, self._Pad14, self._Pad15]])
            #Drum Bank B -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            self._Pad16 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 12, name='Pad16')        
            self._Pad17 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 14, name='Pad17')
            self._Pad18 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 16, name='Pad18')
            self._Pad19 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 17, name='Pad19')
            #
            self._Pad20 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 19, name='Pad20')
            self._Pad21 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 21, name='Pad21')
            self._Pad22 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 23, name='Pad22')
            self._Pad23 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 24, name='Pad23')
            #
            self._Pad24 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 26, name='Pad24')
            self._Pad25 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 28, name='Pad25')
            self._Pad26 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 29, name='Pad26')
            self._Pad27 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 31, name='Pad27')
            #
            self._Pad28 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 33, name='Pad28')      
            self._Pad29 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 35, name='Pad29')
            self._Pad30 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 36, name='Pad30')
            self._Pad31 = ButtonElement(True, MIDI_NOTE_TYPE, 6, 38, name='Pad31')
            
            #Listeners on individual pads
            self._Pad16.add_value_listener(self._trig_pad16, False)
            self._Pad17.add_value_listener(self._trig_pad17, False)
            self._Pad18.add_value_listener(self._trig_pad18, False)
            self._Pad19.add_value_listener(self._trig_pad19, False)
            #
            self._Pad20.add_value_listener(self._trig_pad20, False)
            self._Pad21.add_value_listener(self._trig_pad21, False)
            self._Pad22.add_value_listener(self._trig_pad22, False)
            self._Pad23.add_value_listener(self._trig_pad23, False)
            #
            self._Pad24.add_value_listener(self._trig_pad24, False)
            self._Pad25.add_value_listener(self._trig_pad25, False)
            self._Pad26.add_value_listener(self._trig_pad26, False)
            self._Pad27.add_value_listener(self._trig_pad27, False)
            #
            self._Pad28.add_value_listener(self._trig_pad28, False)
            self._Pad29.add_value_listener(self._trig_pad29, False)
            self._Pad30.add_value_listener(self._trig_pad30, False)
            self._Pad31.add_value_listener(self._trig_pad31, False)
            
            self._Pads1 = ButtonMatrixElement(rows=[[self._Pad16, self._Pad17, self._Pad18, self._Pad19],
                                                   [self._Pad20, self._Pad21, self._Pad22, self._Pad23], 
                                                   [self._Pad24, self._Pad25, self._Pad26, self._Pad27],
                                                   [self._Pad28, self._Pad29, self._Pad30, self._Pad31]])
            self._AllPads = [self._Pads0, self._Pads1]
            #Drum Bank C -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #Drum Bank D -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #
            #Drum rack -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #drum_rack = DrumRackComponent(name='Drum_Rack', is_enabled=False, layer=Layer(pads=self._Pads))
            #drum_rack.set_enabled(True)
            #Transport -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            transport = TransportComponent(name='Transport', is_enabled=False, layer=Layer(play_button=midimap['Play'], record_button=midimap['Record'], stop_button=midimap['Stop'], loop_button=midimap['Loop']))
            #, seek_forward_button=midimap['Forward'], seek_backward_button=midimap['Backward']
            transport.set_enabled(True)
            #Make the Back/Fwd button just normal mapable CC senders
            self._BackButton = ButtonElement(False, MIDI_CC_TYPE, 0, 116, name='BackButton')
            self._FwdButton = ButtonElement(False, MIDI_CC_TYPE, 0, 115, name='FwdButton')
            #Device -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            self._device = DeviceComponent(name='Device', is_enabled=False, layer=Layer(parameter_controls=midimap['Encoders']), device_selection_follows_track_selection=True)
            self._device.set_enabled(True)
            self.set_device_component(self._device)
            #Mixer -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            mixer_size = 24
            self._mixer = MixerComponent(mixer_size, name='Mixer', is_enabled=False)
            #Super crude and repetitive mapping because after all this shit I'm not spending time learning how to loop this crap hehe
            #Bank A
            self._mixer.channel_strip(0).layer = Layer(volume_control = self._VolumeSlider0, arm_button=self._ArmButton0, pan_control=self._Encoder0)
            self._mixer.channel_strip(1).layer = Layer(volume_control = self._VolumeSlider1, arm_button=self._ArmButton1, pan_control=self._Encoder1)
            self._mixer.channel_strip(2).layer = Layer(volume_control = self._VolumeSlider2, arm_button=self._ArmButton2, pan_control=self._Encoder2)
            self._mixer.channel_strip(3).layer = Layer(volume_control = self._VolumeSlider3, arm_button=self._ArmButton3, pan_control=self._Encoder3)
            self._mixer.channel_strip(4).layer = Layer(volume_control = self._VolumeSlider4, arm_button=self._ArmButton4, pan_control=self._Encoder4)
            self._mixer.channel_strip(5).layer = Layer(volume_control = self._VolumeSlider5, arm_button=self._ArmButton5, pan_control=self._Encoder5)
            self._mixer.channel_strip(6).layer = Layer(volume_control = self._VolumeSlider6, arm_button=self._ArmButton6, pan_control=self._Encoder6)
            self._mixer.channel_strip(7).layer = Layer(volume_control = self._VolumeSlider7, arm_button=self._ArmButton7, pan_control=self._Encoder7)
            #Bank B
            self._mixer.channel_strip(8).layer = Layer(volume_control = self._VolumeSlider8, arm_button=self._ArmButton8, pan_control=self._Encoder8)
            self._mixer.channel_strip(9).layer = Layer(volume_control = self._VolumeSlider9, arm_button=self._ArmButton9, pan_control=self._Encoder9)
            self._mixer.channel_strip(10).layer = Layer(volume_control = self._VolumeSlider10, arm_button=self._ArmButton10, pan_control=self._Encoder10)
            self._mixer.channel_strip(11).layer = Layer(volume_control = self._VolumeSlider11, arm_button=self._ArmButton11, pan_control=self._Encoder11)
            self._mixer.channel_strip(12).layer = Layer(volume_control = self._VolumeSlider12, arm_button=self._ArmButton12, pan_control=self._Encoder12)
            self._mixer.channel_strip(13).layer = Layer(volume_control = self._VolumeSlider13, arm_button=self._ArmButton13, pan_control=self._Encoder13)
            self._mixer.channel_strip(14).layer = Layer(volume_control = self._VolumeSlider14, arm_button=self._ArmButton14, pan_control=self._Encoder14)
            self._mixer.channel_strip(15).layer = Layer(volume_control = self._VolumeSlider15, arm_button=self._ArmButton15, pan_control=self._Encoder15)
            #Bank C     
            self._mixer.channel_strip(16).layer = Layer(volume_control = self._VolumeSlider16, arm_button=self._ArmButton16, pan_control=self._Encoder16)
            self._mixer.channel_strip(17).layer = Layer(volume_control = self._VolumeSlider17, arm_button=self._ArmButton17, pan_control=self._Encoder17)
            self._mixer.channel_strip(18).layer = Layer(volume_control = self._VolumeSlider18, arm_button=self._ArmButton18, pan_control=self._Encoder18)
            self._mixer.channel_strip(19).layer = Layer(volume_control = self._VolumeSlider19, arm_button=self._ArmButton19, pan_control=self._Encoder19)
            self._mixer.channel_strip(20).layer = Layer(volume_control = self._VolumeSlider20, arm_button=self._ArmButton20, pan_control=self._Encoder20)
            self._mixer.channel_strip(21).layer = Layer(volume_control = self._VolumeSlider21, arm_button=self._ArmButton21, pan_control=self._Encoder21)
            self._mixer.channel_strip(22).layer = Layer(volume_control = self._VolumeSlider22, arm_button=self._ArmButton22, pan_control=self._Encoder22)
            self._mixer.channel_strip(23).layer = Layer(volume_control = self._VolumeSlider23, arm_button=self._ArmButton23, pan_control=self._Encoder23)
            self._mixer.set_enabled(True)
            #Track change listener
            self.song().view.add_selected_track_listener(self._update_selected_device)
        
    #-- DrumBank A ----------------------------------------------------------
    def _trig_pad0(self, value):        
        if value > 0:
            #Track 0 Stop
            self.song().tracks[0].stop_all_clips()
            self.show_message("TFMX Debug: Pad0 triggered")
            
    def _trig_pad1(self, value):                
        if value > 0: 
            #Track 1 Stop
            self.song().tracks[1].stop_all_clips()
            self.show_message("TFMX Debug: Pad1 triggered")
    
    def _trig_pad2(self, value):        
        if value > 0:
            #Track 2 Stop
            self.song().tracks[2].stop_all_clips()
            self.show_message("TFMX Debug: Pad2 triggered")
                
   
    def _trig_pad3(self, value):        
        if value > 0:
            #Track 3 Stop
            self.song().tracks[3].stop_all_clips()
            self.show_message("TFMX Debug: Pad3 triggered")

    #2nd row
    def _trig_pad4(self, value):        
        if value > 0:
            #Track 0 Cell 2: Fire
            self.song().tracks[0].clip_slots[2].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad4 triggered")
 
    def _trig_pad5(self, value):        
        if value > 0:
            #Track 1 Cell 2: Fire
            self.song().tracks[1].clip_slots[2].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad5 triggered")
                  
    def _trig_pad6(self, value):        
        if value > 0:
            #Track 2 Cell 2: Fire
            self.song().tracks[2].clip_slots[2].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad6 triggered")
   
    def _trig_pad7(self, value):        
        if value > 0:
            #Track 3 Cell 2: Fire
            self.song().tracks[3].clip_slots[2].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad7 triggered")
            
    #3rd-row
    def _trig_pad8(self, value):     
        if value > 0:
            #Track 0 Cell 1: Fire
            self.song().tracks[0].clip_slots[1].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad8 triggered")
            
    def _trig_pad9(self, value):        
        if value > 0:
            #Track 1 Cell 1: Fire
            self.song().tracks[1].clip_slots[1].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad9 triggered")    
        
    def _trig_pad10(self, value):        
        if value > 0:
            #Track 2 Cell 1: Fire
            self.song().tracks[2].clip_slots[1].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad10 triggered")

    def _trig_pad11(self, value):        
        if value > 0:
            #Track 3 Cell 1: Fire
            self.song().tracks[3].clip_slots[1].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad11 triggered")
    #Top-row
    def _trig_pad12(self, value):        
        if value > 0:
            #Track 0 Cell 0: Fire            
            slot = self.song().tracks[0].clip_slots[0]
            slot.set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad11 triggered")
            self.log_message("TFMX Debug: Setting clip color")
            #slot.color = 30
            #clip = slot.clip
            #clip.color = 30
    
    #Lights up a pad
    #def _light_pad(self, pads_index, pad_index):
     #   global _last_color
        #Shut all lights in track. Light up the triggered one
        #for slot in self.song().view.selected_track.clip_slots:
            #if slot.has_clip == 1:
                #Need to default to original color, shit.
                #slot.clip.color =  
     #   if self.song().view.highlighted_clip_slot.has_clip == 0:
     #       self._AllPads[pads_index]._Pads0[pad_index].color = (26,255,47)
            
    def _trig_pad13(self, value):        
        if value > 0:
            #Track 1 Cell 0: Fire
            self.song().tracks[1].clip_slots[0].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad13 triggered")
            
    def _trig_pad14(self, value):        
        if value > 0:
            #Track 2 Cell 0: Fire
            self.song().tracks[2].clip_slots[0].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad14 triggered")

    def _trig_pad15(self, value):        
        if value > 0:
            #Track 3 Cell 0: Fire
            self.song().tracks[3].clip_slots[0].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad15 triggered")
    
    #-- DrumBank B ----------------------------------------------------------
    def _trig_pad16(self, value):        
        if value > 0:
            #Track 4 Stop
            self.song().tracks[4].stop_all_clips()
            self.show_message("TFMX Debug: Pad16 triggered")
    
    def _trig_pad17(self, value):                
        if value > 0:
            #Track 5 Stop
            self.song().tracks[5].stop_all_clips()
            self.show_message("TFMX Debug: Pad17 triggered")
    
    def _trig_pad18(self, value):        
        if value > 0:
            #Track 6 Stop
            self.song().tracks[6].stop_all_clips()
            self.show_message("TFMX Debug: Pad18 triggered")
                
   
    def _trig_pad19(self, value):        
        if value > 0:
            #Track 7 Stop
            self.song().tracks[7].stop_all_clips()
            self.show_message("TFMX Debug: Pad19 triggered")

    #2nd row
    def _trig_pad20(self, value):        
        if value > 0:
            #Track 4 Cell 2: Fire
            self.song().tracks[4].clip_slots[2].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad20 triggered")
 
    def _trig_pad21(self, value):        
        if value > 0:
            #Track 5 Cell 2: Fire
            self.song().tracks[5].clip_slots[2].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad21 triggered")
                  
    def _trig_pad22(self, value):        
        if value > 0: 
            #Track 6 Cell 2: Fire
            self.song().tracks[6].clip_slots[2].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad22 triggered")
   
    def _trig_pad23(self, value):        
        if value > 0:
            #Track 7 Cell 2: Fire
            self.song().tracks[7].clip_slots[2].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad23 triggered")
            
    #3rd-row
    def _trig_pad24(self, value):     
        if value > 0:
            #Track 4 Cell 1: Fire
            self.song().tracks[4].clip_slots[1].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad24 triggered")
            
    def _trig_pad25(self, value):        
        if value > 0:
            #Track 5 Cell 1: Fire
            self.song().tracks[5].clip_slots[1].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad25 triggered")    
        
    def _trig_pad26(self, value):        
        if value > 0:
            #Track 6 Cell 1: Fire
            self.song().tracks[6].clip_slots[1].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad26 triggered")

    def _trig_pad27(self, value):        
        if value > 0:
            #Track 7 Cell 1: Fire
            self.song().tracks[7].clip_slots[1].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad27 triggered")
            
    #Top-row
    def _trig_pad28(self, value):        
        if value > 0:
            #Track 4 Cell 0: Fire
            self.song().tracks[4].clip_slots[0].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad28 triggered")
            
    def _trig_pad29(self, value):        
        if value > 0:
            #Track 5 Cell 0: Fire
            self.song().tracks[5].clip_slots[0].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad29 triggered")
            
    def _trig_pad30(self, value):        
        if value > 0:
            #Track 6 Cell 0: Fire
            self.song().tracks[6].clip_slots[0].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad30 triggered")

    def _trig_pad31(self, value):        
        if value > 0:
            #Track 7 Cell 0: Fire
            self.song().tracks[7].clip_slots[0].set_fire_button_state(True)
            self.show_message("TFMX Debug: Pad31 triggered")
            
    #----------------------------------------------------------------------------------------------------------------------------
    
    #Track changed    
    def _update_selected_device(self):
        track = self.song().view.selected_track
        #self.show_message("----- Track changed! -----")
    
    #Launch/Record/Overdub    
    def _launch_clip(self, value):
        global _overdub_flag
        #self.log_message("--> Track launch! -----")
        #self.song().view.highlighted_clip_slot.set_fire_button_state(True)
        _current_slot = self.song().view.highlighted_clip_slot 
        if _current_slot.is_playing == 0 and _current_slot.is_recording == 0:            
            self.song().view.highlighted_clip_slot.set_fire_button_state(True)
        elif _current_slot.is_playing == 1 and _current_slot.is_recording == 0:
            self.song().overdub = 1
            _overdub_flag = 1
        elif _current_slot.is_playing == 1 and _current_slot.is_recording == 1 and _overdub_flag == 1:
            self.song().overdub = 0
            _overdub_flag = 0
        else:
            self.song().view.highlighted_clip_slot.set_fire_button_state(True)
    
    #Move up/down
    def _move_clipslot(self, up):
        scene = self.song().view.selected_scene
        scenes = self.song().scenes
        max_scenes = len(scenes)
        for i in range(max_scenes):
            if scene == scenes[i]:
                #Found our guy
                if up == 1:
                    self.song().view.selected_scene = scenes[i-1]
                    self.show_message("TFMX Debug: Up!")
                else:
                    if scene == scenes[max_scenes-1]:
                        self.song().view.selected_scene = scenes[0]
                    else:
                        self.song().view.selected_scene = scenes[i+1]
                    self.show_message("TFMX Debug: Down!")
    
    #Move left/right
    def _move_track(self, left):
        #Get track and tracks
        track = self.song().view.selected_track
        tracks = self.get_all_tracks(only_visible = True)
        max_tracks = len(tracks)
        #Iterate to find current track's index.
        for i in range(max_tracks):
            if track == tracks[i]:
                #Found our track
                if left == 1:
                    self.song().view.selected_track = tracks[i-1]
                else:
                    if track == tracks[max_tracks-1]:
                        self.song().view.selected_track = tracks[0]
                    else:
                        self.song().view.selected_track = tracks[i+1]
                        
    def get_all_tracks(self, only_visible = False):
        tracks = []
        for track in self.song().tracks:
            if not only_visible or track.is_visible:
                tracks.append(track)
        #Include the master track?
        #NOPE tracks.append(self.song().master_track)
        return tracks
        
    def _move_up(self, value):
        if value > 0:
            self._move_clipslot(1)
            
    def _move_down(self, value):
        if value > 0:
            self._move_clipslot(0)
            
    def _move_left(self, value):
        if value > 0:
            self._move_track(1)
    
    def _move_right(self, value):
        if value > 0:
            self._move_track(0)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------