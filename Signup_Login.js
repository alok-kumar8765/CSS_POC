const signIpbtnLink=document.querySelector("signInbtnLink");
const signUpbtnLink=document.querySelector("signUpbtnLink");
const wrapper = document.querySelector('.wrapper');

signInbtnLink.addEventListener("click",()=>{
    wrapper.classList.toggle("active");
});
signUpbtnLink.addEventListener("click",()=>{
    wrapper.classList.toggle("active")
});