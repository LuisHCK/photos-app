const MODAL_IFRAME_ID = 'tier-modal-iframe'
const TIER_FORM_MODAL = 'tier-form-modal'

const PHOTO_SAMPLE_IFRAME_ID = 'photo-sample-delete-modal-iframe'
const PHOTO_SAMPLE_MODAL = 'photo-sample-delete-modal'

function createIframe(src, id = '', height = 640) {
    const iframe = document.createElement('iframe')
    iframe.id = id
    iframe.src = src
    iframe.height = height
    return iframe
}

function destroyIframe() {
    const iframe = document.getElementById(MODAL_IFRAME_ID)
    iframe.remove()
}

function openEditModal(packageId, tierId) {
    const $modal = document.getElementById(TIER_FORM_MODAL)
    const $modalContainer = $modal.querySelector('.modal-card')
    const iframe = createIframe(`/packages/${packageId}/tiers/${tierId}/edit/`, MODAL_IFRAME_ID)
    $modalContainer.replaceChildren(iframe)
    $modal.classList.add('is-active')
}

function openCreateModal(packageId) {
    const $modalContainer = document.getElementById(TIER_FORM_MODAL).querySelector('.modal-card')
    const iframe = createIframe(`/packages/${packageId}/tiers/create/`, MODAL_IFRAME_ID)
    $modalContainer.replaceChildren(iframe)
}

function closeModal() {
    document.querySelectorAll('.modal').forEach(($modal) => {
        $modal.classList.remove('is-active')
    })
    destroyIframe()
    updateTierList()
}

function updateTierList() {
    const $tierList = document.getElementById('tier-list')
    const listUrl = window.location.pathname.replace('/edit/', '/tiers/')

    fetch(listUrl, {
        method: 'get',
        headers: {
            'x-requested-with': 'XMLHttpRequest'
        }
    })
        .then((response) => response.text())
        .then((html) => {
            $tierList.innerHTML = html
        })
}

function photoExampleOnChange(event) {
    const files = event.target.files
    const $samplePhotosName = document.getElementById('sample-photos-name')

    if (files.length > 0) {
        let fileNames = []
        for (let i = 0; i < files.length; i++) {
            fileNames.push(files[i].name)
        }
        $samplePhotosName.innerHTML = fileNames.join(', ')
    } else {
        $samplePhotosName.innerHTML = $samplePhotosName.dataset.label
    }
}

function openDeleteSamplePhotoModal(event) {
    const $modal = document.getElementById(PHOTO_SAMPLE_MODAL)
    const $modalContainer = $modal.querySelector('.modal-card')
    const iframe = createIframe(event.target.dataset.url, PHOTO_SAMPLE_IFRAME_ID, 380)
    $modalContainer.replaceChildren(iframe)
    $modal.classList.add('is-active')
}

function closeDeleteSampleModal() {
    document.querySelectorAll('.modal').forEach(($modal) => {
        $modal.classList.remove('is-active')
    })

    const iframe = document.getElementById(PHOTO_SAMPLE_IFRAME_ID)
    iframe.remove()
    window.location.reload()
}

document.addEventListener('DOMContentLoaded', () => {
    window.addEventListener(
        'message',
        function (e) {
            if (e.data === 'tierFormSubmitted') {
                closeModal()
            }

            if (e.data === 'closePhotoSampleModal') {
                closeDeleteSampleModal()
            }
        },
        false
    )
})
