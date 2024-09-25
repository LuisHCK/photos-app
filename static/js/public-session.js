/**
 * Preview the selected photo in a modal
 * @param {Event} event
 * @returns {void}
 */
function openPreview(event) {
    const $container = document.querySelector('#photo-modal-content')
    const $buttonSouce = event.target.parentElement

    // Create a new <img> element
    const $img = document.createElement('img')
    $img.classList.add('photo-preview')
    $img.src = $buttonSouce.dataset.url
    $img.alt = $buttonSouce.dataset.alt || 'Image preview'

    // Replace the content of the modal with the new image
    $container.replaceChildren($img)
}
