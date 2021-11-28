let filter = document.querySelector(".filter"),
    openFilter = document.querySelector(".open-filter"),
    closeFilter = document.querySelector(".close-filter"),
    blockMap = document.querySelector(".block-map");

openFilter.onclick = showFilter;
closeFilter.onclick = hideFilter;
blockMap.onclick = showMap;


function showFilter(){
    filter.style.display = "flex";
}
function hideFilter(){
    filter.style.display = "none";   
}
function showMap(){
    blockMap.style.display = "none";   
}