def selective_repeat(frames, window_size):
    sent_frames = [False] * len(frames)
    i = 0
    
    while i < len(frames):
        # Send frames within the window
        for j in range(i, min(i + window_size, len(frames))):
            if not sent_frames[j]:
                print(f"Sending frame {frames[j]}")
        
        ack = input("Enter acknowledged frame number (or 'NAK' for error): ")
        
        if ack == "NAK":
            frame_num = int(input("Enter frame number to resend: "))
            print(f"Resending frame {frame_num}")
            sent_frames[frame_num] = False
        else:
            frame_num = int(ack)
            sent_frames[frame_num] = True
            # Slide window if all frames from i to window are acknowledged
            while i < len(frames) and sent_frames[i]:
                i += 1