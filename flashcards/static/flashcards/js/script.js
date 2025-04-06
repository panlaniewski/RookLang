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
// -----------------------------------------------------------------------------------------------------
const getDataUrl = 'get_data/';
const flashcardBlocks = document.querySelectorAll('.flashcard');
const flashcardsContainer = document.querySelector('.flashcards__popup');
let flashcardsCache = null;

async function fetchFlashcards() {
    if (flashcardsCache) {
        return flashcardsCache;
    }
    try {
        const response = await fetch(getDataUrl);
        const data = await response.json();
        flashcardsCache = data.flashcards;
        return flashcardsCache;
    } catch (error) {
        console.error('Ошибка:', error);
        return null;
    }
}

flashcardBlocks.forEach(item => {
    item.addEventListener('click', async () => {
        const id = item.id;
        const flashcards = await fetchFlashcards();
        if (flashcards) {
            const flashcardData = flashcards[id - 1];
            createFlashcard(flashcardData);
        }
    });
});

function createFlashcard(data) {
    flashcardsContainer.innerHTML = '';
    
    const flashcardElement = document.createElement('div');
    flashcardElement.innerHTML = `
        <div class="popup__wrapper">
            <p class="popup__translate">Перевод: ${data.translate}</p>
        </div>
    `;
    flashcardsContainer.appendChild(flashcardElement);
    flashcardsContainer.style.display = 'flex';
}


