"use strict";

$(document).ready(function (){    //запускается функция
    $(".reply").on("click", function (){    // при клике на класс reply добавляется иветн - click и запускается функция
        var parentId = $(this).attr("data-id")    // получение id
        $("#form-"+parentId).fadeToggle();
    })
    $(".submit-reply").on("click", function (e){    // при отправке на сервер (плике на submit_reply)
        e.preventDefault()
        var parentId = $(this).attr("data-submit-reply")
        var id = $(this).attr("data-id")
        var text = $("#form-"+id).find("textarea[name='comment-text']").val();
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');
        data = {
            user : "{{ request.user.username }}",
            parentId: parentId,
            text: text,
            id: id,
            csrfmiddlewaretoken: csrftoken
        }
        // Ajax запрос на Django
        $.ajax({
            method: "POST",    // метод запроса
            data: data,    // передача данных
            url: "{% url 'comment_child_create' %}"    // URL
            success: function (data){    // если комментарий успешно добавился
                window/location.replace("/post-comments")    // редирект на страницу
            }
        })
    })
})