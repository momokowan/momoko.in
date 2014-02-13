# momoko.in

Pelican for momoko.in Project

## idea from

http://fengmk2.github.io/mx-2013.html

## making

- 根据官方教程,使用标准模板,
- 填写历史节点情节
- 发表为页面
    - e.g
    - `https://docs.google.com/spreadsheet/pub?key=[文档ID]&output=html`
- 从中获得关键 ID 然后手工
    - 组成转换URI
    - `https://spreadsheets.google.com/feeds/list/[文档ID]/od6/public/basic?hl=en_US&alt=json`
    - 下载为 JSON
- 装配到 Pelican 的页面中!



