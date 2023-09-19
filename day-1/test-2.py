# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/19 23:03
@Auth ： liangya
@File ：test-2.py
"""
import logging
import logging.config

#配置文件的方式来处理日志
#记录器

logging.config.fileConfig('logging.conf',encoding='UTF-8')

logger = logging.getLogger('applog')



#打印日志的代码
logger.debug("debug log")
logger.info("info log")
logger.warning("warning log")
logger.error("error log")
logger.critical("critical log")