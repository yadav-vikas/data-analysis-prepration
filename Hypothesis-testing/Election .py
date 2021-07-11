import numpy as np
import matplotlib.pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']
total_ceballos=sum([1 for n in survey_responses if n == 'Ceballos'])
print(total_ceballos)
survey_length=float(len(survey_responses))
percentage_ceballos= total_ceballos / survey_length
print(percentage_ceballos)
possible_surveys=np.random.binomial(survey_length,0.54,size=10000) / survey_length
plt.hist(possible_surveys,range=(0,1),bins=20)
plt.show()
possible_survey_length=float(len(possible_surveys))
incorrect_predictions=len(possible_surveys[possible_surveys < 0.5])
celballos_loss_surveys=incorrect_predictions / possible_survey_length
print(celballos_loss_surveys)
large_survey_length=float(7000)
large_survey=np.random.binomial(large_survey_length,0.54,size=10000) / large_survey_length
incorrect_prediction_large=len(large_survey[large_survey < 0.5])
ceballos_loss_new=incorrect_prediction_large / large_survey_length
print(ceballos_loss_new)
