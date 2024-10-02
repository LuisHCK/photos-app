function scrollToSecion(id) {
    const element = document.getElementById(id)
    element.scrollIntoView({ behavior: 'smooth', block: 'start' })
}

document.addEventListener('DOMContentLoaded', () => {
    const backToTopButton = document.getElementById('back-to-top')
    const $heroSection = document.getElementById('main-hero-section')
    const $heroVideo = document.getElementById('hero-video-player')

    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    })

    window.addEventListener('scroll', () => {
        // Back to top button
        if (window.scrollY > 100) {
            document.querySelector('.back-to-top').style.display = 'flex'
        } else {
            document.querySelector('.back-to-top').style.display = 'none'
        }

        // Stop video when scrolling
        if (window.scrollY > $heroSection.offsetHeight - 100) {
            $heroVideo.pause()
        } else {
            $heroVideo.play()
        }
    })
})
