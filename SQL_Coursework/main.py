import pymysql
import data
import tel
import random

user_num = 100
shop_num = 50
product_num = 100
order_num = 200
logistics_num = order_num
# 打开数据库连接
try:
    db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, database="course_work")
    print('连接成功！')
except:
    print('something wrong!')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
# 使用预处理语句创建表
'''--USER-- '''
for i in range(user_num):
    sql = """INSERT INTO user(u_id,u_name,u_tel,u_address)
             VALUES ({},{}{}{},{}{}{},{}{}{});"""
    # cursor.executemany(sql,input_name)
    # print(sql.format(i,
    #                  "\'", data.get_name(i), "\'",
    #                  "\'", tel.get_tel(i), "\'",
    #                  "\'", data.get_address(), "\'",
    #                  ))
    cursor.execute(sql.format(i,
                              "\'", data.get_u_name(i), "\'",
                              "\'", tel.get_tel(i), "\'",
                              "\'", data.get_address(), "\'",
                              ))
    # if i % (number_of_row/1000) == 0:
    #     print(i/number_of_row)

'''---SHOP---'''

for i in range(shop_num):
    sql = """INSERT INTO shop(s_id,s_name,s_tel,s_category)
             VALUES ({},{}{}{},{}{}{},{}{}{});"""
    # cursor.executemany(sql,input_name)
    # print(sql.format(i,
    #                  "\'", data.get_s_name(i), "\'",
    #                  "\'", tel.get_tel(i), "\'",
    #                  "\'", data.get_s_category(), "\'",
    #                  ))
    cursor.execute(sql.format(i,
                              "\'", data.get_s_name(i), "\'",
                              "\'", tel.get_tel(i), "\'",
                              "\'", data.get_s_category(), "\'",
                              ))

'''---PRODUCT---'''
# 使用预处理语句创建表
for i in range(product_num):
    sql = """INSERT INTO product(p_id,p_name,p_category,price,imageURL,shop_s_id)
                 VALUES ({},{}{}{},{}{}{},{}{}{},{}{}{},{}{}{});"""
    # cursor.executemany(sql,input_name)
    # print(sql.format(i,
    #                  "\'", data.get_s_name(i), "\'",
    #                  "\'", tel.get_tel(i), "\'",
    #                  "\'", data.get_s_category(), "\'",
    #                  ))
    # print(i)
    cursor.execute(sql.format(i,
                              "\'", data.get_p_name(i), "\'",
                              "\'", data.get_p_category(i), "\'",
                              "\'", random.randint(0, 10000), "\'",
                              "\'", data.get_p_url(), "\'",
                              "\'", random.randint(0, shop_num-1), "\'",
                              ))
'''---order--'''
for i in range(order_num):
    sql = """INSERT INTO order(o_id,o_time,total_price,u_id,s_id,l_id)
                 VALUES ({},{}{}{},{}{}{},{}{}{},{}{}{},{}{}{});"""
    # cursor.executemany(sql,input_name)
    # print(sql.format(i,
    #                  "\'", data.get_s_name(i), "\'",
    #                  "\'", tel.get_tel(i), "\'",
    #                  "\'", data.get_s_category(), "\'",
    #                  ))
    # print(i)
    cursor.execute(sql.format(i,
                              "\'", data.get_l_time(), "\'",
                              "\'", data.get_p_category(i), "\'",
                              "\'", random.randint(0, 10000), "\'",
                              "\'", data.get_p_url(), "\'",
                              "\'", random.randint(0, shop_num-1), "\'",
                              ))

'''--order item---'''

'''---logistic--'''
for i in range(logistics_num):
    sql = """INSERT INTO logisticsinfo(l_id,inc,l_state,expect_date,from,to)
                 VALUES ({},{}{}{},{}{}{},{}{}{},{}{}{},{}{}{});"""
    # cursor.executemany(sql,input_name)
    print(sql.format(i,
                              "\'", data.get_l_inc(), "\'",
                              "\'", data.get_l_state(), "\'",
                              "\'", data.get_l_time(), "\'",
                              "\'", data.get_address(), "\'",
                              "\'", data.get_address(), "\'",
                              ))
    print(i)
    cursor.execute(sql.format(i,
                              "\'", data.get_l_inc(), "\'",
                              "\'", data.get_l_state(), "\'",
                              "\'", data.get_l_time(), "\'",
                              "\'", data.get_address(), "\'",
                              "\'", data.get_address(), "\'",
                              ))

db.commit()
# cursor.execute(sql)
# print(cursor.fetchall())
print('成功！')

# 关闭数据库连接
db.close()
