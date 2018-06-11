#python view job run time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyodbc
driver= '{SQL Server Native Client 13.0}'

conn = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 13 for SQL Server}',
    Server='ociodw1,6739',
    Database='ETL_ADMIN'
)

#cursor = conn.cursor()

#uses %(name)s so use params={‘name’ : ‘value’} --\'USP_RZ_PEOPLE_D\'
#with params  
df=pd.read_sql(('''select right(cast(run_date as varchar(10)),2) as run_date,run_duration 
					from msdb.dbo.sysjobhistory
					where step_name=?
					and run_date > \'20180501\'
					order by run_date'''),con=conn,params={'USP_RZ_PEOPLE_D'})

x=list(df.run_date)
print(x)
y=list(df.run_duration)
print(y)
#Z=list(df.END_DT)	

##plt.plot(x,y,"r--")		
#plt.xlim('2018-02-11 21:27:05.050','2018-02-16 20:04:07.160')	
	
plt.xlabel("Date")
plt.ylabel("RUNTIME")
plt.title("Job RunTime")
plt.plot(x,y,marker='o',markersize=5)
#plt.plot(x,y, linewidth=3, color='r', marker='o',markerfacecolor='blue', markersize=20)

plt.show()
##print(type(x))



conn.close()

