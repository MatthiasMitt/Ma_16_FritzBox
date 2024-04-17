modulname = 'Ma_16_einfacheAnfragen'
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'



# 2023-05-27 neues Passwort. 
# 2024-04-17 neue  IP-nummer
# 2024-04-17 Details von import boxen
# 2024-04-17 Don't try to use 'console' on macOS

from fritzconnection.lib.fritzphonebook     import FritzPhonebook

from fritzconnection.lib.fritzcall          import FritzCall

#__ import console # um Schriftfarbe zu ändern
from   boxen                                import boxen

def frage(box):
	
	beschreibung,ip,modelnamePattern,u,pw = box
	
	print('Fritzbox ',beschreibung)
	
	print('get_missed_calls')
	try:
		fc = FritzCall(address=ip, user=u, password=pw)
		calls = fc.get_missed_calls()
		for call in calls:
			print(call)
		
		print('get_all_names(all phonebooks)')
		fp = FritzPhonebook(address=ip, user=u, password=pw)
		for phonebook_id in fp.phonebook_ids:
			contacts = fp.get_all_names(phonebook_id)
			for name, numbers in contacts.items():
				print(name, numbers)
			
	except:
		#__ console.set_color(1.0,0.0,0.0)
		print('... diese FritzBox antwortet nicht !')
		#__ console.set_color()
			

if __name__ == '__main__':
	
	print(modulname)
	
	#print(boxen.len)
	for box in boxen:
		#print(box[0])
		frage(box)
		

	print('\n-----',modulname)
