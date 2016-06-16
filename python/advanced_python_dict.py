from collections import defaultdict
import re

with open('faculty.csv') as f:
  faculty_dict = defaultdict(list)
  professor_dict = defaultdict(list)
  f.readline()

  for line in f:
    data = line.strip().split(',')
    
    firstname = data[0].split()[0]
    lastname = data[0].split()[-1]
    degree = data[1].split()[-1]
    title = re.search(r'.*Professor', data[2]).group()
    email = data[3]
    
    faculty_dict[lastname].append([degree, title, email])
    professor_dict[(firstname, lastname)].extend([degree, title, email])

result = sorted([(i,a) for i,a in professor_dict.items()], key=lambda x: x[0][1])

for i in result:
  print i
#print faculty_dict.items()[:3]
#print professor_dict.items()[:3]
