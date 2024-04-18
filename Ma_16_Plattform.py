modulname = 'Ma_16_Plattform'
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'

# 'testplatform.py'

import platform

class Ma_Plattform():
	
	def __init__(self):
		self.p_p = platform.platform()
	
	def auf_iPad(self):
		return self.p_p[0:6] == 'iPadOS'
	
	def auf_iPhone(self):
		return self.p_p[0:3] == 'iOS'
	
	def auf_iMac(self):
		return self.p_p[0:5] == 'macOS'
	
	def auf_Mac(self):
		return self.auf_iMac()
	
	def auf_iPhone_o_iPad(self):
		return self.auf_iPhone() or self.auf_iPad()
		
	def druckeWoIchBin(self):
		if   self.auf_Mac():
			print('Ich bin auf einem Mac.')
		elif self.auf_iPad():
			print('Ich bin auf einem iPad.')
		elif self.auf_iPhone():
			print('Ich bin auf einem iPhone.')
		else:
			print('Ich weiss nicht wo ich bin.' +
			      ' Wahrscheinlich könnte man es aus "{0}" herauslesen.'.format(self.p_p))


'''
Mal gucken, was sich alles abfragen läßt.


print('\n\nImport-related module attributes')

#The import machinery fills in these attributes on each module object during loading, based on the module’s spec, before the loader executes the module.

print('__name__',__name__)
# The __name__ attribute must be set to the fully-qualified name of the module. This name is used to uniquely identify the module in the import system.
print('__loader__',__loader__)
#The __loader__ attribute must be set to the loader object that the import machinery used when loading the module. This is mostly for introspection, but can be used for additional loader-specific functionality, for example getting data associated with a loader.
print('__package__',__package__)
#The module’s __package__ attribute must be set. Its value must be a string, but it can be the same value as its __name__. When the module is a package, its __package__ value should be set to its __name__. When the module is not a package, __package__ should be set to the empty string for top-level modules, or for submodules, to the parent package’s name. See PEP 366 for further details.

#This attribute is used instead of __name__ to calculate explicit relative imports for main modules, as defined in PEP 366. It is expected to have the same value as __spec__.parent.

#Changed in version 3.6: The value of __package__ is expected to be the same as __spec__.parent.

print('__spec__',__spec__)
#The __spec__ attribute must be set to the module spec that was used when importing the module. Setting __spec__ appropriately applies equally to modules initialized during interpreter startup. The one exception is __main__, where __spec__ is set to None in some cases.

#When __package__ is not defined, __spec__.parent is used as a fallback.

#New in version 3.4.

#Changed in version 3.6: __spec__.parent is used as a fallback when __package__ is not defined.

print('__path__',   '** not defined **')   # __path__)
#If the module is a package (either regular or namespace), the module object’s __path__ attribute must be set. The value must be iterable, but may be empty if __path__ has no further significance. If __path__ is not empty, it must produce strings when iterated over. More details on the semantics of __path__ are given below.

#Non-package modules should not have a __path__ attribute.
print('__file__',__file__)
print('__cached__',__cached__)
#__file__ is optional. If set, this attribute’s value must be a string. The import system may opt to leave __file__ unset if it has no semantic meaning (e.g. a module loaded from a database).

#If __file__ is set, it may also be appropriate to set the __cached__ attribute which is the path to any compiled version of the code (e.g. byte-compiled file). The file does not need to exist to set this attribute; the path can simply point to where the compiled file would exist (see PEP 3147).

#It is also appropriate to set __cached__ when __file__ is not set. However, that scenario is quite atypical. Ultimately, the loader is what makes use of __file__ and/or __cached__. So if a loader can load from a cached module but otherwise does not load from a file, that atypical scenario may be appropriate.


##________
print('\n\nplatform.')
print('.architecture()',platform.architecture())
print('.freedesktop_os_release()','  [errno 2]') # platform.freedesktop_os_release())
print('.java_ver()',platform.java_ver())
print('.mac_ver()',platform.mac_ver())
print('.libc_ver()',platform.libc_ver())
print('.platform()',platform.platform())
print('.node()',platform.node())
print('.machine()',platform.machine())
print('.processor()',platform.processor())
print('.architecture()',platform.architecture())

print('.python_build()',platform.python_build())
print('.python_compiler()',platform.python_compiler())
print('.python_branch()',platform.python_branch())
print('.python_implementation()',platform.python_implementation())
print('.python_revision()',platform.python_revision())
print('.python_version()',platform.python_version())
print('.python_version_tuple()',platform.python_version_tuple())
print('.release()',platform.release())
print('.system()',platform.system())
#rint('.system_alias()',platform.system_alias())
print('.version()',platform.version())
print('.uname()',platform.uname())

'''

if __name__ == '__main__':
	
	print(modulname)
	
	pf = Ma_Plattform()
	pf.druckeWoIchBin()
