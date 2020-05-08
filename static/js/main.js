const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

<<<<<<< HEAD

=======
/* This will fade out the error message on register and login. You may need to first clear the cache in the browser for it to work with shift + F5 (windows)  cmd + shift + r (mac) */
>>>>>>> e6bb281abdc5b67e5d8be6f5bdf515f4c772e6be
setTimeout(function(){
  $('#message').fadeOut('slow')
}, 3000)