
    function delete_row(row){
        
        var box = $("#mb-remove-row");
        box.addClass("open");
        
        box.find(".mb-control-yes").off("click").on("click",function(){
            box.removeClass("open");

        var delete_url=document.getElementById('delete_url_id').value;

            $.ajax({
                type: "GET",
                url:  delete_url,
                data: {
                    'id':row
                },
                dataType: "json",
                success: function (data) {
                    if('success' in data){
                        $('trow'+ row ).hide("slow",function(){
                            $(this).remove();
                    });
                    alert(data.success)
                    location.reload(true);

                }
                else{
                    alert(data.error);
                }
                    
                },
                error: function (error) {
                    console.log(error)
                    
                }
    
            });
        });
    }
    

            
       
        
    

    function edit_dpt(dpt_id){
        document.getElementById('spinner'+dpt_id).className="fa fa-spinner";
        document.getElementById("edit_data").value=dpt_id;
        // alert(dpt_id)
        // var name = $("#name").val();


        
        $.ajax({
            type: "GET",
            url:  document.getElementById('url_id').value,
            data: {
                'id':dpt_id
            },
            dataType: "json",
            success: function (data) {
                document.getElementById('dpt_name_id').value=data.name;
                document.getElementById('dpt_code_id').value=data.code;
                document.getElementById('dpt_status_id').value=data.status;
                $('#modal_basic').modal("show");
                document.getElementById('spinner'+dpt_id).className="fa fa-pencil";

            },
            error: function (error) {
                console.log(error);
            }

        });
        
    }



   function update_dpt(){
        document.getElementById("disabled_btn").disabled=true;
        document.getElementById("disabled_btn").innerHTML="loading.."
        
        var name_s=document.getElementById("dpt_name_id").value
        var code_s=document.getElementById("dpt_code_id").value
        var status_s=document.getElementById("dpt_status_id").value
        var db_id=document.getElementById("edit_data").value
        $.ajax({
            type: "GET",
            url:  document.getElementById('update_url_id').value,
            data: {
                'id':db_id,
                'name':name_s,
                'code':code_s,
                'status':status_s,

            },
            dataType: "json",
            success: function (data) {
                // alert(data.error_msg+data.sucscess_msg);
                if(data.error_msg){
                    noty({ text:  data.error_msg ,timeout: 1000, layout: 'topRight', type: 'error'}).show();  
                setTimeout(function(){
                    location.reload(true);

                }, 2000); 
                }

                if(data.success_msg){
                    noty({ text: data.success_msg, timeout: 1000, layout: 'topRight', type: 'success'}).show();
                setTimeout(function(){
                     location.reload(true);
    
                }, 2000); 
                }
                document.getElementById("disabled_btn").disabled=false;
                document.getElementById("disabled_btn").innerHTML="update"
                
            },
            error: function (error) {
                console.log(error);
            }

        });

    }

    

    // DESIGNATION


    function des_delete_row(row){
        
        var box = $("#mb-remove-row");
        box.addClass("open");
        
        box.find(".mb-control-yes").off("click").on("click",function(){
            box.removeClass("open");

        var delete_url=document.getElementById('delete_url_id').value;

            $.ajax({
                type: "GET",
                url:  delete_url,
                data: {
                    'id':row
                },
                dataType: "json",
                success: function (data) {
                    if('success' in data){
                        $('trow'+ row ).hide("slow",function(){
                            $(this).remove();
                    });
                    alert(data.success)
                    location.reload(true);

                }
                else{
                    alert(data.error);
                }
                    
                },
                error: function (error) {
                    console.log(error)
                }
    
            });
        });
    }
    

            
       
        
    

    function edit_des(des_id){
        document.getElementById('spinner'+des_id).className="fa fa-spinner";
        document.getElementById("edit_data").value=des_id;
        // alert(dpt_id)
        // var name = $("#name").val();


        
        $.ajax({
            type: "GET",
            url:  document.getElementById('url_id').value,
            data: {
                'id':des_id
            },
            dataType: "json",
            success: function (data) {
                document.getElementById('des_name_id').value=data.name;
                document.getElementById('des_code_id').value=data.code;
                document.getElementById('des_status_id').value=data.status;
                $('#modal_basic').modal("show");
                document.getElementById('spinner'+des_id).className="fa fa-pencil";

            },
            error: function (error) {
                console.log(error);
            }

        });
        
    }



   function update_des(){
        document.getElementById("disabled_btn").disabled=true;
        document.getElementById("disabled_btn").innerHTML="loading.."
        
        var name_s=document.getElementById("des_name_id").value
        var code_s=document.getElementById("des_code_id").value
        var status_s=document.getElementById("des_status_id").value
        var db_id=document.getElementById("edit_data").value
        $.ajax({
            type: "GET",
            url:  document.getElementById('update_url_id').value,
            data: {
                'id':db_id,
                'name':name_s,
                'code':code_s,
                'status':status_s,

            },
            dataType: "json",
            success: function (data) {
                // alert(data.error_msg+data.sucscess_msg);
                if(data.error_msg){
                    noty({ text:  data.error_msg ,timeout: 1000, layout: 'topRight', type: 'error'}).show();  
                setTimeout(function(){
                    location.reload(true);

                }, 2000); 
                }

                if(data.success_msg){
                    noty({ text: data.success_msg, timeout: 1000, layout: 'topRight', type: 'success'}).show();
                setTimeout(function(){
                     location.reload(true);
    
                }, 2000); 
                }
                document.getElementById("disabled_btn").disabled=false;
                document.getElementById("disabled_btn").innerHTML="update"
                
            },
            error: function (error) {
                console.log(error);
            }

        });

    }

    
// QUALIFICATION

// function qua_delete_row(id){
        
//     var box = $("#mb-remove-row");
//     box.addClass("open");
    
//     box.find(".mb-control-yes").on("click",function(){
//         box.removeClass("open");

//     var delete_url=document.getElementById('delete_url_id').value;
//         $.ajax({
//             type: "GET",
//             url:  delete_url,
//             data: {
//                 'id':id
//             },
//             dataType: "json",
//             success: function (data) {
//                 if('success' in data){
//                     $('#'+ id ).hide("slow",function(){
//                         $(this).remove();
//                 });
                

//             }
//             else{
//                 alert(data.error);
//             }
                
//             },
//             error: function (error) {
//                 console.log(error)
//             }

//         });
//     });
// }



        
   
    


function qua_delete_row(row){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url=document.getElementById('delete_url_id').value;

        $.ajax({
            type: "GET",
            url:  delete_url,
            data: {
                'id':row
            },
            dataType: "json",
            success: function (data) {
                if('success' in data){
                    $('#'+ row ).hide("slow",function(){
                        $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else{
                alert(data.error);
            }
                
            },
            error: function (error) {
                console.log(error)
            }

        });
    });
}


        
   
    


function edit_qua(qua_id){
    document.getElementById('spinner'+qua_id).className="fa fa-spinner";
    document.getElementById("edit_data").value=qua_id;
    // alert(dpt_id)
    // var name = $("#name").val();


    
    $.ajax({
        type: "GET",
        url:  document.getElementById('url_id').value,
        data: {
            'id':qua_id
        },
        dataType: "json",
        success: function (data) {
            document.getElementById('qua_name_id').value=data.name;
            document.getElementById('qua_status_id').value=data.status;
            $('#modal_basic').modal("show");
            document.getElementById('spinner'+qua_id).className="fa fa-pencil";

        },
        error: function (error) {
            console.log(error);
        }

    });
    
}



function update_qua(){
    document.getElementById("disabled_btn").disabled=true;
    document.getElementById("disabled_btn").innerHTML="loading.."
    
    var name_s=document.getElementById("qua_name_id").value
    var status_s=document.getElementById("qua_status_id").value
    var db_id=document.getElementById("edit_data").value
    $.ajax({
        type: "GET",
        url:  document.getElementById('update_url_id').value,
        data: {
            'id':db_id,
            'name':name_s,
            'status':status_s,

        },
        dataType: "json",
        success: function (data) {
            // alert(data.error_msg+data.sucscess_msg);
            if(data.error_msg){
                noty({ text:  data.error_msg ,timeout: 1000, layout: 'topRight', type: 'error'}).show();  
            setTimeout(function(){
                location.reload(true);

            }, 2000); 
            }

            if(data.success_msg){
                noty({ text: data.success_msg, timeout: 1000, layout: 'topRight', type: 'success'}).show();
            setTimeout(function(){
                 location.reload(true);

            }, 2000); 
            }
            document.getElementById("disabled_btn").disabled=false;
            document.getElementById("disabled_btn").innerHTML="update"
            
        },
        error: function (error) {
            console.log(error);
        }

    });

}

//CLASS

function cls_delete_row(row){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url=document.getElementById('delete_url_id').value;

        $.ajax({
            type: "GET",
            url:  delete_url,
            data: {
                'id':row
            },
            dataType: "json",
            success: function (data) {
                if('success' in data){
                    $('trow'+ row ).hide("slow",function(){
                        $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else{
                alert(data.error);
            }
                
            },
            error: function (error) {
                console.log(error)
            }

        });
    });
}


        
   
    


function edit_cls(cls_id){
    document.getElementById('spinner'+cls_id).className="fa fa-spinner";
    document.getElementById("edit_data").value=cls_id;
    // alert(dpt_id)
    // var name = $("#name").val();


    
    $.ajax({
        type: "GET",
        url:  document.getElementById('url_id').value,
        data: {
            'id':cls_id
        },
        dataType: "json",
        success: function (data) {
            document.getElementById('cls_name_id').value=data.name;
            document.getElementById('cls_status_id').value=data.status;
            $('#modal_basic').modal("show");
            document.getElementById('spinner'+cls_id).className="fa fa-pencil";

        },
        error: function (error) {
            console.log(error);
        }

    });
    
}



function update_cls(){
    document.getElementById("disabled_btn").disabled=true;
    document.getElementById("disabled_btn").innerHTML="loading.."
    
    var name_s=document.getElementById("cls_name_id").value
    var status_s=document.getElementById("cls_status_id").value
    var db_id=document.getElementById("edit_data").value
    $.ajax({
        type: "GET",
        url:  document.getElementById('update_url_id').value,
        data: {
            'id':db_id,
            'name':name_s,
            'status':status_s,

        },
        dataType: "json",
        success: function (data) {
            // alert(data.error_msg+data.sucscess_msg);
            if(data.error_msg){
                noty({ text:  data.error_msg ,timeout: 1000, layout: 'topRight', type: 'error'}).show();  
            setTimeout(function(){
                location.reload(true);

            }, 2000); 
            }

            if(data.success_msg){
                noty({ text: data.success_msg, timeout: 1000, layout: 'topRight', type: 'success'}).show();
            setTimeout(function(){
                 location.reload(true);

            }, 2000); 
            }
            document.getElementById("disabled_btn").disabled=false;
            document.getElementById("disabled_btn").innerHTML="update"
            
        },
        error: function (error) {
            console.log(error);
        }

    });

}


//DIVISION

function div_delete_row(row){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url=document.getElementById('delete_url_id').value;

        $.ajax({
            type: "GET",
            url:  delete_url,
            data: {
                'id':row
            },
            dataType: "json",
            success: function (data) {
                if('success' in data){
                    $('#'+ row ).hide("slow",function(){
                        $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else{
                alert(data.error);
            }
                
            },
            error: function (error) {
                console.log(error)
            }

        });
    });
}


        
   
    


function edit_div(div_id){
    document.getElementById('spinner'+div_id).className="fa fa-spinner";
    document.getElementById("edit_data").value=div_id;
    // alert(dpt_id)
    // var name = $("#name").val();


    
    $.ajax({
        type: "GET",
        url:  document.getElementById('url_id').value,
        data: {
            'id':div_id
        },
        dataType: "json",
        success: function (data) {
            document.getElementById('div_name_id').value=data.name;
            document.getElementById('div_status_id').value=data.status;
            $('#modal_basic').modal("show");
            document.getElementById('spinner'+div_id).className="fa fa-pencil";

        },
        error: function (error) {
            console.log(error);
        }

    });
    
}



function update_div(){
    document.getElementById("disabled_btn").disabled=true;
    document.getElementById("disabled_btn").innerHTML="loading.."
    
    var name_s=document.getElementById("div_name_id").value
    var status_s=document.getElementById("div_status_id").value
    var db_id=document.getElementById("edit_data").value
    $.ajax({
        type: "GET",
        url:  document.getElementById('update_url_id').value,
        data: {
            'id':db_id,
            'name':name_s,
            'status':status_s,

        },
        dataType: "json",
        success: function (data) {
            // alert(data.error_msg+data.sucscess_msg);
            if(data.error_msg){
                noty({ text:  data.error_msg ,timeout: 1000, layout: 'topRight', type: 'error'}).show();  
            setTimeout(function(){
                location.reload(true);

            }, 2000); 
            }

            if(data.success_msg){
                noty({ text: data.success_msg, timeout: 1000, layout: 'topRight', type: 'success'}).show();
            setTimeout(function(){
                 location.reload(true);

            }, 2000); 
            }
            document.getElementById("disabled_btn").disabled=false;
            document.getElementById("disabled_btn").innerHTML="update"
            
        },
        error: function (error) {
            console.log(error);
        }

    });

}

//EMPLOYEE

function emp_delete_row(row){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url=document.getElementById('delete_url_id').value;

        $.ajax({
            type: "GET",
            url:  delete_url,
            data: {
                'id':row
            },
            dataType: "json",
            success: function (data) {
                if('success' in data){
                    $('trow'+ row ).hide("slow",function(){
                        $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else{
                alert(data.error);
            }
                
            },
            error: function (error) {
                console.log(error)
            }

        });
    });
}


        
   
    


function edit_emp(emp_id){
    document.getElementById('spinner'+emp_id).className="fa fa-spinner";
    document.getElementById("edit_data").value=emp_id;
    // alert(dpt_id)
    // var name = $("#name").val();


    
    $.ajax({
        type: "GET",
        url:  document.getElementById('url_id').value,
        data: {
            'id':emp_id
        },
        dataType: "json",
        success: function (data) {
            document.getElementById('emp_name_id').value=data.name;
            document.getElementById('emp_area_id').value=data.area;
            document.getElementById('emp_status_id').value=data.status;
            $('#modal_basic').modal("show");
            document.getElementById('spinner'+dpt_id).className="fa fa-pencil";

        },
        error: function (error) {
            console.log(error);
        }

    });
    
}



function update_emp(){
    document.getElementById("disabled_btn").disabled=true;
    document.getElementById("disabled_btn").innerHTML="loading.."
    
    var name_s=document.getElementById("emp_name_id").value
    var area_s=document.getElementById("emp_area_id").value
    var status_s=document.getElementById("emp_status_id").value
    var db_id=document.getElementById("edit_data").value
    $.ajax({
        type: "GET",
        url:  document.getElementById('update_url_id').value,
        data: {
            'id':db_id,
            'name':name_s,
            'area':area_s,
            'status':status_s,

        },
        dataType: "json",
        success: function (data) {
            // alert(data.error_msg+data.sucscess_msg);
            if(data.error_msg){
                noty({ text:  data.error_msg ,timeout: 1000, layout: 'topRight', type: 'error'}).show();  
            setTimeout(function(){
                location.reload(true);

            }, 2000); 
            }

            if(data.success_msg){
                noty({ text: data.success_msg, timeout: 1000, layout: 'topRight', type: 'success'}).show();
            setTimeout(function(){
                 location.reload(true);

            }, 2000); 
            }
            document.getElementById("disabled_btn").disabled=false;
            document.getElementById("disabled_btn").innerHTML="update"
            
        },
        error: function (error) {
            console.log(error);
        }

    });

}

//SUBJECT
function sub_delete_row(row){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url=document.getElementById('delete_url_id').value;

        $.ajax({
            type: "GET",
            url:  delete_url,
            data: {
                'id':row
            },
            dataType: "json",
            success: function (data) {
                if('success' in data){
                    $('#'+ row ).hide("slow",function(){
                        $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else{
                alert(data.error);
            }
                
            },
            error: function (error) {
                console.log(error)
            }

        });
    });
}


        
   
    


function edit_sub(sub_id){
    document.getElementById('spinner'+sub_id).className="fa fa-spinner";
    document.getElementById("edit_data").value=sub_id;
    // alert(dpt_id)
    // var name = $("#name").val();


    
    $.ajax({
        type: "GET",
        url:  document.getElementById('url_id').value,
        data: {
            'id':sub_id
        },
        dataType: "json",
        success: function (data) {
            document.getElementById('sub_name_id').value=data.name;
            document.getElementById('sub_status_id').value=data.status;
            document.getElementById('sub_class_id').value=data.class_details;
            $('#modal_basic').modal("show");
            document.getElementById('spinner'+sub_id).className="fa fa-pencil";

        },
        error: function (error) {
            console.log(error);
        }

    });
    
}



function update_sub(){
    document.getElementById("disabled_btn").disabled=true;
    document.getElementById("disabled_btn").innerHTML="loading.."
    
    var name_s=document.getElementById("sub_name_id").value
    var status_s=document.getElementById("sub_status_id").value
    var db_id=document.getElementById("edit_data").value
    $.ajax({
        type: "GET",
        url:  document.getElementById('update_url_id').value,
        data: {
            'id':db_id,
            'name':name_s,
            'status':status_s,

        },
        dataType: "json",
        success: function (data) {
            // alert(data.error_msg+data.sucscess_msg);
            if(data.error_msg){
                noty({ text:  data.error_msg ,timeout: 1000, layout: 'topRight', type: 'error'}).show();  
            setTimeout(function(){
                location.reload(true);

            }, 2000); 
            }

            if(data.success_msg){
                noty({ text: data.success_msg, timeout: 1000, layout: 'topRight', type: 'success'}).show();
            setTimeout(function(){
                 location.reload(true);

            }, 2000); 
            }
            document.getElementById("disabled_btn").disabled=false;
            document.getElementById("disabled_btn").innerHTML="update"
            
        },
        error: function (error) {
            console.log(error);
        }

    });

}

function showDropdowns(){
    var emp_cat=document.getElementById("Employee");
    var additionalDropdowns=document.getElementById("additionalDropdowns");

        if(emp_cat.value === '4'){// change 'desired value ' to the actual value u r checking
            additionalDropdowns.style.display = "block";
        }
        else{
            additionalDropdowns.style.display = "none";
        }
  }
  



  