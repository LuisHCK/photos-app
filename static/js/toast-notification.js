// Harcode styles here
const styles = `
    position: fixed;
    top: 1rem;
    right: 1rem;
    width: 300px;
    max-width: 100%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    z-index: 1000;
`

/**
 * Show toast nofitication
 * @param {{ message: string, duration: number, variant: string }} param0
 */
function toast({ message, duration = 3000, variant }) {
    const container = document.createElement('div')
    const closeButton = document.createElement('button')

    container.classList.add('notification')

    if (variant) {
        container.classList.add(`is-${variant}`)
    }

    // Setup styling
    container.style.cssText = styles

    // Setup close button
    closeButton.classList.add('delete')
    closeButton.type = 'button'

    // Append content to parent notification cotainer
    container.appendChild(closeButton)
    container.appendChild(document.createTextNode(message))

    document.body.appendChild(container)

    // Close notification after duration
    setTimeout(() => {
        container.remove()
    }, duration)

    closeButton.addEventListener('click', () => {
        container.remove()
    })
}

document.addEventListener('DOMContentLoaded', () => {
    window.Toast = toast
})
