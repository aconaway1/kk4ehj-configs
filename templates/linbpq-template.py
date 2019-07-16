; Basic Webmail configuration

SIMPLE ; This set a whole load of paramters to reasonable defaults

LOCATOR={{ locator }}
MAPCOMMENT={{ mapcomment }}
NODECALL={{ callsign }}
INFOMSG:
{{ callsign }}'s LinBPQ Gateway
***
; This is the CMS side
PORT
  ID=Telnet Server
  DRIVER=TELNET
  WL2KREPORT PUBLIC, api.winlink.org, 80, {{ callsign }}-{{ ssid }}, {{ locator }}, 00-23, {{ freq }}, PKT1200
  CONFIG
    LOGGING=1
    CMS=1 ; Enable CMS Gateway
    CMSCALL={{ callsign }}
    CMSPASS={{ cmspass }}
    HTTPPORT=8080 ; Port used for Web Management/WebMail
    TCPPORT=8010 ; Port for Telnet Access
    FBBPORT=8011 ; Not required, but allows monitoring using BPQTermTCP
    MAXSESSIONS=10 ;
    CloseOnDisconnect=1 ; Close Telnet Session when Node disconnects
    USER={{ callsign }},{{ localpass }},{{ callsign }}, "",SYSOP
ENDPORT
; We're using Direwolf as a TNC, so we're using the KISS protocol
PORT
  ID=Kiss Port
  TYPE=ASYNC
  PROTOCOL=KISS
  FRACK=10000
  RESPTIME=3000
  RETRIES=10
  MAXFRAME=2
  PACLEN=200
  TXDELAY=500
  SLOTTIME=100
  PERSIST=64
  IPADDR=127.0.0.1
  TCPPORT=8100
ENDPORT
APPLICATION 1,BBS,,{{ callsign }}
APPLICATION 2,RMS,C 1 CMS,{{ callsign }}-{{ ssid }}
LINMAIL                 ; Enable BBS
