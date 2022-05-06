function tryLuck(url) {
    $.ajax({
        url: url,
        cache: false
    }).done(contents => {
        $('#result').append(contents.replace('\n', '<br />') + '<br />');
    });
}
