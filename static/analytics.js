document.addEventListener("DOMContentLoaded", function () {

    // Read the real data supplied by Flask
    const dataElement = document.getElementById("analytics-data");

    if (!dataElement) {
        console.error("Analytics data element not found.");
        return;
    }

    const analyticsData = JSON.parse(dataElement.textContent);

    // Check whether Chart.js loaded
    if (typeof Chart === "undefined") {
        console.error("Chart.js failed to load.");
        return;
    }

    Chart.defaults.font.family = "Inter, sans-serif";
    Chart.defaults.color = "#9ba9b5";

    // -------------------------------
    // Equipment Distribution Chart
    // -------------------------------

    const equipmentCounts = analyticsData.equipment_counts || {};

    const categoryLabels = Object.keys(equipmentCounts);
    const categoryValues = Object.values(equipmentCounts);

    new Chart(document.getElementById("equipmentChart"), {
        type: "bar",

        data: {
            labels: categoryLabels,

            datasets: [{
                label: "Equipment Count",
                data: categoryValues,

                backgroundColor: "rgba(201, 169, 110, 0.75)",
                hoverBackgroundColor: "#ead4a1",

                borderRadius: 6,
                borderSkipped: false,
                maxBarThickness: 48
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            plugins: {
                legend: {
                    labels: {
                        color: "#c8d1d9",
                        usePointStyle: true
                    }
                }
            },

            scales: {
                x: {
                    ticks: {
                        color: "#aab5be"
                    },
                    grid: {
                        display: false
                    }
                },

                y: {
                    beginAtZero: true,

                    ticks: {
                        color: "#aab5be",
                        precision: 0
                    },

                    grid: {
                        color: "rgba(255,255,255,.07)"
                    }
                }
            }
        }
    });


    // -------------------------------
    // Average Armour Statistics Chart
    // -------------------------------

    const averageStats = analyticsData.average_stats || {};

    const statLabels = Object.keys(averageStats);
    const statValues = Object.values(averageStats);

    new Chart(document.getElementById("statsChart"), {
        type: "radar",

        data: {
            labels: statLabels,

            datasets: [{
                label: "Average Stats",
                data: statValues,

                backgroundColor: "rgba(115, 169, 201, 0.18)",
                borderColor: "#73a9c9",

                borderWidth: 2,

                pointBackgroundColor: "#c9a96e",
                pointBorderColor: "#f2dfb7",
                pointRadius: 4
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            plugins: {
                legend: {
                    labels: {
                        color: "#c8d1d9",
                        usePointStyle: true
                    }
                }
            },

            scales: {
                r: {
                    beginAtZero: true,

                    ticks: {
                        color: "#aab5be",
                        backdropColor: "transparent"
                    },

                    pointLabels: {
                        color: "#d1d9df",

                        font: {
                            size: 10
                        }
                    },

                    grid: {
                        color: "rgba(255,255,255,.10)"
                    },

                    angleLines: {
                        color: "rgba(255,255,255,.10)"
                    }
                }
            }
        }
    });

    console.log("God of War Analytics Dashboard loaded successfully.");

});