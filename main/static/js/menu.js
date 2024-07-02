$(document).ready(function() {
    $('#icon-toggle').on('click', function() {
        var icon = $('#icon');
        var iconAlternate = $('#icon-alternate');
        var body = $('body');

        if (icon.css('display') === 'none') {
            icon.css('display', 'block');
            iconAlternate.css('display', 'none');
            body.attr('data-theme', 'light');
        } else {
            icon.css('display', 'none');
            iconAlternate.css('display', 'block');
            body.attr('data-theme', 'dark');
        }
    });

    $('#search-button').on('click', function() {
        var query = $('#search-box').val();
        console.log("Ищем: " + query);
    });
});