/*const btn = document.querySelector('#btn')

btn.addEventListener('click', function(){
  console.log('click!');
})

const plus = document.querySelector('#plus')
const num = document.querySelector('#num')
const minus = document.querySelector('#minus')

let n = 0

plus.addEventListener('click', function(){
  n++;
  num.innerText = n;
})
minus.addEventListener('click', function(){
  n--;
  num.innerText = n;
});

const bar = document.querySelector('.bar')
const newbar = document.querySelector('.newBar')

bar.addEventListener('click', function(){
  //newbar.style.display = "block";
  newbar.classList.toggle('show')
  bar.innerText = '눌렀어'
});*/

const lis = document.querySelectorAll('.tab-button')
const contents = document.querySelectorAll('.tab-content')

lis.forEach(function(li, idx){
  li.addEventListener('click', function(){
    lis.forEach(function(l){
      l.classList.remove('here')
    })
    contents.forEach(function(content){
      content.classList.remove('show')
    })
    li.classList.add('here')
    contents[idx].classList.add('show')
  })
})