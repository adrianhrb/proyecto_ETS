const signin_container = document.querySelector('.signin_container'),
    signup_container = document.querySelector('.signup_container');
signin_container.style.display = "none"
document.addEventListener('click', e => {
    if (e.target.matches('.ok_account')) {
        signin_container.style.display = 'block';
        signup_container.style.display = "none";
    } else if (e.target.matches('.no_account')) {
        signup_container.style.display = "block";
        signin_container.style.display = "none";
    }
})