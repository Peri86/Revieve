#!/usr/bin/python3
# Author: Pau Pericay Vendrell
"""
 #Task3
 To evaluate our customers, we need a customer_ranking.csv containing the following columns,
 ranked in descending order by total_euros:

 id numeric id of the customer
 firstname customer first name
 lastname customer last name
 total_euros total euros this customer has spent on products
"""

import csv

listcustomers = {}
listorders = {}
listproducts = {}

# load file info in memory
def loadfiles():
    #modifying global variables
    global listcustomers
    global listorders
    global listproducts

    #Read file customers.csv
    with open('files/customers.csv') as csv_file:
        customers_reader = csv.DictReader(csv_file)
        listcustomers = list(customers_reader)

    #Read file orders.csv
    with open('files/orders.csv') as csv_file:
        orders_reader = csv.DictReader(csv_file)
        listorders = list(orders_reader)

    #Read file products.csv
    with open('files/products.csv') as csv_file:
        products_reader = csv.DictReader(csv_file)
        listproducts = list(products_reader)

# get names of customers
def get_cust_names(idcustomer):
    global listcustomers
    firstname=listcustomers[int(idcustomer)]['firstname']
    lastname=listcustomers[int(idcustomer)]['lastname']
    return firstname,lastname

# get total spent given a list of products
def sum_spent(orderproducts):
    sum_cost=0
    for product in orderproducts:
        # add the cost
        sum_cost += float(listproducts[int(product)]['cost'])
    return sum_cost

# build ranking
def order_customers(spent_customer):
    list_ranking = []

    # loop customers products
    for idcustomer, listprod in spent_customer.items():
        # get cost
        total_spent = sum_spent(listprod)
        # get names
        firstname,lastname = get_cust_names(idcustomer)

        list_ranking.append(dict({'id': idcustomer,'firstname': firstname,'lastname': lastname,'total_euros': total_spent}))

    list_ranking = sorted(list_ranking, key=lambda i: i['total_euros'], reverse=True)
    return list_ranking

def _main_():

    #load files info
    loadfiles()

    spent_customer = {}
    # loop though all the orders
    for order in listorders:
        idcustomer = order['customer']
        # populate dict with products that link with customer
        if idcustomer not in spent_customer:
            spent_customer[str(idcustomer)] = list(order['products'].split())
        else:
            spent_customer[str(idcustomer)].extend(order['products'].split())

    # get list of dicts with columns required
    list_ranking = order_customers(spent_customer)

    # get the keys from the first dict of the list
    keys = list_ranking[0].keys()

    #Write to file
    with open('files/customer_ranking.csv',"w", newline='') as outcsvfile:
        writer = csv.DictWriter(outcsvfile, keys)

        # write header
        writer.writeheader()
        writer.writerows(list_ranking)

if __name__ == "__main__" :
    _main_()