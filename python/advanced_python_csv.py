from advanced_python_regex import email

with open('email.csv', 'w') as f:
  for e in email:
    f.write(e + '\n')
  