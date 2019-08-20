from config import DB
import pymysql
from flask import Flask
import json
app = Flask(__name__,static_folder='templates')

#1、创建连接
conn = pymysql.connect(
    host = DB.host,
    user = DB.user,
    passwd = DB.passwd,
    port = DB.port,
    db = DB.dbname,
    cursorclass = pymysql.cursors.DictCursor #字典形式
    )
cur = conn.cursor()


@app.route("/",methods=["GET"])
def index():
    return app.send_static_file('welcome.html')

@app.route("/getinfo", methods=["GET"])
def getinfo():
    sql1 = "select gender, domiroryInfo.buildingNo ,emptyBedNum, count(*)allRemainNum " \
          "from User.roomInfo join User.domiroryInfo " \
          "on roomInfo.buildingNo = domiroryInfo.id " \
          "where emptyBedNum != 0 " \
          "group by roomInfo.gender, domiroryInfo.buildingNo,roomInfo.emptyBedNum " \
          "order by roomInfo.gender desc, domiroryInfo.buildingNo,roomInfo.emptyBedNum"
    cur.execute(sql1)
    result1 = cur.fetchall()
    print(result1)


    sql2 = "select gender, buildingNo, emptyBedNum, count(*) allRequestNum from User.submit_info " \
           "group by gender, buildingNo, emptyBedNum " \
          "order by gender desc, buildingNo,emptyBedNum;"
    cur.execute(sql2)
    result2 = cur.fetchall()
    print(result2)
    print('\n\n')

    # 把两个字典拼接起来，如果字典名一样，后面的就覆盖前面
    # result = dict(list(result2.items()) + list(result1.items()))
    res = []
    m = {'allRequestNum': 0}

    for i in result1:
        flag = False
        for j in result2:
            if i['gender'] == j['gender'] and i['buildingNo'] == j['buildingNo'] and i['emptyBedNum'] == j['emptyBedNum']:
                res.append(dict(i, **j))
                flag = True
                break
        if flag == False:
            res.append(dict(i, **m))


    print(res)
    buildings_dict = dict()
    # 生成字典
    for item in res:
        key = ("男" if (item["gender"]==1) else "女")+","+str(item["buildingNo"])
        if not key in buildings_dict:
            buildings_dict[key] = []
        buildings_dict[key].append({"sparebed":item["emptyBedNum"],"total":item["allRemainNum"],"applied":item["allRequestNum"]})

    # 遍历字典
    buildings_json = {"code":200, "data":[]}
    for key,value in buildings_dict.items():
        buildings_json["data"].append({"gender":key.split(",")[0],"building_no":key.split(",")[1],"detail":value})
    return json.dumps(buildings_json)
getinfo()

if __name__ == '__main__':
    app.run(port=8080, debug=True)



