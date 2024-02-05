console.log("modeswitch.js loaded");
const toggle = document.getElementById('toggleDark');
const body = document.querySelector('body');

toggle.addEventListener('click', function(){
  this.classList.toggle('bi-moon');
  if(this.classList.toggle('bi-brightness-high-fill')){
    body.style.background = 'white';
    body.style.color = '#282828';
    body.style.transition = '1.5s';
  }else{
    body.style.background = '#282828';
    body.style.color = 'white';
    body.style.transition = '1.5s';
  }
})