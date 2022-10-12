function calculate_fuel_value(){
  $fuel_values = $(".fuel_value");

  $fuel_values.each(function(){
    $value = $(this).text().split(",");
    var sum = 0;
    for (let i=0; i<$value.length; i++){
      $v = $.trim($value[i])
      if ($v!=""){
        sum += Number($v)
      }
    }
    $(this).text(sum)
  })
}


function calculate_expense_values(){
    $oil_values = $(".the_value");

    $oil_values.each(function(){
        $value = $(this).text().split(",");
        var sum = 0;
        for (let i=0; i<$value.length; i++){
        $v = $.trim($value[i])
        if ($v!=""){
            sum += Number($v)
        }
        }
        $(this).text(sum)
    })
}














// calculate_fuel_value();
calculate_expense_values();

