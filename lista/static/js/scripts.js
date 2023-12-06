$(document).ready(function() {

    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchform = $('#search-form')

    $(deleteBtn).on('click', function(e) {
        e.preventDefault();

        var delLink = $(this).attr('href')
        var result = confirm('Quer deletar esta tarefa?')

        if(result) {
            window.location.href = delLink;
        }
   
    });

    $(searchBtn).on('click', function(e) {
    
        searchform.submit();
    
    });
});

