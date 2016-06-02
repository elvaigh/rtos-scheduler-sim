# processor-rms
a simple Rate Monotonic Scheduling (RMS) and Earliest deadline first (EDF). This is an assignment for my Operating Systems for Embedded Applications

###Issues:
  
  **RMS:**
  
     At 20, decrements process B twice
      time 0:
      time 5:
      [process A: 30 20 33, process B: 40 15 25, process C: 50 5 20]
      time 10:
      [process A: 30 5 33, process B: 40 15 25, process C: 50 5 20]
      time 15:
      [process B: 40 15 25, process C: 50 5 20]
      time 20:
      [process B: 40 5 25, process C: 50 5 20]
      time 25:
      [process C: 50 5 20]
      time 30:
      time 35:
      [process A: 30 10 33]

  
