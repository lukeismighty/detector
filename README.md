# detector
Door Detector using Raspberry Pi and a reed switch/magnet combo

The whole point of the project here was to make a door detector so while sitting in my office, I would know if someone opened the front door or not. I could have used a light or a push notification or something but I didn't want the device on the internet, nor did I want something I wouldn't see if I weren't facing it. So I opted for an auditory notification.

The hardware used is a Raspbery Pi 3 Model B, an SD card, a USB cable and USB wall outlet, a bunch of wire (3 in count), a reed switch, a magnet, some solder to hold the switch to the wires, some breadboard testing cables that would plug onto the Pi's GPIO pins, some Liquid Nails glue, and some hot glue to cover the bare metal connections before heat shrinking them all. The layout looks like this:

USB wall outlet -> USB cable -> Raspberry PI and SD Card -> breadboard testing cables -> solder -> wires and heat shrink -> solder -> reed switch, hot glue, and heat shrink. Then the reed switch hangs out on the door jam near the floor where nobody kicks it next to the magnet on the door when the door is shut. 

The sound file was snipped to only play the first two seconds of the file and saved into a new file, it is not provided, but the original file is here in the repo. In the end, I ended up using the original file that is provided, but allowed it to only run for 4 seconds before stopping the playback. The door is checked every tenth of a second if it should make a noise or not.

The desktop file is so I could drop the program into an autoplay fashion on the Raspberry Pi. It'll autorun and keep going until I reboot the machine or kill the process and restart it manually.

The detector.py program itself uses RPi.GPIO to sense the reed switch's status, whether it be open or closed. It'll be one way when the magnet is near it and the other when not. You can read up on reed switches here, https://en.wikipedia.org/wiki/Reed_switch.

The detector.py program also utilizes the time library, so it can wait between noises, otherwise it'll try to annoy you to death with its constant chirping.

The detector.py program utilizes vlc's py library to play the audio. There were a lot of ways to go about this, but VLC is a wonderful program and plays just about anything under the sun. I opted for their library as it is easy to use, inside one file, didn't require anything to be installed aside from the file being next to the detector program, and lastly, it worked.

The detector.py program utilizes the os library to control the sound level of the computer.

The idea is, when the door is closed, the magnet that is glued to the bottom left of the door by the door's hinges, will not trigger the program to make a sound. When the door is opened, the magnet moves away with the door, triggering the reed switch to change and having the program make the sound.

The speaker I used is not attached to the Raspberry Pi either, it is a bluetooth shower speaker on the other side of my office, roughly 30 feet away. I left the volume at 100%.

Occasionally the Raspberry Pi will lose connection to the bluetooth speaker, but I think that is due to distance. I had it farther away before where it sits now and would lose it each day, it has turned to around once a month or every other month. I can live with that.
