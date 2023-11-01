document.getElementById("startCompetition").addEventListener("click", startCompetition);

function startCompetition() {
    // Simulate starting a competition and updating the leaderboard
    const leaderboard = document.getElementById("leaderboardList");
    leaderboard.innerHTML = "";

    const participants = [
        { name: "User1", score: 100 },
        { name: "User2", score: 85 },
        { name: "User3", score: 75 },
        { name: "User4", score: 60 },
        { name: "User5", score: 50 },
    ];

    participants.forEach((participant, index) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${index + 1}. ${participant.name} - Score: ${participant.score}`;
        leaderboard.appendChild(listItem);
    });
}
