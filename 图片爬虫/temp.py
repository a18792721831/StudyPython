import demjson
st = '{imgpath:"Q(5I(H<(;3(;9(H8(D7(D<(H<(;5(DD(H:(D8(<H(5I93(H;(DI(<GJT(5I",startimg:1,totalimg:11,mhid:"nitianxieshen",mhname:"逆天邪神",pageid:1619423,pagename:"第60话 一战惊城6",pageurl:"60",readmode:1,maxpreload:5,defaultminline:1,domain:"cnmanhua.com",comic_size:"-mht.middle",default_price:0,price:0,time_diff:3756960319,image_suffix:"jpg"}'
hjson = demjson.decode(st)
print(type(hjson))
print(hjson)
