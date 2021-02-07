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
from gooey import local_resource_path

@Gooey(
    program_name='Augmented Reality',   # Defaults to script name
    # image_dir=local_resource_path('\icon\program_icon.png'), 
    # image_dir=local_resource_path(r'C:\Users\razor\Documents\github\CV_Project\icon\program_icon.png'), 
    advanced=True,  
    default_size=(720, 600),            # starting size of the GUI
    # image_dir='/icon/program_icon.png', 
    menu=[{
        'name': 'File',
        'items': [{
                'type': 'AboutDialog',
                'menuTitle': 'About',
                'name': 'Augmented Reality 101',
                'description': 'Group project for Computer Vision CS231',
                'website': 'https://github.com/VinhDevNguyen/CV_Project',
                'developer': 'Vu Dinh Xuan, Quang Nguyen Hong, Vinh Nguyen Thanh',
                # 'license': 'MIT'
            }, ]
        },{
        'name': 'Help',
        'items': [{
            'type': 'Link',
            'menuTitle': 'Documentation',
            'url': 'https://github.com/VinhDevNguyen/CV_Project'
        }]
    }]
) 
def main():
    """
    This functions loads the target surface image,
    """
    # Command line argument parsing
    # NOT ALL OF THEM ARE SUPPORTED YET
    parser = GooeyParser(description='Augmented reality application')
    parser.add_argument('Draw surface',
                        action = 'store_false',  
                        # widget = 'TextCtrl', 
                        help = 'Draw rectangle delimiting target surface on frame') 
    # parser.add_argument('-r',
    #                     '--rectangle', 
    #                     help = 'draw rectangle delimiting target surface on frame', 
    #                     action = 'store_true')

    parser.add_argument('Draw matches from surface to video stream',
                        action = 'store_false',  
                        help = 'Draw matches between keypoints') 
    # parser.add_argument('-ma',
    #                     '--matches', 
    #                     help = 'draw matches between keypoints', 
    #                     action = 'store_true')

    # parser.add_argument('-nm',
    #                     '--number_matches', 
    #                     type = int, 
    #                     help = 'Set number of minimum matches keypoint', 
    #                     widget='IntegerField') 
    parser.add_argument('Minimum matches',
                        # '--number_matches', 
                        type = int, 
                        help = 'Set number of minimum matches keypoint', 
                        widget='IntegerField') 

    # parser.add_argument('-obj', 
    #                     '--object', 
    #                     help = 'Choose model to draw on surface ',
    #                     widget = 'FileChooser', 
    #                     type=argparse.FileType('r', encoding='UTF-8'))  
    parser.add_argument('Object', 
                        help = 'Choose model to draw on surface ',
                        widget = 'FileChooser', 
                        type=argparse.FileType('r', encoding='UTF-8'))  

    # parser.add_argument('-s', 
    #                     '--surface', 
    #                     help = 'Choose custom surface instead default ',
    #                     widget = 'FileChooser', 
    #                     type=argparse.FileType('r', encoding='UTF-8'))  
    parser.add_argument('Surface',  
                        help = 'Choose custom surface instead default ',
                        widget = 'FileChooser', 
                        type=argparse.FileType('r', encoding='UTF-8'))  

    args = parser.parse_args()

if __name__ == '__main__':
    main()
