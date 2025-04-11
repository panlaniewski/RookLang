// ------------------------------------------------------------------------------------------------------------------
const searchElement = document.querySelector('.search-header__wrapper');
const searchButton = document.querySelector('.search-header__btn');
const body = document.querySelector('body');

searchButton.addEventListener('click', () => {
    searchElement.classList.toggle('search-header__btn_active');
    body.classList.toggle('_lock');
});
// ------------------------------------------------------------------------------------------------------------------
const burgerButton = document.querySelector('.header__burger');
const sideBar = document.querySelector('.page__sidebar');

burgerButton.addEventListener('click', function () {
   sideBar.classList.toggle('_sidebar-active');
   this.classList.toggle('_burger-active');
   body.classList.toggle('_lock');
})
// ------------------------------------------------------------------------------------------------------------------
const getDataUrl = 'get_data/';
const flashcardBlocks = document.querySelectorAll('.flashcard');
const flashcardsContainer = document.querySelector('.flashcards__popup');
const wordElement = document.getElementById("flashcard_word");
const translateElement = document.getElementById("flashcard_translate");
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
    item.addEventListener('click', async (event) => {
        event.stopPropagation();
        const id = item.id;
        const flashcards = await fetchFlashcards();
        if (flashcards) {
            const flashcardData = flashcards[id - 1];
            createFlashcard(flashcardData);
        }
    });
});

window.document.addEventListener('click', event => {
    if (!event.target.closest('.popup__wrapper')) {
        flashcardsContainer.style.display = 'none';
    }
})

function createFlashcard(data) {
    wordElement.innerHTML = data.word;
    translateElement.innerHTML = data.translate;
    flashcardsContainer.style.display = 'flex';
}
// ------------------------------------------------------------------------------------------------------------------
const card = document.querySelector('.popup__wrapper');

card.addEventListener('click', () => {
    card.classList.toggle('is_flipped');
})
