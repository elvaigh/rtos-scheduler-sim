'''struct

void RMS( int period[], int runTime[], int process[]){
  for(int time=0; time<120; time=time+5){
    //determine the process to be scheduled

    //determine highest priority based on rate
    //run it
  }//for
}//RMS
'''
import copy

class Schedule:
  def __init__(self, name, period, runTime):
    self.name = name
    self.period = period
    self.runTime = runTime
    self.priority=1000/period
  def __repr__(self):
    return '{}: {} {} {}'.format(self.name, self.period, self.runTime, self.priority)

def getPriority(sched):
    return sched.priority

def RMS(list_processes):
  active=[]
  actual_processes=copy.deepcopy(list_processes)
  #check if there's processes
  if not list:
    print "no processes to be ran\n"
    return
  for time in range(0,120,5):
    print 'time ',time+5

    #determine the process to be scheduled
    for i in list_processes:
      if time==5:
        active.append(i)
        print 'here'
        if active:
          active[0].runTime=active[0].runTime+5
      elif (time)%(i.period)== 0:
        for o in active:
          if o.name != i.name:
              active.append(i)
        active[1:].sort(key=getPriority, reverse=True)
        if active:
          active[0].runTime=active[0].runTime+5
    if len(active)>0:
        print active, '\n'
    #determine highest priority based on rate
    for j in active:
      if active[0].runTime>0:
        active[0].runTime=active[0].runTime-5
      if active[0].runTime == 0:
    #    print 'pop'
        for k in actual_processes:
          if k.name == active[0].name:
            active[0].runTime= k.runTime
        active.pop(0)

    #if len(active)>0:
    #    print active, '\n'

processes=[]

processes.append(Schedule('process A', 30, 10))
processes.append(Schedule('process B', 40, 15))
processes.append(Schedule('process C', 50, 5))


RMS(processes)
