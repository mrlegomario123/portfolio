function resizeCanvas(){
    //resize: same size as window width init
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
}

window.addEventListener("load", () => {
    console.log("hello silly billys")
    const canvas = document.querySelector("#canvas"); 
    const ctx = canvas.getContext("2d"); //context   
    resizeCanvas()

    ctx.fillRect(50,50,200,100)//position (x,y), size 

});

window.addEventListener('resize', () => {
    resizeCanvas()
}); 