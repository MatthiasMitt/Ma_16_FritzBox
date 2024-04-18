modulname = 'Ma_16_ZeigeAlles'
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'

#modulname = 't6.py'

from   Ma_16_Plattform                              import Ma_Plattform
Ma16ZAPlattfrom = Ma_Plattform()

from   time                                         import sleep

if Ma16ZAPlattfrom.auf_iPhone_o_iPad():
	from M_fritzconnection.core.fritzconnection import FritzConnection
else:
	from   fritzconnection.core.fritzconnection import FritzConnection

from   fritzconnection.lib.fritzwlan                import FritzWLAN

if Ma16ZAPlattfrom.auf_iPhone_o_iPad():
	from M_fritzconnection.core.exceptions      import FritzServiceError, FritzConnectionException
else:
	from   fritzconnection.core.exceptions      import FritzServiceError, FritzConnectionException

if Ma16ZAPlattfrom.auf_iPhone_o_iPad():
	from   fritzconnection.fritzhosts           import FritzHosts

from   fritzconnection.lib.fritzstatus              import FritzStatus
from   fritzconnection.lib.fritzhomeauto            import FritzHomeAutomation

from   boxen                                        import boxen


class FritzTest():

	def __init__(self,box):
		
		self.beschreibung,self.ip,self.modellpatter,self.u,self.pw = box
		
	def do_call_action(self,a_service,a_action,a_arguments=None):
		print('call',a_service,',',a_action,end='')
		if a_arguments:
			print(' ,arguments=',a_arguments,sep='',end='')
		print(':','\n  ',end=' ')
		try:
			print(self.fc.call_action(a_service,a_action,arguments=a_arguments))
		except FritzConnectionException as e:
			print("\n!! call_action('",a_service,"','",a_action,"')  will nicht !", sep='')
			print('!!', e.__class__, '\n')
			print('!!', e          , '\n')
		except:
			print('!!! anderer Fehler')
	
	def do_call_and_print(self,a_handle,a_handle_name,a_func,a_arguments=None):
		print('call ',a_handle_name,'.',a_func,'(',sep='',end='')
		if a_arguments != None:
			print(a_arguments,sep='',end='')
		print(') : ',end='')
		try:
			if a_arguments != None:
				r = getattr(a_handle,a_func)(a_arguments)
			else:
				r = getattr(a_handle,a_func)()
			print(r)
			# learnt from
			# https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
		except :
			print('...failed.')
	
	def do_get_and_print(self,a_handle,a_handle_name,a_attr):
		print(a_handle_name,'.',a_attr,' : ',sep='',end='')
		try:
			r = getattr(a_handle,a_attr)
			print(r)
			# learnt from
			# https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
		except :
			print('...failed.')
		
	def sleep_verbose(self,tim):
		print('sleep ',tim,' seconds',end='')
		for tick in range(tim):
			sleep(1)
			print('.',end='')
		print(' ')
	
	def test(self):
		
		print( '\nTeste' , self.beschreibung )
		print(  '=======================')
		try:
			if self.u != '':
				self.fc    = FritzConnection( address= self.ip
				                       , user=    self.u
				                       , password=self.pw
				                       #, use_tls=False
				                       )
			else:
				self.fc    = FritzConnection( address= self.ip
				                       #,user=    self.u
				                       , password=self.pw
				                       #,use_tls= False
				                       )
		except:
			print('... diese FritzBox antwotet nicht !')
			self.fc = None
			
		if self.fc:
		
			print( 'modelname       :' , self.fc.modelname)
			print( 'system_version  :' , self.fc.system_version)
			
			print( 'services        :' )
			fss = self.fc.services
			for fs in fss:
				print( '}-', fs )
			print('---services\n')
			
			#print(fc.actionnames)
			#print(fc.get_action_arguments('GetStatusInfo'))
			self.do_call_action('WANIPConn1','GetStatusInfo')
			self.do_call_action('WANCommonInterfaceConfig1','GetTotalBytesSent')
			self.do_call_action('WANCommonInterfaceConfig1','GetTotalBytesReceived')
			self.do_call_action('WANIPConnection1','GetExternalIPAddress')
			self.do_call_action('WANCommonInterfaceConfig1','GetCommonLinkProperties')
			
			self.do_call_action('X_VoIP1','X_AVM-DE_DialNumber',a_arguments={"NewX_AVM-DE_PhoneNumber": "**621"})
			self.sleep_verbose(7)
			self.do_call_action('X_VoIP1','X_AVM-DE_DialHangup')
			
			print('\nWLAN')
			print(  '----')
			
			fw = FritzWLAN(self.fc)
			ssidn = fw.ssid
			print(  'ssid          :' , ssidn)
			print(  'channel       :' , fw.channel)
			print(  'channel_infos :' , fw.channel_infos())
			print(  'get_hosts_info:' , fw.get_hosts_info())
			
			try:
				print('\nget_generic_host_entry(0):' , fw.get_generic_host_entry(0))
				print('\nget_generic_host_entry(1):' , fw.get_generic_host_entry(1))
			except:
				None
			
			
			if Ma16ZAPlattfrom.auf_iPhone_o_iPad():
				fho = FritzHosts(self.fc)
				hosts = fho.get_hosts_info()
				print('\nhosts :')
				for host in hosts:
					print( '}-' , host ) # , '\n' )
				print('---hosts---    wahrscheinlich mehr, aber Box zeigt nur 16  :-( \n')
			else:
				print('*** FritzHosts  auf dieser Plattform nicht verfügbar. ***')
			
			
			print('\nStatus')
			print(  '------')
			
			fs = FritzStatus(self.fc)
			self.do_get_and_print(fs,'fs','str_transmission_rate')
			self.do_get_and_print(fs,'fs','str_max_linked_bit_rate')
			self.do_get_and_print(fs,'fs','str_max_bit_rate')
			self.do_call_and_print(fs,'fs','get_monitor_data')
			
			
			
			print('\nHomeAutomation')
			print(  '--------------')
			
			fh  = FritzHomeAutomation(self.fc)
			ain ='11657 0217798'
			
			try:
				
				#for x in range(3): #
				self.do_call_and_print(fh,'fh','get_device_information_by_index',0)
				self.do_call_and_print(fh,'fh','get_device_information_by_index',1)
				self.do_call_and_print(fh,'fh','device_informations')
				
				
				#fh.set_switch(ain, on=True)
				#fh.set_switch(ain, on=False)
				
				#bang print(fw.total_host_number)
			except FritzServiceError as eFSE:
				print('\n!! mehr HomeAutomation scheint von dieser FritzBox nicht angeboten zu sein!')
				print('!!', eFSE.__class__)
				print('!!', eFSE          , '\n')
		
	def finish(self):
		pass
	
#end class

if __name__ == '__main__':
	
	#print(boxen.len)
	for box in boxen:
		#print(box[0])
		tc = FritzTest(box)
		tc.test()
		tc.finish()
