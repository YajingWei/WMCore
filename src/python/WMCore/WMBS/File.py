#!/usr/bin/env python
"""
_File_

A simple object representing a file in WMBS

"""

__revision__ = "$Id: File.py,v 1.4 2008/05/12 11:58:07 swakef Exp $"
__version__ = "$Revision: 1.4 $"

class File(object):
    """
    A simple object representing a file in WMBS
    """
#    id = -1
#    lfn = ''
#    size = ''
#    events = ''
#    run = ''
#    lumi = ''
    def __init__(self, lfn='', id=-1, size=0, events=0, run=0, lumi=0,
                 parents=set(), locations=set(), wmbs=None):
        """
        Create the file object
        """
        self.wmbs = wmbs
        self.id = id
        self.lfn = lfn
        self.size = size 
        self.events = events
        self.run = run
        self.lumi = lumi
        self.parents = parents
        self.locations = locations
    
    def getInfo(self):
        """
        Return the files attributes as a tuple
        """
        return self.lfn, self.id, self.size, self.events, self.run, \
                                    self.lumi, list(self.locations), list(self.parents)
    
    def load(self, parentage=0):
        """
        use lfn to load file info from db
        """
        result = self.wmbs.fileDetails(self.lfn)[0]
        self.id = result[0]
        self.lfn = result[1]
        self.size = result[2]
        self.events = result[3]
        self.run = result[4]
        self.lumi = result[5]
        self.locations = result[6]
        self.parents = set()
        
        if not parentage > 0:
            return self

        for lfn in self.wmbs.parentsForFile(self.id,
                                conn = None, transaction = False):
            self.parents.add( \
                    File(lfn=lfn, wmbs=self.wmbs).load(parentage=parentage-1))
        
        return self


    def __eq__(self, rhs):
        """
        Are objects the same, go from lfn
        """
        return self.lfn == rhs.lfn
    
    def __ne__(self, rhs):
        return not self.__eq__(rhs)
