import Adafruit_BBIO.ADC as ADC
import time
import datetime

T = 0.001 #Sampling time

ADC.setup()

a = []
log = []
trigger_counter = 0

fo = open("DBS903_TENS_Trigger.txt","wb")

while trigger_counter < 5:
	voltage = ADC.read("P9_39")*1.8
	#print(voltage)

	if voltage < 1.00:
		current_time = datetime.datetime.now().time()
		log.append(current_time)
		print('TRIGGER @' + str(voltage) + 'V; Trigger NUMBER: ' + str(trigger_counter))
		fo.write(str(current_time) + "\n")
		trigger_counter += 1


	time.sleep(T)

fo.close()
	
	

#while 1:
#	value = ADC.read("P9_39")
#	print(value)
