import os

#check if os has file
product = []
if os.path.isfile('product.csv'):
	print('found the file!')
	with open('product.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'Product, Price' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
	print(product)

else:
	print('lol you fucked up')

#let user input the data
while True:
	name = input('please enter the merchandise name: ')
	if name == 'q':
		break
	price = input('please enter the cost for merchandise: ')
	prine = int(price)
	p = [name, price]
	product.append(p)

#print out the result
for p in product: 
	print(p[0], 'price are', p[1])

#overwrite the file
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('Product, Price\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')