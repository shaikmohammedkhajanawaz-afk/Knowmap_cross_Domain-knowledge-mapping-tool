import pkgutil
print('pkgutil file:', getattr(pkgutil, '__file__', 'built-in'))
print('has_get_loader:', hasattr(pkgutil, 'get_loader'))
print('attrs:', [a for a in dir(pkgutil) if 'get_loader' in a or 'get' in a][:50])
