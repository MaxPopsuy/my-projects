const btnRef = document.querySelector('.test');
const randomAction = ['Don`t CLICK', 'Stop Please!!!', 'If u click - u die!', 'Kazahstan space program activated!'];

function changeBtn (e) {
	console.log("Worked");
	
};

btnRef.addEventListener('click', () => {
	btnRef.textContent = randomAction[Math.floor(Math.random()*4)];
});

