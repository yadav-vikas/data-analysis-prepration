#Our favorite online shoe store, ShoeFly.com is performing an A/B Test.
#They have two different versions of an ad, which they have placed in emails,
#as well as in banner ads on Facebook, Twitter, and Google. 
#They want to know how the two ads are performing on each of the different platforms on each day of the week. 
#Help them analyze the data using aggregate measures.

import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

most_views=ad_clicks.groupby('utm_source').user_id.count().reset_index()

print(most_views)

ad_clicks['is_click']=~ad_clicks.ad_click_timestamp.isnull()

print(ad_clicks)

click_by_source=ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

print(click_by_source)

clicks_pivot = click_by_source.pivot(columns='is_click',index='utm_source',values='user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True]+ clicks_pivot[False]) * 100

print(clicks_pivot)

total_count_AB=ad_clicks.groupby('experimental_group').user_id.count().reset_index()

print(total_count_AB)

great_percentage_users=ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

print(great_percentage_users)

greater_percentage_count_pivot=great_percentage_users.pivot(columns='is_click',index='experimental_group',values='user_id').reset_index()

greater_percentage_count_pivot['percent']=greater_percentage_count_pivot[True] / (greater_percentage_count_pivot[True] + greater_percentage_count_pivot[False]) * 100

print(greater_percentage_count_pivot)

a_clicks=ad_clicks[ad_clicks.experimental_group =='A']

b_clicks=ad_clicks[ad_clicks.experimental_group =='B']

print(a_clicks)
print(b_clicks)

#A
users_on_a=a_clicks.groupby(['day','is_click']).user_id.count().reset_index()

users_on_a_pivot=users_on_a.pivot(columns='is_click',index='day',values='user_id').reset_index()

users_on_a_pivot['percent_of_a']=users_on_a_pivot[True] / (users_on_a_pivot[True] + users_on_a_pivot[False]) * 100

print(users_on_a_pivot)

#B
users_on_b=b_clicks.groupby(['day','is_click']).user_id.count().reset_index()

users_on_b_pivot=users_on_b.pivot(columns='is_click',index='day',values='user_id').reset_index()

users_on_b_pivot['percent_of_b']=users_on_b_pivot[True] / (users_on_b_pivot[True] + users_on_b_pivot[False]) * 100

print(users_on_b_pivot)

"""The performance of A is better over the weak than B"""
"""The Performance of A have growth as well as B but in over the weak the total performance is better on A"""

""" NOTE:clicks_pivot[True] is the number of people who clicked (because is_click was True for those users)
clicks_pivot[False] is the number of people who did not click (because is_click was False for those users)
So, the percent of people who clicked would be (Total Who Clicked) / (Total Who Clicked + Total Who Did Not Click)  """
