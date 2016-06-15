from collections import Counter
import string, re

with open('faculty.csv') as f:
  degrees = list()
  titles = list()
  email = list()
  lastnames = list()
  f.readline()

  for line in f:
    data = line.strip().split(',')
    d = data[1].strip().split()
    d = [s.translate(string.maketrans('',''), string.punctuation) for s in d]
    degrees.extend(d)
    
    t = data[2].strip()
    t = re.search(r'.*Professor', t).group()
    titles.append(t)

    e = data[3].strip()
    email.append(e)
    
    domains = {re.search(r'(.*)@(.*)',s).group(2) for s in email}

    d = data[0].strip().split()
    lastnames.append(d[len(d)-1])

if __name__ == '__main__':
  print Counter(degrees)
  print Counter(titles)
  # print email
  print domains
  print lastnames
