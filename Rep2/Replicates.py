#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

from rtshell import rtconf
"""
 @file Replicates.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import test_idl

# Import Service implementation class
# <rtc-template block="service_impl">
from test_idl_example import *

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
import RTR, RTR__POA
from subprocess import Popen, PIPE

# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
replicates_spec = ["implementation_id", "Replicates", 
		 "type_name",         "Replicates", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.tlin1", "0",
		 "conf.default.tlin2", "0",
		 "conf.default.tlin3", "0",
		 "conf.default.tlsout", "0",
		 "conf.default.group_name", "replicates",
		 "conf.default.priority", "0",
		 "conf.__widget__.tlin1", "text",
		 "conf.__widget__.tlin2", "text",
		 "conf.__widget__.tlin3", "text",
		 "conf.__widget__.tlsout", "text",
		 "conf.__widget__.group_name", "text",
		 "conf.__widget__.priority", "text",
		 ""]
# </rtc-template>

##
# @class Replicates
# @brief ModuleDescription
# 
# 
class Replicates(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_TLin = RTC.TimedLong(RTC.Time(0,0),0)
		"""
		"""
		self._TLinIn = OpenRTM_aist.InPort("TLin", self._d_TLin)
		self._d_TLSin = RTC.TimedLongSeq(RTC.Time(0,0),[])
		"""
		"""
		self._TLSinIn = OpenRTM_aist.InPort("TLSin", self._d_TLSin)
		self._d_TLout = RTC.TimedLong(RTC.Time(0,0),0)
		"""
		"""
		self._TLoutOut = OpenRTM_aist.OutPort("TLout", self._d_TLout)
		self._d_TLSout = RTC.TimedLongSeq(RTC.Time(0,0),[])
		"""
		"""
		self._TLSoutOut = OpenRTM_aist.OutPort("TLSout", self._d_TLSout)

		"""
		"""
		self._test_proPort = OpenRTM_aist.CorbaPort("test_pro")
		"""
		"""
		self._test_reqPort = OpenRTM_aist.CorbaPort("test_req")

		"""
		"""
		self._test_idl_prov = Test1_i()
		

		"""
		"""
		self._test_idl_req = OpenRTM_aist.CorbaConsumer(interfaceType=RTR.Test1)

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  tlin1
		 - DefaultValue: 0
		"""
		self._tlin1 = [0]
		"""
		
		 - Name:  tlin2
		 - DefaultValue: 0
		"""
		self._tlin2 = [0]
		"""
		
		 - Name:  tlin3
		 - DefaultValue: 0
		"""
		self._tlin3 = [0]
		"""
		
		 - Name:  tlsout
		 - DefaultValue: 0
		"""
		self._tlsout = [0]
		"""
		
		 - Name:  group_name
		 - DefaultValue: replicates
		"""
		self._group_name = ['replicates']
		"""
		
		 - Name:  priority
		 - DefaultValue: 0
		"""
		self._priority = [0]
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("tlin1", self._tlin1, "0")
		self.bindParameter("tlin2", self._tlin2, "0")
		self.bindParameter("tlin3", self._tlin3, "0")
		self.bindParameter("tlsout", self._tlsout, "0")
		self.bindParameter("group_name", self._group_name, "replicates")
		self.bindParameter("priority", self._priority, "0")
		
		# Set InPort buffers
		self.addInPort("TLin",self._TLinIn)
		self.addInPort("TLSin",self._TLSinIn)
		
		# Set OutPort buffers
		self.addOutPort("TLout",self._TLoutOut)
		self.addOutPort("TLSout",self._TLSoutOut)
		
		# Set service provider to Ports
		self._test_proPort.registerProvider("test_idl", "RTR::Test1", self._test_idl_prov)
		
		# Set service consumers to Ports
		self._test_reqPort.registerConsumer("test_idl", "RTR::Test1", self._test_idl_req)
		
		# Set CORBA Service Ports
		self.addPort(self._test_proPort)
		self.addPort(self._test_reqPort)
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	# 
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
                
		if self._TLinIn.isNew():
		    tmp = self._TLinIn.read()

		    update_conf("tlin1", tmp.data)
		    update_conf("tlin2", tmp.data*10)
		    update_conf("tlin3", tmp.data*100)

		self._d_TLout.data = self._tlin1[0]
		self._TLoutOut.write()
		
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	
def update_conf(param, new_val):
#    s = time.clock()
    cmd = "rtconf localhost/Rep2.rtc set " + param +" " + str(new_val)
    
    p = Popen(cmd, shell=True, stdout=PIPE)
    while True:
        line = p.stdout.readline()
        if not line:
            break
        print line.rstrip()

#    e = time.clock()
#    f = open('../../ExecutionTimeLog/Rep2_update_conf_time.txt', 'a')
#    f.write(str(param) + "," + str(e-s)+'\n')
#    f.close()


def ReplicatesInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=replicates_spec)
    manager.registerFactory(profile,
                            Replicates,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ReplicatesInit(manager)

    # Create a component
    comp = manager.createComponent("Replicates")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

