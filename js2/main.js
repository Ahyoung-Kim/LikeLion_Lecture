//========================== 타입 변환 =============================

// 자바스크립트는 데이터 타입을 자기가 맞다고 생각하는대로 변환한다.
// 그래서 우리느 보다 정확하게 데이터 타입을 넘겨줘야 한다. 

console.log('7' * '4'); // -> 28
console.log('7' + '4'); // -> '74'
console.log('hello' * 'world'); // -> NaN


//=========================== Truthy & Falsy ========================= 
// 다른 데이터타입을 boolean으로 바꾸기

const input = prompt();  // 사용자에게 입력값 받을 수 있는 함수

// 빈 문자열이면 '' -> false로 인식
// Falsy 값: undefined, null, false, 0, '', NaN
if(input === ''){
  console.log('입력값이 없습니다.');
}else{
  console.log(input);
}

if(!input){
  console.log('입력값이 없습니다.');
}else{
  console.log(input);
}


//============================== 함수 ==============================
// 1. 입력과 출력이 선택적이다. 
function add(a, b){
  return a + b;
}
function printHello(){
  console.log('hello!');
}
function print(message){
  console.log(message)
}
function returnMyName(){
  return '김아영'
}

//2. side-effect 부가기능이 있어도 된다. 
function print(message){
  console.log(message)
}

//3. 화살표 함수 arrow-function
// 화살표 함수는 반환 코드만 있을 경우 축약형이 가능
const add2 = (a, b) => {
  return a + b;
}
const add3 = (a, b) => a + b;


// 일급 객체 First-class citizen
// [조건]
//1. 해당 타입이 변수에 할당될 수 있어야 한다. 
//2. 해당 타입이 함수의 인자로 넘어갈 수 있어야 한다.
//3. 해당 타입이 함수의 반환값으로 반환될 수 있어야 한다. 
// ex) 숫자, 불린, 문자열, undefined, null, *함수*
function exec(fn){
  fn('hello world');
}
exec(console.log);
exec(alert);

function curry(f){
  return function(a){
    return function(b){
      return f(a, b);
    }
  }
}
function sub(a, b){
  return a-b;
}
let curriedSub = curry(sub)
console.log(curriedSub(3)(1))


// ================= 비동기와 promise ==========================
// 비동기 자바스크립트 
// test.py 와 비교 
const result = fetch('https://jsonplaceholder.typicode.com/posts/1');
console.log(result)

//test.py같이 출력하기 위해선
result.then(res => res.json()).then(console.log);
console.log('test'); // test가 먼저 찍힘

// 동기: 직렬적으로. 순서대로. -> 파이썬
// 비동기: 병렬적으로. 먼저 끝나는대로. -> 자바스크립트 

// 자바스크립트가 비동기를 처리하는 법 -> 프로미스 Promise
// 프로미스의 상태
// 1. Pending: 프로미스 처리중
// 2. Fulfilled: 프로미스 이행(정상처리완료)
// 3. Rejected: 프로미스 실패(처리완료. 하지만 비정상적으로)


// ======================== 논리 연산자 심화 ============================
// && : 처음 나오는 falsy 값을 반환, 만약 둘다 truthy라면 마지막 값 반환
const me = {
  name: '김아영',
  age: 24,
  gender: 'female'
};
const someone = {
  name: '홍길동',
  age: 25,
  gender: 'male'
}

function addMilitaryStateIfMale(person){
  if(person.gender === 'male'){
    person.militaryState = false;
  }
}
addMilitaryStateIfMale(me);
addMilitaryStateIfMale(someone);
console.log(me);
console.log(someone);

function parseBoolean(value){
  if(value === true){
    return '참'
  }else if(value === false){
    return '거짓'
  }
}

if(me.militaryState !== undefined){
  console.log(parseBoolean(me.militaryState));
}
someone.militaryState !== undefined && console.log(parseBoolean(someone.militaryState));


// || : 처음 나오는 truthy 값을 반환, 만약 둘다 falsy라면 마지막 값 반환
const input2 = prompt();
console.log(input2 || '입력값이 없습니다.')


//================= 비구조화 할당 Destructing ===========================
const person = {
  name: 'neo',
  age: 20
}
// 만약 우리가 선언하고싶은 변수의 이름과
// 객체의 멤버변수 이름이 동일하다면
// const name = person.name 대신
// 이렇게 작성 가능 -> 비구조화 할당
const { name } = person
const { age } = person
//const { name, age } = person
// 배열도 가능 
// const a = arr[0]  =  const [a] = arr



// =====================스프레드 Spread =========================
// 객체나 배열의 원소들을 흩뿌리다
/*const militaryPerson = {
  name: 'neo',
  age: 20,
  militaryState: false
}*/
const militaryPerson = {
  ...me,  // 스프레드
  militaryState: false
}

const animals = ['dog', 'cat']
const another = [...animals, 'bird']

console.log(militaryPerson)
console.log(another)


//=======================레스트 Rest================================
// 나머지 아이들을 모두 모아 하나의 내용물로 만듬
const { militaryState, ...rest1 } = militaryPerson
console.log(rest1)

const numbers = [0, 1, 2, 3, 4, 5];
const [ zero, ...rest2 ] = numbers;
console.log(rest2)
