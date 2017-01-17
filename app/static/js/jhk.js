/**
 * Created by Administrator on 2017/1/17.
 */

function getResult() {
    console.log("hh");
        $.ajax({
            type:"GET",
            url:"/packaction",
            dataType:"json",
            data:'',
            success:function (data1) {
              parseJSON(data1)
            }
     });
    console.log("hhs");
}

