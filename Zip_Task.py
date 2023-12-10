a = {'apple', 'orange', 'tomato', 'salad', 'potato', 'carrot','pear', 'kiwi', 'grape', 'watermelon'}
b = {10.12, 9.18, 5, 6.70, 9.27, 4, 2,2, 4.5, 1.8, 9.0}
c = {12, 156, 178, 1023, 99, 67, 54, 33, 33, 67}
for product, price, employee in zip(a,b,c):
    print('product:', product, 'price:', price, 'employee:', employee)
