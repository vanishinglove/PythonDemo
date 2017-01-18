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
                  var str;
                  data1 = eval("(" + data1 + ")");
                  for(i in data1){
                      console.log(data1[i]);
                      for(j in data1[i]){
                            console.log(data1[i][j]);

                      }
                      str = str + buildResult(data1[i]['packname'],data1[i]['env'],data1[i]['time'],data1[i]['result'],data1[i]['link']);
                  }

                  console.log(str);
                $('#result').append(str);
            }
     });
    console.log("hhs");
}
function clickSub() {
    console.log("kaishidabao");
    $.ajax({
        type: "GET",
        url: "/jenkins",
        dataType: "json",
        data: '',
        success: function (data1) {

        }
    });
   // buildResult(1,2,3,4,5);
}

function buildResult(packname,env,time,lcfresult,link) {
    //$('#result').append("<tr>"+
      var res = "<tr>"+
        "<td>"+packname+"</td>" +
        "<td>"+env+"</td> " +
        "<td>"+time+"</td> " +
        "<td>"+lcfresult+"</td> " +
        "<td><a href=link>"+link+"</a></td>"+
        "<td><img src='http:\/\/qr.liantu.com/api.php?text=http:\/\/172.16.16.18:9999/job/com.lcf.android.debug/lastBuild/artifact/Lcf-Android/app/build/outputs/apk/app-debug.apk -o app-debug.png' height='100px' width='100px'></td>"+
        "</tr>";
      return res
}


getResult();