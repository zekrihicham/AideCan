
$('.a').each(function(index){
    $(this).hover(function(){
        $(this).find('p').css('color','green');
        $(this).find('p').css('border-bottom','solid 2px');

    },function(){
        $(this).find('p').css('color','black');

        $(this).find('p').css('border-bottom','');

    });
 
    

  

});

   var i=0;
    
    $('#burger').on("click", function(){
     $('.a').fadeToggle("slow");
        
}); 


$(window).resize(function(){

       if ($(window).width() > 991) {  
        $('.a').fadeIn();

       }     

});
