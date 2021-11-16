import pandas as pd
import pymysql
import time
import threading
import math
from tqdm import tqdm
def run():
	"""这里是f2函数"""
	for i in range(100):
		print('f4',i)
		time.sleep(1)
# host_m1 = '10.10.8.52'
# port_m1 = 30007
# user_m1 = 'find_lonlat'
# password_m1 = 'Passw0rd_jobprodreport826'
# db_m1 = 'SENSOR1'

# conn_1 = pymysql.connect(host=host_m1, port=port_m1, user=user_m1, passwd=password_m1, db=db_m1)
# cursor1 = conn_1.cursor()

# QUERY_SQL = '''SELECT BLOCK_ID,STAND_GRIDID FROM T_DICT_BLOCK_BASIC_INFO_{PRI_ID} WHERE LONGITUDE_UP_LEFT<{LON} AND  LATITUDE_UP_LEFT>{LAT} AND LONGITUDE_UP_RIGHT>{LON} AND LATITUDE_DOWN_RIGHT<{LAT} '''
# NEW_QUERY = QUERY_SQL.format(PRI_ID=str(int(PRI_ID)), LON=LON, LAT=LAT)
# print(NEW_QUERY)
# cursor1.execute(NEW_QUERY)
# STAND_GRIDID = cursor1.fetchall()
# print(STAND_GRIDID)
# if len(STAND_GRIDID) == 0:
#     pass


