from microbit import pin1, sleep

from Single_Relay import Single_Relay

relay = Single_Relay(pin1)

relay.on()
sleep(1000)
relay.off()
