import os
from os import listdir
from os.path import splitext

flags = ''

def options(opt):
    opt.load('compiler_c')

def configure(cnf):
    cnf.load('compiler_c')

def build(bld):
    sources = [f for f in listdir("cmd") if f.endswith('.c')]
    print(sources)
    for f in sources:
        bld.program(source="cmd/"+f,
                    target=splitext(f)[0],
                    cflags=flags)