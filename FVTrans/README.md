# Fast Visual Transformers (FVTrans)
出于研究Transformer目的，分析并调试PyTorch的Transformer模块，基于PyTorch官方Transformer源代码形成本项目。欢迎大家参考！


## 应用场景: 基于FVTrans的Word-level Language Modeling

测试命令
```bash
# Train a Transformer m2 on Wikitext-2.
python main.py --epochs 6 --model Transformer --lr 5   
# Train a Transformer m2 on Wikitext-2 with CUDA.
python main.py --cuda --epochs 6 --model Transformer --lr 5   

# Generate samples from the trained Transformer m2.
python generate.py --model Transformer
# Generate samples from the trained Transformer m2 with cuda.                  
python generate.py --cuda --model Transformer      
```

点击 [详情](./README_.md) 查看项目训练和测试详细说明。 

# 致谢
+ https://github.com/pytorch/pytorch
+ https://github.com/pytorch/examples/tree/master/word_language_model