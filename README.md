Overview: 

 

The Runway Incursion Prevention System (RIPS) is designed to minimize frequent runway 

incursions at both controlled(towered) and uncontrolled(non-towered) airports by providing an 

additional visual warning system to alert Pilots and other users of the taxiways and runways 

(ground personnel) of the use or imminent use of the runway. 

RIPS uses available ADSB Automatic Dependent Surveillance-Broadcast technology which is 

now required in almost all General Aviation Aircraft as well as all commercial aircraft. ADSB-out 

technology transmits an extended sequence or extended squitter from an equipped Transponder 

indicating the aircraft’s identity, altitude, latitude, and longitude. This extended squitter is 

transmitted over the standard transponder 1090 Mhz frequency. A lower cost ADSB-out 

technology is also available using a dedicated 978 Mhz Universal Access Transmitter or UAT 

frequency in order to obviate replacing the expensive transponder on low value aircraft. 

The RIPS system employs a dual ADSB-In receiver with the ability to receive transmissions from 

both 1090 Mzzzzxxkhz Extended Squitter and 978 Mhz UAT ADSB out systems. In addition to 

depending on the ADSB technology for determining aircraft position, an optional “Optical 

Detector” system can be added at all entrances and exits to/from any runway. This way, 

vehicles, in addition to aircraft can be detected, even if they do not have ADSB out. Also, the few 

legacy NORDO or no radio antique aircraft without electrical systems could be detected taking 

the runway and taking off or landing and exiting the runway. This optical system should use 

multiple detectors at each location to indicate the direction of traffic on or off the runway. 

The ADSB receive will pass all aircraft detections received from any location and altitude from 

airport to a processing system which will apply rules that are used to make runway in use 

determinations. Similarly, the Optical detectors will pass all detections onto the processing 

system in order to apply rules. 

 

Processing and Rules: 

Processing for ADSB detections and Optical detections can be handled by a basic embedded 

computer processing system which would handle power disruptions and reboot automatically. 

The system could be tested and refined with a more conventional personal computer during initial 

testing. 

 

ADSB Detections and Rules: 

 

Aircraft detected within 4 miles of airport and below 2000 feet AGL(above ground level) will 

generate an alert to track that aircraft. Tracked aircraft will be placed on a queue and monitored 

further. Once tracked, they will be removed from the queue of their altitude or distance from the 

airport indicates they no longer should be tracked. 

 

Aircraft detected outside of 4 miles of airport and/or above 2000 feet AGL will be ignored. 

 

Aircraft detected below 1000 feet AGL and within 2 miles of airport will generate a 

Runway_Use_Imminent token which will be passed to the lighting control hardware. 

 

Aircraft detected below 500 feet AGL and within 1 mile of airport will generate a Runway_In_Use 

token which will be passed to the lighting control hardware. 

  

A Runway_Clear token will be issued when a climbing aircraft is detected at 200 feet AGL while 

taking off. 

 

Optical Detections and Rules: 

 

Any vehicle (aircraft or other vehicle) that triggers an optical detection at entrance to the runway 

generates a Runway_In_Use token and passes it to the lighting control hardware. 

 

A Runway_Clear token will be issued once that vehicle is detected leaving the runway. 

 

In addition, a Runway_Clear token will be issued when a landing aircraft is detected leaving the runway. 

 

Lighting Control: 

 

Only receives tokens from both the ADSB and Optical Processing Systems. The state of the 

Lighting control system is considered latching. Contradictory tokens from the two processing 

systems will always assume the more severe state, which cannot be removed until a lessor state 

is indicated.  

 

Inputs to Runway Incursion Protection System: 

  

Aircraft_In_Pattern_Detect (from ADSB non-ground receiver system) 

Aircraft_On_Runway_Detect (from ADSB ground receiver system) 

Aircraft_Leaving_Runway(from ADSB ground receiver system) 

  

These inputs assume a local ground based ADSB receiver system that can detect ground and air based ADSB transmissions over 1090 Mhz Extended Squiter and 978 Mhz UAT. 

  

Outputs from Runway Incursion Protection System: 

  

Runway_Clear 

Runway_In_Use 

Runway_Use_Imminent 

  

The three outputs could be used to control runway incursion lighting at each runway entrance.  Clear could indicate Green, In_Use could indicate Red, and Imminent could indicate Yellow. 