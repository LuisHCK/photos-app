// Common dashboard functions

/**
 * Handles new photoshoot submission
 * @param {Event} event
 * @returns {void}
 */
async function submitForm(event) {
    event.preventDefault()
    const formData = new FormData(event.target)
    formData.append['source'] = 'dynamic-tier-form'

    $submitButton = event.target.querySelector('button[type="submit"]')
    $submitButton.disabled = true
    $submitButton.classList.add('is-loading')

    displayProgress()
    let response

    try {
        response = await axios.post('', formData, {
            onUploadProgress: updateProgress,
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
    } catch (error) {
        console.error(error)
    }

    hideProgress()

    if (response && response.status === 200) {
        return location.replace('/dashboard/')
    }

    $submitButton.disabled = false
    $submitButton.classList.remove('is-loading')
}

/**
 * Display progress bar
 * @returns {void}
 */
function displayProgress() {
    $progress = document.querySelector('#form-upload-progress')
    $progress.classList.remove('is-hidden')
}

/**
 * Hide progress bar
 * @returns {void}
 */
function hideProgress() {
    $progress = document.querySelector('#form-upload-progress')
    $progress.classList.add('is-hidden')
}

/**
 * Update progress bar
 * @param {ProgressEvent} progressEvent
 */
function updateProgress(progressEvent) {
    if (!progressEvent) {
        return
    }

    const { loaded, total } = progressEvent
    let precentage = Math.floor((loaded * 100) / total)
    $progress = document.querySelector('#form-upload-progress')
    $progress.value = precentage
    $progress.innerHTML = `${precentage}%`
}

/**
 * Delete a photo from the photoshoot
 * @param {string} photoId Photo ID
 * @param {string} url URL to delete photo
 * @param {string} csrftoken CSRF token
 * @returns {void}
 */
function deletePhoto(photoId, url, csrftoken) {
    axios
        .post(
            url,
            {
                csrfmiddlewaretoken: csrftoken
            },
            {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }
        )
        .then((response) => {
            if (response.status === 200) {
                removePhoto(photoId)
            }
        })
        .catch((error) => {
            console.error(error)
        })
    const photo = document.getElementById(`uploaded-photo-${photoId}`)
    photo.remove()
}

/**
 * Initialize dropdowns
 * @returns {void}
 */
function initDropdowns() {
    const $dropdowns = document.querySelectorAll('.dropdown-trigger')

    $dropdowns.forEach(($dropdown) => {
        $dropdown.addEventListener('click', (event) => {
            event.stopPropagation()
            $dropdown.parentElement.classList.toggle('is-active')
        })

        document.addEventListener('click', (event) => {
            if (!$dropdown.contains(event.target)) {
                $dropdown.parentElement.classList.remove('is-active')
            }
        })
    })
}

/**
 * Copy photoshoot link to clipboard if supported by the browser
 * @param {Event} event
 * @returns {void}
 */
function copyLink(event) {
    const url = `${window.location.origin}${event.target.dataset.url}`

    if (!navigator.clipboard) {
        Toast({ message: event.target.dataset.error, variant: 'danger' })
        return
    }

    navigator.clipboard.writeText(url)
    Toast({ message: event.target.dataset.success, variant: 'success' })
}

/**
 * Share link using web share api if supported by the browser
 * @param {Event} event
 * @returns {void}
 */
function webShare(event) {
    if (!navigator.share) {
        Toast({ message: event.target.dataset.error, variant: 'danger' })
        return
    }

    if (!event.target.dataset) {
        return Toast({ message: event.target.dataset.error, variant: 'danger' })
    }

    navigator.share({
        title: event.target.dataset.tile,
        text: event.target.dataset.text,
        url: `${window.location.origin}${event.target.dataset.url}`
    })
}

document.addEventListener('DOMContentLoaded', () => {
    initDropdowns()
})
