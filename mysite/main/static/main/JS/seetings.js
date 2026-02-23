const theme_toggle = document.getElementById('theme-toggle');

theme_toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});
