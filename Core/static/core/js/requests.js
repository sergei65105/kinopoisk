const sendPost = async (url, data) => {
    return await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data)
    });
}

const sendGet = async (url, data) => {
    return await fetch(`${url}?${new URLSearchParams(data).toString()}`);
}

function getCookie(name) {
    let cookie = document.cookie.split('; ').find(row => row.startsWith(name + '='));
    return cookie ? cookie.split('=')[1] : null;
}