$(function () {
    let time=0;
    $("header .left").click(function () {
        time++;
        if (time%2!=0) {
            $(".alert").css("display","block")
        }
        else if (time%2==0) {
            $(".alert").css("display","none")
        }
    })
    $("#meau").click(function () {
        time++;
        if (time%2!=0) {
            $(".meau").css("width","400px")
        }
        else if (time%2==0) {
            $(".meau").css("width","0")
        }
    })
})