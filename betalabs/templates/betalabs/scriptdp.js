// script.js

// Sample contest data for illustration
const contests = [
    {
        name: "DP Challenge 1",
        date: "2023-11-10",
        time: "14:00",
    },
    {
        name: "DP Challenge 2",
        date: "2023-12-05",
        time: "15:30",
    },
];

// Function to populate contest schedule
function populateContestSchedule() {
    const contestList = document.getElementById("contestList");

    contests.forEach((contest, index) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${index + 1}. ${contest.name} - Date: ${contest.date}, Time: ${contest.time}`;
        contestList.appendChild(listItem);
    });
}

// Register button click event
document.getElementById("registerButton").addEventListener("click", () => {
    // Implement registration logic (e.g., redirect to a registration page).
    alert("Redirecting to the registration page...");
});

// Populate the contest schedule on page load
populateContestSchedule();
