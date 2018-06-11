import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyodbc
driver= '{SQL Server Native Client 13.0}'

conn = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 13 for SQL Server}',
    Server='ociodw1-qa,6739',
    Database='ETL_ADMIN'
)

"""
#--READ DATABASE
cursor = conn.cursor()

#cursor.execute('SELECT * FROM ETL_BATCH_LOG WHERE JOB_NM=?', 'USP_IC_CSP_COMPUTER')
#row = cursor.fetchone()
#while row:
#    print("LOAD_JOB_NR=%d, JOB_NM=%s" % (row[0], row[2]))
#    row = cursor.fetchone()

#cursor.execute('select * into dbo.[TRE_JOB_TABLE_BKP] from dbo.[TRE_JOB_TABLE]')	
#cursor.commit()	#modify data need commit 

#Table_type=input('please input table type: ')
#cursor.execute("insert into dbo.[TRE_JOB_TABLE_BKP] values(151,303,\'test\',?,GETDATE())",Table_type)	
#cursor.commit()	#modify data need commit 

conn.close()
"""

"""
#--EXTRACT DATA FROM DB
Table_type='Source'
df=pd.read_sql(('''SELECT *
					FROM dbo.[TRE_JOB_TABLE_BKP]
					where TABLE_TYPE=?'''),con=conn,params={Table_type})
print(df.JOB_ID)					
"""

