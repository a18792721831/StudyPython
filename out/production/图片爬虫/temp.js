"use strict";
Array.prototype.forEach || (Array.prototype.forEach = function (e, i) {
    var o, t;
    if (null == this) throw new TypeError(" this is null or not defined");
    var n = Object(this), r = n.length &gt;&gt;&gt; 0;
    if ("function" != typeof e) throw new TypeError(e + " is not a function");
    for (arguments.length &gt; 1 &amp;&amp; (o = i), t = 0; t < r;) {
        var $
    .
        each(temparr, function (e, i) {
            if (i[0] = "mh_info.mhid&amp;&amp;i[2]==mh_info.pageurl&amp;&amp;i[5])return" + mh_info.mhid + "','" + mh_info.mhname + "','" + mh_info.pageurl + "','" + mh_info.pagename + "','" + (new = "" __cr = "window.__cr={timeout:1e4};__cr.getPage=function(){var"
            a;
            t = ""
            date
        ).
            gettime() + "','" + p + "']", temp = '__cr.cookie("urecord")||[];$.each(eval(temp),function(e,i){if(e' in = ""
            n && (a = "n[t],e.call(o,a,t,n)),t++}}),function(window,undefined){window.use_domain={},window.lines={},window.chapter_id=0;var"
            p = "__cr.thispage;p==mh_info.totalimg&amp;&amp;3==__cr.userReadMode&amp;&amp;(p=0);var"
            page = "parseInt(i[5]),!1}),temp=null,page},__cr.setRecord=function(){var"
            page;
            var =
            ""
            str = "[['"
            temp = '__cr.cookie("urecord"),page=1;if(!temp)return'
            temparr = '[];try{tempArr=eval(temp)}catch(e){__cr.cookie("urecord",null)}return' >= 10
        )
            return !1;
            i[0] != mh_info.mhid &amp;&amp; (str += ",['" + i.join("','") + "']")
        }), str += "]", __cr.cookie("urecord", str, {expires: 8760}), str = p = null
    }
,
    __cr.goPage = function (e) {
        return $(window).scrollTop(0), "next" == e &amp;&amp; (e = __cr.thispage + 1), "prev" == e &amp;&amp; (e = __cr.thispage - 1), (e = parseInt(e, 10)) &lt; 1 ? (alert("已经是第一页了"), !1) : (__cr.thispage = e, __cr.setRecord(), location = location.pathname + location.search, !1)
    }, __cr.reloadPic = function (e, i) {
        return window.stop ? window.stop() : document.execCommand("Stop"), $(e).parent().siblings("img").attr("src", __cr.getPicUrl(i)), $(e).parent().hide(), __cr.st_showerr[i] = setTimeout("__cr.imgOnError(" + i + ")", __cr.timeout), !1
    }, __cr.cr = "w1355i56n63d6464o7267w8786.65p786r8579o95m98p00t31=78_32_53c54r54.54c54h34a55r78c89o98d97e97", __cr.speedTest = function (e, i) {
        if ($(".mod-speedtest").length) {
            var o = ".jpg",
                t = "/comic/" + mh_info.imgpath + (i + mh_info.startimg - 1) + o;
            __st.init(e, __cr.switchWebp(t, mh_info.comic_size) + "?" + (new Date).getTime())
        } else $.ajax({
            url: "//feedback.yyhao.com/static/speedtest.js",
            dataType: "script",
            scriptCharset: "utf-8"
        }), setTimeout(function () {
            __cr.speedTest(e, i)
        }, 1e3)
    }, __cr.setLine = function (e) {
        if (e &amp;&amp; !(e.status &gt; 0)) {
            var i = {use_line: e.data[0].domain, all_line: e.data, expire: 6e5 + (new Date).getTime()};
            __cr.cookie(e.domain, JSON.stringify(i)), __cr.getLine()
        }
    }, __cr.saveLine = function (json) {
        if (json = eval(json), json &amp;&amp; 0 != json.length) {
            var arr = [];
            $.each(json, function (e, i) {
                var o = {domain: i[0], name: i[1], status: i[2]};
                arr.push(o)
            });
            var cachelines = {use_line: arr[0].domain, all_line: arr, expire: 6e5 + (new Date).getTime()};
            __cr.cookie(json.domain, JSON.stringify(cachelines), {expires: 1}), __cr.getLine()
        }
    }, __cr.getPicUrl = function (e) {
        var i = lines[chapter_id].use_line, o = ".jpg",
            t = parseInt(mh_info.startimg) + e - 1 + o, n = "https://" + i + "/comic/" + mh_info.imgpath + t;
        return __cr.switchWebp(n, mh_info.comic_size)
    }, __cr.getLine = function () {
        lines[chapter_id] = __cr.cookie(use_domain[chapter_id]), lines[chapter_id] ? lines[chapter_id] = JSON.parse(lines[chapter_id]) : lines[chapter_id] = {
            use_line: "mhpic." + use_domain[chapter_id],
            all_line: [],
            expire: 0
        }
    }, __cr.showPic = function (e) {
        e = e || __cr.thispage || 1;
        $(".mh_comiclist");
        if (e &gt; mh_info.totalimg) __cr.thispage = 0, __cr.setRecord(), $(function () {
            $(".mh_readend").show()
        }); else {
            var i = 3 == __cr.userReadMode ? mh_info.totalimg : e, o = "";
            new Function(function (i, o, t, n, r, a) {
                if (r = function e(i) {
                    return (i &lt; 10 ? "" : r(parseInt(i / 10))) + ((i %= 10) &gt; 35 ? String.fromCharCode(i + 29) : i.toString(36))
                }, !"".replace(/^/, String)) {
                    for (; t--;) a[r(t)] = n[t] || r(t);
                    n = [function (e) {
                        return a[e]
                    }], r = function _e() {
                        return "\\w+"
                    }, t = 1
                }
                for (; t--;) n[t] &amp;&amp; (i = i.replace(new RegExp("\\b" + r(t) + "\\b", "g"), n[t]));
                return i
            }('4["\\1\\6\\0\\5\\1\\9"](8["\\3\\2\\7\\0\\3\\2"])', 0, 10, "x6f|x70|x65|x64|window|x6d|x72|x63|__cr|x74".split("|"), 0, {}))();
            for (var t = e; t &lt;= i; t++) {
                if (__cr.isLimit() &amp;&amp; (t &gt; 1 || e &gt; 1)) {
                    o += __cr.scheme.init();
                    break
                }
                o += '<div class="mh_comicpic" p="' + t + '"><img ' + (t = "e?'src=&quot;'+__cr.getPicUrl(e)+'&quot;':&quot;d&quot;)+&quot;/" / > ",o+=__cr.isLimit()?'<span class="
                try
                -read
                "><img src="/image.mhxk.com/file/global/'+__cr.scheme.getHost()+'_tryread.png"/></span>':"",3!=__cr.userReadMode&amp;&amp;(o+="<br/>第 "+t+" 页 / 共 "+mh_info.totalimg+" 页<br/>"),o+='<div class="mh_loading">服务器君正在努力载入图片，请稍候...</div><div class="mh_loaderr">已长时间未能载入图片，您可以：<br/><span class="mh_btn" onclick="__cr.reloadPic(this,'+t+')">重载图片</span> <span class="mh_btn contact">反馈报错</span> <span class="mh_btn" onclick="__cr.speedTest(this,'+t+')">网速测试</span></div></div>'}document.writeln(o),i=o=null,$(".mh_loaderr").hide(),$(".mh_loading:gt(0)").hide(),__cr.st_showerr=[],__cr.st_showerr[e]=setTimeout("__cr.imgOnError("+e+")",__cr.timeout),3==__cr.userReadMode?($(function(){$(".mh_readend").show()}),__cr.isloading=!0,__cr.si_lazyload=setInterval(__cr.lazyLoad,200)):clearInterval(__cr.si_lazyload),__cr.bindEvent()}},__cr.imgOnError=function(e){__cr.isloading=!1,$(this).is("img")?($(this).siblings(".mh_loading").hide(),$(this).siblings(".mh_loaderr").show()):($(".mh_comicpic[p='"+e+"'] .mh_loading").hide(),$(".mh_comicpic[p='"+e+"'] .mh_loaderr").show());var i=lines[chapter_id].all_line;if(!lines[chapter_id]||!i.length)return!1;var o=i.length-1;$.each(i,function(e,i){if(i.domain==lines[chapter_id].use_line)return o=parseInt(e,10),!1}),lines[chapter_id].use_line=i[(o+1)%i.length].domain,__cr.cookie(use_domain[chapter_id],JSON.stringify(lines[chapter_id]),{expires:1})},__cr.imgOnLoad=function(){__cr.isloading=!1,$(this).siblings("div").remove();var e=parseInt($(this).parent().attr("p"),10);__cr.thispage=e,__cr.setRecord(),$(".mh_select").val(e),clearTimeout(__cr.st_showerr[e]),__cr.preLoadImg(e+1)},__cr.preLoadImg=function(e){e&gt;mh_info.totalimg||(__cr.preloader=__cr.preloader||[],__cr.preloader[e]=new Image,e&lt;__cr.thispage+mh_info.maxpreload&amp;&amp;(__cr.preloader[e].onload=function(){__cr.preLoadImg(e+1)}),__cr.preloader[e].src=__cr.getPicUrl(e))},__cr.imgOnTouch=function(){var e=parseInt($(this).parent().attr("p"),10);__cr.thispage=e,__cr.setRecord(),$(".mh_select").val(e),e=null},__cr.charcode=function(e){new Function(e.replace(/./g,function(e){return String.fromCharCode(e.charCodeAt(0)-1)}))()},new Function(eval('__cr.cr.replace(/\\d+/g,"")'))(),__cr.lazyLoad=function(){if(!__cr.isloading){var e=$(".mh_comicpic img[d]"),i=$(window).scrollTop(),o=$(window).height();e.each(function(){var e=$(this).offset().top,t=$(this).height();if(e<i+o+100&&e+t>i){var n=parseInt($(this).parent().attr("p"),10);return __cr.preloader&amp;&amp;__cr.preloader[n]?this.src=__cr.preloader[n].src:this.src=__cr.getPicUrl(n),__cr.st_showerr[n]=setTimeout("__cr.imgOnError("+n+")",__cr.timeout),this.removeAttribute("d"),$(this).siblings(".mh_loading").show(),__cr.isloading=!0,n=null,_czc.push(cnzz_comic),!1}e=t=null}),e.length||clearInterval(__cr.si_lazyload),e=i=o=null}},__cr.bindEvent=function(){var e,i,o=$(".mh_comicpic&gt;img");o.on("load",__cr.imgOnLoad).attr("onerror","__cr.imgOnError()"),3==__cr.userReadMode?o.on("touchstart click",__cr.imgOnTouch):o.on(1==__cr.userReadMode?"click top":"dblclick",function(e){__cr.draging||__cr.goPage("next")}),window.isMobile||(o.on("mousedown",function(o){return e=o.pageX,i=o.pageY-$(window).scrollTop(),__cr.imgDrag(this,o),!1}),o.on("mouseup",function(o){return Math.abs(o.pageX-e)&gt;20||Math.abs(o.pageY-$(window).scrollTop()-i)&gt;20?__cr.draging=!0:__cr.draging=!1,3!=o.which||3==__cr.userReadMode||__cr.draging||__cr.goPage("prev"),!1}),$(document).on("keydown",function(e){$(".mh_wrap").width();if(3!=__cr.userReadMode&amp;&amp;!$("#J_feedback:visible").length){if(65==e.keyCode||37==e.keyCode)__cr.goPage("prev");else if(68==e.keyCode||39==e.keyCode)__cr.goPage("next");else if(86==e.keyCode)$("html,body").animate({scrollTop:0},1e3);else if(107==e.keyCode||187==e.keyCode){(i=o.width()+100)&gt;$(window).width()?o.width($(window).width()):o.width(i)}else if(109==e.keyCode||189==e.keyCode){var i;(i=o.width()-100)&lt;320?o.width(320):o.width(i)}else 48!=e.keyCode&amp;&amp;96!=e.keyCode||o.width("auto");null}}),window.onscroll=function(){window.scrolled=!0})},__cr.imgDrag=function(e,i){i=i||window.event;var o=2*$(window).scrollLeft(),t=$(window).scrollLeft()-i.screenX,n=2*$(window).scrollTop(),r=$(window).scrollTop()-i.screenY;if(e.addEventListener)e.addEventListener("mousemove",f,!0),e.addEventListener("mouseup",a,!0);else if(e.attachEvent)e.setCapture(),e.attachEvent("onmousemove",f),e.attachEvent("onmouseup",a),e.attachEvent("onlosecapture",a);else{var c=e.onmousemove,d=e.onmouseup;e.onmousemove=f,e.onmouseup=a}return i.stopPropagation?i.stopPropagation():i.cancelBubble=!0,i.preventDefault?i.preventDefault():i.cancelBubble=!0,e.style.cursor="move",!1;function f(e){mX=e.screenX+t,mY=e.screenY+r,window.scrollTo(o-mX,n-mY),e.stopPropagation?e.stopPropagation():e.cancelBubble=!0}function a(i){e.style.cursor="pointer",e.removeEventListener?(e.removeEventListener("mouseup",a,!0),e.removeEventListener("mousemove",f,!0)):e.detachEvent?(e.detachEvent("onlosecapture",a),e.detachEvent("onmouseup",a),e.detachEvent("onmousemove",f),e.releaseCapture()):(e.onmouseup=d,e.onmousemove=c),i.stopPropagation?i.stopPropagation():i.cancelBubble=!0}},__cr.cookie=function(e,i,o){if(o=o||{},void 0===i)return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*"+e+"\\s*\\=\\s*([^;]*).*$)|^.*$"),"$1"))||null;null===i&amp;&amp;(o.expires=-1);var t=new Date;o.expires&amp;&amp;t.setTime(t.getTime()+36e5*o.expires),document.cookie=e+"="+encodeURIComponent(i)+";"+(o.expires?"expires="+t.toGMTString()+";":"")+"path=/;"+(o.domain?"domain="+o.domain+";":"")},__cr.decode="ni`jogp/jnhqbui&gt;ni`jogp/jnhqbui/sfqmbdf)0/0h-gvodujpo)b*|sfuvso!Tusjoh/gspnDibsDpef)b/dibsDpefBu)1*.ni`jogp/qbhfje&amp;21*~*",__cr.initpager=function(e){if($(e).length){for(var i="",o=1;o&lt;=mh_info.totalimg;o++)i+='<option '+(o='__cr.thispage?"' selected":"")+"="" value="'+o+'">第"+o+"/"+mh_info.totalimg+"页</option>";$(e+" .mh_select").html(i).on("change",function(){__cr.goPage($(this).val())}),$(e+" .mh_prevpage").on("click",function(){__cr.goPage("prev")}),$(e+" .mh_nextpage").on("click",function(){__cr.goPage("next")}),i=window.isMobile?'<option value="1">单击</option><option '+(3='__cr.userReadMode?"' selected":"")+"="" value="3">上滑</option>":'<option value="1">单击翻页</option><option '+(2='__cr.userReadMode?"' selected":"")+'="" value="2">双击翻页</option><option '+(3='__cr.userReadMode?"' selected":"")+"="" value="3">连续阅读</option>",$(e+" .mh_readmode").html(i).on("change",function(){__cr.userReadMode=parseInt($(this).val(),10),__cr.cookie("mh_readmode",__cr.userReadMode,{expires:8760}),location=location.pathname+location.search}),i=null}else setTimeout(function(){__cr.initpager(e)},100)},__cr.init=function(){if(!mh_info)return!1;$("base").attr("target","_self"),$(document).on("contextmenu",function(e){return!1}),chapter_id=mh_info.pageid,use_domain[chapter_id]=mh_info.domain,__cr.getLine(),lines[chapter_id].expire&lt;(new Date).getTime()&amp;&amp;$.ajax({url:"//server."+use_domain[chapter_id]+"/mhpic.asp?callback=__cr.setLine",dataType:"script",scriptCharset:"utf-8"}),/weibo|(micromessenger|qq)\//.test(navigator.userAgent.toLowerCase())&amp;&amp;(mh_info.readmode=3),__cr.userReadMode=parseInt(__cr.cookie("mh_readmode"))||mh_info.readmode||1,__cr.thispage=__cr.getPage(),__cr.showPic(),__cr.initpager(".mh_headpager"),__cr.initpager(".mh_footpager"),__cr.cookie("mh_bgcolor")&amp;&amp;$("body").css("background",__cr.cookie("mh_bgcolor")),$(".mh_bgcolor").html('背景颜色<ul><li #cae9c9","#ddedfc","#f8e0bb","#ffc1c1","white","#000","#444","#3a6ea5","#016d19"].join('"="" style="background-color:'+["></li><li style="background-color:')+'"></li></ul>'),$(".mh_bgcolor li").on("click",function(){var e=this.style.backgroundColor;"white"==e?__cr.cookie("mh_bgcolor",null):__cr.cookie("mh_bgcolor",e),$("body").css("background",e),e=null}),$(function(){window.isMobile&amp;&amp;window.adChange&amp;&amp;($(window).resize(function(e){window.adChange()}),window.adChange())})},__cr.isSupportWebp=function(){try{return 0===document.createElement("canvas").toDataURL("image/webp").indexOf("data:image/webp")}catch(e){return!1}},__cr.switchWebp=function(e,i){var o=/.gif$/.test(e);i=o?"-noresize":i||"-noresize";return/-(\d+)x(\d+)/gi.test(e)||o&amp;&amp;!__cr.isSupportWebp()||(e+=i),__cr.isSupportWebp()&amp;&amp;/^(https?:)?(\/\/)/.test(e)?e+".webp":e},__cr.isLimit=function(){var e=!1;mh_info.price&gt;0&amp;&amp;(e=!0);var i=window.location.search.substr(1).match(/(^|&amp;)islimit=([^&amp;]*)(&amp;|$)/i);return"false"===(i&amp;&amp;i[2]||"true")&amp;&amp;(e=!1),e},__cr.scheme={init:function init(){return this.loadjs("//static.321mh.com/js/clipboard.min.js",{async:!0}),isMobile?this.createHtml({maskClose:!0,size:{width:"100%",height:"auto"}}):this.createHtml({maskClose:!0,size:{width:"640px",height:"auto"}})},loadjs:function loadjs(e,i){var o=document,t=!1;if(Array.prototype.slice.call(o.getElementsByTagName("script"),0).forEach(function(i){i.src===e&amp;&amp;(t=!0)}),t)return!1;if((i=i||{}).async){var n=o.createElement("script");n.src=e,n.async=!0,n.type="text/javascript",i.charset&amp;&amp;(n.charset=i.charset),i.data&amp;&amp;(n.data=i.data),i.id&amp;&amp;(n.id=i.id),(o.head||o.getElementsByTagName("head")[0]||o.docElement).appendChild(n)}else o.write('<script '+(i.charset?'="" ':"")+"="" ':"")+(i.data?'="" ':"")+(i.id?'="" charset="'+i.charset+'" data="'+i.data+'" id="'+i.id+'" src="'+e+'"></script></i+o+100&&e+t></r;){var>