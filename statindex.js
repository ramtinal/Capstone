var numIndexPage = localStorage.getItem('numIndexPage');
if (numIndexPage === null) {
    numIndexPage = 0;
}

numIndexPage++;

localStorage.setItem("numIndexPage", numIndexPage);

document.getElementById('numIndexPage').innerHTML = numIndexPage;
localStorage.setItem("p1", "Index Page");
localStorage.setItem("numIndexPage", numIndexPage);