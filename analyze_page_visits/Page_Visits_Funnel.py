import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
#Inspect the DataFrames using print and head:

 #   visits lists all of the users who have #visited the website
   # cart lists all of the users who have added a #t-shirt to their cart
   # checkout lists all of the users who have #started the checkout
    #purchase lists all of the users who have #purchased a t-shirt
print(cart.head())
print(checkout.head())
print(purchase.head())

#Combine visits and cart using a left merge.
visits_cart=(pd.merge(visits,cart,how='left'))
print(visits_cart)
#How long is your merged DataFrame?
visits_cart_rows=len(visits_cart)
print(len(visits))
print(len(checkout))
print(len(purchase))

#How many of the timestamps are null for the column cart_time?
null_cart_times=(cart[cart.cart_time.isnull()])
print(null_cart_times)

#What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
print((null_cart_times) /visits_cart_rows*1.0)
      
#What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?    
cart_checkout = cart.merge(checkout,how='left')
print(cart_checkout)
cart_checkout_rows=len(cart_checkout)
null_checkout_times=len(cart_checkout[cart_checkout.checkout_time.isnull()])
print(float(null_checkout_times)/(cart_checkout_rows)) 
      
      #Merge all four steps of the funnel, in order, 
      #using a series of left merges. Save the results to the variable all_data.
all_data=visits.merge(cart,how='left')\
      .merge(checkout,how='left')\
      .merge(purchase,how='left')
print(all_data.head())
      
      #What percentage of users proceeded to checkout, but did not purchase a t-shirt?
checkout_purchase=pd.merge(checkout,purchase,how='left')

 #Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?

#How might Cool T-Shirts Inc. change their website to fix this problem?

checkout_purchase_rows=len(checkout_purchase)
null_purchase_times=len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
print(float(null_purchase_times)/(checkout_purchase_rows))
#Using the giant merged DataFrame all_data that you created, 


#Start by adding the following column to your DataFrame:
      
      
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase)
      
      #Calculate the average time to purchase using the following code:
print(all_data.time_to_purchase.mean())
