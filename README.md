A repo for keeping ham radio configurations.  We'll start with different Direwolf configs for different scenarios, but we'll go on from there, I'm sure.
# The Basic Setup
* Raspberry Pi 3B+
* USB sound card (either a Pluggable or uGreen that use the C-Media chip)
* Custom interface cables (just some wire, connectors, and solder...nothing fancy)
* Yaesu FT-1900 and FT-2800 radios
#  Templates


I've started adding some templates and scripts to generate Direwolf and LinBPQ config files dynamically.  These are Jinja2 templates with accompanying Python scripts.
* **gendirewolfaprs.py**: Generates a simple APRS config for Direwolf based on **direwolf-aprsbeacon-template.py**
* **genlinbpq.py**: Generates a config file to be used as **bpq32.cfg**; based on the contents of **linbpq-template.py**

```
Usage: gendirewolfaprs.py CALLSIGN LATITUDE LONGITUDE
  Where:
    CALLSIGN is your amateur radio call (duh!)
    LATITUDE and LONGITUDE are like XX^YY.ZZN or AAA^BB.CCW
```
```
Usage: genlinbqp.py CALLSIGN SSID LOCATOR FREQUENCY CMSPASS LOCALPASS
  Where:
    CALLSIGN is your amateur radio call (duh!)
    SSID is your SSID (duh, again!)
    LOCATOR is your gridsquare
    FREQUENCY is your frequency in Hz (so 145MHz is 145000000)
    CMSPASS is your Winlink sysop password
    LOCALPASS is the local LinBPQ password
```
#  Some of the working config files
There may be quite a few files in the config directory, but these are actually working. Yes, I know I need to learn what branches are.  :)
* **direwolf/direwolf.conf-aprsbeacon-gpsd-simple** : This queries a remote GPSD server for location and configured direwolf to act like a tracker.
* **direwolf/direwolf.conf-winlink-simple** : This sets up Direwolf to be a network-based KISS TNC.  The idea is that you plug your Pi in to your radio and run the Winlink client on you laptop or shack computer to connect and get out.
* **direwolf/direwolf.service** : This is the startup script for Direwolf to run in the background.  It makes sure that `/etc/direwolf.conf` exists before running.
* **bpq/linbpq.service** : This is the startup script for LinBQP to run in the background.  LinBQP isn't packaged as gracefully as Direwolf, so it's a little convoluted.  The important part is the `After` directive, which makes sure Direwolf is running before LinBPQ fires up.
