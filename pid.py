class PID:
  def __init__(self, p,i,d,max):
    ''' 
    Inicialización del PID
    '''
    self.p=p
    self.i=i
    self.d=d
    self.max=max
    self.acu=0
    self.anterior=0
    print("Initialized")

  def step(self,actual,reference,ts,accelerationCompensation=0):
    '''
    Reference to follow, actual state of the system, ts time sampling, 
    accelerationCompensation, is for motion mechanisms
    '''
    error=reference-actual
    ksignal=self.p*error

    dsignal=(actual-(self.anterior))/ts*self.d
    self.anterior=actual

    self.acu=self.acu+error*ts
    isignal=self.acu*self.i

    output=ksignal+dsignal+isignal

    if(output>self.max):
      self.acu=self.acu-error*ts #Anti windup
      output=self.max*np.sign(output)
    return output
