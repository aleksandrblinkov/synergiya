weight = input('Введите вес с обозначением веса;')

ves =  int(weight.replace("kg", " ").replace('g', ' ').replace('t', ' '))

if 'kg' in weight:
	print(str(ves * 1000) + 'g')
	print(str(ves / 1000) + 't')
elif 'g' in weight:
	print(str(ves / 1000) + 'kg')
	print(str(ves / 100000) + 't')
elif 't' in weight:
	print(str(ves * 1000) + 'kg')
	print(str(ves * 1000000) + 'g')