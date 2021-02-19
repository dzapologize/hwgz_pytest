#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME :hwgz_pytest 
# @FileName  :test_One.py
# @Time      :2021/2/5 15:51
# @Author    :adiao
import pytest

# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

@pytest.mark.parametrize("a,b",[(10,20),(10,40)])
def test_param(self,a,b):
    print(a + b)