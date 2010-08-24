#!/usr/bin/env python

import logging
from WMCore_t.WMBS_t.Performance_t.Base_t import Base_t
from WMCore.Database.DBFactory import DBFactory

class Location_t(Base_t):
    """
    __Location_t__

     Performance testcase for WMBS Location class

     This class is abstract, proceed to the DB specific testcase
     to run the test


    """
    
    def setUp(self, sqlURI='', logarg=''):
        #Call common setUp method from Base_t
                
        self.logger = logging.getLogger(logarg + 'FilePerformanceTest')
        
        dbf = DBFactory(self.logger, sqlURI)
        
        Base_t.setUp(self,dbf=dbf)

    def tearDown(self):
        #Call superclass tearDown method
        Base_t.tearDown(self)

    def testNew(self):         
        print "testNew"
        
        time = self.perfTest(dao=self.dao, action='Locations.New', execinput=['sename="TestLocation"'])
        assert time <= self.threshold, 'New DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'

    def testList(self):         
        print "testList"
        
        time = self.perfTest(dao=self.dao, action='Locations.List', execinput='')
        assert time <= self.threshold, 'List DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'

    def testDelete(self):         
        print "testDelete"
        
        time = self.perfTest(dao=self.dao, action='Locations.Delete', execinput=['sename="TestLocation"'])
        assert time <= self.threshold, 'Delete DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'

#    def testFiles(self):         
#        print "testFiles"
#        
#        time = self.perfTest(dao=self.mysqldao, action='Locations.Files', execinput=['sename="TestLocation"'])
#        assert time <= self.threshold, 'Files DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'
