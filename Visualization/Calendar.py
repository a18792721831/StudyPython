from pyecharts.charts import Calendar
import pyecharts.options as opts
from datetime import date
from random import randint
import datetime

begin = date(2019, 1, 1)
end = date(2019, 12, 24)
data = [
    [str(begin + datetime.timedelta(days=i)), randint(0, 10000)]
    for i in range((end - begin).days)
]

# 1号，2号，3号

cal = Calendar(init_opts=opts.InitOpts(page_title='test_page'))
cal.add(series_name='', yaxis_data=data,
        calendar_opts=opts.CalendarOpts( range_=[begin, end]))
cal.set_global_opts(title_opts=opts.TitleOpts(title='test2one'), toolbox_opts=opts.ToolboxOpts(),
                    visualmap_opts=opts.VisualMapOpts(
                        max_=10000,
                        min_=0,
                        is_piecewise=True
                    ))
cal.render('./Calendar.html')