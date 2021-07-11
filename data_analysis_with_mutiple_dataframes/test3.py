load_file_in_context('script.py')

if not 'time' in v_to_c:
  fail_tests('Did you remember to define `time`?')
else:
  pass_tests()
