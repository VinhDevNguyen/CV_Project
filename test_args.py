# import sys,getopt 

# def main(argv): 
#     obj_path = '' 
#     surface_path = '' 

#     try: 
#         opts, args = getopt.getopt(argv) 
#     except getopt.GetoptError: 
#         # print('test.py -i <inputfile> -o <outputfile>')
#         print('Use main.py -h for more details with passing arguments')
#         sys.exit(2)

#     for opt, arg in opts: 
#         if opt == '-h': 
#             print('main.py -r <draw rectangle delimiting target surface on frame>')
#             print('main.py -s <surface_model_path>')
#             print('main.py -obj <object_model_path')
#             print('main.py -ma <draw matches between keypoints>')
#             print('main.py -ma <draw matches between keypoints>')

#     # inputfile = ''
#     # outputfile = ''
#     # try:
#     #     opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#     # except getopt.GetoptError:
#     #     print('test.py -i <inputfile> -o <outputfile>')
#     #     sys.exit(2)
#     # for opt, arg in opts:
#     #     if opt == '-h':
#     #         print('test.py -i <inputfile> -o <outputfile>') 
#     #         sys.exit()
#     #     elif opt in ("-i", "--ifile"):
#     #         inputfile = arg
#     #     elif opt in ("-o", "--ofile"):
#     #         outputfile = arg
#     # print('Input file is "', inputfile) 
#     # print('Output file is "', outputfile) 

# if __name__ == "__main__":
#    main(sys.argv[1:])



# import argparse
# from pathlib import Path 


# parser = argparse.ArgumentParser()
# # parser.add_argument("file_path", type=Path)
# parser.add_argument(
#     '-mo',
#     '--model', 
#     type=Path)
#     # help = 'Specify model to be projected', 
#     # action = 'store_true')

# p = parser.parse_args()
# print(p.file_path, type(p.file_path), p.file_path.exists())
# parser.add_argument('--infile', type=argparse.FileType('r', encoding='UTF-8'), 
#                       required=True)


# parser.add_argument('-obj',
#                     '--object',
#                     dest = 'filename', 
#                     action = 'store_true', 
#                     help = '-obj or --object <object_model_path>')


# parser.add_argument('-s',
#                     '--surface',
#                     dest = 'filename', 
#                     # action = 'store_true',
#                     required = True, 
#                     help = '-s or --surface <surface_path>',
#                     metavar='FILE', 
#                     type=lambda x: is_valid_file(parser, x))

# def is_valid_file(parser, arg):
#     # if not os.path.exists(arg):
#     #     parser.error("the file %s does not exist!" % arg)
#     # else:
#     #     return open(arg, 'r')  # return an open file handle
#     try: 
#         return open(arg, 'r')  # return an open file handle
#     except IOError:
#         parser.error("the file %s does not exist!" % arg)
#         # print('[ERROR] File {} does not exists!'.format()) 


from gooey import Gooey
import argparse
from argparse import ArgumentParser
import sys # add
import os.path # add 
from subprocess import Popen, PIPE # add

@Gooey(
    program_name='Settings',
    menu=[{
        'name': 'File',
        'items': [{
                'type': 'AboutDialog',
                'menuTitle': 'About',
                # 'name': 'Gooey Layout Demo',
                # 'description': 'An example of Gooey\'s layout flexibility',
                # 'version': '1.2.1',
                # 'copyright': '2018',
                'website': 'https://github.com/dxv2k',
                # 'developer': 'http://chriskiehl.com/',
                # 'license': 'MIT'
            }, {
                'type': 'MessageDialog',
                'menuTitle': 'Information',
                'caption': 'My Message',
                'message': 'I am demoing an informational dialog!'
            }, {
                'type': 'Link',
                'menuTitle': 'Visit Our Site',
                'url': 'https://github.com/chriskiehl/Gooey'
            }]
        },{
        'name': 'Help',
        'items': [{
            'type': 'Link',
            'menuTitle': 'Documentation',
            'url': 'https://www.readthedocs.com/foo'
        }]
    }]
) 
def main(): 
    # parser = argparse.ArgumentParser(description='Augmented reality application')
    # parser.add_argument('-s', 
    #                     '--surface', 
    #                     help = '-s or --surface <surface_path>',
    #                     type=argparse.FileType('r', encoding='UTF-8'))  

    # parser.add_argument('-obj', 
    #                     '--object', 
    #                     type=argparse.FileType('r', encoding='UTF-8'))  

    # args = parser.parse_args()
    # print(args)
    # print(args.surface)

    # Command line argument parsing
    # NOT ALL OF THEM ARE SUPPORTED YET
    parser = argparse.ArgumentParser(description='Augmented reality settings')

    # parser.add_argument('-nm',
    #                     '--number_matches', 
    #                     help = 'Set number of matches keypoint', 
    #                     action = 'store_true')
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
    
    # Test sub-process 
    PYTHON_PATH = sys.executable
    process = Popen([PYTHON_PATH, 'gui.py'], stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    print(output)
    print(error) 



if __name__ == '__main__':
    main() 
