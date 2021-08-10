import os

def read_file(filename):
	product = []
	with open(filename, 'r', encoding='utf-8') as f:
			for line in f:
				if 'Product, Price' in line:
					continue
				name, price = line.strip().split(',')
				product.append([name, price])
	return product

#let user input the data
def user_input(product):
	while True:
		name = input('please enter the merchandise name: ')
		if name == 'q':
			break
		price = input('please enter the cost for merchandise: ')
		price = int(price)
		product.append(name, price)
	print(product)
	return product

#print out the result
def print_products(product):
	for p in product: 
		print(p[0], 'price are', p[1])

#overwrite the file
def over_write(filename, product):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Product, Price\n')
		for p in product:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'product.csv'
	if os.path.isfile(filename):
		print('found the file ')
		product = read_file(filename)
	else:
		print('lol you fucked')

	product = user_input(product)
	print_products(product)
	over_write('product.csv', product)

main()

