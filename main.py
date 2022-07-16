import streamlit as st

st.set_page_config(page_title="我的主页", page_icon="random", layout="wide", initial_sidebar_state="auto", menu_items=None)
st.header('我的主页')
st.markdown("____")
col1,col2,col3,col4,col5 = st.columns(5)
with col1:
     st.markdown("[<img src='https://lemonhall.synology.me:9090/static/logo.png' width='30%'>](https://lemonhall.synology.me:9090/bookmarks)", unsafe_allow_html=True)
     st.caption('书签')
     st.markdown("[<img src='https://lemonhall.synology.me:28443/favicon.ico' width='27%'>](https://lemonhall.synology.me:28443/) ", unsafe_allow_html=True)
     st.caption('画图')
     st.markdown("[<img src='http://192.168.50.233:48801/static/app/assets/redis-insight.5808b9940889343624348c985ef6d568.svg' width='160%' style='clip:rect(0px 100px 200px 0px);'>](http://192.168.50.233:48801/) ", unsafe_allow_html=True)
     st.caption('redis')
     st.markdown("[<img src='https://lemonhall.synology.me:25678/n8n-logo.svg' width='60%'>](https://lemonhall.synology.me:25678/) ", unsafe_allow_html=True)
     st.caption('n8n')

with col2:
     st.markdown("[<img src='https://lemonhall.synology.me:8200/static/img/favicon.png' width='30%'>](https://lemonhall.synology.me:8200/notesview/add) ", unsafe_allow_html=True)
     st.caption('写日记')
     st.markdown("[<img src='https://lemonhall.synology.me:15001/synohdpack/images/dsm/modules/PkgManApp/images/package_center_256.png?v=42661-s3' width='30%'>](https://lemonhall.synology.me:15001/) ", unsafe_allow_html=True)
     st.caption('群晖套件')
     st.markdown("[<img src='http://192.168.50.233:23000/assets/img/logo.svg' width='30%'>](http://192.168.50.233:23000/) ", unsafe_allow_html=True)
     st.caption('Gittea')
     st.markdown("[<img src='http://www.btbtt12.com/plugin/view_btbbt/logo.gif' width='30%'>](http://www.btbtt12.com/) ", unsafe_allow_html=True)
     st.caption('BT之家')


with col3:
     st.markdown("[<img src='https://lemonhall.synology.me:23005/favicon.ico' width='30%'>](https://lemonhall.synology.me:23005/) ", unsafe_allow_html=True)
     st.caption('截网页')
     st.markdown("[<font size='72'>🕙</font>](http://192.168.50.233:38501/)", unsafe_allow_html=True)
     st.caption('定时任务')
     st.markdown("[<img src='https://lemonhall.synology.me:22380/dashboard/_nuxt/img/512x512-trans.5601bce.png' width='30%'>](https://lemonhall.synology.me:22380/) ", unsafe_allow_html=True)
     st.caption('低代码开发')

with col4:
     st.subheader("送手机📱消息")
     msg = st.text_input('消息内容:', '测试消息')
     st.button('发送消息')
     st.write('送出的消息为:', msg)
     st.subheader("监听总线开关")
     switch_lightbus1 = st.select_slider(key="lskjlbah",label="",options=['OFF', 'ON'])
     st.write('开关状态:', switch_lightbus1)

with col5:
     st.subheader("lightbus总线开关")
     switch_lightbus2 = st.select_slider(key="ckkksjkk",label="",options=['OFF', 'ON'])
     st.write('开关状态:', switch_lightbus2)

