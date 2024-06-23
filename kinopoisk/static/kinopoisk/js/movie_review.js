const movieReviewContainer = document.querySelector('.movie_reviews_container');

const reviewTextInput = document.querySelector('textarea[name="review"]')
const movieIdInput = document.querySelector('input[name="movie_id"]')
const btnSendMovieReview = document.querySelector('#btnSendMovieReview')

btnSendMovieReview.addEventListener('click', (e) => {
    e.preventDefault()
    sendReview().then((response) => {
        console.log('Review successfully sent.')
        console.log(response)
        movieReviewContainer.appendChild(createReviewEl(response))
    })
})

async function getMovieReviews() {
    return await sendGet('/get_movie_reviews/', {
        movieId: movieIdInput.value,
    })
}

getMovieReviews().then(async (response) => {
    console.log(response)
    if (response.status === 200) {
        const data = await response.json()
        console.log(data)
        for (const review of data) {
            movieReviewContainer.appendChild(createReviewEl(review));
        }
    }
})

async function sendReview() {
    const response = await sendPost('/add_movie_review/', {
        movie: movieIdInput.value,
        text: reviewTextInput.value
    })
    if (response.status === 401) {
        window.location.href = '/signin/'
        return;
    }
    return await response.json()
}

function createReviewEl(review) {
    const reviewEl = document.createElement('div');
    reviewEl.classList.add('fc', 'gap-2', 'border', 'border-1', 'border-secondary',
        'bg-transparent', 'w-100', 'rounded-2', 'my-2', 'p-2');

    const reviewAuthorName = document.createElement('h5');
    reviewAuthorName.innerHTML = review.author_name;
    reviewEl.appendChild(reviewAuthorName)

    const reviewText = document.createElement('p');
    reviewText.innerHTML = review.text;
    reviewEl.appendChild(reviewText)

    const reviewDiv = document.createElement('div');
    reviewDiv.classList.add('frsc', 'gap-2',)

    const likeAmount = document.createElement('span');
    likeAmount.innerHTML = review.votes_count;
    reviewDiv.appendChild(likeAmount)

    const likeEl = document.createElement('i');
    likeEl.setAttribute('width', '20')
    likeEl.classList.add('like-icon', 'fa-solid', 'fa-heart')
    likeEl.addEventListener("click", async () => {
        console.log('123')
        const r = await sendPost('/movie_review_vote/', {'reviewId': review.id})
        console.log(r)
        const data = await r.json()
        if (data.vote) {
            likeAmount.innerHTML = parseInt(likeAmount.innerHTML) + (result.vote === false ? 1 : -1)
            likeEl.classList.toggle('like-icon-active')
        }
    })

    reviewDiv.appendChild(likeEl)


    const createdAt = document.createElement('span');
    createdAt.innerHTML = review.created_at
    createdAt.classList.add('ms-auto')
    reviewDiv.appendChild(createdAt)

    reviewEl.appendChild(reviewDiv)
    return reviewEl;
}