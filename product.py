product = []

while True:
	name = input('please enter the merchandise name: ')
	if name == 'q':
		break
	price = input('please enter the cost for merchandise: ')
	prine = int(price)
	p = [name, price]
	product.append(p)

for p in product: 
	print(p[0], 'price are', p[1])

with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('Product, Price\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')