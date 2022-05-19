# PID
A simple PID code, for your own tests

## For use it, declare the variable P, I, D, and max output
MyPID=PID(3,1,1,10)
## You can change any value in real time
MyPID.d=0
### Example

for i in range(100):
  a=MyPID.step(0,1,0.1)
MyPID.step(1,0,0.1)

### Example II
ts=0.1
for i in range(100):
  reference=0
  actual=system.actual()
  controlSignal=MyPID.step(actual,setpoint,0.1)
  system.input(controlSignal)
 
