import pymysql
import xlwt

wb = xlwt.Workbook()
sh = wb.add_sheet('DailyReport')

try:
    conn = pymysql.connect(host="", user="", passwd="", db="",
                           port=, charset="")
    cur = conn.cursor()
    cur.execute("SELECT realname "
                "FROM user WHERE id='14'")
    data = cur.fetchone()
    sh.write(0, 0, "realname")
    sh.write(1, 0, data[0])
    wb.save('DailyReport.xls')
    cur.close()
    conn.close()

except Exception : print("发生异常")