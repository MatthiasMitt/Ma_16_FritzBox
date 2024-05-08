modulname = 'Ma_16_ZeigeAlles'
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'


import sys
import os
b2 = os.path.realpath(__file__).split("/")
b4 = "/".join(b2[0:-2]) 
b5 = "/".join(b2[0:-1])
# 'import' soll auch in dem Ordner suchen, in dem dises Programm gespeichet ist.
sys.path.insert(1,b5)
# 'import' soll auch in dem umfassenden Ordner suchen, wo es hoffentlich das
# Hilfspaket 'Ma_Util' gibt. Unabhänge davon, wie und von wo aus gestartet wurde.
sys.path.insert(1,b4)

from   Ma_Util.Ma_Print                             import print_dict, print_list, print_list_of_dicts
from   Ma_Util.Ma_Console                           import Ma_Console
from   Ma_Util.Ma_Plattform                         import Ma_Plattform
Ma16ZAPlattform = Ma_Plattform()

from   time                                         import sleep

if Ma16ZAPlattform.auf_iPhone_o_iPad():
	# mit Korrekturen
	from M_fritzconnection.core.fritzconnection import FritzConnection
else:
	from   fritzconnection.core.fritzconnection import FritzConnection

from   fritzconnection.lib.fritzwlan                import FritzWLAN

if Ma16ZAPlattform.auf_iPhone_o_iPad():
	# mit Korrekturen
	from M_fritzconnection.core.exceptions      import FritzServiceError, FritzConnectionException
else:
	from   fritzconnection.core.exceptions      import FritzServiceError, FritzConnectionException

if Ma16ZAPlattform.auf_iPhone_o_iPad():
	from   fritzconnection.fritzhosts           import FritzHosts
#else:
#	# fehlt der Modul

from   fritzconnection.lib.fritzstatus              import FritzStatus
from   fritzconnection.lib.fritzhomeauto            import FritzHomeAutomation

from   boxen                                        import boxen

if Ma16ZAPlattform.auf_iPhone_o_iPad():
	import console

class FritzTest():

	def __init__(self,box):
		
		self.beschreibung,self.ip,self.modelnamePattern,self.u,self.pw = box
		self.out = Ma_Console()

	def print_result(self,r):
		if type(r) == dict:
			# print_dict(r,title="   [dict]",keyWidth=40)
			print_dict(r,title=" ",keyWidth=40)
		elif type(r) == list:
			if type(r[0]) == dict:
				print_list_of_dicts(r)
			else:
				print_list(r)
		else:
			#deb print("   type=",type(r))
			print(r)

	def do_call_action(self,a_service,a_action,a_arguments=None):
		print('\naction    ',a_service,'/',a_action,sep='',end='')
		if a_arguments:
			print(' ,arguments=',a_arguments,sep='',end='')
		print(':')
		try:
			res = self.fc.call_action(a_service,a_action,arguments=a_arguments)
			self.print_result(res)
		except FritzConnectionException as e:
			str1 = "\n!! call_action('"+str(a_service)+"','"+str(a_action)+"')  will nicht !"
			str2 = '!!'+str(e.__class__)+'\n'
			str3 = '!! '+str(e)+'\n'
			self.out.print_red(str1)
			self.out.print_red(str2)
			self.out.print_red(str3)
			return False
		except:
			self.out.print_red('!!! anderer Fehler')
			return False
		return True



	def do_call_and_print(self,a_handle,aMethod,a_arguments=None):
		print('\nmethod    ',aMethod,'(',sep='',end='')
		if a_arguments != None:
			print(a_arguments,sep='',end='')
		print(') : ')
		try:
			if a_arguments != None:
				r = getattr(a_handle,a_func)(a_arguments)
				r = getattr(a_handle,aMethod)(a_arguments)
			else:
				r = getattr(a_handle,aMethod)()
			self.print_result(r)
			# learnt from
			# https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
		except :
			self.out.print_red('...failed.')
	
	
	def do_get_and_print(self,a_handle,aAttribute):
		print('\nattribute ',aAttribute,' : ',sep='',end='')
		try:
			r = getattr(a_handle,aAttribute)
			print(r)
			# learnt from
			# https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
		except :
			self.out.print_red('...failed.')
	
		
	def sleep_verbose(self,tim):
		progress = '_'*tim
		print('sleep ',tim,' seconds ',progress,sep='',end='')
		for tick in range(tim):
			sleep(1)
			dot = '\b'*(tick+1) + ':'
			print(dot,sep='',end='')
		print(' ')
	
	
	def print_WLAN_hosts(self,hosts):
		print('\nWLAN hosts :')
		# {'service': 1, 'index': 0, 'status': False, 'mac': '84:c7:ea:4c:fd:f9', 'ip': '192.168.178.86', 'signal': 0, 'speed': 0}
		linepattern = '|{0!s:^7s}|{1!s:^5s}|{2!s:<6s}|{3!s:<20s}|{4!s:<15s}|{5!s:>6s}|{6!s:>5s}|'
		print( linepattern.format('service','index','status','mac','ip','signal','speed') )
		for host in hosts:
			if len(host) == 7:
				try:
					se = host['service']
					ix = host['index']
					st = host['status']
					ma = host['mac']
					ip = host['ip']
					si = host['signal']
					sp = host['speed']
					print( linepattern.format(se,ix,st,ma,ip,si,sp) )
				except :
					print( '}-' , host )
			else:		
				print( '}-' , host , '    len(host):',len(host))
		if len(hosts) != 16:
			print('---WLAN hosts---')
		else:
			print('---WLAN hosts---    ',end='')
			console.set_color(1.0,0.2,0.2)
			print('wahrscheinlich mehr, aber Box zeigt nur 16  :-( \n')
			console.set_color()
			
		
	def print_Fritz_hosts(self,hosts):
		print('\nFritz hosts :')
		# {'ip': '192.168.178.93', 'name': 'AppleWavonMirja', 'mac': '60:9A:C1:6A:07:6C', 'status': False}
		linepattern = '|{0!s:<15s}|{1!s:<28s}|{2!s:<20s}|{3!s:^6s}|'
		print( linepattern.format('ip','name','mac','status') )
		for host in hosts:
			if len(host) == 4:
				try:
					ip = host['ip']
					na = host['name']
					st = host['status']
					ma = host['mac']
					print( linepattern.format(ip,na,ma,st) )
				except :
					print( '}-' , host )
			else:		
				print( '}-' , host , '    len(host):',len(host))
		if len(hosts) != 16:
			print('---Fritz hosts---')
		else:
			print('---Fritz hosts---    wahrscheinlich mehr, aber Box zeigt nur 16  :-( \n')
	
	
	def test(self):
		
		self.out.title1('Teste '+self.beschreibung)
		
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
			self.out.print_red('... diese FritzBox antwortet nicht !')
			self.fc = None
			
		if self.fc:
		
			print( '\nmodelname       :' , self.fc.modelname)
			
			if self.modelnamePattern == '':
				pass # there is no pattern
			else:
				if self.modelnamePattern in self.fc.modelname:
					pass # good chance that it is the right FritzBox
				else:
					console.set_color(1.0,0.0,0.0)
					print("\n    nicht '",self.modelnamePattern,"'?\n!! Scheinbar eine falsche FritzBox !!\n",sep='')
					console.set_color()
					self.fc = None
			
		if self.fc:
				
			print( '\nsystem_version  :' , self.fc.system_version)
			
			print( '\nservices        :' )
			fss = self.fc.services
			print_list(fss,title="- ")
			#for fs in fss:
			#	print( '}-', fs )
			print('---services\n')
			
			#print(fc.actionnames)
			self.do_get_and_print(self.fc,'actionnames')
			#print(fc.get_action_arguments('GetStatusInfo'))
			self.do_call_and_print(self.fc,'get_action_arguments')
				
			self.do_call_action('WANIPConn1','GetStatusInfo')
			self.do_call_action('WANCommonInterfaceConfig1','GetTotalBytesSent')
			self.do_call_action('WANCommonInterfaceConfig1','GetTotalBytesReceived')
			self.do_call_action('WANIPConnection1','GetExternalIPAddress')
			self.do_call_action('WANCommonInterfaceConfig1','GetCommonLinkProperties')
			
			success = self.do_call_action('X_VoIP1','X_AVM-DE_DialNumber',a_arguments={"NewX_AVM-DE_PhoneNumber": "**621"})
			if success:
				self.sleep_verbose(7)
			self.do_call_action('X_VoIP1','X_AVM-DE_DialHangup')
			
			self.out.title2('WLAN')
			
			fw = FritzWLAN(self.fc)
			# bricht ab, wenn das Passwort nicht stimmte:  ssidn = fw.ssid
			self.do_get_and_print(fw, 'ssid')
			self.do_get_and_print(fw, 'channel')
			self.do_call_and_print(fw, 'channel_infos')
			
			#self.do_call_and_print(fw, 'get_hosts_info')
			try:
				hosts = fw.get_hosts_info()
				self.print_WLAN_hosts(hosts)
			except :
				self.out.print_red('FritzWLAN(...).get_hosts_info  failed.')
			
			try:
				for ix in range(16):
					res = fw.get_generic_host_entry(ix)
					print('\nget_generic_host_entry(',ix,'):')
					self.print_result(res)
			except:
				None
			
			
			if Ma16ZAPlattform.auf_iPhone_o_iPad():
				fho = FritzHosts(self.fc)
				try:
					hosts = fho.get_hosts_info()
					self.print_Fritz_hosts(hosts)
				except :
					self.out.print_red('FritzHosts(...).get_hosts_info  failed.')
			else:
				print('\n*** FritzHosts  auf dieser Plattform nicht verfügbar. ***')
			
			self.out.title2('Status')
			
			fs = FritzStatus(self.fc)
			self.do_get_and_print( fs,'str_transmission_rate')
			self.do_get_and_print( fs,'str_max_linked_bit_rate')
			self.do_get_and_print( fs,'str_max_bit_rate')
			self.do_call_and_print(fs,'get_monitor_data')
			
			
			
			self.out.title2('HomeAutomation')
			
			fh  = FritzHomeAutomation(self.fc)
			ain ='11657 0217798'
			
			try:
				
				#for x in range(3): #
				self.do_call_and_print(fh,'get_device_information_by_index',0)
				self.do_call_and_print(fh,'get_device_information_by_index',1)
				self.do_call_and_print(fh,'device_informations')
				
				
				#fh.set_switch(ain, on=True)
				#fh.set_switch(ain, on=False)
				
				#bang print(fw.total_host_number)
			except FritzServiceError as eFSE:
				self.out.print_red('\n!! mehr HomeAutomation scheint von dieser FritzBox nicht angeboten zu sein!')
				self.out.print_red('!!'+str(eFSE.__class__))
				self.out.print_red('!!'+str(eFSE)+'\n')
		
	def finish(self):
		pass
	
#end class

if __name__ == '__main__':
	
	print(modulname)
	
	#print(boxen.len)
	for box in boxen:
		#print(box[0])
		tc = FritzTest(box)
		tc.test()
		tc.finish()

	print('\n-----',modulname)
