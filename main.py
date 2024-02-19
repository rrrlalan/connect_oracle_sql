import cx_Oracle
import yagmail


# My_Query = "SELECT * FROM HELP"


# def oracle_db_conn(m_q):
#     """Will accept query and return result"""
#     USER_NAME = "system"
#     PASSWORD = "lalan"
#     HOST_NAME = "localhost"
#     PORT = "1521"
#     SID = "xe"
#     DSN = f"{HOST_NAME}:{PORT}/{SID}"
#     My_Query = m_q
#     try:
#         con = cx_Oracle.connect(user=USER_NAME, password=PASSWORD, dsn=DSN, encoding="UTF-8")
#         cur = con.cursor()
#         cur.execute(My_Query)
#         return cur.fetchall()
#     # To raise the error if any database connection error happen
#     except cx_Oracle.DatabaseError as e:
#         return ("Error :", e)
#     # To close The Current Connection
#     finally:
#         if cur:
#             cur.close()
#         if con:
#             con.close()
# # print(oracle_db_conn("SELECT * FROM HELP"))
USER_NAME = "jhar.lalan@gmail.com"
AAP_CODE = "pkoghinhkjixuajy"
to = ["rrrlalan@gmail.com", "kr.lalanhzb@gmail.com"]
subject = "Mail through Pycharm"
content = "Write your content here. Have a good day!"
with yagmail.SMTP(USER_NAME, AAP_CODE) as yag:
    yag.send(to, subject, content)



















