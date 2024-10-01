function scrollToSecion(id) {
    const element = document.getElementById(id)
    element.scrollIntoView({ behavior: 'smooth', block: 'start' })
}

document.addEventListener('DOMContentLoaded', () => {
    const backToTopButton = document.getElementById('back-to-top')
    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    })
})

window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        document.querySelector('.back-to-top').style.display = 'flex'
    } else {
        document.querySelector('.back-to-top').style.display = 'none'
    }
})
