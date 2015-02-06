from random import choice

frases = ['lol', 'hola', 'ke', 'ase']

def basico(request):
	return {'titulo': choice(frases)}