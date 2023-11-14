# GLMServer

A Simple Django Server for ChatGLM and Stable Diffusion application.

![](https://img.shields.io/badge/author-Gaozih-%2366ccff)
![](https://img.shields.io/github/license/Gzh0821/Optimization_project)
![](https://img.shields.io/github/stars/Gzh0821/glmServer)

## Quickstart
- 安装python 3.11
- 安装本项目依赖:
```
    pip install -r requirements.txt
```
- 建立项目所需的数据库(SQLite):
```
    python manage.py makemigrations
    python manage.py migrate
```
- 创建超级管理员,按提示输入用户名和密码:
```
    python manage.py createsuperuser
```
- 启动开发用服务器,设置端口号为8000(可更改):
```
    python manage.py runserver 8000
```
- 在windows上使用WSGI服务器:
```
    python run.py
```
- 访问`http://127.0.0.1:8000`,进入swagger api文档界面.
## Path
- `/api`:api接口
- `/admin`:django管理员界面
- `/swagger`:Swagger-ui风格的api文档
- `/redoc`:Redoc风格的api文档
- `/temp/auth/`:DRF提供的临时用户登录/注销界面

