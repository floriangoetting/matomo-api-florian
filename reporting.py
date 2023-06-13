import json
import os
from piwikapi.analytics import PiwikAnalytics
import plotly.graph_objects as go
import pandas as pd

authToken = "APITOKEN"

pa = PiwikAnalytics()
pa.set_api_url("APIURL")
pa.set_id_site(1) # 1 is the side ID you want to log to
pa.set_format('json')
pa.set_filter_limit(-1)
pa.set_period('range')
pa.set_date('previous30')
pa.set_method('Actions.getPageUrls')

#pa.set_parameter('apiModule', 'PagePerformance')
#pa.set_parameter('apiAction', 'get')

pa.set_parameter('token_auth', authToken)

print(pa.get_query_string()) #print query string to console

apiResponseDict = json.loads(pa.send_request());
print(apiResponseDict)

df = pd.DataFrame.from_dict(data = apiResponseDict)
print(df.head())