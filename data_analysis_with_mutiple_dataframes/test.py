load_file_in_context('script.py')

try:
  v_to_c
except:
  fail_tests('Did you remember to define `v_to_c`?')
  
ans = pd.merge(visits, checkouts)

if set(ans.columns) != set(v_to_c.columns):
  fail_tests('Are you sure you merged correctly? You should have columns: {}, but you have columns {}'.format(
      ', '.join(ans.columns), ', '.join(v_to_c.columns)))

pass_tests()
