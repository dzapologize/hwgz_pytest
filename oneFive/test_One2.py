#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME :hwgz_pytest 
# @FileName  :test_One2.py
# @Time      :2021/2/5 15:51
# @Author    :adiao
import pytest

@pytest.mark.run(order = 2)
def test_foo():
    print("test_foo")
    # assert True

@pytest.mark.run(order = 1)
def test_bar():
    print("test_bar")
    # assert True
