文字爬虫的项目分析：
1.输入：
带有目标文字的网站url
2.输出：
符合要求的所有目标文字文件(txt)

项目流程：
1.获取第一个网站的HTML
2.获取baseUrl
3.获取next
4.组装nextUrl
5.放入全局Queue

6.获取网站的HTML
7.获取目标文字
8.目标文字格式化

9.目标文字写入文件(mini.txt)

10.文件合并(mini.txt->all.txt)
11.mini.txt删除

13.为了提高效率，mini.txt就是缓存(100个文件/50个文件一组)

其中抽取：
1.url->HTML
2.HTML->nextUrl
3.HTML->str
4.全局Queue
5.str->mini.txt
6.mini.txt->all.txt
7.del nimi.txt