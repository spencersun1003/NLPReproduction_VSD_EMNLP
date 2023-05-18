output=snap/sp/baseline
#--load snap/pretrain/VLBart/Epoch30 \
PYTHONPATH=$PYTHONPATH:./src \
python -m torch.distributed.launch \
    --nproc_per_node=$1 \
    VLModel/src/vrd_caption.py \
        --distributed --multiGPU \
        --evaluate_only \
        --train train \
        --valid val \
        --test test \
        --optim adamw \
        --warmup_ratio 0.1 \
        --clip_grad_norm 5 \
        --lr 4e-5 \
        --epochs 12 \
        --num_workers 4 \
        --backbone 'facebook/bart-base' \
        --output $output ${@:2} \
        --load snap/sp/e2efull/BEST \
        --num_beams 5 \
        --batch_size 80 \
        --valid_batch_size 100 \
