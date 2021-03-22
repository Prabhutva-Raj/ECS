$(document).ready(function() {
  $('select').material_select();
});


$.myjQuery=function(cols)
{
  $('.select').material_select();
  // setup listener for custom event to re-initialize on change
  $('select').on('contentChanged', function() {
    $(this).material_select();
  });

  for(var i=0;i<cols.length;i++)
  {
    var $newOpt_indep = $("<option>").attr("value",i).text(cols[i])
    var $newOpt_dep = $("<option>").attr("value",i).text(cols[i])
    $("#select_indep").append($newOpt_indep);
    $("#select_dep").append($newOpt_dep);

    // fire custom event anytime you've updated select
    $("#select_indep").trigger('contentChanged');
    $("#select_dep").trigger('contentChanged');
  }
}

function select_ops(cols)
{
  $.myjQuery(cols);
  var elmnt = document.getElementById("process");
  elmnt.scrollIntoView();
}


var input = document.getElementById("fileUpload");
input.addEventListener( 'change', Upload );
function Upload(event)
{
 var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
 var fileUpload = event.srcElement;

 if (regex.test(fileUpload.value.toLowerCase()))
 {
     if (typeof (FileReader) != "undefined")
     {
         var reader = new FileReader();
         reader.readAsText(fileUpload.files[0]);
         reader.onload = function (e) {
             //var table = document.createElement("table");
             var rows = e.target.result.split("\n");
             var cols = rows[0].split(",");
             select_ops(cols);
            }

     }
     else
     {
         alert("This browser does not support HTML5.");
     }
   }

   else
   {
       alert("Please upload a valid CSV file.");
   }
}
