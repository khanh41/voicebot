import pandas as pd 
import os
import csv

path = './data/CV'
for i in os.listdir(path):
  if i[-4:] == '.tsv':
    tsv_file = path + '/' + i
    csv_table=pd.read_table(tsv_file,sep='\t')
    csv_table.to_csv(tsv_file[:-3] + 'csv',index=False)

sentence = ''
for i in os.listdir(path):
  if i[-4:] == '.csv':
    with open('./data/CV/'+i, newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        sentence += row['sentence'].lower()

str_write = ''
for i in set(sentence):
  str_write += i + '\n'

with open('./data/alphabet.txt','w',encoding='utf-8') as f:
  f.write(str_write.lower())