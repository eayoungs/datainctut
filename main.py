from flask import Flask,render_template,request
import requests
from bokeh.plotting import figure
from bokeh.embed import components


api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session.get(api_url)

plot = figure(tools=TOOLS
              title="Data from Quandl WIKI set",
              x_axis_label='date',
              y_axis_type='datetime')

script, div = components(plot)
return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
    app.run(port=33507)
