#Our favorite online shoe store, ShoeFly.com is performing an A/B Test.
#They have two different versions of an ad, which they have placed in emails,
#as well as in banner ads on Facebook, Twitter, and Google. 
#They want to know how the two ads are performing on each of the different platforms on each day of the week. 
#Help them analyze the data using aggregate measures.
import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
#which platform is getting most views
most_views=ad_clicks.groupby('utm_source')\
									.user_id.count()\
									.reset_index()
print(most_views)
ad_clicks['is_click']=~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks\
   .groupby(['utm_source',
             'is_click'])\
   .user_id.count()\
   .reset_index()

click_pivot=clicks_by_source.pivot(
  index='utm_source',                     columns='is_click',values='user_id')
print(clicks_pivot)

#to figure out which have the best rate of resources
click_pivot['percent_clicked'] =
clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])
print(clicks_pivot)
#% click will be there

ad_clicks.groupby('experimentalgroup').user_id.count().reset_index()
ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()\
.pivot(index='experimental_group',
      columns='is_click',
      values='user_id').reset_index()
a_clicks=ad_clicks[ad_clicks.experimetal_group == 'A']
a_clicks=ad_clicks[ad_clicks.experimetal_group == 'B']
a_clicks_pivot=a_clicks.groupby(['is_click','day']).user_id.count().pivot(index='day',                                            columns='is_click',
                              values='user_id').reset_index()
a_clicks_pivot['percent_clicked']=a_clicks_pivot[True]/(a_clicks[True]+a_clicks[False])
print(a_clicks_pivot)

a_clicks=ad_clicks[ad_clicks.experimetal_group == 'A']
b_clicks=ad_clicks[ad_clicks.experimetal_group == 'B']
b_clicks_pivot=b_clicks.groupby(['is_click','day']).user_id.count().pivot(index='day',                                            columns='is_click',
                              values='user_id').reset_index()
b_clicks_pivot['percent_clicked']=b_clicks_pivot[True]/(b_clicks[True]+b_clicks[False])
print(b_clicks_pivot)
