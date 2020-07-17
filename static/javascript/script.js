document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('h4').onmouseover = playState;
});

function playState() {
  const h4 = document.querySelector('h4');
  h4.style.animationPlayState  = 'running';
}
