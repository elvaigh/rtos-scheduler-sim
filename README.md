# processor-rms
a simple Rate Monotonic Scheduling (RMS) 

  **Issues:**
  
    At 20, decrements process B twice
      time  20 :
      hi3 [process B: 40 15 25, process C: 50 5 20]
      hi3 [process B: 40 10 25, process C: 50 5 20]
      [process B: 40 5 25, process C: 50 5 20] 
  
