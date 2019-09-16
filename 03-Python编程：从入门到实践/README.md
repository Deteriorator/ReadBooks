## 书籍简介
书名|作者译者|ISBN号码
---|---|---
Python编程:从入门到实践|[美]Eric Matthes著  袁国忠译|ISBN 978-7-115-42802-8 

## 注意

模块 pygal.i18n 不存在，更改为 pygal_maps_world 需要重新使用 pip 安装。<br>
`python -m pip3 install -i https://pypi.douban.com/simple pygal_maps_world`

## 项目依赖模块

1. 外星人入侵
    1. Pygame 模块<br>
    `pip install -i https://pypi.douban.com/simple pygame`
    
2. 数据可视化
    1. Matplotlib模块<br>
    `pip install -i https://pypi.douban.com/simple matplotlib`
    2. Pygal模块<br>
    `pip install -i https://pypi.douban.com/simple pygal`
    3. Pygal_maps_world模块<br>
    `pip install -i https://pypi.douban.com/simple pygal_maps_world`
    4. Requests模块<br>
    `pip install -i https://pypi.douban.com/simple requests`
    
3. Web应用程序
    1. Django模块<br>
    `python -m pip install -i https://pypi.douban.com/simple Django`<br>
    `D:\anaconda3\envs\spider\Scripts\django-admin.exe startproject WebApplication`<br>
    `D:\anaconda3\envs\spider\python manage.py migrate`<br>
    `D:\anaconda3\envs\spider\python manage.py runserver`<br>
    `D:\anaconda3\envs\spider\python manage.py startapp DjangoApplication`<br>
    `D:\anaconda3\envs\spider\python manage.py makemigrations DjangoApplication`<br>
    `D:\anaconda3\envs\spider\python manage.py migrate`
        1. 创建超级用户<br>
        `D:\Projects\MyGitHub\ReadBooks\Python编程：从入门到实践\WebApplication>D:\anaconda3\envs\spider\python manage.py createsuperuser`<br>
        `Username (leave blank to use 'xxx'): Deteriorator`<br>
        `Email address: 1930812245@qq.com`<br>
        `Password:(123456)`<br>
        `Password (again):`<br>
        `This password is too short. It must contain at least 8 characters.`<br>
        `This password is too common.`<br>
        `This password is entirely numeric.`<br>
        `Bypass password validation and create user anyway? [y/N]: y`<br>
        `Superuser created successfully.`<br>

### 书上的Django版本太老了，新版本不懂如何操作，暂时停止学习Django