#!/usr/bin/python

import email.parser
import os, sys, stat
import shutil


def ExtractSubPayload(filename):
    ''' Extract the subject and payload from the .eml file.

    '''
    if not os.path.exists(filename):  # dest path doesnot exist
        print "ERROR: input file does not exist:", filename
        os.exit(1)
    fp = open(filename)
    msg = email.message_from_file(fp)

    payload = msg.get_payload()
    if type(payload) == type(list()):
        payload = payload[0]  # only use the first part of payload
    sub = msg.get('subject')
    sub = str(sub)
    if type(payload) != type(''):
        payload = str(payload)

    for part in msg.walk():
        # each part is a either non-multipart, or another multipart message
        # that contains further parts... Message is organized like a tree
        if part.get_content_type() == 'text/plain':
            ctype = 'plain'
        else:
            ctype = 'html'

    return sub + payload, ctype


def ExtractBodyFromDir(srcdir, dstdir):
    '''Extract the body information from all .eml files in the srcdir and

    save the file to the dstdir with the same name.'''
    if not os.path.exists(dstdir):  # dest path doesnot exist
        os.makedirs(dstdir)
    files = os.listdir(srcdir)
    for file in files:
        srcpath = os.path.join(srcdir, file)
        dstpath = os.path.join(dstdir, file)
        src_info = os.stat(srcpath)
        if stat.S_ISDIR(src_info.st_mode):  # for subfolders, recurse
            ExtractBodyFromDir(srcpath, dstpath)
        else:  # copy the file
            body, ctype = ExtractSubPayload(srcpath)
            dstfile = open(dstpath, 'w')
            dstfile.write(body)
            dstfile.close()

            if dstfile.name[dstfile.name.rfind('.')+1:] in ['eml']:
                os.rename(dstfile.name, dstfile.name[:dstfile.name.rfind('.')] + '_' + ctype + '.eml')


###################################################################
# main function start here
# srcdir is the directory where the .eml are stored
print 'Input source directory: '  # ask for source and dest dirs
srcdir = raw_input()
if not os.path.exists(srcdir):
    print 'The source directory %s does not exist, exit...' % (srcdir)
    sys.exit()
# dstdir is the directory where the content .eml are stored
print 'Input destination directory: '  # ask for source and dest dirs
dstdir = raw_input()
if not os.path.exists(dstdir):
    print 'The destination directory is newly created.'
    os.makedirs(dstdir)

###################################################################
ExtractBodyFromDir(srcdir, dstdir)
