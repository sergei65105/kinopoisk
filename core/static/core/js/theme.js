const btnChangeTheme = document.querySelector('.btn-change-theme');

function setTheme(value) {
    if (value) {
        btnChangeTheme.src = '/static/core/img/moon.png'
        document.body.setAttribute('data-bs-theme', 'dark')
        btnChangeTheme.classList.add('white_theme_icon')
    } else {
        btnChangeTheme.src = '/static/core/img/sun.png'
        document.body.setAttribute('data-bs-theme', 'light')
        btnChangeTheme.classList.remove('white_theme_icon')
    }
    currentTheme = value
}

let currentTheme = true


function toggleTheme() {
    setTheme(!currentTheme);
    localStorage.setItem('theme', currentTheme);
}

btnChangeTheme.addEventListener('click', toggleTheme)

if (localStorage.getItem('theme') === 'false')  toggleTheme();