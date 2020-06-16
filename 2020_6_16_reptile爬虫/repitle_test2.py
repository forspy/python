import urllib
import urllib.request
import re
#打开网页下载器
def open_html(url):
    require=urllib.request.Request(url)
    reponse=urllib.request.urlopen(require)
    html=reponse.read()
    return html
#这里的本质是html是一个文件在open_html（url）这个函数里存放了jpg的图片信息，使用正则表达式匹配到链接jpg链接之后
#再使用url图片的链接通过urllib.request模块请求得到数据
#存入文件当中就是图片信息了
#下载图片
def load_image(html):
    regx='https://[\S]*jpg'#正则匹配，注意https匹配还是http匹配
    pattern=re.compile(regx)
    get_image=re.findall(pattern,repr(html)) #得到一些列image链接

    num=1
    for img in get_image:
        photo=open_html(img)
        with open(r'E:\python code\repitle\img\%s.jpg'%num,'wb') as f:
            print('开始下载图片')
            f.write(photo)
            print('正在下载第%s张图片'%num)
            f.close()
        num=num+1
    if num>1:
        print('下载成功')
    else:
        print('下载失败')

url='https://m.gmw.cn/baijia/2020-06/12/1301283184.html'
html=open_html(url)
load_image(html)
from urllib.request import urlretrieve
urlretrieve('https://www.python.org/',r'E:\python code\repitle\python_webpage.html')
urlretrieve('https://m.gmw.cn/baijia/2020-06/12/1301283184.html',r'E:\python code\repitle\python_webpage1.html')#保存网页
