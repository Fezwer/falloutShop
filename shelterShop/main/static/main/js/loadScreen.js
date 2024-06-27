document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("load").style.pointerEvents = "none";
    
    // Добавляем анимацию для #centralTranslate
    document.getElementById("centralTranslate").style.animation = "translateDoor 10s";

    // Добавляем анимацию для #centralDoor
    document.getElementById("centralDoor").style.animation = "openDoor 10s";

    // Добавляем анимацию через 1 секунду для #leftWall и #leftWallExtra
    setTimeout(function() {
        document.getElementById("leftWall").style.animation = "translateLeftWall 10s";
        document.getElementById("leftWallExtra").style.animation = "translateLeftWall 10s";
    }, 1500);

    // Добавляем анимацию через 1 секунду для #rightWallExtra и #rightWall
    setTimeout(function() {
        document.getElementById("rightWallExtra").style.animation = "translateRightWall 10s";
        document.getElementById("rightWall").style.animation = "translateRightWall 10s";
    }, 1500);

    setTimeout(function() {
        document.getElementById("load").style.visibility = "hidden";
    }, 8500);
});