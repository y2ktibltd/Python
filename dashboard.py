#!/usr/bin/env python3
#import modules for connecting to Oracle and building dashboards
import cx_Oracle, plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

#create Oracle BI read-only connection information
dsn=cx_Oracle.makedsn('10.117.9.146','1551',service_name='BIPRD01')
conn=cx_Oracle.connect(user='robertsm',password='changeme123',dsn=dsn)
c=conn.cursor()

#generate empty list of tuples
dock_data=[("",)*5] *21 

#open SQL query file
sql=open("sql.txt","r")
dock=c.execute(sql.read())

#insert data from SQL into positions inside list of tuples
#Generate internal dashboard data and empty lists for plotly bar plots
for row in dock:
    add_data=(row[0],row[1],row[2],row[3],row[4])
    dock_data.insert(row[0],add_data)
sql.close()
xdata=[]
ydata=[]
zdata=[]
for i in range (1,21):
    xdata.insert(i,("Door#"+str(i)+"    "+str(dock_data[i][1])+"    "+str(dock_data[i][2])))
    ydata.insert(i,(dock_data[i][4]),)
    zdata.insert(i,(dock_data[i][3]),)

#Draw dashboard in plotly
fig=go.Figure(data=[
    go.Bar(name="Loaded to Dock",x=xdata,y=ydata,marker_color="Green",text="Loaded",textposition='auto'),
    go.Bar(name="Not Loaded",x=xdata,y=zdata,marker_color="Red",text="Not Loaded",textposition='auto')
    ])
fig.update_layout(barmode="stack")
#fig.show()

app=dash.Dash()
app.layout=html.Div([
    dcc.Graph(figure=fig)
])
if __name__=='__main__':
    app.run_server(debug=False,host='127.0.0.1',port=8050)#True,use_reloader=False)
