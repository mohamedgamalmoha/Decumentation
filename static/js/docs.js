window.addEventListener('DOMContentLoaded', event => {
    // Toggle sidebar
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
            document.body.classList.toggle('sb-sidenav-toggled');
        }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

    // Toggle dropdown
    let dropdownBtn = document.querySelectorAll(".dBtn")
    let dropdownContainer = document.querySelectorAll(".dropDown")
    let dropIcon = document.querySelectorAll(".dropIcon")
    for (let i = 0; i < dropdownBtn.length; i++) {
        dropdownBtn[i].addEventListener("click", (e) => {

            // for(let elm of e.target.querySelectorAll('.dropDown')){
            //     elem.classList.toggle("d-none");
            // }
            // for(let elm of e.target.querySelectorAll('.dropIcon')){
            //     elem.classList.toggle("fa-square-plus");
            // }

            for (let j = 0; j < dropdownBtn.length; j++) {
                dropdownContainer[j].classList.toggle("d-none")
            }
            for (let h = 0; h < dropIcon.length; h++) {
                dropIcon[h].classList.toggle("fa-square-plus")
            }

            dropIcon[i].classList.toggle("fa-square-minus")
            dropdownContainer[i].classList.toggle("d-block")
            }
        )
    }
});
