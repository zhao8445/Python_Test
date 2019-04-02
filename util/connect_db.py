import pymysql as pm

class OperationMysql:
	def __init__(self):
		self.conn = pm.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='443215211',
			db='test',
			charset='utf8',
            cursorclass=pm.cursors.DictCursor
			)
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		#result = json.dumps(result)
		return result

if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_one("select * from d1;")
	print(res)
