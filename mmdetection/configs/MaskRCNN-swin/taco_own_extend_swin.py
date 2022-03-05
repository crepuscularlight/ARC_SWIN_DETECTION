#base config file
_base_='../swin/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco.py'

#declare self-customed dataset type
dataset_type='CocoDataset'

#images directory
prefix='./data/taco'

#classes list
classes=('Can', 'Carton/Paper', 'GlassBottle',
         'Other', 'PlasticBottle', 'PlasticOther', 'Wrapper')

# classes=('Can', 'Carton', 'Cup', 'GlassBottle',
#          'Other', 'Paper','PlasticBottle', 'PlasticContainer', 'Wrapper')

#test images directory
test_prefix=prefix

#model configuration
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=7),#change bbox and mask head numbers here.
        mask_head=dict(num_classes=7)))

# data setup
data=dict(
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file=[
            'data/week17_7classes/final_7classes.json',#train file path
        ],
        img_prefix=prefix
    ),

    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file=[
            'data/fix_carton_coco/fixed_annotations.json'#validate file path
        ],
        img_prefix=prefix
    ),

    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/week17_7classes/ann_4_ann_05_week17val.json',#test file path
        img_prefix=test_prefix
    )
)

#pretrained model
# load_from='week17_fix_carton/latest.pth'
