"""
@File  :utils.py
@Author:Sapphire
@Date  :2021/5/30 3:00
@Desc  :
"""
import uuid


def gen_id_by_uuid():
    """通过uuid生成id的通用方法"""
    return str(uuid.uuid4())