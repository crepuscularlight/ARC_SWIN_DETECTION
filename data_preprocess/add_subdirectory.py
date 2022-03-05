import json
import argparse
import copy

parser=argparse.ArgumentParser()
parser.add_argument('--input',required=True)
parser.add_argument('--name',required=True)
args=parser.parse_args()

input_file=args.input
sub_dir=args.name

with open(input_file,'r') as f:
    input_dataset=json.loads(f.read())


output_dataset=copy.deepcopy(input_dataset)
images=output_dataset['images']
for image in images:
    image['file_name']=sub_dir+'/'+image['file_name']

output_file='trashcan_renamed.json'
with open(output_file,'w+') as f:
    f.write(json.dumps(output_dataset))


