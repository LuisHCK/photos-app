'use strict'
const MAX_WIDTH = 128
const MAX_HEIGHT = 128

/**
 * Conserve aspect ratio of the original region. Useful when shrinking/enlarging
 * images to fit into a certain area.
 *
 * @param {Number} srcWidth width of source image
 * @param {Number} srcHeight height of source image
 * @param {Number} maxWidth maximum available width
 * @param {Number} maxHeight maximum available height
 * @return {Object} { width, height }
 */
function calculateAspectRatioFit(srcWidth, srcHeight, maxWidth, maxHeight) {
    var ratio = Math.min(maxWidth / srcWidth, maxHeight / srcHeight)
    return { width: srcWidth * ratio, height: srcHeight * ratio }
}

/**
 * Compress the image and render it to the target element
 * @param {File} file
 * @param {HTMLImageElement} target
 */
function renderImage(file, target) {
    const reader = new FileReader()
    reader.readAsDataURL(file)

    reader.onloadend = function (e) {
        let image = new Image()

        image.onload = function (ev) {
            const canvas = document.createElement('canvas')
            // Calculate the aspect ratio of the image
            const { width, height } = calculateAspectRatioFit(
                image.width,
                image.height,
                MAX_WIDTH,
                MAX_HEIGHT
            )
            canvas.width = width
            canvas.height = height

            const ctx = canvas.getContext('2d')
            ctx.drawImage(image, 0, 0, width, height)

            // Resize the image to the desired size
            target.src = canvas.toDataURL('image/jpeg', 0.7)
            target.classList.remove('skeleton-block')
        }
        image.src = e.target.result
    }
}

/**
 * Remove a file from the input and the preview container
 * @param {number} fileIndex
 * @param {HTMLDivElement} container
 * @param {HTMLInputElement} fileInput
 * @return {void}
 */
function removeFile(fileIndex, container, fileInput) {
    container.remove()
    URL.revokeObjectURL(fileInput.files[fileIndex])

    // Remove the file from the input
    const fileBuffer = new DataTransfer()

    for (let i = 0; i < fileInput.files.length; i++) {
        if (i !== fileIndex) {
            fileBuffer.items.add(fileInput.files[i])
        }
    }

    fileInput.files = fileBuffer.files
}

document.addEventListener('DOMContentLoaded', () => {
    const $fileInput = document.getElementById('photos')
    const $fileUploader = document.querySelector('.file-uploader')

    // Listen for file input change
    $fileInput.addEventListener('change', (e) => {
        const files = e.target.files

        // Loop through each file
        for (let i = 0; i < files.length; i++) {
            const file = files[i]

            // Create image container
            const $container = document.createElement('div')
            $container.classList.add('file-uploader-image-container')
            $container.id = `file-uploader-image-${i}`

            // Create a new <img> element
            const $img = document.createElement('img')
            renderImage(file, $img)
            $img.alt = file.name
            $img.classList.add('file-uploader-image', 'skeleton-block')

            // Create delete button
            const $deleteButton = document.createElement('button')
            $deleteButton.type = 'button'
            $deleteButton.classList.add('file-uploader-delete-button', 'delete')
            $deleteButton.addEventListener('click', () => removeFile(i, $container, $fileInput))

            // Add delete button to the image container
            $container.appendChild($deleteButton)

            // Add the <div> element to the preview container
            $container.appendChild($img)

            // Add the <img> element to the preview container
            $fileUploader.querySelector('#file-uploader-preview').appendChild($container)
        }
    })
})
