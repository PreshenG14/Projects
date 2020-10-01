import BlynkLib
import RPi.GPIO as GPIO # Importing Raspberry Pi GPIO Pins
import time # Importing time module
GPIO.setwarnings(False) # Disabling GPIO warnings
GPIO.setmode(GPIO.BCM) # Using GPIO Name 

blynk = BlynkLib.Blynk('ja7MnU7v8fQGAlvXCMUs8FMfRp3CsnOH')
blynk.run()
time.sleep(4)

PWM = 0
PWM1=0
delay=0.01
delay1=0.3

#set GPIO Pins

LL = 14
LC = 15
LR = 18
RL = 25
RC = 7
RR = 1
OB1=17
OB2=22

GPIO.setup(OB1, GPIO.IN)
GPIO.setup(OB2, GPIO.IN)
GPIO.setup(LL, GPIO.IN)
GPIO.setup(LC, GPIO.IN)
GPIO.setup(LR, GPIO.IN)
GPIO.setup(RL, GPIO.IN)
GPIO.setup(RC, GPIO.IN)
GPIO.setup(RR, GPIO.IN)


GPIO.setup(5,GPIO.OUT) # Setting GPIO 5 as output (Input signal for L293DNE - Left Motor +)
my_pwm1=GPIO.PWM(5,50) # Setting GPIO 5 as PWM Signal 50Hz
my_pwm1.start(0) # GPIO 5 PWM start value = 0

GPIO.setup(6,GPIO.OUT) # Setting GPIO 6 as output (Input signal for L293DNE - Left Motor +)
my_pwm2=GPIO.PWM(6,50) # Setting GPIO 6 as PWM Signal 50Hz
my_pwm2.start(0) # GPIO 6 PWM start value = 0

GPIO.setup(20,GPIO.OUT) # Setting GPIO 20 as output (Input signal for L293DNE - Right Motor -)
my_pwm3=GPIO.PWM(20,50) # Setting GPIO 20 as PWM Signal 50Hz
my_pwm3.start(0) # GPIO 20 PWM start value = 0

GPIO.setup(21,GPIO.OUT) # Setting GPIO 21 as output (Input signal for L293DNE - Right Motor +)
my_pwm4=GPIO.PWM(21,50) # Setting GPIO 21 as PWM Signal 50Hz
my_pwm4.start(0) ## GPIO 21 PWM start value = 0



def forward():
    my_pwm1.ChangeDutyCycle(0) # Supply duty cycle to GPIO 5
    my_pwm2.ChangeDutyCycle(PWM1) # Supply duty cycle to GPIO 6
    my_pwm3.ChangeDutyCycle(0) # Supply duty cycle to GPIO 20
    my_pwm4.ChangeDutyCycle(PWM) # Supply duty cycle to GPIO 21

    blynk.virtual_write(5,PWM1)
    blynk.virtual_write(6,PWM)
    blynk.virtual_write(7,0)
    blynk.virtual_write(8,0)
    blynk.virtual_write(3,'Forward')
    blynk.virtual_write(1,0)
    blynk.virtual_write(2,0)
    time.sleep(0.05)
        
def left():
    my_pwm1.ChangeDutyCycle(PWM) # Supply duty cycle to GPIO 5
    my_pwm2.ChangeDutyCycle(0) # Supply duty cycle to GPIO 6
    my_pwm3.ChangeDutyCycle(0) # Supply duty cycle to GPIO 20
    my_pwm4.ChangeDutyCycle(PWM) # Supply duty cycle to GPIO 21
	
    blynk.virtual_write(5,PWM)
    blynk.virtual_write(6,0)
    blynk.virtual_write(7,0)
    blynk.virtual_write(8,PWM)
    blynk.virtual_write(3,'Left')
    blynk.virtual_write(1,PWM)
    blynk.virtual_write(2,0)
    time.sleep(0.05)

def right():
    my_pwm1.ChangeDutyCycle(0) # Supply duty cycle to GPIO 5
    my_pwm2.ChangeDutyCycle(PWM) # Supply duty cycle to GPIO 6
    my_pwm3.ChangeDutyCycle(PWM) # Supply duty cycle to GPIO 20
    my_pwm4.ChangeDutyCycle(0) # Supply  duty cycle to GPIO 21

    blynk.virtual_write(5,0)
    blynk.virtual_write(6,PWM)
    blynk.virtual_write(7,PWM)
    blynk.virtual_write(8,0)
    blynk.virtual_write(3,'Right')
    blynk.virtual_write(1,0)
    blynk.virtual_write(2,PWM)
    time.sleep(0.05)

def stop():
    my_pwm1.ChangeDutyCycle(0) # Supply duty cycle to GPIO 5
    my_pwm2.ChangeDutyCycle(0) # Supply duty cycle to GPIO 6
    my_pwm3.ChangeDutyCycle(0) # Supply duty cycle to GPIO 20
    my_pwm4.ChangeDutyCycle(0) # Supply duty cycle to GPIO 21

    blynk.virtual_write(5,0)
    blynk.virtual_write(6,0)
    blynk.virtual_write(7,0)
    blynk.virtual_write(8,0)
    blynk.virtual_write(3,'Stop')
    blynk.virtual_write(1,0)
    blynk.virtual_write(2,0)
    time.sleep(0.05)


while 1:
    
    if (GPIO.input(OB1)==False or GPIO.input(OB2)==False): #Stop
         stop()
         blynk.virtual_write(4,'Obstacle Detected')
         blynk.virtual_write(9,255)
         time.sleep(0.03)
        
    else: #Check for Movement
         blynk.virtual_write(4,'All Clear')
         blynk.virtual_write(9,0)
         time.sleep(0.03)

         if(GPIO.input(LC)==False and GPIO.input(LR)==False and GPIO.input(RL)==False and GPIO.input(RC)==True):
            PWM= 90
            
            if(GPIO.input(LL)==False):
                PWM = PWM + 10                        
            else:
                PWM=PWM
              
            left()
            time.sleep(delay1)
            
         elif(GPIO.input(LC)==False and GPIO.input(LR)==False and GPIO.input(RL)==True and GPIO.input(RC)==True):
        
            PWM = 80   
            if(GPIO.input(LL)==False):
                PWM = PWM + 20                       
            else:
                PWM=PWM                          
            
            left()
            time.sleep(delay1)
            
            
         elif(GPIO.input(LC)==False and GPIO.input(LR)==True and GPIO.input(RL)==True and GPIO.input(RC)==True):
            
            PWM = 80
            if(GPIO.input(LL)==False):
                PWM = PWM + 20                      
            else:
                PWM=PWM
                                   
            left()
            time.sleep(delay1)
            
        
         elif(GPIO.input(LC)==True and GPIO.input(LR)==False and GPIO.input(RL)==False and GPIO.input(RC)==False):
            
            
            PWM = 90
            if(GPIO.input(RR)==False):
                PWM = PWM + 10
                             
            else:
                PWM=PWM                              
             
            right()
            time.sleep(delay1)
            
         elif(GPIO.input(LC)==True and GPIO.input(LR)==False and GPIO.input(RL)==True and GPIO.input(RC)==True):
            
            PWM = 70
            if(GPIO.input(LL)==False):
                PWM = PWM + 20                       
            else:
                PWM=PWM                            
             
            left()
            time.sleep(delay)
            
         elif(GPIO.input(LC)==True and GPIO.input(LR)==True and GPIO.input(RL)==False and GPIO.input(RC)==False):
            
            PWM = 80            
            if(GPIO.input(RR)==False):
                PWM = PWM + 20                        
            else:
                PWM=PWM                          
            
            right()
            time.sleep(delay1)
            
         elif(GPIO.input(LC)==True and GPIO.input(LR)==True and GPIO.input(RL)==False and GPIO.input(RC)==True):
            
            PWM = 70          
            if(GPIO.input(RR)==False):
                PWM = PWM + 20                      
            else:
                PWM=PWM                       
            
            right()
            time.sleep(delay)

         elif(GPIO.input(LC)==True and GPIO.input(LR)==True and GPIO.input(RL)==True and GPIO.input(RC)==False):
            
            PWM = 80            
            if(GPIO.input(RR)==False):
                PWM = PWM + 20                  
            else:
                PWM=PWM                          
            
            right()
            time.sleep(delay)
            
         elif(GPIO.input(LC)==False and GPIO.input(LR)==False and GPIO.input(RL)==True and GPIO.input(RC)==False):
            
            PWM = 70            
            if(GPIO.input(RR)==False):
                PWM = PWM + 20                  
            else:
                PWM=PWM                          
            
            left()
            time.sleep(delay)
            
         elif(GPIO.input(LC)==False and GPIO.input(LR)==True and GPIO.input(RL)==False and GPIO.input(RC)==False):
            
            PWM = 70            
            if(GPIO.input(RR)==False):
                PWM = PWM + 20                  
            else:
                PWM=PWM                          
            
            left()
            time.sleep(delay)


         elif(GPIO.input(LC)==True and GPIO.input(LR)==True and GPIO.input(RL)==True and GPIO.input(RC)==True):
          
            PWM = 75
            if(GPIO.input(LL)==False and GPIO.input(RR)==True):
                PWM = 100
                
                left()
                time.sleep(delay1)
            elif(GPIO.input(RR)==False and GPIO.input(LL)==True):
                PWM = 100
                
                right()
                time.sleep(delay1)
            else:
                PWM=50
                PWM1=65
                
                forward()

         elif(GPIO.input(LC)==False and GPIO.input(LR)==False and GPIO.input(RL)==False and GPIO.input(RC)==False):
            
            PWM = 0
            
            stop()
            
         elif(GPIO.input(LC)==True and GPIO.input(LR)==False and GPIO.input(RL)==False and GPIO.input(RC)==True):
            
            PWM = 40
            PWM1=60
            
            forward()
            time.sleep(0.1)
            stop()
            
    

         else:
            
            stop()
  

