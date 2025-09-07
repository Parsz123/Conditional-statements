actual_amount = float(int(input("Please enter actual price- how much does it cost you?")))
sales_amount = float(int(input("Please enter dsales price- how much do ypu sell it for?")))
if (sales_amount > actual_amount):
    amount = sales_amount - actual_amount
    print("Total profit ={0}".format(amount))
else:
    print("No profit!")