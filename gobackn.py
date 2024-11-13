
def go_back_n(frames, window_size):
    i = 0
    while i < len(frames):
        # Send frames within the window
        print(f"Sending frames {frames[i:i+window_size]}")
        
        # Simulate acknowledgment
        ack = input("Enter the last acknowledged frame (or 'NAK' for error): ")
        
        if ack == "NAK":
            print("Error detected! Resending frames from", frames[i])
        else:
            # Move window according to last acknowledged frame
            ack = int(ack)
            i = ack + 1  # Start sending from next unacknowledged frame

