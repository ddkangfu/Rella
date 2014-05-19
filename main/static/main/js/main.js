$(function(){
    $('input:radio[name="tasksRadios"]').click(function(){
        var val = $('input:radio[name="tasksRadios"]:checked').val();
        $.get('/task/svn/' + val + '/', {'t': new Date().getTime()}, function(data){
            //alert("Data Load:" + data.author);
            $('#svn_revision').text(data.revision);
            $('#svn_author').text(data.author);
            $('#svn_date').text(data.date);
            $('#svn_message').text(data.message);
        }, 'json');
    });
});