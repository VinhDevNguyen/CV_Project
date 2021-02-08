import argparse

from gooey import Gooey 
from gooey import GooeyParser
from gooey import local_resource_path

def custom_args(): 
    ''' 
    '''  
    # Command line argument parsing
    # NOT ALL OF THEM ARE SUPPORTED YET
    parser = GooeyParser(description='Augmented reality application')
    parser.add_argument('-Rectangle',
                        '--rectangle', 
                        action = 'store_true',  
                        # widget = 'TextCtrl', 
                        help = 'Draw rectangle delimiting target surface on frame') 
    # parser.add_argument('-r',
    #                     '--rectangle', 
    #                     help = 'draw rectangle delimiting target surface on frame', 
    #                     action = 'store_true')

    parser.add_argument('-Draw matches from surface to video stream',
                        '--matches', 
                        action = 'store_true',  
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
    parser.add_argument('-Minimum matches',
                        '--number_matches', 
                        type = int, 
                        help = 'Set number of minimum matches keypoint', 
                        widget='IntegerField') 

    # parser.add_argument('-obj', 
    #                     '--object', 
    #                     help = 'Choose model to draw on surface ',
    #                     widget = 'FileChooser', 
    #                     type=argparse.FileType('r', encoding='UTF-8'))  
    parser.add_argument('-Object', 
                        '--object', 
                        help = 'Choose model to draw on surface ',
                        widget = 'FileChooser', 
                        type=argparse.FileType('r', encoding='UTF-8'))  

    # parser.add_argument('-s', 
    #                     '--surface', 
    #                     help = 'Choose custom surface instead default ',
    #                     widget = 'FileChooser', 
    #                     type=argparse.FileType('r', encoding='UTF-8'))  
    parser.add_argument('-Surface',  
                        '--surface', 
                        help = 'Choose custom surface instead default ',
                        widget = 'FileChooser', 
                        type=argparse.FileType('r', encoding='UTF-8'))  

    args = parser.parse_args()

    return args  
    
# def default_args(): 
#     # Command line argument parsing
#     # NOT ALL OF THEM ARE SUPPORTED YET
#     parser = argparse.ArgumentParser(description='Augmented reality application')
#     parser.add_argument('-r',
#                         '--rectangle', 
#                         help = 'draw rectangle delimiting target surface on frame', 
#                         action = 'store_true')
#     parser.add_argument('-ma',
#                         '--matches', 
#                         help = 'draw matches between keypoints', 
#                         action = 'store_true')
#     parser.add_argument('-nm',
#                         '--number_matches', 
#                         type = int, 
#                         help = 'Set number of minimum matches keypoint') 
#     parser.add_argument('-obj', 
#                         '--object', 
#                         help = 'Choose model to draw on surface with passing arguments -obj or --object <MODEL_PATH>',
#                         type=argparse.FileType('r', encoding='UTF-8'))  
#     parser.add_argument('-s', 
#                         '--surface', 
#                         help = 'Choose custom surface instead default with passing arguments -s or --surface <SURFACE_PATH>',
#                         type=argparse.FileType('r', encoding='UTF-8'))  

#     # UNSUPPORTED ARGUMENTS 
#     # parser.add_argument('-mk','--model_keypoints', help = 'draw model keypoints', action = 'store_true')
#     # parser.add_argument('-fk','--frame_keypoints', help = 'draw frame keypoints', action = 'store_true')

#     args = parser.parse_args()

