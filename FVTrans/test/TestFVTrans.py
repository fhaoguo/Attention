# -*- coding: utf-8 -*-
# @Author     :fenghaoguo
# @Time       :2022/5/18 13:49
# @FileName   :TestFVTrans.py
# @Description:

import unittest
import torch
from ..modules.transformer import Transformer


class TestFVTrans(unittest.TestCase):

    def test_transformer(self):
        transformer_model = Transformer(nhead=16, num_encoder_layers=12)
        src = torch.rand((10, 32, 512))
        tgt = torch.rand((20, 32, 512))
        out = transformer_model(src, tgt)
        print(out.shape)
