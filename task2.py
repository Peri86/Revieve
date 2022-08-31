#!/usr/bin/python3
# Author: Pau Pericay Vendrell
"""
Task2
he marketing department wants to know which customers are interested in each product;
they've asked for a product_customers.csv file that, for each product, gives the list of customers who have purchased this product:
id numeric product id
customer_ids a space-separated list of customer ids of the customers who have purchased this product
"""


import csv

#Read file orders.csv
with open('files/orders.csv') as csv_file:
    orders_reader = csv.DictReader(csv_file)
    listorders = list(orders_reader)

product_customer = {}
# loop though all the orders
for order in listorders:
    #split and delete duplicates
    productlist = list(set(order['products'].split()))


    # loop products of the order
    for product in productlist:

        #check if product exist in dict, create if not
        if product not in product_customer:
            product_customer[str(product)] = list(order['customer'])
        else:
            product_customer[str(product)].append(order['customer'])

#Write to file
with open('files/product_customers.csv',"w", newline='') as outcsvfile:
    fieldnames = ['id', 'customers_ids']
    writer = csv.DictWriter(outcsvfile, fieldnames)
    # write header
    writer.writeheader()

    # loop with cost results
    for k, v in product_customer.items():
        # create space separated list
        clist = " ".join(set(v))
        writer.writerow({'id' : "{}".format(k),'customers_ids' : "{}".format(clist)})
