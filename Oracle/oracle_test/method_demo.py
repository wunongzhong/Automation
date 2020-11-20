#coding=utf-8
from oracle_test import BaseOracle
from oracle_test.log_demo import log
db = BaseOracle()
log = log()

def find_jiegou(table):
    a,b = db.find_estrutura(table)
    if set(a)^set(b):
        log.info('{}数据结构异常：{}'.format(table,set(a)^set(b)))
    else:
        log.debug('{}数据结构正常'.format(table))
    return b

def find_total(table):
    a,b = db.find_total(table)
    log.info('{}表，旧库:新库 {}:{}'.format(table,b,a))
    return int(b)

def find_shuju(table):
    find_jiegou(table)
    num = find_total(table)
    for i in range(num):
        xianshi,shuju = db.find_dados(table,i)
        shuju[0].pop('RN')
        tiaojian = ' and '.join("%s = '%s'"%(key,value) for key,value in shuju[0].items() if value)
        result = db.find_demo(table,tiaojian)
        if result:
            log.debug('旧数据{}在新数据库比对成功'.format(shuju[0][xianshi]))
        else:
            log.info('select * from {} where {}'.format(table,tiaojian))