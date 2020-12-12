from PIL import Image
import sys
import os.path

def getArgs():
    argumentList = {}

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        try:
            if arg == '--help' or arg == '-h':
                exit("""
Help:
Usage: goldjack [options]

Required options:
-s, --source
-q, --quality

Options:
-h, --help Show help message and exit
-s, --source Target image from launch directory
-t, --to Path to final image (/home/testUser/Pictures/jakalPic.png)
-f, --format Format final image (jpg, png, qweqwe, anything)
-q, --quality Quality finaml image (0-100) 
                     """)
            elif arg == '-s' or arg == '--source':
                argumentList.update({'-s': sys.argv[i+1]})
            elif arg == '-t' or arg == '--to':
                argumentList.update({'-t': sys.argv[i+1]})
            elif arg == '-f' or arg == '--format':
                argumentList.update({'-f': sys.argv[i+1]})
            elif arg == '-q' or arg == '--quality':
                argumentList.update({'-q': int(sys.argv[i+1])})
            elif sys.argv[i-1][0] == '-' and arg[0] != '-':
                pass
            else:
                exit('Unknown argument: ' + arg)
        except Exception:
            exit('Need value after argument: ' + arg)
        i += 1

    if argumentList.get('-s', 'none') == 'none' or argumentList.get('-q', 'none') == 'none':
        exit("Required args: '-s', '-q'.")

    if argumentList.get('-t', 'none') != 'none' and argumentList.get('-f', 'none') != 'none':
        exit("Use one of these two parameters: '-t', '-f'")

    return argumentList

def convert(args):
    imgSource = args.get('-s')
    imgName = imgSource.split('/')[-1].split('.')[0]
    imgFormat = args.get('-f', '.jpg')
    imgQuality = args.get('-q')
    imgPath = '/'.join(imgSource.split('/')[0:-1]) + '/'

    if not os.path.exists(imgSource):
        exit('Does not exist: ' + imgSource)

    img = Image.open(imgSource)
    img = img.convert('RGB')

    if args.get('-t', 'none') != 'none':
        img.save(args.get('-t'), quality=imgQuality)
        return 0

    img.save(imgPath+imgName+imgFormat, quality=imgQuality)

if __name__ == '__main__':
    convert(getArgs())
