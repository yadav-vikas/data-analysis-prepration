#data analyst for a chain of gardening stores called Petal Power.
import pandas as pd
inventory=pd.read_csv('inventory.csv')
print(inventory.head(10))
staten_island=inventory[inventory.location=='Staten Island']
print(staten_island)
product_request=staten_island['product_description']
print(product_request)
seed_request=inventory[(inventory.location=='Brooklyn') & (inventory.product_type=='seeds')]
print(seed_request)
mylambda=lambda x:  True \
							if inventory[inventory.quantity > 0]
							else False
inventory['in_stock']=mylambda							
inventory['total_value']=inventory['price']*inventory['quantity']
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description']=combine_lambda




------------------------------------------------------------------------------------------------
import pandas as pd
df= pd.read_csv('inventory.csv')
print(df.head(10))
staten_island=df[df.location== 'Staten Island']

product_request = staten_island.product_description

seed_request = df[(df.location =='Brooklyn') & (df.product_type =='seeds')]

inventory=df

inventory['in_stock'] = inventory.quantity.apply(lambda x:True if x >0 else False)

inventory['total_value'] = inventory.price * inventory.quantity

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda,axis=1)
print(inventory)


