#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/TriggerFinger/__init__.py
from _Framework.Capabilities import controller_id, inport, outport, CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT, REMOTE
from .TriggerFingerMX import TriggerFingerMX

#def get_capabilities():
#    return {PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SCRIPT, REMOTE])]}

def create_instance(c_instance):
    """ The generic script can be customised by using parameters (see config.py). """
    #return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTIONS, MIXER_OPTIONS)
    #Fuck this generic bullshit. Let's try something.
    return TriggerFingerMX(c_instance)