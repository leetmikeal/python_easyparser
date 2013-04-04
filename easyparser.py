#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import re

# constant
debug = True   # if true, will print
debug_level = 5  # debug level


class func(object):
  def __init__(self, name="", args="", nline=""):
    self.name = name    # string: function name
    self.args = args    # list: auguments
    self.nline = nline  # int: number of lines

  def parseFunc(self, sline):
    print sline
    sline = 'a' + sline
    l = sline.split("def ")
    if not(l[1]):
      return None
    s = l[1].strip()

    r = re.search("(.+)\(", s)
    if r is None:
      return None
    t = r.groups()
    self.name = t[0]

    r = re.search("\((.+)\)", s)
    if r is None:
      return None
    t = r.groups()
    args = t[0].split(",")
    for i in range(len(args)):
      args[i] = args[i].strip()
    self.args = args[:]

  def parseFile(self, fhandle):
    pass


def debugprint(s, lev=0):
  if debug:
    if lev >= debug_level:
      print s


def outMatched(func):
  print "%-8d %-50s return" % (func.nline, func.name)
  for i in range(len(func.args)):
    print "%59s %-20s" % ("", func.args[i])


def isnotNone(b):
  return False if b is None else True

if __name__ == '__main__':
  argv = sys.argv
  argc = len(sys.argv)
  if argc != 2:
    print "python %s <input file>" % (__file__)
    exit()

  infile = argv[1]
  if not(os.path.exists(infile)):
    print "file not found: %s" % (infile)
    exit()

  try:
    f = open(infile, 'r')
  except IOEror:
    print "%s can NOT be opened." % (infile)
    exit()

  funcs = []
  sfunc = ""
  i = -1
  il = 1
  rbgn = re.compile("^\s*def\W")  # ex) " def function(arg1, arg2):"
  rend = re.compile(":")
  rcmt = re.compile("([^#]*)#?.*")
  for line in f.readlines():
# remove white space etc.
    lntri = line.strip('\r\n').strip()
    ac = rcmt.search(lntri)
    if isnotNone(ac):
      lntri = ac.group(1)
      debugprint(lntri, 3)

# search function lines
    ab = rbgn.search(lntri)
    ae = rend.search(lntri)

    debugprint("%s *** %s, %s," % (lntri, isnotNone(ab), isnotNone(ae)), 0)

# trace function statement
# if it's multiple line, "sfunc" keep previous letter.
    if(isnotNone(ab) and isnotNone(ae)):
      fu = func("", "", il)
      funcs.append(fu)
      i += 1
      funcs[i].parseFunc(lntri)
      pass
    elif(isnotNone(ab) and not(isnotNone(ae))):
      sfunc = lntri
      fu = func("", "", il)
      funcs.append(fu)
      i += 1
      pass
    elif(not(isnotNone(ab)) and isnotNone(ae)):
      if sfunc != "":
        sfunc = sfunc + lntri
        print sfunc
        funcs[i].parseFunc(sfunc)
        sfunc = ""
      pass
    else:
      if sfunc != "":
        sfunc = sfunc + lntri
      pass
    il += 1
    debugprint("%5d %s" % (il, sfunc), 1)

  for i in range(len(funcs)):
    outMatched(funcs[i])

  f.close()
  exit  # main
