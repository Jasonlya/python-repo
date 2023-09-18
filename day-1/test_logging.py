# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/18 23:33
@Auth ： liangya
@File ：test_logging.py
"""
import logging
"""
    logging模块采用了模块化设计，主要包含四种组件：
    Loggers：记录器，提供应用程序代码能直接使用的接口；
    Handlers：处理器，将记录器产生的日志发送至目的地；
    Filters：过滤器，提供更好的粒度控制，决定哪些日志会被输出；
    Formatters：格式化器，设置日志内容的组成结构和消息字段；
"""

# logging.debug("debug log")
# logging.info("debug log")
# logging.warning("debug log")
# logging.critical("debug log")

#记录器 'cn.cccb.log' 关联过滤器使用
logger = logging.getLogger('cn.cccb.log')
logger.setLevel(logging.INFO)
# print(logger)
# print(type(logger))

#处理器
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

#没有给handler指定日志级别，将使用logger的级别
fileHandler = logging.FileHandler(filename='addDemo.log')

#formatter格式
formatter = logging.Formatter("%(asctime)s - %(filename)s:%(lineno)s | %(levelname)s - %(message)s")
# formatter1 = logging.Formatter("%(asctime)s|%(levelname)8s|%(filename)10s%lineno)s|%(message)s")

#给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

#记录器要设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

#定义一个过滤器
flt = logging.Filter("1cn.cccb")

#关联过滤器
# logger.addFilter(flt)
consoleHandler.addFilter(flt)
# fileHandler.addFilter(flt)

#打印日志的代码
logger.debug("debug log")
logger.info("info log")
logger.warning("warning log")
logger.error("error log")
logger.critical("critical log")
