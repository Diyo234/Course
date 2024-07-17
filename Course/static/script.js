accentLightBlue = '#3C91E6';
function expandSection(section){
    sectionHeader = section.parentElement;
    sectionList = sectionHeader.querySelector('.dropdown');
    console.log(sectionList);
    sectionList.classList.toggle('section-expand');
    section.firstElementChild.classList.toggle('arrow-rotate');
}
function selected(box){
    var boxes = document.querySelectorAll('.choice');
    boxes.forEach(choice => {
        answerCircle=choice.children[0];
        answerCircle.style.backgroundColor = 'transparent';
    });
    box.classList.add('selected');
    answerCircle=box.children[0];
    answerCircle.style.backgroundColor = accentLightBlue;
}
document.addEventListener('DOMContentLoaded', function() {
    function toggleSidebar() {
        sidebar.classList.toggle('collapsed');
        mainWindow.classList.toggle('recentre');
        navBar.classList.toggle('move-navbar');
        extender.classList.toggle('move-extender');
        filter.classList.toggle('filter');
        document.body.classList.toggle('no-scroll');
        if (sidebar.classList.contains('collapsed') ){
            document.body.classList.remove('no-scroll');
        }
    };
    toggleButton.addEventListener('click', toggleSidebar);
    function toggleSmallScreenSidebar (){
        sidebar.classList.toggle('collapsed');
        mainWindow.classList.toggle('recentre');
        navBar.classList.toggle('move-navbar');
        extender.classList.toggle('move-extender');
        filter.classList.toggle('filter');
        document.body.classList.toggle('no-scroll');
        triggerMessage();
        if (sidebar.classList.contains('collapsed') ){
            document.body.classList.remove('no-scroll');
        }
    }
    hidden.addEventListener('click', toggleSmallScreenSidebar);
    const home = document.getElementById('home');
    home.addEventListener('click', function() {
        window.open(this.getAttribute('url'),'_self')
    });
    // const icons = document.querySelectorAll('.icon');
    // icons.forEach(icon => {
    //     icon.addEventListener('click', function() {
    //         window.open(this.getAttribute('url'),'_self')
    //     });
    // });
    flashcards = document.querySelectorAll('.flashcard');
    console.log(flashcards);
    flashcards.forEach(flashcard => {
        flashcard.addEventListener('click', function(){
            flashcard.style.boxShadow = 'none';
            flashcard.classList.toggle('flipped');
            setTimeout(function() {
                flashcard.style.boxShadow = '0 5px 10px rgba(154,160,185,.05), 0 15px 40px rgba(166,173,201,.2)';
            }, 450);
        });
    });
});
// This is for the schematic
function clicked(dot){
    vector = document.getElementById('vector');
    var replacedString = vector.src.replace(/-(.)/, '-'+dot.id);
    vector.style.opacity = 0;
    setTimeout(function() {
        vector.src = replacedString;
        vector.style.opacity = 1;
    }, 50);
    var dots = document.querySelectorAll('.dot');
    dots.forEach(choice => {
        choice.style.backgroundColor = 'red';
    });
    dot.style.backgroundColor = 'green';
}
function submit(){
    var selected = document.querySelector('.selected');
    if(selected){
        if(selected.id == selected.parentElement.getAttribute('answer')){
            alert('Correct');
        } else {
            alert('Incorrect');
        }
    }
    else{
        alert('Please select a choice');
    }
}
document.addEventListener('input', function(event) {
    if (event.target.classList.contains('missing-word')) {
        const width = (event.target.value.length + 2) + 'ch';
        event.target.style.width = width;
    }
});
