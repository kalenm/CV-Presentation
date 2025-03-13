### Tuning Files

This is a quick note about the tuning files contained in this directory. They all come from the common tuning files that are included with libcamera, without any tweaks to the json.
 
Vc4 is specifically for the raspberry pi 4 and pisp is specific to the raspberry pi 5.

At some point I may actually sit down and make custom tuning files if I feel that would be the best decision for the highest level of accuracy but considering I am just doing this for fun I won't go that insane(currently).

I included both ir and noir as honestly they are both fairly inaccurate to the curent sensor and lens setup that I am using so its kinda up to if I want warmer or darker colors today.

NOTE: The speicifc tuning file to use should be the pi5 json file in pisp, which was downloaded from arducam directly. Further testing is required to see how well it performs againsts the native tuning files but I will include test photos to see how it works.
