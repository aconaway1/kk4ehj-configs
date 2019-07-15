#  The audio device to use
ADEVICE  plughw:1,0
#  The number of audio channels on this device
ACHANNELS 1
#  The audio channel config
CHANNEL 0
#  Ummmm...your call
MYCALL {{ callsign }}
#  Usually 1200
MODEM 1200
#  The GPIO pin to use.  Use -X to invert the PTT state
PTT GPIO -17
#  Beacon properties
#    delay = wait to start
#    every = interval
#    overlay = avatar stuff
#    symbol = APRS symbol to use
#    lat, long = duh!
#    power, height, gain = artificial antenna stuff to inject
#    comment = text to include in the beacon
#    via = APRS path (should ALWAYS be "WIDE1-1,WIDE2-1")
PBEACON delay=1 every=30 overlay=S symbol="home" lat={{ lat }} long={{ long }} power=50 height=20 gain=4 comment="{{ comment }}" via=WIDE1-1,WIDE2-1 
#  Bind TNC protocols to certain ports
AGWPORT 8000
KISSPORT 8100
#  Log to this directory
LOGDIR	/var/log/direwolf
