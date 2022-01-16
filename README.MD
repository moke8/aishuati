<!--
 * @Author: mokevip
 * @Date: 2020-09-14 13:54:03
 * @LastEditors: mokevip
 * @LastEditTime: 2020-09-14 14:26:26
 * @Description: 
-->
<h1>爱刷题</h1>
<p>一个简单的无数据库的刷题H5应用</p>
<h3>更新</h3>
<p>爱刷题PLUS在<a href="https://github.com/moke8/aishuati/">爱刷题</a>的基础上，舍弃了部署简单、纯前端部署等优势，加入了管理后台、更加方便管理操作和题库录入、修改等。</p>
<p>在UI界面上采用了新的设计（原本大概属于没有设计）。</p>
<p>具体内容可以查看<a href="https://github.com/moke8/aishuati-plus-admin/">爱刷题PLUS--ADMIN</a>、<a href="https://github.com/moke8/aishuati-plus-wechat/">爱刷题PLUS--WECHAT</a>和<a href="https://github.com/moke8/aishuati-plus-api/">爱刷题PLUS--API</a>.</p>

<h3>前言</h3>
<p>迫于最近需要考试，平时碎片化时间较多，并不能合理利用碎片化时间。便想着可以用类似于<code>驾考宝典</code>的应用帮助自己充分利用碎片化时间。</p>
<p>于是将试卷WORD整理出来，导入了一些刷题网站（如<code>刷刷题</code>、<code>考试宝</code>等），发现，都是需要收费的，可能一周就要10元。</p>
<p>逐到GITHUB搜索，可能因为姿势不正确，并没有找到合适的仓库。</p>
<p>被逼无奈，只好自己上手。做好了之后也可以分享给大家，共同学习共同努力。</p>
<h3>特色内容</h3>
<ol>
    <li>无后端、无数据库轻量化部署简单</li>
    <li>使用JSON作为题库存储，层次清晰，结构简单易懂</li>
    <li>有配套的word模板和模板到JSON转换工具</li>
    <li>四种刷题模式：顺序刷题、乱序刷题、错题模式、背题模式</li>
    <li>顺序答题和背题模式支持恢复答题进度</li>
</ol>

<h3>主要结构</h3>
<ul>
    <li>index.html      主页，显示题库列表</li>
    <li>type.html       刷题模式选择页面，可选四种模式</li>
    <li><b>timu.html</b>      刷题页面</li>
    <li>json/*.json    存储题库</li>
    <li>js/public.js     js数组对应JSON题库的文件路径和描述信息ID等</li>
    <li>py-timuToJson    转换JSON的模板和脚本</li>
</ul>

<p><b>注：下载后双击index.html是无法直接食用的，需要配合web服务（如静态资源服务器或live-server等）食用</b></p>

<h3>效果预览</h3>
<p>目前自用演示站：<a href="http://shuati.mokevip.top/">http://shuati.mokevip.top/</a></p>
<p>效果图：</p>
<img src="https://s1.ax1x.com/2020/09/14/wD3NTA.png" alt="wD3NTA.png" border="0" />
<img src="https://s1.ax1x.com/2020/09/14/wD8KBQ.png" alt="FireShot Capture 020 答题类型选择 shuati.mokevip.top" border="0">
<img src="https://s1.ax1x.com/2020/09/14/wD8lAs.png" alt="FireShot Capture 023 爱刷题 shuati.mokevip.top" border="0">
<img src="https://s1.ax1x.com/2020/09/14/wD81Nn.png" alt="FireShot Capture 026 爱刷题 shuati.mokevip.top" border="0">
<img src="https://s1.ax1x.com/2020/09/14/wD83hq.png" alt="FireShot Capture 029 爱刷题 shuati.mokevip.top" border="0">
