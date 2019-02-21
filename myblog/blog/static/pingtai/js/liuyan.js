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
    let time1=0
    $("#comment").click(function () {
        time1++;
        if (time1%2!=0) {
            $(".comment").slideDown()
        }
        else if (time1%2==0) {
            $(".comment").slideUp()
        }
    })
    $("#share").click(function () {
        time++;
        if (time%2!=0) {
            $(".share").slideDown()
        }
        else if (time%2==0) {
            $(".share").slideUp()
        }
    })
    $("#meau").click(function () {
        time++;
        if (time%2!=0) {
            $(".meau").css("width","330px")
        }
        else if (time%2==0) {
            $(".meau").css("width","0")
        }
    })

    $(".btn_left").click(function () {
        time++;
        if (time%2!=0) {
            $(".slide").css("width","270px")
        }
        else if (time%2==0) {
            $(".slide").css("width","0")
        }
    })
    $(".btn_right").click(function () {
        time++;
        if (time%2!=0) {
            $(".slide1").css("width","270px")
        }
        else if (time%2==0) {
            $(".slide1").css("width","0")
        }
    })
    $(".ul").click(function(e){
        let target=$(e.target)

        if(target.hasClass("huifu1")){
            time++;
            if (time%2!=0) {
                target.parent().parent().parent().css("height","180px");
                target.parent().siblings(".huifu").css("display","block")
            }
            else if (time%2==0) {
                target.parent().parent().parent().css("height","108px");
                target.parent().siblings(".huifu").css("display","none")
            }
        }
    })
})