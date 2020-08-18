import codecademylib
import numpy as np
calorie_stats=np.genfromtxt('cereal.csv',delimiter=",")
print(calorie_stats)
average_calories=np.mean(calorie_stats)
print(average_calories)
calorie_stats_sorted=sorted(calorie_stats)
print(calorie_stats_sorted)
median_calories=np.median(calorie_stats_sorted)
print(median_calories)
nth_percentile=np.percentile(calorie_stats_sorted,80)
print(nth_percentile)
more_calories=np.mean(calorie_stats_sorted  > 60) * 100
print(str(more_calories) + '%')
calorie_std=np.std(calorie_stats_sorted)
print(calorie_std)
