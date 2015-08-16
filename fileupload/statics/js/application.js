$(function () {

    $(document).bind('dragover', function (e) {
        var dropZone = $('#dropzone');
        var found = false,
            node = e.target;
        do {
            if (node === dropZone[0]) {
                found = true;
                break;
            }
            node = node.parentNode;
        } while (node != null);
        if (found) {
            dropZone.addClass('hover');
        } else {
            dropZone.removeClass('hover');
        }
    });

    /*global window, $ */
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    var url = "/import_allocation_data/";
    var csrftoken = $.cookie('csrftoken');
    $('#fileupload').fileupload({
        url: url,
        crossDomain: false,
        dropZone: $('#dropzone'),
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        dataType: 'json',
        progressall: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            $('#progress .bar').css(
                'width',
                progress + '%'
            );
        },
        done: function (e, data) {
            $('#progress .bar').css(
                'width',
                '0%'
            );
            var info = "Total Rows: 100, Total Employees: 100, Error Rows: 30";
            $('#resultInfo').text(info);
            loadImportResult('tablecontent', 'testgrid')

            $.each(data.result.files, function (index, file) {
                $('<p/>').text(file.name).appendTo(document.body);
            });
        }
    });
    // loadImportResult('tablecontent', 'testgrid');
});

