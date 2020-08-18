import familiar
from scipy.stats import ttest_1samp,ttest_ind,chisquare
from scipy.stats import chi2_contingency 
#importing data
vein_pack_lifespans=familiar.lifespans(package='vein')
print(vein_pack_lifespans)
#1=sample t-test
vein_pack_test=ttest_1samp(vein_pack_lifespans,71)
print(vein_pack_test)
stat,pval=vein_pack_test
def pval_check(pval):
  if pval < 0.05:
    return "The Vein Pack Is Proven To Make You Live Longer!"
  else:
    return "The Vein Pack Is Probably Good For You Somehow!"
#hypothesis result
print(pval_check(pval))
#importing another data
artery_pack_lifespans=familiar.lifespans(package='artery')
#2-sample t-test
package_comparison_results=ttest_ind(artery_pack_lifespans,vein_pack_lifespans)
print(package_comparison_results)
stat,pval_1=package_comparison_results
def pval_artery(pval):
  if pval < 0.05:
    return "The Artery Pack guarantees even stronger results!"
  else:
    return "The Artery Pack is also a great product!"
#2-sample t-test results
print(pval_artery(pval_1))

#importing another data
iron_contingency_table=familiar.iron_counts_for_package()
print(iron_contingency_table)
tstat,iron_pvalue,df,expected=chi2_contingency(iron_contingency_table)
iron_pval=iron_pvalue
print iron_pval
print iron_pvalue
def p_iron(pval):
  if pval < 0.05:
    return "The Artery Package Is Proven To Make You Healthier!"
  else:
    return "While We Can’t Say The Artery Package Will Help You, I Bet It’s Nice!"
print(p_iron(iron_pvalue))    



