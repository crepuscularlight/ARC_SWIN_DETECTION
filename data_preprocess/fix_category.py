import json
import argparse
import copy

parser=argparse.ArgumentParser()
parser.add_argument('--input',required=True)
parser.add_argument('--source',required=True)

args=parser.parse_args()


input_file=args.input
source_file=args.source
output_file='fixed_annotations.json'

with open(input_file,'r') as f:
    input_dataset=json.loads(f.read())
with open(source_file,'r') as f:
    source_dataset=json.loads(f.read())
input_cat=input_dataset['categories']
source_cat=source_dataset['categories']

output_dataset=copy.deepcopy(input_dataset)
output_dataset['categories']=source_cat
mapping={}
for old_cat in input_cat:
    for new_cat in source_cat:
        if old_cat['name']==new_cat['name']:
            mapping[old_cat['id']]=new_cat['id']


for item in output_dataset['annotations']:

    item['category_id']=mapping[item['category_id']]


with open(output_file,'w+') as f:
    f.write(json.dumps(output_dataset))