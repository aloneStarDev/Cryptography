import argparse
import CoDecode
import os
import rotorGenerator

parser = argparse.ArgumentParser(description='code and decode by anigma algoritm :)')
parser.add_argument('--file', metavar='file_name', type=str, nargs='+', help='enter file or files path')
parser.add_argument('--inline', metavar='some_text', type=str, help='enter string to code or decode')
parser.add_argument('--dgr', metavar='disable_generate_rotor', type=bool, default=False, help='disable auto generate '
                                                                                              'rotor by current day')
args = parser.parse_args()

if not args.dgr:
    rotorGenerator.__main__()
if args.file is not None:
    for file in args.file:
        code = True
        if not os.path.exists(file):
            if os.path.exists("$"+file):
                code = False
                file = '$'+file
            else:
                print(file+' not found')
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        res = []
        for line in lines:
            res.append(CoDecode.__main__(line))
        os.remove(file)
        if code:
            file = "$"+file
        else:
            file = file[1:]
        f = open(file, 'x')
        f.writelines(res)
        f.close()
elif args.inline is not None:
    print(CoDecode.__main__(args.inline))

else:
    print('\n\n********>\tplease enter a valid args \t\t[one of the file or inline option is required]\n\n')

