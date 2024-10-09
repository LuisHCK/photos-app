const MODAL_IFRAME_ID = 'tier-modal-iframe'

function createIframe(src) {
    const iframe = document.createElement('iframe')
    iframe.id = MODAL_IFRAME_ID
    iframe.src = src
    iframe.height = '500'
    return iframe
}

function destroyIframe() {
    const iframe = document.getElementById(MODAL_IFRAME_ID)
    iframe.remove()
}

function openEditModal(packageId, tierId) {
    const $modalContainer = document.getElementById('tier-form-modal').querySelector('.modal-card')
    const iframe = createIframe(`/packages/${packageId}/tiers/${tierId}/edit/`)
    $modalContainer.replaceChildren(iframe)
}

function openCreateModal(packageId) {
    const $modalContainer = document.getElementById('tier-form-modal').querySelector('.modal-card')
    const iframe = createIframe(`/packages/${packageId}/tiers/create/`)
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
    }).then(response => response.text()).then((html) => {
        $tierList.innerHTML = html
    })
}

document.addEventListener('DOMContentLoaded', () => {
    window.addEventListener(
        'message',
        function (e) {
            if (e.data === 'tierFormSubmitted') {
                closeModal()
            }
        },
        false
    )
})
