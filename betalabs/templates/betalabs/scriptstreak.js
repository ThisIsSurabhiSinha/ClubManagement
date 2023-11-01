let streakCount = 0;
let userRating = 1000;
let currentDifficulty = "Medium";

document.getElementById("increaseStreak").addEventListener("click", increaseStreak);
document.getElementById("increaseRating").addEventListener("click", increaseRating);
document.getElementById("changeDifficulty").addEventListener("click", changeDifficulty);

function increaseStreak() {
    streakCount++;
    document.getElementById("streakCount").textContent = streakCount + " days";
}

function increaseRating() {
    userRating += 50;
    document.getElementById("userRating").textContent = userRating;
}

function changeDifficulty() {
    const difficulties = ["Easy", "Medium", "Hard"];
    const currentIndex = difficulties.indexOf(currentDifficulty);
    const nextIndex = (currentIndex + 1) % difficulties.length;
    currentDifficulty = difficulties[nextIndex];
    document.getElementById("currentDifficulty").textContent = currentDifficulty;
}