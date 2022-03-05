import json
import argparse
import copy

parser=argparse.ArgumentParser()
parser.add_argument("--input")
parser.add_argument("--original")
parser.add_argument("--new")
args=parser.parse_args()

input_file=args.input
original_dir=args.original
new_dir=args.new

with open(input_file,'r') as f:
    input_dataset=json.loads(f.read())

output_dataset=copy.deepcopy(input_dataset)
images=output_dataset['images']
for image in images:
    image['file_name']=image['file_name'].replace(original_dir,new_dir)

output_file='annotations_renamed.json'
with open(output_file,'w+') as f:
    f.write(json.dumps(output_dataset))