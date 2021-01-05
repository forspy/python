#在matplotlib的基础上，可以尝试pyechart---属于python的可视化UI#

#pip install pyecharts
#若下载失败可以使用清华镜像
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts

#导入柱状图-Bar

# from pyecharts.charts import Bar
# #设置行名
# columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# #设置数据
# data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# #设置柱状图的主标题与副标题
# bar = Bar("柱状图","一年的降水量与蒸发量")
# #添加柱状图的数据及配置项
# bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
# bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
# #生成本地文件（默认为.html文件）
# bar.render()
qqqqqww

from pyecharts.charts import Bar
from pyecharts import options as opts

# V1 版本开始支持链式调用
bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render()

# 不习惯链式调用的开发者依旧可以单独调用方法
bar = Bar()
bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
bar.render()


# from snapshot_selenium import snapshot as driver
#
# from pyecharts import options as opts
# from pyecharts.charts import Bar
# from pyecharts.render import make_snapshot
#
#
# def bar_chart() -> Bar:
#     c = (
#         Bar()
#         .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
#         .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
#         .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#         .reversal_axis()
#         .set_series_opts(label_opts=opts.LabelOpts(position="right"))
#         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
#     )
#     return c
#
# # 需要安装 snapshot-selenium 或者 snapshot-phantomjs
# make_snapshot(driver, bar_chart().render(), "bar.png")