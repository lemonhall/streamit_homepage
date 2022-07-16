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
docker build -t lemonhall/apns:v1 .
docker login
docker push lemonhall/apns:v1

这样就能成功的push了

