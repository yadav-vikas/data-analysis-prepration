import numpy as np
import fetchmaker
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import binom_test,f_oneway,chi2_contingency
##getting data from fetchmaker
rottweiler_t1=fetchmaker.get_tail_length("rottweiler")
print(np.mean(rottweiler_t1))
print(np.std(rottweiler_t1))
whippet_rescue=fetchmaker.get_is_rescue('whippet')
num_whippet_rescues=np.count_nonzero(whippet_rescue)
print(num_whippet_rescues)
num_whippets=np.size(whippet_rescue)
#Binomial_test
pval=binom_test(num_whippet_rescues,n=num_whippets,p=0.08)
print pval
#getting more data
terriers=fetchmaker.get_is_rescue('terrier')
print(terriers)
pitbulls=fetchmaker.get_is_rescue('pitbull')
print(pitbulls)
#ANOVA TEST
anova_test=f_oneway(whippet_rescue,terriers,pitbulls)
print(anova_test)
##Tukey's test
v=np.concatenate([whippet_rescue,terriers,pitbulls])
labels=['whippet'] * len(whippet_rescue) + ['terriers'] * len(terriers) + ['pitbullls'] * len(pitbulls)
tukey_result=pairwise_tukeyhsd(v,labels,0.05)
print(tukey_result)
#Chi-square test
##filling colors counts in color_table for test
color_table = [[2, 3], [1, 3], [2, 2], [4, 1], [1, 2]]
chi_result=chi2_contingency(color_table)
print(chi_result)
