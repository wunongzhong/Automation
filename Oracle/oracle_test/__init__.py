#coding=utf-8
import cx_Oracle as cx
#数据库信息
new_oracle = ''
old_oracle = ''
#连接数据库
class DB1():
    def __init__(self):
        self.conn_new = cx.connect(new_oracle)
    def __enter__(self):
        return self.conn_new.cursor()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn_new.rollback()
        else:
            self.conn_new.commit()
    def close(self):
        if self.conn_new:
            self.conn_new.close()
class DB2():
    def __init__(self):
        self.conn_old = cx.connect(old_oracle)
    def __enter__(self):
        return self.conn_old.cursor()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn_old.rollback()
        else:
            self.conn_old.commit()
    def close(self):
        if self.conn_old:
            self.conn_old.close()

#设置基础查询
class BaseOracle():
    def __init__(self):
        self.db1 = DB1
        self.db2 = DB2
    #查询新旧表结构，返回列表
    def find_estrutura(self,table):
        new_list = []
        old_list = []
        sql = "select column_name from user_tab_columns where table_name = '{}'".format(table)
        with self.db1 as c1:
            c1.execute(sql)
            result1 = c1.fetchall()
            for i in result1:
                new_list.append(i[0])
        with self.db2 as c2:
            c2.execute(sql)
            result2 = c1.fetchall()
            for j in result2:
                old_list.append(j[0])
        return new_list,old_list
    #查询数据总数
    def find_total(self,table):
        sql = "select count(*) from {}".format(table)
        with self.db1 as c1:
            c1.execute(sql)
            result1 = c1.fetchall()
        with self.db2 as c2:
            c2.execute(sql)
            result2 = c2.fetchall()
        return result1[0][0],result2[0][0]
    #查询旧库中数据，逐一查询
    def find_dados(self,table,num):
        sql = "select a1.* from (select {}.*,rownum rn from {})a1 where rn between {} and {}".format(table,table,num+1,num+1)
        with self.db2 as c2:
            c2.execute(sql)
            desc = [d[0] for d in c2.description]
            result = [dict(zip(desc,line)) for line in c2]
        return desc[0],result
    #根据find_dados返回结果重组后查询新表
    def find_demo(self,table,data):
        sql = "select * from {} where {}".format(table,data)
        with self.db1 as c1:
            c1.execute(sql)
            if c1.fetchall():
                return True
            else:
                return False


#思考：v3.0版本，往数据存储方向

