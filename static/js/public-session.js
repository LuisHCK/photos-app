/**
 * Preview the selected photo in a modal
 * @param {Event} event
 * @returns {void}
 */
function openModal(event) {
    const $container = document.querySelector('#photo-modal-content')

    // Create a new <img> element
    const $img = document.createElement('img')
    $img.classList.add('photo-preview')
    $img.src = event.target.dataset.url
    $img.alt = event.target.dataset.alt || 'Image preview'

    // Replace the content of the modal with the new image
    $container.replaceChildren($img)
}
