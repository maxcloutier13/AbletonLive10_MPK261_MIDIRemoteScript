#-v1.0 ---------------------------------------------------------------------------------------------------------------------
#   -Sets the encoder knobs to relative instead of absolute (Remember to also change setting on the mpk261 preset
#   -The 8 encoders now auto-map to selected device (blue hand) instead of being pan knobs. Who needs constant pan knobs?
#-v1.1 ---------------------------------------------------------------------------------------------------------------------
#   -Encoder auto-map now auto switches with selected track
#-v1.2 ---------------------------------------------------------------------------------------------------------------------
#   -Bank B and C are working finally! Mapped to tracks 9-16 and 17-24, as would have been expected stock.
#-TODO ---------------------------------------------------------------------------------------------------------------------
#   -I ... think that's it! Phew!

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

#Global variables
mixer = None #Global so it can be manipulated everywhere

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
        self.add_button('Forward', 0, 115, MIDI_CC_TYPE)
        self.add_button('Backward', 0, 116, MIDI_CC_TYPE)
        self.add_matrix('Encoders', make_encoder, 0, [[22, 23, 24, 25, 26,  27, 28, 29]], MIDI_CC_TYPE)
        self.add_matrix('Drum_Pads', make_button, 1, [[81, 83, 84, 86],[74, 76, 77, 79], [67, 69, 71, 72],[60, 62, 64, 65]], MIDI_NOTE_TYPE)

class MPK261MX(ControlSurface):

    def __init__(self, *a, **k):
        super(MPK261MX, self).__init__(*a, **k)
        self.show_message("-----------------------= MPK261MX LOADING - maxcloutier13 says hi =----------------------------------------------------------")
        self.log_message("-----------------------= MPK261MX LOADING - maxcloutier13 says hi =----------------------------------------------------------")
        with self.component_guard():
            midimap = MidiMap()
            #Super crude manual init for the custom buttons and faders 
            #Bank A - Channel 1
            self._ArmButton0 = ButtonElement(False, MIDI_CC_TYPE, 0, 32)
            self._ArmButton1 = ButtonElement(False, MIDI_CC_TYPE, 0, 33)
            self._ArmButton2 = ButtonElement(False, MIDI_CC_TYPE, 0, 34)
            self._ArmButton3 = ButtonElement(False, MIDI_CC_TYPE, 0, 35)
            self._ArmButton4 = ButtonElement(False, MIDI_CC_TYPE, 0, 36)
            self._ArmButton5 = ButtonElement(False, MIDI_CC_TYPE, 0, 37)
            self._ArmButton6 = ButtonElement(False, MIDI_CC_TYPE, 0, 38)
            self._ArmButton7 = ButtonElement(False, MIDI_CC_TYPE, 0, 39)
            self._VolumeSlider0 = SliderElement(MIDI_CC_TYPE, 0, 12)
            self._VolumeSlider1 = SliderElement(MIDI_CC_TYPE, 0, 13)
            self._VolumeSlider2 = SliderElement(MIDI_CC_TYPE, 0, 14)
            self._VolumeSlider3 = SliderElement(MIDI_CC_TYPE, 0, 15)
            self._VolumeSlider4 = SliderElement(MIDI_CC_TYPE, 0, 16)
            self._VolumeSlider5 = SliderElement(MIDI_CC_TYPE, 0, 17)
            self._VolumeSlider6 = SliderElement(MIDI_CC_TYPE, 0, 18)
            self._VolumeSlider7 = SliderElement(MIDI_CC_TYPE, 0, 19)
            #Bank B - Channel 2
            self._ArmButton8 = ButtonElement(False, MIDI_CC_TYPE, 1, 32)
            self._ArmButton9 = ButtonElement(False, MIDI_CC_TYPE, 1, 33)
            self._ArmButton10 = ButtonElement(False, MIDI_CC_TYPE, 1, 34)
            self._ArmButton11 = ButtonElement(False, MIDI_CC_TYPE, 1, 35)
            self._ArmButton12 = ButtonElement(False, MIDI_CC_TYPE, 1, 36)
            self._ArmButton13 = ButtonElement(False, MIDI_CC_TYPE, 1, 37)
            self._ArmButton14 = ButtonElement(False, MIDI_CC_TYPE, 1, 38)
            self._ArmButton15 = ButtonElement(False, MIDI_CC_TYPE, 1, 39)
            self._VolumeSlider8 = SliderElement(MIDI_CC_TYPE, 1, 12)
            self._VolumeSlider9 = SliderElement(MIDI_CC_TYPE, 1, 13)
            self._VolumeSlider10 = SliderElement(MIDI_CC_TYPE, 1, 14)
            self._VolumeSlider11 = SliderElement(MIDI_CC_TYPE, 1, 15)
            self._VolumeSlider12 = SliderElement(MIDI_CC_TYPE, 1, 16)
            self._VolumeSlider13 = SliderElement(MIDI_CC_TYPE, 1, 17)
            self._VolumeSlider14 = SliderElement(MIDI_CC_TYPE, 1, 18)
            self._VolumeSlider15 = SliderElement(MIDI_CC_TYPE, 1, 19)
            #Bank C - Channel 3
            self._ArmButton16 = ButtonElement(False, MIDI_CC_TYPE, 2, 32)
            self._ArmButton17 = ButtonElement(False, MIDI_CC_TYPE, 2, 33)
            self._ArmButton18 = ButtonElement(False, MIDI_CC_TYPE, 2, 34)
            self._ArmButton19 = ButtonElement(False, MIDI_CC_TYPE, 2, 35)
            self._ArmButton20 = ButtonElement(False, MIDI_CC_TYPE, 2, 36)
            self._ArmButton21 = ButtonElement(False, MIDI_CC_TYPE, 2, 37)
            self._ArmButton22 = ButtonElement(False, MIDI_CC_TYPE, 2, 38)
            self._ArmButton23 = ButtonElement(False, MIDI_CC_TYPE, 2, 39)
            self._VolumeSlider16 = SliderElement(MIDI_CC_TYPE, 2, 12)
            self._VolumeSlider17 = SliderElement(MIDI_CC_TYPE, 2, 13)
            self._VolumeSlider18 = SliderElement(MIDI_CC_TYPE, 2, 14)
            self._VolumeSlider19 = SliderElement(MIDI_CC_TYPE, 2, 15)
            self._VolumeSlider20 = SliderElement(MIDI_CC_TYPE, 2, 16)
            self._VolumeSlider21 = SliderElement(MIDI_CC_TYPE, 2, 17)
            self._VolumeSlider22 = SliderElement(MIDI_CC_TYPE, 2, 18)
            self._VolumeSlider23 = SliderElement(MIDI_CC_TYPE, 2, 19)
            #Drum rack
            drum_rack = DrumRackComponent(name='Drum_Rack', is_enabled=False, layer=Layer(pads=midimap['Drum_Pads']))
            drum_rack.set_enabled(True)
            transport = TransportComponent(name='Transport', is_enabled=False, layer=Layer(play_button=midimap['Play'], record_button=midimap['Record'], stop_button=midimap['Stop'], seek_forward_button=midimap['Forward'], seek_backward_button=midimap['Backward'], loop_button=midimap['Loop']))
            transport.set_enabled(True)
            #This "Device" object enables the automapping of the encoders
            device = DeviceComponent(name='Device', is_enabled=False, layer=Layer(parameter_controls=midimap['Encoders']), device_selection_follows_track_selection=True)
            device.set_enabled(True)
            self.set_device_component(device)
            #Set mixer to full size
            mixer_size = 24
            self._mixer = MixerComponent(mixer_size, name='Mixer', is_enabled=False)
            #Super crude and repetitive mapping because after all this shit I'm not spending time learning how to loop this crap hehe
            #Bank A
            self._mixer.channel_strip(0).layer = Layer(volume_control = self._VolumeSlider0, arm_button=self._ArmButton0)
            self._mixer.channel_strip(1).layer = Layer(volume_control = self._VolumeSlider1, arm_button=self._ArmButton1)
            self._mixer.channel_strip(2).layer = Layer(volume_control = self._VolumeSlider2, arm_button=self._ArmButton2)
            self._mixer.channel_strip(3).layer = Layer(volume_control = self._VolumeSlider3, arm_button=self._ArmButton3)
            self._mixer.channel_strip(4).layer = Layer(volume_control = self._VolumeSlider4, arm_button=self._ArmButton4)
            self._mixer.channel_strip(5).layer = Layer(volume_control = self._VolumeSlider5, arm_button=self._ArmButton5)
            self._mixer.channel_strip(6).layer = Layer(volume_control = self._VolumeSlider6, arm_button=self._ArmButton6)
            self._mixer.channel_strip(7).layer = Layer(volume_control = self._VolumeSlider7, arm_button=self._ArmButton7)
            #Bank B
            self._mixer.channel_strip(8).layer = Layer(volume_control = self._VolumeSlider8, arm_button=self._ArmButton8)
            self._mixer.channel_strip(9).layer = Layer(volume_control = self._VolumeSlider9, arm_button=self._ArmButton9)
            self._mixer.channel_strip(10).layer = Layer(volume_control = self._VolumeSlider10, arm_button=self._ArmButton10)
            self._mixer.channel_strip(11).layer = Layer(volume_control = self._VolumeSlider11, arm_button=self._ArmButton11)
            self._mixer.channel_strip(12).layer = Layer(volume_control = self._VolumeSlider12, arm_button=self._ArmButton12)
            self._mixer.channel_strip(13).layer = Layer(volume_control = self._VolumeSlider13, arm_button=self._ArmButton13)
            self._mixer.channel_strip(14).layer = Layer(volume_control = self._VolumeSlider14, arm_button=self._ArmButton14)
            self._mixer.channel_strip(15).layer = Layer(volume_control = self._VolumeSlider15, arm_button=self._ArmButton15)
            #Bank C     
            self._mixer.channel_strip(16).layer = Layer(volume_control = self._VolumeSlider16, arm_button=self._ArmButton16)
            self._mixer.channel_strip(17).layer = Layer(volume_control = self._VolumeSlider17, arm_button=self._ArmButton17)
            self._mixer.channel_strip(18).layer = Layer(volume_control = self._VolumeSlider18, arm_button=self._ArmButton18)
            self._mixer.channel_strip(19).layer = Layer(volume_control = self._VolumeSlider19, arm_button=self._ArmButton19)
            self._mixer.channel_strip(20).layer = Layer(volume_control = self._VolumeSlider20, arm_button=self._ArmButton20)
            self._mixer.channel_strip(21).layer = Layer(volume_control = self._VolumeSlider21, arm_button=self._ArmButton21)
            self._mixer.channel_strip(22).layer = Layer(volume_control = self._VolumeSlider22, arm_button=self._ArmButton22)
            self._mixer.channel_strip(23).layer = Layer(volume_control = self._VolumeSlider23, arm_button=self._ArmButton23)
            self._mixer.set_enabled(True)
