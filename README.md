
## 爬取需求：

Snowflake 2015-2020 年特性发布的目录

https://docs.snowflake.com/en/release-notes/2015-11.html

## 实现

- 用变量 year month 实现不同年和月的 release note
- 用 requests 请求 snowflake 官网文档
- 将返回的 HTML 进行正则解析
- 解析完毕后存到 Snowflake-ReleaseNote-2015-2020.md

## 希望输出：

ReleaseNote.md
2018-05
new feature ...
2018-04
new feature ...
