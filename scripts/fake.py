# _*_ coding:utf-8 _*_
import os
import pathlib
import random
import sys
from datetime import timedelta
import django
import faker
from django.utils import timezone
from loguru import logger

back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
BASE_DIR1 = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


fake = faker.Factory().create('zh_CN')

for i in range(5):
    logger.info(f'电话:{i}--{fake.phone_number()}')
    logger.info(f'姓名：{i}--{fake.name()}')
    logger.info(fake.address())
    logger.info(fake.country())
    logger.info(fake.city_name())
    logger.info(fake.license_plate())
    logger.info(fake.paragraphs(10))



