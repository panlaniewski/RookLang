// -----------------------------------------------------------------------------------------------------
const searchElement = document.querySelector('.search-header__wrapper');
const searchButton = document.querySelector('.search-header__btn');
const body = document.querySelector('body');

searchButton.addEventListener('click', () => {
    searchElement.classList.toggle('search-header__btn_active');
    body.classList.toggle('_lock');
});
// -----------------------------------------------------------------------------------------------------
const burgerButton = document.querySelector('.header__burger');
const sideBar = document.querySelector('.page__sidebar');

burgerButton.addEventListener('click', function () {
   sideBar.classList.toggle('_sidebar-active');
   this.classList.toggle('_burger-active');
   body.classList.toggle('_lock');
})