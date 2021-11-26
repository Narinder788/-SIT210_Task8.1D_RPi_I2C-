import smbus
import time

address_device = 0x23

p_on= 0x01
p_off = 0x00  
Reset   = 0x07

address = 0x23

bus = smbus.SMBus(1)


def light_value(addr): 
  var=(addr[1] + (256 * addr[0])) / 1.2
  return (var)


def convert_light_value():
  address = bus.read_i2c_block_data(address_device,address)
  return light_value(address) 

def cases():
  while True:
    intensity= light_value()
    print(intensity)
    if(intensity>= 2000):
        print("too brightly")
    elif(intensity> 1000 and intensity<500):
        print(" bright")
    elif(intensity > 500 and intensity< 200):
        print("average bright")
    elif(intensity<200 and intensity>150):
        print("dark")
    elif(intensity<50):
        print("too dark")
 
    time.sleep(0.025)
