
# Useful links
# http://www.pygame.org/wiki/OBJFileLoader
# https://rdmilligan.wordpress.com/2015/10/15/augmented-reality-using-opencv-opengl-and-blender/
# https://clara.io/library

# TODO -> Implement command line arguments (scale, model and object to be projected)
#      -> Refactor and organize code (proper funcition definition and separation, classes, error handling...)

import argparse

import cv2
import numpy as np
import math
import os
from objloader_simple import *

# import logging
from utils import hex_to_rgb, render, projection_matrix
from custom_args import custom_args

from gooey import Gooey 
# from gooey import GooeyParser
# from gooey import local_resource_path

DEFAULT_COLOR = (0, 0, 0)

# Gooey Decorator
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
            # 'url': 'https://github.com/VinhDevNguyen/CV_Project'
            'url': 'https://github.com/VinhDevNguyen/CV_Project/blob/main/README.md'
        }]
    }]
) 
def main():
    """
    This functions loads the target surface image,
    """

    args = custom_args() 

    homography = None 

    # matrix of camera parameters (made up but works quite well for me) 
    camera_parameters = np.array([[800, 0, 320], [0, 800, 240], [0, 0, 1]])

    # create ORB keypoint detector
    orb = cv2.ORB_create()

    # create BFMatcher object based on hamming distance  
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # TODO: Put args into a fucntion, shouldn't write like this 
    # load the reference surface that will be searched in the video stream
    dir_name = os.getcwd()
    if args.surface: 
        # model = cv2.imread(os.path.join(dir_name, 'reference/model.jpg'), 0)
        model = cv2.imread(args.surface.name, 0)
    else: 
        model = cv2.imread(os.path.join(dir_name, 'reference/model.jpg'), 0)

    # Compute model keypoints and its descriptors
    kp_model, des_model = orb.detectAndCompute(model, None)

    # Load 3D model from OBJ file
    if args.object: 
        obj = OBJ(args.object.name,swapyz=True)
    else: 
        obj = OBJ(os.path.join(dir_name, 'models/fox.obj'), swapyz=True)  

    # Set mimimum number of matches that have to be found
    # to consider the recognition is valid 
    if args.number_matches: 
        MIN_MATCHES = args.number_matches 
        # logging.info('[INFO] MINIMUM MATCHES: ', MIN_MATCHES) 
        print('[INFO] MINIMUM MATCHES: ', MIN_MATCHES) 
    else: 
        MIN_MATCHES = 10 
        print('[INFO] DEFAULT MINIMUM MATCHES: ', MIN_MATCHES) 

    # init video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened(): 
        print('[INFO] Camera not detected, please resolve it and restart the program before program!')

    # TODO: move while loop to mainloop parameter 
    # TODO: find a proper name for mainloop function
    # def mainloop(args, 
    #             cap, 
    #             homography=None, # not sure  
    #             kp_model, des_model # from orb detecAndCompute
    #             camera_parameters # 
    # ):
    while True:
        # read the current frame
        ret, frame = cap.read()
        if not ret:
            print("[INFO] Unable to capture video")
            return 
        # find and draw the keypoints of the frame
        kp_frame, des_frame = orb.detectAndCompute(frame, None)
        # match frame descriptors with model descriptors
        matches = bf.match(des_model, des_frame)
        # sort them in the order of their distance
        # the lower the distance, the better the match
        matches = sorted(matches, key=lambda x: x.distance)

        # compute Homography if enough matches are found
        if len(matches) > MIN_MATCHES:
            # differenciate between source points and destination points
            src_pts = np.float32([kp_model[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp_frame[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
            # compute Homography
            homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if args.rectangle:
                # Draw a rectangle that marks the found model in the frame
                h, w = model.shape
                pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                # project corners into frame
                dst = cv2.perspectiveTransform(pts, homography)
                # connect them with lines  
                frame = cv2.polylines(frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)  
            # if a valid homography matrix was found render cube on model plane
            if homography is not None:
                try:
                    # obtain 3D projection matrix from homography matrix and camera parameters
                    projection = projection_matrix(camera_parameters, homography)  
                    # project cube or model
                    frame = render(frame, obj, projection, model, False)
                    #frame = render(frame, model, projection)
                except:
                    pass
            # draw first 10 matches.
            if args.matches:
                frame = cv2.drawMatches(model, kp_model, frame, kp_frame, matches[:10], 0, flags=2)
            # show result
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            print("Not enough matches found - %d/%d" % (len(matches), MIN_MATCHES))

    cap.release()
    cv2.destroyAllWindows()

    return 0




if __name__ == '__main__':
    main()
