# Cleaning Output json cleaning"""
import json
with open('output.json') as data_file:
  parsed=json.load(data_file)
with open ('output.json', 'w') as data_file:
  json.dump(parsed, data_file, indent=4)
