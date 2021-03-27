function fillcity()
{removeoption()
    switch(state.selectedIndex)
    {
        case 1:
            ap=['--city--','Visakhapatnam','Vijaywada','Guntur','Nellore','Kurnool','Kakinada','Rajamahendravaram','Kadapa','Tirupati','Anantapuram','Vizianagaram','Eluru','Chirala','Ongole','Adoni','Madanapalle','Machilipatnam','Tenali','Proddatur','Chittoor','Hindupur','Srikakulam','Bhimavaram','Guntakal','Dharmavaram','Gudivada','Narasaraopet','Tadipatri','Mangalagiri','Tadepalligudem','Amaravati','Chilakaluripet']
            fillarray(ap)
            break

        case 2:
            ap=['--city--','Itanagar','Tezu','Roing','Khonsa','Namsai','Pasighat','Jairampur','East Siang','Ziro','Bomdila','Deomali','Tawang','Naharlagun','Daporijo','Seppa','Changlang','Hawai','Aalo','Vijoynagar','Anini','Yingkiong','Koloriang','Basar','Dirang','Boleng','Yupia','Mechuka','Bhalukpong','Kharsang','Bordumsa','Chowkham','Wakro','Pangin']
            fillarray(ap)
            break        
    }
}

function fillarray(array){
    for(i=0;i<array.length;i++){
        var opt=document.createElement('option')
        opt.text=array[i]
        opt.value=array[i]
        city.add(opt)
    }
}

function removeoption(){
    for(j=city.options.length-1;j>=0;j--)
    {
        city.remove(j)
    }
}



$(document).ready(function(){

    $('#repeatpwd').keyup(function(){
        if($('#pwd').val()==$('#repeatpwd').val())
        {
            $('#pmsg').html('Password Matched').css('color','green')
        }
        else
        {
            $('#pmsg').html('Password Not Matched').css('color','red')
        }
    })

    $('#city').append($('<option>').text("--Select City--"))

    $.getJSON("http://127.0.0.1:8000/displaythana",{ajax:true},function(data){
        $.each(data,function(index,item){
            $('#city').append($('<option>').text(item))
        })
    })

    $('#city').change(function(){
        $.getJSON("http://127.0.0.1:8000/displaycomplaintjson/",{ajax:true,city:$('#city').val()},function(data){
            htm=''
            if(data.length==0)
            {htm=''}
            else
            {
                htm+="<table class='table'>"
                htm+="<thead>"
                htm+="<tr>"
                htm+="<th scope='col'>Complaint id</th>"
                htm+="<th scope='col'>Username</th>"
                htm+="<th scope='col'>Complaint Type</th>"
                htm+="<th scope='col'>Email Address</th>"
                htm+="<th scope='col'>Mobile Number</th>"
                htm+="<th scope='col'>Status</th>"
                htm+="</tr>"
                htm+="</thead>"
                $.each(data,function(index,item){
                    htm+="<tbody>"
                    htm+="<tr>"
                    htm+="<th scope='row'>"+item[0]+"</th>"
                    htm+="<td>"+item[1]+"</td>"
                    htm+="<td>"+item[2]+"</td>"
                    htm+="<td>"+item[5]+"</td>"
                    htm+="<td>"+item[6]+"</td>"
                    htm+="<td>"+item[8]+"<br><a href='/editstatus?complaintid="+item[0]+"'>View/Update</a></td>"
                    htm+="</tr>"
                    htm+="</tbody>"                   
                })
                htm+="</table>"
            }
            $('#result').html(htm)
        })
    })

    $('#btn').click(function(){
        $.getJSON("http://127.0.0.1:8000/admindisplayall/",{ajax:true},function(data){
            htm=''
            if(data.length==0)
            {htm='<h1>No Records</h1>'}

            else
            {
                htm+="<table class='table'>"
                htm+="<thead>"
                htm+="<tr>"
                htm+="<th scope='col'>Complaint id</th>"
                htm+="<th scope='col'>Username</th>"
                htm+="<th scope='col'>Complaint Type</th>"
                htm+="<th scope='col'>Email Address</th>"
                htm+="<th scope='col'>Mobile Number</th>"
                htm+="<th scope='col'>City</th>"
                htm+="<th scope='col'>Status</th>"
                htm+="</tr>"
                htm+="</thead>"
                $.each(data,function(index,item){
                    htm+="<tbody>"
                    htm+="<tr>"
                    htm+="<th scope='row'>"+item[0]+"</th>"
                    htm+="<td>"+item[1]+"</td>"
                    htm+="<td>"+item[2]+"</td>"
                    htm+="<td>"+item[5]+"</td>"
                    htm+="<td>"+item[6]+"</td>"
                    htm+="<td>"+item[7]+"</td>"
                    htm+="<td>"+item[8]+"<br><a href='/editstatus?complaintid="+item[0]+"'>View/Update</a></td>"
                    htm+="</tr>"
                    htm+="</tbody>"                   
                })
                htm+="</table>"
            }
            $('#result').html(htm)
        })
    })
})