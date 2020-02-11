import cv2
import time
import os

def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        try:
            cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        except:
            count = count + 1
            if (count > (video_length - 1)):
                # Log the time again
                time_end = time.time()
                # Release the feed
                cap.release()
                # Print stats
                print("Done extracting frames.\n%d frames extracted" % count)
                print("It took %d seconds forconversion." % (time_end - time_start))
                break
            continue
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break

if __name__=="__main__":



    lines = []
    basedir = "C:/temp/motion"
    source_dir = os.path.join(basedir, "source")
    dest_dir = os.path.join(basedir, "dest")
    lines = os.listdir(source_dir)
    # hoffentlich sind es nicht so viele Zeilen. ;-)
    for line in lines:
        # Parent Directory path
        # Path
        print (line)
        inputfile=os.path.join(source_dir,line)
        parts = line.split('.')
        path = os.path.join(dest_dir, parts[0])
        print(path)
        if not os.path.exists(path):
            os.mkdir(path)

        input_loc = 'Testvideo.avi'
        output_loc = path
        video_to_frames(input_loc, output_loc)


