jQuery(document).ready(function() {
	
/* в эту переменную сохраняется начальная строка с данными */
	//var callerid_input = "041230393330313232343630393535353132313251";
	var callerid_input = "";  
	var type_CID;		//тип информации CID(1,2 байт) 04h - стандартный формат, 80h - формат SI3000
	var cid_count;	//число байт даты, времени, номера (3,4 байт)
	var cid_count_h;
//------------------------------------------------------------------------------------------
	var date_count_h; //определяет размер в байтах блока даты и времени для формата SI3000
	var date_count; //	определяет размер в Int блока даты и времени для формата SI3000
	var date_start_indx; // номер индекса начала блока в массиве строки 
//------------------------------------------------------------------------------------------
	var number_count_h; // определяет размер в байтах блока номера для формата SI3000
	var number_count; // определяет размер в Int блока номера для формата SI3000
	var number_start_indx; // номер индекса начала блока в массиве строки 
//------------------------------------------------------------------------------------------
  var name_id_h; //
  var name_id;
	var name_count_h; // определяет размер в байтах блока имени для формата SI3000
	var name_count; // пределяет размер в Int блока имени для формата SI3000
	var name_start_indx; // номер индекса начала блока в массиве строки 
//------------------------------------------------------------------------------------------
    var month_id;   //месяц 4 байта
    var month_id_h;
    var day_id;     //день 4 байта
    var day_id_h;
    var hour_id;    //час 4 байта
    var hour_id_h;
    var minute_id;  //минута 4 байта
    var minute_id_h;
    var number_id 	;  //номер - остальные байты
    var number_id_h;
    var hash; 	//контрольная сумма - последние байты
    var stsbtn = true; //определяет состояние кнопки Открыть/Закрыть детализацию
//------------------------------------------------------------------------------------   
    //функция переводит числовые 2 байти в кодировку ASCCI
    var to_ASCCI = function(item){
        var ascci="";
 				
        for(var i=0; i<item.length;i+=2){
             toint = parseInt(item.substring(i,i+2),16); //преобразуем 2 байта из строки в число
             tochar = String.fromCharCode(toint); // преобразуем с ASCCI кодировку
             ascci = ascci+tochar;   
         } 
         return ascci;
    }
   
//----------------------------  end to_ASCCI ------------------------------------------

var	to_decode = function(callerid_input){
//читаем первые два байта - тип CallerID
		 type_CID = callerid_input.substring(0,2);
		 		if(type_CID == "80")
		 			{ 
		 														//callerid_input = callerid_input.substring(0,4)+callerid_input.substring(8,callerid_input.length);
		 														cid_count_h = callerid_input.substring(2,4); // вычисляем длинну полезной в байтах информации в hex
        											  cid_count = parseInt(cid_count_h,16)*2; //преобразуем счетчик в Int в количестве бит. 
        											  //console.log(cid_count_h);
        											  //console.log(cid_count);
        											//вычислить длину даты и времени 4 и 5 бит
        											  date_start_indx = 4; 			 
        											  if(callerid_input.substring(date_start_indx,date_start_indx+2) == '01')
        											  	{ //блок date идентифицируется = 01 + следующий байт - длинна блока
        											  			 date_count_h = callerid_input.substring(date_start_indx+2,date_start_indx+4); //размер блока даты и времени в Hex
        											 				 date_count = parseInt(date_count_h,16)*2; //размер блока даты и времени в INT
        											 			
        											 				 month_id_h = callerid_input.substring(date_start_indx+4,date_start_indx+8);
    
        											 				 day_id_h = callerid_input.substring(date_start_indx+8,date_start_indx+12);	
        											 			
        											 				 hour_id_h = callerid_input.substring(date_start_indx+12, date_start_indx+16);
        											 			
        											 				 minute_id_h = callerid_input.substring(date_start_indx+16, date_start_indx+20);	
        											  	}
        											  else
        											  	{
        											  		alert('Неправильный идентификатор блока даты и времени(01): '+ callerid_input.substring(date_start_indx,date_start_indx+2)+
        											  						"\n Введите правильный код CallerID!");
        											  		return false;
        											  	}
        											//вычислить длинну блока с номером CAllerID
        											  number_start_indx = date_start_indx + date_count+4;
        											  if(callerid_input.substring(number_start_indx,number_start_indx+2)=='02')
        											  		{//блок number идентифицируется = 01 + следующий байт - длинна блока
        											  			number_count_h = callerid_input.substring(number_start_indx+2, number_start_indx+4); //размер блока номера в Hex
        											  			number_count = parseInt(number_count_h,16)*2; //размер блока номера в INT
        											  			number_id_h = callerid_input.substring(number_start_indx+4, number_start_indx+4+number_count);
        											  		}
        											  else
        											  		{
        											  				alert('Неправильный идентификатор номера(02): '+ callerid_input.substring(number_start_indx,number_start_indx+2)+
        											  							"\n Введите правильный код CallerID!");
        											  				return false;
        											  		}
        											// вычислить длинну блока с именем CallerID
        										    name_start_indx = number_start_indx +number_count + 4;
        										    if(callerid_input.substring(name_start_indx,name_start_indx+2) == '07')
        										    	{ //блок name идентифицируется = 07 + следующий байт - длинна блока
        										    		  name_count_h = callerid_input.substring(name_start_indx+2, name_start_indx+4); //размер блока имени в Hex
        										    	 		name_count = parseInt(name_count_h,16)*2; //размер блока имени в INT
        										    	 	 	name_id_h = callerid_input.substring(name_start_indx+4, name_start_indx+4+name_count);
        										    		  name_id = to_ASCCI(name_id_h);
        										    	}
        										    else
        										    	{
        										    		alert('Неправильный идентификатор блока имени (07): '+ callerid_input.substring(name_start_indx,name_start_indx+2)+
        											  					"\n Введите правильный код CallerID!");
        											  		return false;
        										    	}
		 														
		 			}
		 		 else { //если type_CID != 80
								cid_count_h = callerid_input.substring(2,4);
         				cid_count = parseInt(cid_count_h,16);
         				month_id_h = callerid_input.substring(4,8);
         				day_id_h = callerid_input.substring(8,12);
         				hour_id_h = callerid_input.substring(12,16);
         				minute_id_h = callerid_input.substring(16,20);
         				number_id_h = callerid_input.substring(20, 22+cid_count );
		 		 			}
// end if/else
//читаем байты. преобразуем в ASCCI с помощью функции to_ASCCI
         month_id = to_ASCCI(month_id_h);
         day_id = to_ASCCI(day_id_h);
         hour_id = to_ASCCI(hour_id_h);
         minute_id = to_ASCCI(minute_id_h);
         number_id = to_ASCCI(number_id_h);
//вывод результата в TextArea 
       $("#inputDecode").val
       	(
        	type_CID+"h.............идентификатор CID. \n"+
        	cid_count_h+"h => "+cid_count+".............число бит даты, времени, номера.\n"+
        	month_id_h+"h => ASCCI => "+month_id+"...............месяц.\n"+
        	day_id_h+"h => ASCCI => "+day_id+"...............день.\n"+
        	hour_id_h+"h => ASCCI => "+ hour_id+"...............час.\n"+
        	minute_id_h+"h => ASCCI => "+minute_id+"...............минута.\n"+
        	number_id_h+"h => ASCCI => "+number_id+"..........номер CAllerID.\n"+
        	name_id_h+"h => ASSCI =>"+name_id+".................имя callerID."
        ); //end val 
     		  //заполнить таблицу вывода информации
     		  $("#month_td").text(month_id); // месяц
     		  $("#day_td").text(day_id); // день
     		  $("#hour_td").text(hour_id);	// час
     		  $("#minute_td").text(minute_id);	// минута
     		  $("#number_td").text(number_id);	// номер
     		  $("#name_td").text(name_id);	//имя
   		 
    };
//----------------------------- end to_decode ----------------------------------------

$(':text:first').focus(); //делаем фокус на первом поле
$('#inputDecode').hide(); //при начальной загрузки, скраваем поле с выводом подробной информацией
 //отображаем & скрываем поле с подробной информацией при нажатии на слово Дешифровка
		$('#buttonDecode').click(function() {
				
				$('#inputDecode').fadeToggle(1000, function() {
					 if(stsbtn){
					 							$('#buttonDecode').html('Закрыть детализацию');
					 							 stsbtn= false; 
					 						}
					 	else{
					 				$('#buttonDecode').html('Открыть детализацию');
					 				stsbtn = true;
					 			}
				}); // end fadeToggle

		}); // end click Дешифровка
		
/*Реагируем на кнопки, начинаем рассчет  */
    $(':submit').click(function() {
    		var Selectedbutton = $(this).val(); //определить выбранную кнопку
    		switch(Selectedbutton){
    			case 'run': //нажата кнопка: Дешифровать
    									if($('#inputCallerId').val()==''){  //проверяем на пустое поле
           							 			alert("Пустую строку нельзя дешифровать!!!");
            						 			//return false; //останавливаем работу формы
            						}
            					else{  // приступаем к дешифровке
            									to_decode($('#inputCallerId').val());
            								//	return false; //останавливаем работу формы
            							 }
    									break;	
    			case 'test': // нажата кнопка: Тест - подставляем тестовый CallerID 
    										$('#inputCallerId').val('80190108303131323039323302073930303030303007044564696BE2');
    										to_decode($('#inputCallerId').val());
    									//	return false; //останавливаем работу формы
    										break;
    			case 'reset': // нажата кнопка Сброс
    										return true; // сбросить форму
    										break;
    			case 'help': // нажата кнопка Помощь
    									  $('#ModalHelp').modal('show');
    										return false; //останавливаем работу формы
    										break;
    		}     
    	return false;   //останавливаем передачу формы
	}); //end click
}); //end ready