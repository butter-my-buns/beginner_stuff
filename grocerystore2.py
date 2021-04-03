import sys
while True:
	grocery_store2={
	'food1':[{'name': "apples" , "price":10 , "stock":100}],
	"food2":[{"name": "mangoes" , "price":25 , "stock":80}],
	"food3":[{"name": "pears" , "price":20 , "stock":50}]}
	
	print("Welcome to Monu Market")

	for key,value in grocery_store2.items():
		print(key,value)

	need=input('Which item would you like to buy: ')
	quantity=input('How much would you like to buy: ')

	if need=="apples":
		for data in grocery_store2['food1']:
			data["stock"]=(data["stock"])-int(quantity)
	elif need=="mangoes":
		for data in grocery_store2['food2']:
			data["stock"]=(data["stock"])-int(quantity)
	elif need=="pears":
		for data in grocery_store2['food3']:
			data["stock"]=(data["stock"])-int(quantity)
	else:
		print("Plz enter a valid food item")	

	
	if need=="apples":
		for data in grocery_store2['food1']:
			amount=data["price"]*int(quantity)

	elif need=="mangoes":
		for data in grocery_store2['food2']:
			amount=data["price"]*int(quantity)
	
	elif need=="pears":
		for data in grocery_store2['food3']:
			amount=data["price"]*int(quantity)
	else:
		pass
	
	print("Do you want to buy again?(y/n)")
	again=input()
	
	if again!="y":
		print("Thanks for shopping at Monu Market!")
		total=0
		total+=amount
		print(f'Your total bill is {total}')
		break
	else:
		print("Great")

sys.exit






