var slider = document.getElementById("myRange");
var output = document.getElementById("value");
output.innerHTML = slider.value;
output.style.left = (Number(slider.value) - 5.5) + "%";

slider.oninput = function () {
	output.innerHTML = this.value;
	output.style.left =(Number(this.value) - 5.5) + "%";	
};
