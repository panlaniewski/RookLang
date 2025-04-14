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
const wordElement = flashcardsContainer.querySelector('[data-flashcard="word"]');
const translateElement = flashcardsContainer.querySelector('[data-flashcard="translate"]');
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
        const id = parseInt(item.id);
        const flashcards = await fetchFlashcards();
        if (flashcards) {
            const flashcardData = flashcards.find(flashcard => flashcard.id === id);
            console.log(flashcardData);
            createFlashcard(flashcardData);
        }
    });
});

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
// ------------------------------------------------------------------------------------------------------------------
const repeatButton = document.getElementById('btn-repeat');
const learnContainer = document.querySelector('.page__learn');
const learnWrapper = document.querySelector('.learn__wrapper');
const learnWord = learnContainer.querySelector('[data-flashcard="word"]');
const learnTranslate = learnContainer.querySelector('[data-flashcard="translate"]');
const nextButton = document.querySelector('.learn__next');

let shuffled_flashcards = [];
let index = 0;

repeatButton.addEventListener('click', async (event) => {
    event.stopPropagation();
    shuffled_flashcards = shuffle(await fetchFlashcards());
    index = 0;

    learnContainer.style.display = 'flex';
    learnWrapper.style.display = 'flex';

    showFleshcard(index);
    nextButton.style.display = 'block'; 
});

function showFleshcard(index) {
    if (index < shuffled_flashcards.length) {
        const card = shuffled_flashcards[index];
        learnWord.innerHTML = card.word;
        learnTranslate.innerHTML = card.translate;
    } else {
        learnContainer.style.display = 'none'; 
    }
}

nextButton.addEventListener('click', () => {
    index++;
    showFleshcard(index);
});

learnWrapper.addEventListener('click', () => {
    learnWrapper.classList.toggle('is_flipped');
    nextButton.style.display = 'block';
})

function shuffle(array) {
    let result = array;
    if (array) {
        for (let i = array.length - 1; i > 0; i--) {
            let j = Math.floor(Math.random() * (i + 1));
            [result[i], result[j]] = [result[j], result[i]];
        }
    }
    return result;
}

window.document.addEventListener('click', event => {
    if (!event.target.closest('.popup__wrapper')) {
        flashcardsContainer.style.display = 'none';
    }
})


