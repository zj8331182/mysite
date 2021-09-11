const baseUrl = 'http://127.0.0.1:8000/backend/';
const allDepartments = [
    {
        value: "sale",
        label: "销售部",
    },
    {
        value: "market",
        label: "市场部",
    },
    {
        value: "office",
        label: "办公室",
    },
    {
        value: "randd",
        label: "研发部",
    },
];

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export default {
    baseUrl,
    allDepartments,
    getCookie,
}