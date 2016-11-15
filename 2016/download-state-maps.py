import os

raw = open('state-codes').readlines()
state_codes = [line.split()[-1] for line in raw]

for code in state_codes:
  json_link = "wget http://interactives.ap.org/interactives/2016/general-election/results/data/shapes/%s.json" % code
  print "Fetching", json_link
  os.system(json_link)
