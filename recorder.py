import cv2

def recorder(iter):
    filenames=['rock.mp4','paper.mp4','scissors.mp4']
    filename = filenames[iter]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter(filename, fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if(__name__=="__main__"):
    recorder(0)
