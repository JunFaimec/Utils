# 前备知识
    1.  ./config 命名规则：{model}_[model setting]_{backbone}_{neck}_[norm setting]_[misc]_[gpu x batch_per_gpu]_{schedule}_{dataset}


# 自定义数据集
## 数据集实体
    1. 数据组织形式： data/coco/
                        ├── annotations/
                        │   ├── instances_train2017.json
                        │   ├── instances_val2017.json
                        │   └── instances_test2017.json
                        ├── train2017/
                        │   ├── img1.jpg
                        │   ├── img2.jpg
                        │   └── ...
                        ├── val2017/
                        │   ├── img1.jpg
                        │   ├── img2.jpg
                        │   └── ...
                        └── test2017/
                            ├── img1.jpg
                            ├── img2.jpg
                            └── ...
## 数据集配置与准备:
    ## data/custom -->  mmdet/datasets/custom.py(copy) --> mmdet/datasets/__init__.py --> config.py/_base_/datasets/custom_coco_detection.py(copy)-->   

    2. /mmdet/config == /config，所有config有的，改外层的/config就行，更全！
       注意：只有mmdet/datasets/是唯一的
    # 修改数据集类别信息 == classes.txt
    3. copy mmdet/datasets/coco.py to mmdet/datasets/custom.py
    4. 修改 METAINFO = {
                        'classes':
                        ('person', 'bicycle'),
                        'palette':  # palette is a list of color tuples, which is used for visualization.
                        [(220, 20, 60), (119, 11, 32)]
                    }
    5. 修改mmdet/datasets/__init__.py，注册custom.py自定义数据集  ：from .custom import CustomDataset
    # 
    6. 复制/config/_base_/datasets/detection/coco_detection.py，
       创建新的数据处理器，修改dataset_type 、data_root 、 ann_file 、 data_prefix
    7. 复制模型配置文件，修改num_classes


# bug修复记录
    1.  SSD模型验证报错
        Q： TypeError: SSDHead.__init__() got an unexpected keyword argument 'loss_cls'
        A： 修改 if getattr(self.loss_cls, 'custom_cls_channels', False):  -->   if getattr(self, 'loss_cls', None) and getattr(self.loss_cls, 'custom_cls_channels', False):
    2. 增加早停策略，mmengine已经实现了这个钩子，在default_hooks (configs/_base_/default_runtime.py) 中添加:
            early_stopping=dict(
                type="EarlyStoppingHook",
                monitor="coco/bbox_mAP",
                patience=10,
                min_delta=0.005),
    3. 
    
