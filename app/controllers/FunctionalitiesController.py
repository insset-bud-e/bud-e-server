from functionalities.raspberry import *


method_to_call = getattr(raspberry, 'getTemperature')
result = method_to_call()
result()