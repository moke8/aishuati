<!--
 * @Author: mokevip
 * @Date: 2020-09-14 13:54:03
 * @LastEditors: mokevip
 * @LastEditTime: 2020-09-14 14:15:47
 * @Description: 
-->
<h1>爱刷题</h1>
<p>一个简单的无数据库的刷题H5应用</p>
<p>特色内容：</p>
<ol>
    <li>无后端、无数据库轻量化部署简单</li>
    <li>使用JSON作为题库存储，层次清晰，结构简单易懂</li>
    <li>有配套的word模板和模板到JSON转换工具</li>
    <li>四种刷题模式：顺序刷题、乱序刷题、错题模式、背题模式</li>
</ol>

<p>主要结构：</p>
<ul>
    <li>index.html      主页，显示题库列表</li>
    <li>type.html       刷题模式选择页面，可选四种模式</li>
    <li><b>timu.html</b>      刷题页面</li>
    <li>json/*.json    存储题库</li>
    <li>js/public.js     js数组对应JSON题库的文件路径和描述信息ID等</li>
    <li>py-timuToJson    转换JSON的模板和脚本</li>
</ul>

<p>目前自用演示站：<a href="http://shuati.mokevip.top/">http://shuati.mokevip.top/</a></p>
<p>效果图：</p>
<img src="https://s1.ax1x.com/2020/09/14/wD3NTA.png" alt="wD3NTA.png" border="0" />
<img src="https://s1.ax1x.com/2020/09/14/wD8KBQ.png" alt="FireShot Capture 020 答题类型选择 shuati.mokevip.top" border="0">
<img src="https://s1.ax1x.com/2020/09/14/wD8lAs.png" alt="FireShot Capture 023 爱刷题 shuati.mokevip.top" border="0">
<img src="https://s1.ax1x.com/2020/09/14/wD81Nn.png" alt="FireShot Capture 026 爱刷题 shuati.mokevip.top" border="0">
<img src="https://s1.ax1x.com/2020/09/14/wD83hq.png" alt="FireShot Capture 029 爱刷题 shuati.mokevip.top" border="0">
