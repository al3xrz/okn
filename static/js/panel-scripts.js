
       
//--------------------------------------------------------------------------------------       
       function enable_filter(){
            $('#m_select_id').removeAttr('disabled');
            $('#l_select_id').removeAttr('disabled');
            $('#o_select_id').removeAttr('disabled');
            $('#c_select_id').removeAttr('disabled');

        }

        function disable_filter(){
            $('#m_select_id').attr('disabled', 'disabled');
            $('#l_select_id').attr('disabled', 'disabled');
            $('#o_select_id').attr('disabled', 'disabled');
            $('#c_select_id').attr('disabled', 'disabled');

        }


        function fill_category_types(){
            let dropdown = $('#c_select_id');
             dropdown.empty();
             dropdown.append('<option selected="true" value="">Все категории</option>');
             dropdown.prop('selectedIndex', 0);

             const url = '/api/category_types';

             $.getJSON(url, function (data) {
                 //console.log()
                 $.each(data['results'], function (key, entry) {
                     dropdown.append($('<option></option>').attr('value', entry.id).text(entry.name));
                 })
             })
            
         }
        
        
        
        function fill_object_types(){
            let dropdown = $('#o_select_id');
             dropdown.empty();
             dropdown.append('<option selected="true" value="">Все типы</option>');
             dropdown.prop('selectedIndex', 0);

             const url = '/api/object_types';

             $.getJSON(url, function (data) {
                 //console.log()
                 $.each(data['results'], function (key, entry) {
                     dropdown.append($('<option></option>').attr('value', entry.id).text(entry.name));
                 })
             })
         }
        
        function fill_municipality(){
            let dropdown = $('#m_select_id');
             dropdown.empty();
             dropdown.append('<option selected="true" value="">Все муниципальные образования</option>');
             dropdown.prop('selectedIndex', 0);

             const url = '/api/municipalities';

             $.getJSON(url, function (data) {
                 //console.log()
                 $.each(data['results'], function (key, entry) {
                     dropdown.append($('<option></option>').attr('value', entry.id).text(entry.name));
                 })
             })
             
         }




        function fill_locality(m_id){
            let dropdown = $('#l_select_id');
             dropdown.empty();
             dropdown.append('<option selected="true" value="0">Все населенные пункты</option>');
             dropdown.prop('selectedIndex', 0);

             const url = '/api/localities';
             if(m_id==0){
                 $.getJSON(url, function (data) {
                 //console.log()
                 $.each(data['results'], function (key, entry) {
                      dropdown.append($('<option></option>').attr('value', entry.id).text(entry.name));
                 })
             })    
             } else {
                 $.getJSON(url, function (data) {
                 //console.log()
                 $.each(data['results'], function (key, entry) {
                     if(m_id==entry.municipality){
                         dropdown.append($('<option></option>').attr('value', entry.id).text(entry.name));
                     }
                 })
             })    
             }
         }
         $(document).ready(function() {
         //-------------------------------------------------------------------------------------------






             fill_municipality();
             fill_locality(0);
             fill_object_types();
             fill_category_types();

             
             $("#modal_photo").click(function(){	// Событие клика на маленькое изображение
                var img = $(this);	// Получаем изображение, на которое кликнули
                var src = img.attr('src'); // Достаем из этого изображения путь до картинки
                
               

             });

       
             $(function(){
                     $('#c_select_id').change(function(){
                         var selector = document.getElementById('c_select_id');
                         id_category_type = selector[selector.selectedIndex].value;
                         //alert(id_category_type)
                         $.fn.dataTable.ext.search.pop(); 
                         table
                             .columns(11)
                             .search(id_category_type)
                             .draw();
                         if(id_category_type==11){
                             table
                             .columns(9)
                             .search('')
                             .draw();
                         }
                         });
              });


             $(function(){
                     $('#o_select_id').change(function(){
                         var selector = document.getElementById('o_select_id');
                         id_object_type = selector[selector.selectedIndex].value;
                         //alert(id_object_type)
                         $.fn.dataTable.ext.search.pop(); 
                         table
                             .columns(9)
                             .search(id_object_type)
                             .draw();
                         if(id_object_type==0){
                             table
                             .columns(9)
                             .search('')
                             .draw();
                         }
                         });
              });


             $(function(){
                     $('#m_select_id').change(function(){
                         var selector = document.getElementById('m_select_id');
                         id_municipality = selector[selector.selectedIndex].value;
                         $.fn.dataTable.ext.search.pop();   
                         fill_locality(id_municipality);
                         table
                             .columns(3)
                             .search(id_municipality)
                             .draw();
                         if(id_municipality==0){
                             table
                             .columns(3)
                             .search('')
                             .draw();
                         }
                             table
                             .columns(5)
                             .search('')
                             .draw();
                     });
             });

             $(function(){
                     $('#l_select_id').change(function(){
                         var selector = document.getElementById('l_select_id');
                         id_locality = selector[selector.selectedIndex].value;
                         table
                             .columns(5)
                             .search(id_locality)
                             .draw();
                         if(id_locality==0){
                             table
                             .columns(5)
                             .search('')
                             .draw();
                         }
                         });
              });


         
//-------------------------------------------------------------------------------------------------
             function is_null(data){
                 if(data!==null){
                     return data.name;
                 } else {
                 return ''
             }}
             
             function is_null_id(data){
                 if(data!==null){
                     return data.id;
                 } else {
                 return ''
             }}
            
           
             var table = $('#objects').DataTable({
                //"pageLength": 50,  
                //"search": {
                //    "regex": true
                // },
                 "iDisplayLength": 50,        
                 'initComplete': function () {
                      $("#objects_length").appendTo("#for_page_length");

                      
                  },   
                 //'orderCellsTop': true,
                 "processing":   true,
                 //"fixedHeader": {
                 //   "header": true,
                    //"footer": true
                 //},
                 "stripeClasses" : [],
                 "order": [[ 2, "asc" ]],
                 'fixedHeader': true,
                 'serverSide': false,
                 'ajax': '/api/objects/?format=datatables',
                 "language": {
                     "lengthMenu": "Показывать по &nbsp _MENU_",
                     "zeroRecords": "К сожалению ничего не найдено",
                     //"info":  "Showing _START_ to _END_ of _TOTAL_ entries",
                     "info" : "Найдено _TOTAL_  из _MAX_ ",
                     "infoEmpty": "Информация отсутствует",
                     //"infoFiltered": "(filtered from _MAX_ total records)",
                     "paginate": {
                          "previous": "<",
                          "next": ">",
                      },
                     "infoFiltered": "",

                     
                 },
                    "columns": [
                     {  //"targets": 0,
                         "data": "id",
                         "visible" : false
                     },
                     { "data": "nativeName", 
                       "width" : '20%',
                       "render": function ( data, type, row, meta ) {
                                     return '<a href="#" data-toggle="modal" data-target="#exampleModal"  data-id=' + row.id + '><b>' +data+'</b></a>' ;
                                     //return '<a href="'+row.id+'"><b>'+data+'</b></a>';
                                  },
                     },
                     { "data": "municipality",
                        "width" : '12%',
                        "render": function(data, type, row, meta ){
                             return is_null(data);
                     }},
                     { "data": "municipality",
                       "visible" : false,
                         "render": function(data, type, row, meta ){
                             return is_null_id(data);
                     }},
                     
                     { "data": "locality",
                       "width" : '8%',
                       "render": function(data, type, row, meta ){
                             return is_null(data);
                     }},
                       { "data": "locality",
                         "visible" : false,
                         "render": function(data, type, row, meta ){
                             return is_null_id(data);
                     }},
                   
                     { "data": "fullAddress",
                       "width" : '32%', },
                     { "data": "create_date",
                       "width" : '10%', },
                     { "data":  "object_type",
                       "width" : '5%',
                       "render": function(data, type, row, meta ){
                             return is_null(data);
                     }},
                     { "data":  "object_type",
                       "visible" : false,
                        "render": function(data, type, row, meta ){
                             return is_null_id(data);
                     }},
                     
                     { "data": "category_type",
                       "width" : '20%',
                       "render": function(data, type, row, meta ){
                             return is_null(data);
                        },
                    },
                     { "data": "category_type",
                       "visible" : false,
                       "render": function(data, type, row, meta ){
                             return is_null_id(data);
                     }},
                 ]
             });
         //------------------------------------------------------------------------


         function set_sizes(){
            if ($(window).width() <= 1156) 
                { 
                    table.columns(10).visible(false);
                }
                else {
                    table.columns(10).visible(true);
                }
            if ( $(window).width() <= 935) 
            { 
                table.columns(8).visible(false);
                table.columns(7).visible(false);
                table.columns(6).visible(false);
            }
            else {
                table.columns(8).visible(true);
                table.columns(7).visible(true);
                table.columns(6).visible(true);
            }
        }

        set_sizes();

         //------------------------------------------------------------------------
         $("#searchbox").on("keyup input paste cut", function() {
           if(this.value=='') {
                 enable_filter();
             }
             else {
                 disable_filter();
             }
             $('#objects').DataTable().columns(1).search('('+this.value+')', true, false).draw();
         }); 


         // забрать иноформацию об объекте
         $('#exampleModal').on('show.bs.modal', function (e) {
             var id = e.relatedTarget.dataset.id;

             const url = '/api/objects/'+id;
             $("#my_slider_id").empty();
             $.getJSON(url, function (data) {
                 if((data.nativeName!==null)&&(data.nativeName!=='None')) { 
                     $('#modal_nativeName').text(data.nativeName);  
                     $('#exampleModalLabel').text(data.nativeName);  
                 } else {
                     $('#modal_nativeName').text('');
                     $('#exampleModalLabel').text('');  
                 }
                 if((data.fullAddress!==null)&&(data.fullAddress!=='None')) { $('#modal_fullAddress').text(data.fullAddress);
                 } else {
                     $('#modal_fullAddress').text('');
                 }
                 if((data.municipality!==null)&&(data.municipality!=='None')) { $('#modal_municipality').text(data.municipality.name);
                 } else {
                     $('#modal_municipality').text('');
                 }
                 if((data.locality!==null)&&(data.locality!==null)) { $('#modal_locality').text(data.locality.name);  
                 }else {
                     $('#modal_locality').text('');
                 }
                 if(data.images.length>0){
                    for(key in data.images) {
                        console.log(data.images[key]);
                        $('#my_slider_id').
                            append("<a href='/media/" + data.images[key]+
                                   "' ><img src='/media/"+data.images[key]+
                                   "' style='width:100px; padding-left:5px'></a>");
                    
                    }
          
                 } else {
                    //   $('#modal_photo').attr('src', "/media/img/noImage.png");
                    //   $('#img_ref').attr('href', "/media/img/noImage.png");
                    $('#my_slider_id').
                    append("<img src='/media/img/noImage.png' style='width:100px;'></img>");
                  
                 }
                 if((data.description!==null)&&(data.description!=='None')) { $('#modal_description').text(data.description);  
                 } else {
                     $('#modal_description').text('');
                 }
                 if((data.affiliation_U!==null)&&((data.affiliation_U!=='None'))) { $('#modal_affiliation_U').text(data.affiliation_U);
                 } else {
                     $('#modal_affiliation_U').text('');
                 }
                 if((data.esp_valuable_object!==null)&&(data.esp_valuable_object!=='None')) { $('#modal_esp_valuable_object').text(data.esp_valuable_object);
                 } else {
                     $('#modal_esp_valuable_object').text('');
                 }
                 if((data.requisites_and_title!==null)&&(data.requisites_and_title!=='None')) { $('#modal_requisites_and_title').text(data.requisites_and_title); 
                 } else {
                     $('#modal_requisites_and_title').text('');
                 }
                 if((data.gen_species_appearance!==null)&&(data.gen_species_appearance!==null)) { $('#modal_gen_species_appearance').text(data.gen_species_appearance.name); 
                 } else {
                     $('#modal_gen_species_appearance').text('');
                 }
                 if((data.category_type!==null)&&(data.category_type!==null)) { $('#modal_category_type').text(data.category_type.name); 
                 } else {
                     $('#modal_category_type').text('');
                 }
                 if((data.reg_number!==null)&&(data.reg_number!==null)) { $('#modal_reg_number').text(data.reg_number); 
                } else {
                    $('#modal_reg_number').text('');
                }
                if((data.documents!==null)&&(data.documents!==null)) { 
                    $('#modal_documents').text(data.documents);
                    $('#modal_documents').attr("href", data.documents); 
                } else {
                    $('#modal_documents').text('');
                }
                $('#modal_url').text('http://www.oknrd.ru/objects/'+data.id)
                $('#modal_url').attr('href', '/objects/'+data.id)
                
                 
                

             })
         });


       

         });
