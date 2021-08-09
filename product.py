product = []

while True:
	name = input('please enter the merchandise name: ')
	if name == 'q':
		break
	price = input('please enter the cost for merchandise: ')
	p = [name, price]
	product.append(p)

print(product)
