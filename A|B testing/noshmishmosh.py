#importing packages
import noshmishmosh
import numpy as np

#looking into data
all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers 
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
#Calculating the Baseline percent

print("total_visitor_count="+str(total_visitor_count))
print("paying_visitor_count="+str(paying_visitor_count))
baseline_percent = (100.0 * paying_visitor_count) / total_visitor_count
print("baseline_percent="+str(baseline_percent)) 
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
#Average payment

print("average_payment="+str(average_payment))
#Calculating New customers for the product

new_custormers_needed = np.ceil(1240 / average_payment)
print("new_customers_needed="+str(new_custormers_needed))
#percentage point_increase

percentage_point_increase  = (100.0 * new_custormers_needed) / total_visitor_count
print("percent_point_increase="+str(percentage_point_increase))
#Minimum Detectable Effecet

minimum_detectable_effect = (100.0 * percentage_point_increase ) / baseline_percent
print("minimum_detectable_effect="+str(minimum_detectable_effect))
statistical_significance=90
#FROM SAMPLE SIZE CALCULATOR

sample_size=290

#DOCUMENTATION
"""
1.Nosh Mish Mosh wants to run an experiment to see if we can convince more people to purchase meal plans if we use a more artisanal-looking vegetable selection. We’ve photographed these modern meals with blush tomatoes and graffiti eggplants, but aren’t sure if this strategy will sell enough units to benefit from establishing a business relationship with a new provider.

Before running this experiment, of course, we need to know how many people have to see the new assets. We don’t want customers seeing food that we won’t end up offering. Of course, there are three things we need to know before we determine that number.

the Baseline
the Minimum Detectable Effect
and the Statistical Significance

2.Let’s get the ball rolling on finding those numbers! In order to get our baseline, we need to first know how many users visited the site. Let’s grab that logged information, which is stored in noshmishmosh.customer_visits. Assign that to a new variable called all_visitors.

3.Next we need to know how many visitors to the site ultimately end up buying a meal or set of meals from Nosh Mish Mosh. We have that information saved into purchasing_customers field on noshmishmosh. Save that information into a variable called paying_visitors.

4.Calculate the lengths of the two lists, saving the results into variables called total_visitor_count and paying_visitor_count, respectively.

5.Now to get the baseline: since we want a percentage as our answer, multiply the number of purchasing visitors by 100.0. Then divide that by the number of total visitors. Save the result in a variable called baseline_percent.

6.Print out the baseline_percent so we know what to use for our baseline percentage in the A/B Sample Size Calculator

7.These rainbow fingerling potatoes don’t come cheap. We’d like to know for sure that we’ll be pulling in at least $1240 more every week. In order to figure out how many more customers we need we’ll have to investigate the average revenue generated from a given sale. Luckily we have a list of the money spent by each customer in noshmishmosh.money_spent. Save that list into a variable called payment_history.

8.We need to find how many typical purchases it would take to reach $1240 in additional revenue using our historical data.

Let’s start with computing the average payment per paying customer using np.mean, saving it as average_payment.

9.We want to know how many of these “usual” payments it would take to clear our $1240 mark. Round the number up using np.ceil (because that’s how many new customers it takes to bring in more than $1240). Save that value into a new_customers_needed variable.

10.Now find the percent lift required by multiplying the number of customers by 100.0 and dividing the result by the total visitor count ascertained earlier. Save the result in a variable called percentage_point_increase. Print percentage_point_increase to see what it is.

11.In order to find our minimum detectable effect, we need to express percentage_point_increase as a percent of baseline_percent. You can do this by dividing percentage_point_increase by baseline_percent and multiplying by 100.0.

Store the results in a variable called minimum_detectable_effect.

12.Print out the result minimum_detectable_effect.

13.The last thing we need to calculate the sample size for Nosh Mish Mosh’s artisanal rebranding is our statistical significance. We’d like to be fairly certain, but this isn’t going to be a million dollar decision, so let’s go with 90%.

14.Now put it all together! Puch the baseline, the minimum detectable effect, and the statistical significance into the calculator and evaluate how many people need to be shown the new assets before we can check if the results are a significant improvement. Save the results in a variable called ab_sample_size.

SAMPLE SIZE = 290 """
