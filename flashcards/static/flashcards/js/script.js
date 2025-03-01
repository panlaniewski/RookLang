
const searchElement = document.querySelector('.search-header__wrapper');
const searchButton = document.querySelector('.search-header__btn');
const body = document.querySelector('body');

searchButton.addEventListener('click', () => {
    searchElement.classList.toggle('search-header__btn_active');
    body.classList.toggle('search_lock');
})
