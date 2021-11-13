grocery_list = ["Milk","Bread","Eggs","Peanut Butter","Jelly","Jelly"]
print(grocery_list)

grocery_list[3] = 'Almond Butter'
print(grocery_list)

for x in grocery_list:
    print(x)
    if x == 'Jelly':
        print(x)
        # grocery_list.includes('Jelly'):
        grocery_list.remove('Jelly')
        #     print(grocery_list)

grocery_list.append('Coffee')
print(grocery_list)