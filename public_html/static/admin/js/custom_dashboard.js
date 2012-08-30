function ChangeCuponator()
{
    var button = $('button#cuponator');
    $.ajax({
        url: '/change_cuponator/',
        type: 'GET',
        dataType:'json',
        success: function(data){
            button.empty();
            button.append(data[0]);
            button.removeClass();
            button.addClass(data[1]);
        }
    });
}