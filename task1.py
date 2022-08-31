#!/usr/bin/python3
# Author: Pau Pericay Vendrell
"""
 Task1
 Right now the orders.csv doesn't have total order cost information.
 We need to use the data in these files to emit a order_prices.csv file with the following columns:
 id the numeric id of the order
 euros the total cost of the order
"""


import csv

# method takes products and return sum of cost
def read_products_cost(productlist):
    #transform to list
    productlist = productlist.split()

    sum_order = 0
    for product in productlist:
        #get position of product
        position=int(product)

        #add cost of product
        sum_order += float(listproducts[position]['cost'])

    #return total cost
    return sum_order

#Read file product.csv
with open('files/products.csv') as csv_file:
    product_reader = csv.DictReader(csv_file)
    listproducts = list(product_reader)

#Read file order.csv
with open('files/orders.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # variable to get first iteration
    line_count = 0
    # dictionary with total costs
    cost_dict = {}

    # loop for each row
    for row in csv_reader:
        # Get columns
        if line_count == 0:
            line_count += 1

        #Get cost
        product_cost = read_products_cost(row["products"])
        # link cost with order
        cost_dict[row["id"]] = product_cost


#Write to file
with open('files/order_prices.csv',"w", newline='') as outcsvfile:
    fieldnames = ['id', 'euros']
    writer = csv.DictWriter(outcsvfile, fieldnames)
    # write header
    writer.writeheader()

    # loop with cost results
    for k, v in cost_dict.items():
        writer.writerow({'id' : "{}".format(k),'euros' : "{}".format(v)})
