## 项目截图

![This is an image](/screenshot.png)

## 启一个新环境
conda create --name streamit python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

## 切到新环境下去
conda activate streamit

## 官网
https://streamlit.io/

## 安装
pip install streamlit

## Hello World一下
streamlit hello

## 进入正题
import streamlit as st

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

## 启动
streamlit run main.py

## widgets系统
https://docs.streamlit.io/library/api-reference/widgets

## media系统
https://docs.streamlit.io/library/api-reference/media

图片、声音、图像这些的

## 组件系统
https://docs.streamlit.io/library/components

https://streamlit.io/components

组件目录

https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634

一个组件的收集帖

## 布局系统
https://docs.streamlit.io/library/api-reference/layout

## 状态展示
https://docs.streamlit.io/library/api-reference/status/st.warning

## 构建
docker build -t lemonhall/streamlit:v1 .

## push的小技巧

首先需要在自己的空间下build
docker build -t lemonhall/streamlit:v1 .
docker login
docker push lemonhall/streamlit:v1

这样就能成功的push了

## 跑起来
* ssh到群晖里面去，然后sudo docker pull lemonhall/streamlit:v1，把镜像拉下来
* 新建一个容器，需要配置三点，1、Entry Point需要覆盖images的配置。2、共享目录要配好，把项目文件映射到root目录下面去。3、记得start.sh里面写cd
* 然后启动这个容器，配置好端口映射，此时外网还访问不了你。
* 最后是到控制面板，登陆选项，高级，反向代理里面去

![This is an image](/r_proxy_setting.jpeg)

* 按照上面的配置反向代理，否则ws跑不起来
* [[SOLVED] Websocket setup on Synology](https://vaultwarden.discourse.group/t/solved-websocket-setup-on-synology/116/8)
