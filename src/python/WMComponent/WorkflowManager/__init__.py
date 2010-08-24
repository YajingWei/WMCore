#!/usr/bin/env python
"""
_WorkflowManager_

The WorkflowManager automatically creates subscriptions associated with a 
given Workflow when Filesets matching a regular expression (applied to the
Fileset name) become available.

To perform the management, the following messages are available, which expect
the described payload information. In all cases the payload should be pickled:

import pickle
payload = pickle.dumps({"Arg1" : Val, "Arg2" : "StringVal"})

AddWorkflowToManage - Used to add a Fileset name : Subscription creation mapping
   FilesetMatch : string (regex of fileset names to match)
   WorkflowId : string (ID from WMBS database of workflow to apply to new subs)
   SplitAlgo : string (as passed to Subscription constructor)
   Type : string (as passed to Subscription constructor)
   
AddToLocationWhitelist - Adds locations to the whitelist of created subscriptions
    FilesetMatch : string (as passed to AddWorkflowToManage)
    WorkflowId : string (as passed to AddWorkflowToManage)
    Locations : string (comma separated list of locations to add to whitelist)
    
RemoveFromLocationWhitelist - Removes locations from the whitelist of created subscriptions
    FilesetMatch : string (as passed to AddWorkflowToManage)
    WorkflowId : string (as passed to AddWorkflowToManage)
    Locations : string (comma separated list of locations to remove from whitelist)
    
AddToLocationBlacklist - Adds locations to the blacklist of created subscriptions
    FilesetMatch : string (as passed to AddWorkflowToManage)
    WorkflowId : string (as passed to AddWorkflowToManage)
    Locations : string (comma separated list of locations to add to blacklist)
    
RemoveFromLocationBlacklist - Removes locations from the blacklist of created subscriptions
    FilesetMatch : string (as passed to AddWorkflowToManage)
    WorkflowId : string (as passed to AddWorkflowToManage)
    Locations : string (comma separated list of locations to remove from blacklist)

Note there is one potential concurrency problem. If a managment request is made,
and filesets become available before messages to handle location white / black
listing are processed, some jobs may be created before the setup is fully
complete.
"""

__all__ = []
__revision__ = "$Id: __init__.py,v 1.1 2009/02/04 21:57:11 jacksonj Exp $"
__version__ = "$Revision: 1.1 $"
__author__ = "james.jackson@cern.ch"