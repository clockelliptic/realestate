const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(() => { $('#messages-box').fadeOut('slow') }, 3000)
