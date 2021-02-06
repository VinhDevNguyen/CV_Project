# from gooey import Gooey
# from gooey import GooeyParser

# @Gooey()
# def main():

#     parser = GooeyParser(
#         description='''Test''')

#     required = parser.add_argument_group('Optional arguments')

#     parser.add_argument(
#                         '-i', '--input',
#                         required=False,
#                         dest = 'input',
#                         help='Test_file',
#                         widget='FileChooser',
#                         )

#     args = parser.parse_args()

# main()

from gooey import Gooey
import argparse
from argparse import ArgumentParser
import sys # add
import os.path # add 

@Gooey
def main(): 
    parser = argparse.ArgumentParser(description='Test passing args to subprocess')
    parser.add_argument('-r',
                        '--rectangle', 
                        help = 'draw rectangle delimiting target surface on frame', 
                        action = 'store_true')
    parser.add_argument('-ma',
                        '--matches', 
                        help = 'draw matches between keypoints', 
                        action = 'store_true')
    parser.add_argument('-obj', 
                        '--object', 
                        help = 'Choose model to draw on surface with passing arguments -obj or --object <MODEL_PATH>',
                        type=argparse.FileType('r', encoding='UTF-8'))  
    parser.add_argument('-s', 
                        '--surface', 
                        help = 'Choose custom surface instead default with passing arguments -s or --surface <SURFACE_PATH>',
                        type=argparse.FileType('r', encoding='UTF-8'))  

    args = parser.parse_args()
    if args: 
        print('[INFO] Received args!!!')
        print('[INFO] Args receive: ',args._get_kwargs() )
if __name__ == '__main__':
    main()