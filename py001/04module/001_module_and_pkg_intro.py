#!/usr/bin/env python

#===================1. 认识python中的模块============================
# 在python中，一个.py文件就称为一个模块module

# 为了防止模块名称重复，引入了包package的概念，如果：
# mycompany
# |-__init__.py   # 每个包package下，必须有这个文件，否则python会把mycompany当成普通目录
# |-abc.py
# |-xyz.py

# 引入了myconmany包之后，现在abc.py的模块名称就变成了mycompany.abc了，防止了和其他模块的重复

# 注意：包下的__init__.py本身也是一个模块，也可以写python代码，其模块名等于包名mycompany


