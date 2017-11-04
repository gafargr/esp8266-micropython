import dht
import machine, time
d = dht.DHT11(machine.Pin(2))
from machine import Pin, I2C
import ssd1306
import onewire
import ds18x20
i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)
lcd = ssd1306.SSD1306_I2C(128,32,i2c)
led = machine.Pin(16, machine.Pin.OUT)
adc = machine.ADC(0)
#ow = onewire.OneWire(Pin(14))
#ds = ds18x20.DS18X20(ow)
dat = machine.Pin(14)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
linha1=0
linha2=10
linha3=21
lido=1024
volt=1023.0
temp=23.00

print("read DHT11 and ADC0")
roms = ds.scan()
print('found devices:', roms)

def le_ad():
   lido=adc.read()
   volt=lido/1023.0;
   volt=volt*3.3
   vol_1 = 'V=' + str(volt)[:4] 
   lcd.text(vol_1,0,linha3)
   return

def le_dht():
   d.measure()
   temp = d.temperature()
   hum = d.humidity()
   lcd.fill(0)
   lcd.text("temperatura   C",0,linha1)
   lcd.text(str(d.temperature()),95,linha1)  
   lcd.text("umidade ar    % ",0,linha2)
   lcd.text(str(d.humidity()),95,linha2)
   return

def le_1820():
    #print('temperatures:')
    ds.convert_temp()
    time.sleep_ms(500)
    for rom in roms:
        temp = (ds.read_temp(rom))
        sai = 'T=' + str(temp)[:5] 
        lcd.text(sai,62,linha3)
    #print()
    return

   
     
while True:
   led.value(0)
   le_dht()
   le_ad()
   le_1820()
   lcd.show()
   led.value(1)
   time.sleep(0.5)



    
    
    

