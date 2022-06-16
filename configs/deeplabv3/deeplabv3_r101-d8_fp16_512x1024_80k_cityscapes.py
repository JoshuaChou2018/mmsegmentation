_base_ = './deeplabv3_r101-d8_512x1024_80k_cityscapes.py'
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0005)
optim_wrapper = dict(
    _delete_=True,
    type='AmpOptimWrapper',
    optimizer=optimizer,
    loss_scale=512.)
