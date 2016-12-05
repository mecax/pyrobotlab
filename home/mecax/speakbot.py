

from java.lang import String
import threading

##aimlPath = "E:\PROGRAMAS\MRL\ProgramAB\bots\max\aiml"
aimlBotName = "max"
aimlUserName = "fede"
botVoice = "Antonio"
###botVoice = "Rod"

def heard(data):
  print "Speech Recognition Data:"+str(data)

#####################################################
#################
#
# MAIN ENTRY POINT  - Start and wire together all the 
#services.
#
#####################################################
#################

# launch the swing gui?
# gui = Runtime.createAndStart("gui", "GUIService");

#####################################################
#################
# Create ProgramAB chat bot ( This is the inmoov 
#"brain" )
#####################################################
#################
harry = Runtime.createAndStart("harry", "ProgramAB")
##harry.setPath(aimlPath)
harry.startSession("ProgramAB", "fede", "max")
##harry.startSession("ProgramAB", "default", "alice2")

#####################################################
#################
ear = Runtime.createAndStart("i01.ear", "WebkitSpeechRecognition")

# Html filter to clean the output from programab.  
#(just in case)
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")

#####################################################
#################
# mouth service, speech synthesis
mouth = Runtime.createAndStart("i01.mouth", "AcapelaSpeech")
mouth.setVoice(botVoice)

#####################################################
#################
# the "ear" of the inmoov TODO: replace this with 
#just base inmoov ear?

ear.addListener("publishText", python.name, "heard");
ear.addMouth(mouth)

#####################################################
#################
# MRL Routing webkitspeechrecognition/ear -> program 
#ab -> htmlfilter -> mouth
#####################################################
#################
ear.addTextListener(harry)
harry.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
