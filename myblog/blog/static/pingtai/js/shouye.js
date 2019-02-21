$(function (){
    $(".con ul li").click(function () {
        let index=$(this).index()
        $(this).addClass("selected").siblings().removeClass("selected")
    });
    $("#pull").mouseenter(function(){
        console.log("123")
        $(".pull").show(".3s");
        $(".icon-xiangxia").css('transform','rotate(180deg)')
    });
    $("#pull").mouseleave(function(){
        $(".pull").hide(".3s");
        $(".icon-xiangxia").css('transform','rotate(360deg)')
    });
})