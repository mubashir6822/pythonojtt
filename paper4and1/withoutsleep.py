import time

waiting_time =10  # Wait for 5 seconds
# waiting_time =7200 
start_time = time.monotonic()  # show current time

while True:
    current_time = time.monotonic()  # again show current time again
    
    waited = current_time - start_time  
    
    if waited >= waiting_time:  # Check if  wait period has more than waiting time
        n=5
        for i in range(n):
            print(i*" "+(n-i)*"* "+i*" ")
        
        start_time = current_time  # Reset the start time for the next wait period