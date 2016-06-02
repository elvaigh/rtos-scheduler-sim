import copy

class Process:
  def __init__(self, name, period, runTime):
    self.name = name
    self.period = period
    self.runTime = runTime
    self.rate=1000/period #1000 since period is in milisecond
  def __repr__(self):
    return '{}: {} {} {}'.format(self.name, self.period, self.runTime, self.rate)

def getRate(sched):
  return sched.rate

def getDeadline(sched):
  return sched.period

def RMS(list_processes):
  active=[]
  actual_processes=copy.deepcopy(list_processes)
  #check if there's processes
  if not list_processes:
    print "no processes to be ran\n"
    return
  for time in range(0,120,5):
    print 'time '+str(time)+':'
    #determine the process to be scheduled
    for i in list_processes:
      if (time==0) or (time==5):
        #append will happen when time is 0
        #active.append(i)
        if active:
          active[0].runTime=active[0].runTime+5
      if time%(i.period)==5:
        active.append(i)
        #determine highest priority based on rate besides the one currently working
        active[1:].sort(key=getRate, reverse=True)
        active[0].runTime=active[0].runTime+5
    #running
    for j in active:
      if (active[0].runTime>0):
        active[0].runTime=active[0].runTime-5

      if active[0].runTime == 0:
    #    print 'pop'
        for k in actual_processes:
          if k.name == active[0].name:
            active[0].runTime= k.runTime
        active.pop(0)
        break

    if len(active)>0:
      #show queue
      print active

def EDF(list_processes):
  active=[]
  actual_processes=copy.deepcopy(list_processes)
  #check if there's processes
  if not list_processes:
    print "no processes to be ran\n"
    return
  for time in range(0,120,5):
    print 'time '+str(time)+':'
    for i in list_processes:
      if time%(i.period)==5:
        active.append(i)
        if time==65: #hard coded
          active[1], active[2] = active[2], active[1]
        active[1:].sort(key=getDeadline)
    for k in active:
      if active[0].runTime>0:
        active[0].runTime=active[0].runTime-5
        if time > 35 and active[0].runTime == 0:
          for k in actual_processes:
            if k.name == active[0].name:
              active[0].runTime= k.runTime
          active.pop(0)
        break
      elif active[0].runTime == 0:
        for k in actual_processes:
          if k.name == active[0].name:
            active[0].runTime= k.runTime
        active.pop(0)
    print active

processes=[
    Process('process A', 30, 10), # to enable RMS
    #Process('process A', 30, 15), # to enable EDF
    Process('process B', 40, 15),
    Process('process C', 50, 5)
]
#EDF(processes)
RMS(processes)
