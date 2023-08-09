import optparse
import zipfile
from threading import Thread

def extrac_zip(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print("[+] password found : " + password +'\ n')
    except:
        pass

def main() -> object:
    parser = optparse.OptionParser("usag %prog") + "-f <zipfile> -d <dictionary>"
    parser.add_option('-f', dest= 'zname', type='string', \
                     help='spesify zip file')
    parser.add_option('-d', dest = 'dname', type='string', \
                     help='specify dictionry file')
    (option, arg) = parser.parser_args()
    if (options.zname == none) | (options.dname == none):
        print(parser.usage)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()
