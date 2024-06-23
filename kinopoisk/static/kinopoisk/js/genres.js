const genresContainer = document.querySelector('.genres_container');
async function getGenres() {
    return await sendGet('/get_genres/', {})
}
getGenres().then(async (response) => {
    console.log(response)
    if (response.status === 200) {
        const data = await response.json()
        console.log(data)
        for (const genre of data) {
            genresContainer.appendChild(createGenreEl(genre));
        }
    }
})

function createGenreEl(genre) {
    const genreEl = document.createElement('a');
    genreEl.className='btn border-1 border border-secondary hover-scale-3';
    genreEl.setAttribute('href', `/genre/${genre.id}/`)
    genreEl.innerHTML = `${genre.name[0].toUpperCase()}${genre.name.slice(1, genre.name.length)}`

    return genreEl;
}