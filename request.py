from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import func, and_, or_
from flask import  Flask
app = Flask(__name__)

#Flask-SQLAlchemy 中存在的配置值
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/User?charset=utf8mb4'

# SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'submit_info'
    requestID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.INT, unique=False)
    stu_id = db.Column(db.String(45), unique=True)
    requestNum = db.Column(db.INT)
    gender = db.Column(db.INT)
    dormitory = db.Column(db.INT )
    priority = db.Column(db.INT)
    stu01_id = db.Column(db.String(45))
    stu02_id = db.Column(db.String(45))
    stu03_id = db.Column(db.String(45))
    result = db.Column(db.INT)
    time = db.Column(db.DateTime(timezone=True), server_default=func.now(), comment='创建时间')
    remainNum = db.Column(db.INT)
db.create_all() #创建表
#添加数据
r1 = User(status = '1', stu_id='1800022701', requestNum=2, gender= 0, dormitory='13', priority='13', stu01_id='1800022723', result='1', remainNum=15)
r2 = User(status = '1', stu_id='1800022720', requestNum=1, gender= 1, dormitory='5', result='1', remainNum=15)
r3 = User(status = '1', stu_id='1800022715', requestNum=2, gender= 0, dormitory='5', priority='13', stu01_id='1800022802', result='1', remainNum=20)
r4 = User(status = '1', stu_id='1800022760', requestNum=3, gender= 1, dormitory='13', priority='13', stu01_id='1800022803', stu02_id='1800022770', result='1', remainNum=10)
r5 = User(status = '1', stu_id='1800022727', requestNum=2, gender=0, dormitory='13', priority='13', stu01_id='1800022804', result='1', remainNum=15)
r6 = User(status = '1', stu_id='1800022779', requestNum=3, gender=1, dormitory='8', priority='13', stu01_id='1800022805', stu02_id='1800022772', result='1', remainNum=16)
r7 = User(status = '1', stu_id='1800022767', requestNum=3, gender=1, dormitory='8', priority='13', stu01_id='1800022806', stu02_id='1800022774', result='1', remainNum=15)
r8 = User(status = '1', stu_id='1800022730', requestNum=2, gender=1, dormitory='13', priority='13', stu01_id='1800022809', result='1', remainNum=15)
r9 = User(status = '1', stu_id='1800022733', requestNum=2, gender=0, dormitory='14', priority='14', stu01_id='1800022810', result='1', remainNum=18)
r10 = User(status = '1', stu_id='1800022737', requestNum=4, gender=0, dormitory='13', priority='13', stu01_id='1800022811', stu02_id='1800022776', stu03_id='1800022781', result='1', remainNum=9)
r11 = User(status = '1', stu_id='1800022789', requestNum=2, gender=1, dormitory='5', priority='13', stu01_id='1800022815', result='1', remainNum=13)
r12 = User(status = '1', stu_id='1800022777', requestNum=2, gender=1, dormitory='10', priority='13', stu01_id='1800022816', result='1', remainNum=20)
r13 = User(status = '1', stu_id='1800022791', requestNum=2, gender=1, dormitory='9', priority='13', stu01_id='1800022817', result='1', remainNum=12)
r14 = User(status = '1', stu_id='1800022812', requestNum=4, gender=1, dormitory='9', priority='5', stu01_id='1800022818', stu02_id='1800022782', stu03_id='1800022785', result='1', remainNum=6)
r15 = User(status = '1', stu_id='1800022799', requestNum=2, gender=1, dormitory='13', priority='13', stu01_id='1800022819', result='1', remainNum=14)
r16 = User(status = '1', stu_id='1800022744', requestNum=2, gender=1, dormitory='10', priority='13', stu01_id='1800022820', result='1', remainNum=19)
r17 = User(status = '1', stu_id='1800022756', requestNum=2, gender=0, dormitory='13', priority='13', stu01_id='1800022825', result='1', remainNum=14)
r18 = User(status = '1', stu_id='1800022731', requestNum=1, gender= 0, dormitory='5', result='1', remainNum=20)
r19 = User(status = '1', stu_id='1800022734', requestNum=1, gender= 1, dormitory='5', result='1', remainNum=14)
r20 = User(status = '1', stu_id='1800022830', requestNum=1, gender= 1, dormitory='5', result='1', remainNum=13)
r21 = User(status = '1', stu_id='1800022833', requestNum=1, gender= 1, dormitory='8', result='1', remainNum=30)
r22 = User(status = '1', stu_id='1800022835', requestNum=1, gender= 1, dormitory='9', result='1', remainNum=21)
r23 = User(status = '1', stu_id='1800022840', requestNum=1, gender= 0, dormitory='5', result='1', remainNum=19)
r24 = User(status = '1', stu_id='1800022841', requestNum=1, gender= 0, dormitory='13', result='1', remainNum=15)
r25 = User(status = '1', stu_id='1800022787', requestNum=3, gender=0, dormitory='5', priority='13', stu01_id='1810122120', stu02_id='1810122121', result='1', remainNum=13)
r26 = User(status = '1', stu_id='1800022850', requestNum=3, gender=0, dormitory='5', priority='13', stu01_id='1810122125', stu02_id='1810122126', result='1', remainNum=13)
r27 = User(status = '1', stu_id='1800022802', requestNum=4, gender=0, dormitory='5', priority='13', stu01_id='1810122127', stu02_id='1810122128', stu03_id='1810122129', result='1', remainNum=9)
r28 = User(status = '1', stu_id='1800022815', requestNum=3, gender=1, dormitory='5', priority='8', stu01_id='1810122200', stu02_id='1810122201', result='1', remainNum=12)
r29 = User(status = '1', stu_id='1810122202', requestNum=2, gender=1, dormitory='8', priority='13', stu01_id='1810122203', result='1', remainNum=14)
r30 = User(status = '1', stu_id='1810122225', requestNum=1, gender= 1, dormitory='13', result='1', remainNum=21)


#删除表
# db.drop_all()
db.session.add_all([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30])

#

# list = [36][4]
# j = 0
# dom_number = [5,8,9,10,13,14]
# gender = [0,1]
# gender_names = ['女', '男']
# # while j< list.len:
# for dom_num in dom_number:
#     if dom_num == 5 | dom_num == 13:
#         for gen in gender:
#             for i in range(1,5):
#                 res = User.query.filter(and_(User.dormitory.like(dom_num),
#                                     User.gender.like(gen),
#                                     User.requestNum.like(i))).count()
#             print("选%s号楼%s生的%s个床位的请求个数为%s" % (dom_num, gender_names[gen], i, res))
#     elif dom_num == 14 :
#         for i in range(1, 5):
#             res = User.query.filter(and_(User.dormitory.like(dom_num),
#                                     User.gender.like(0),
#                                     User.requestNum.like(i))).count()
#             print("选%s号楼%s生的%s个床位的请求个数为%s" % (dom_num, gender_names[0], i, res))
#     else:
#         for i in range(1,5):
#             res = User.query.filter(and_(User.dormitory.like(dom_num),
#                                     User.gender.like(1),
#                                     User.requestNum.like(i))).count()
#             print("选%s号楼%s生的%s个床位的请求个数为%s" % (dom_num, gender_names[1], i, res))
#
#                 # list[j][0] = dom_num
#                 # list[j][1] = gen
#                 # list[j][2] = i
#                 # list[j][3] = res
#                 # j = j+ 1

    #         print("选%s号楼%s生的%s个床位的请求个数为%s" % (dom_num, gender_names[gen], i, res))
    #     print('\n')
    # print('\n')
#输出二维数组list
# for i in range(0, len(list)):
#     print(i, list[i])

# print(i)
# j = User.query.filter_by(dormitory='5').count()
# print(j)

db.session.commit()
db.session.close()