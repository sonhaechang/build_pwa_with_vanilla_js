window.addEventListener('load', e => {
    const sounds = document.querySelectorAll('.sound');
    const pads = document.querySelectorAll('.pads div');

    pads.forEach((pad, index) => {
        pad.addEventListener('click', e => {
            sounds[index].currentTime = 0;
            sounds[index].play();
        })
    })
});