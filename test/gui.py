# import PIL
# from PIL import Image,ImageTk
# import cv2
# from tkinter import *

# width, height = 1920, 1080
# # width, height = 640, 480
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# root = Tk()
# # root.bind('<Escape>', lambda e: root.quit()) 
# lmain = Label(root)
# lmain.pack()

# def show_frame():
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.flip(frame, 1)
#         cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#         img = PIL.Image.fromarray(cv2image)
#         imgtk = ImageTk.PhotoImage(image=img)
#         lmain.imgtk = imgtk
#         lmain.configure(image=imgtk)
#         lmain.after(10, show_frame)

# show_frame()
# root.mainloop()
import argparse
from gooey import Gooey 
from gooey import GooeyParser

@Gooey(
    advanced=True,  
    default_size=(720, 600),            # starting size of the GUI
    program_name='Augmented Reality',   # Defaults to script name
) 
def main():
    """
    This functions loads the target surface image,
    """
    # Command line argument parsing
    # NOT ALL OF THEM ARE SUPPORTED YET
    parser = GooeyParser(description='Augmented reality application')
    parser.add_argument('Draw Surface',
                        # action = 'store_true',  
                        # widget = 'TextCtrl', 
                        help = 'Draw rectangle delimiting target surface on frame') 
    # parser.add_argument('-r',
    #                     '--rectangle', 
    #                     help = 'draw rectangle delimiting target surface on frame', 
    #                     action = 'store_true')

    parser.add_argument('Draw Matches from surface to video stream',
                        # action = 'store_true',  
                        help = 'Draw matches between keypoints') 
    # parser.add_argument('-ma',
    #                     '--matches', 
    #                     help = 'draw matches between keypoints', 
    #                     action = 'store_true')

    parser.add_argument('-nm',
                        '--number_matches', 
                        type = int, 
                        help = 'Set number of minimum matches keypoint', 
                        widget='IntegerField') 

    parser.add_argument('-obj', 
                        '--object', 
                        help = 'Choose model to draw on surface with passing arguments -obj or --object <MODEL_PATH>',
                        widget = 'FileChooser', 
                        type=argparse.FileType('r', encoding='UTF-8'))  
    parser.add_argument('-s', 
                        '--surface', 
                        help = 'Choose custom surface instead default with passing arguments -s or --surface <SURFACE_PATH>',
                        widget = 'FileChooser', 
                        type=argparse.FileType('r', encoding='UTF-8'))  

    args = parser.parse_args()

if __name__ == '__main__':
    main()
