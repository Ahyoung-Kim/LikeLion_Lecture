const animal = document.getElementsByClassName("animal")
const animals = document.querySelector("#animals")

animal[0].style.color = 'red';
animal[1].style.color = 'green';
animal[2].style.color = 'blue';

animal[0].innerText = "dog";

animals.innerHTML += "<li>cat</li>"

const box = document.querySelector('.box')

box.classList.add('purple')
box.classList.remove('purple')

box.classList.toggle('yellow')  // yellow 클래스가 있다면 제거하고, 없다면 추가 