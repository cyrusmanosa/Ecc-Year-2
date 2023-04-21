var t = document.getElementById("navi-wrap");
var topPos = t.offsetTop;

window.onscroll = function() {myFunction()};

function myFunction(){
    
    if (window.pageYOffset > topPos) 
    {
        t.style.top.add(topPos)
    }
    else
    {
        t.style.top.remove(topPos)
    }
}