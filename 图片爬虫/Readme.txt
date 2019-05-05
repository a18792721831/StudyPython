目标网站：漫画网站

输入：第一张漫画的url地址

输出：以文件夹分割的章节名的漫画

1.根据输入的url获取html
2.根据html获取mh_info字典
3.根据html获取下一章
4.根据mh_info构造本章漫画地址列表
5.根据列表下载漫画到文件夹(文件夹名字是mh_info中的章节名字)
6.使用多线程

获取下一章地址：
从mh_info中提取mh_id
其中mh_id就是下一张的二级地址
然后从mh_info中提取pageUrl
然后加入当前页的序号
后面加入.html后缀
这就是下一章的地址

获取本章页数：
从mh_info中提取totalimg

获取本章的章节名字：
从mh_info中获取pagename

图片的地址:
Q(5I(H<(;3(;9(H8(D7(D<(H<(;5(DD(H:(D8(<H(5I93(H;(DI(<GJT(5I
N%2F%E9%80%86%E5%A4%A9%E9%82%AA%E7%A5%9E%2F60%E8%AF%9DGQ%2F   1
Q  81  N  78    -3
(  40  %  37    -3
5  53  2  50    -3

加密解密方法之迁移法

