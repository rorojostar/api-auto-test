import pymysql


class DBUtils:
    count = -1

    def __init__(self):
        try:
            self.conn = pymysql.connect(host="60.204.225.104",
                                        port=3306,
                                        user="root",
                                        password="beimeng2024",
                                        db="wms")
            self.cursor = self.conn.cursor()
            print("数据库连接成功!")
        except Exception as error:
            print("数据库连接失败，请查看工具类的init方法是否异常！")
            raise error

    # 封装关闭连接对象跟游标对象
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 查询单条数据
    def find_one(self, sql, params=None):
        # 先执行commit，避免数据库上次操作未提交导致当前方法报错
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)
            elif params is not None:
                self.cursor.execute(sql, params)
            return self.cursor.fetchone()  # 从结果集获取一条数据
        except Exception as e:
            print("查询单条数据失败", e)

    # 查询所有数据
    def find_all(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)
            elif params is not None:
                self.cursor.execute(sql, params)
            return self.cursor.fetchall()  # 从结果集获取所有数据
        except Exception as e:
            print("查询所有数据失败", e)

    # 查询结果集的条目数
    def find_count(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, params)

            self.count = self.cursor.rowcount
            return self.count
        except Exception as e:
            print("查询条目数", e)

    # 封装增删改方法
    def cud(self, sql, params=None):
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            if isinstance(params, tuple):
                self.count = self.cursor.execute(sql, params)
            if isinstance(params, list):
                self.count = self.cursor.executemany(sql, params)
            self.conn.commit()
            return self.count
        except Exception as e:
            print("增删改操作失败！", e)
