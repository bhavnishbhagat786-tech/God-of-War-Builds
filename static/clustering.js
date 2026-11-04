document.addEventListener("DOMContentLoaded", function () {

    const rows = document.getElementById("armourRows");

    let statsChart = null;
    let countChart = null;

    async function loadClustering() {

        try {
            const response = await fetch("/api/clustering");

            if (!response.ok) {
                throw new Error("API returned HTTP " + response.status);
            }

            const data = await response.json();

            if (data.error) {
                throw new Error(data.error);
            }

            const armours = data.armours || [];
            const stats = data.statistics || {};
            const counts = data.counts || {};

            // Cluster counts
            [0, 1, 2].forEach(id => {
                document.getElementById("count" + id).textContent =
                    counts[id] ?? counts[String(id)] ?? 0;
            });

            // Armour classification table
            rows.innerHTML = "";

            if (armours.length === 0) {
                rows.innerHTML =
                    '<tr><td colspan="6">No armour records found.</td></tr>';
            } else {
                armours.forEach(item => {

                    const tr = document.createElement("tr");

                    [
                        item.Title,
                        item.Strength,
                        item.Defence,
                        item.Runic,
                        item.Vitality,
                        item.Cluster
                    ].forEach(value => {

                        const td = document.createElement("td");
                        td.textContent = value ?? "";
                        tr.appendChild(td);

                    });

                    rows.appendChild(tr);
                });
            }

            if (typeof Chart === "undefined") {
                throw new Error("Chart.js failed to load.");
            }

            Chart.defaults.font.family = "Inter, sans-serif";
            Chart.defaults.color = "#aeb8c5";

            const labels = [
                "Strength",
                "Defence",
                "Runic",
                "Vitality",
                "Cooldown",
                "Luck"
            ];

            const clusterColors = [
                "#d6b36a",
                "#5badeb",
                "#a76bd1"
            ];

            // Destroy old charts before recreating
            if (statsChart) statsChart.destroy();
            if (countChart) countChart.destroy();

            // Average stats chart
            statsChart = new Chart(
                document.getElementById("statsChart"),
                {
                    type: "bar",

                    data: {
                        labels,

                        datasets: [0, 1, 2].map((id, index) => ({
                            label: "Cluster " + id,
                            data: labels.map(stat =>
                                Number(stats[id]?.[stat] ??
                                       stats[String(id)]?.[stat] ?? 0)
                            ),
                            backgroundColor: clusterColors[index],
                            borderRadius: 5,
                            borderSkipped: false
                        }))
                    },

                    options: {
                        responsive: true,
                        maintainAspectRatio: false,

                        plugins: {
                            legend: {
                                labels: {
                                    color: "#dce6f1",
                                    usePointStyle: true
                                }
                            }
                        },

                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: { color: "#aeb8c5" },
                                grid: { color: "rgba(255,255,255,.07)" }
                            },

                            x: {
                                ticks: { color: "#aeb8c5" },
                                grid: { display: false }
                            }
                        }
                    }
                }
            );

            // Cluster distribution chart
            countChart = new Chart(
                document.getElementById("countChart"),
                {
                    type: "doughnut",

                    data: {
                        labels: [
                            "Cluster 0",
                            "Cluster 1",
                            "Cluster 2"
                        ],

                        datasets: [{
                            data: [0, 1, 2].map(id =>
                                Number(counts[id] ??
                                       counts[String(id)] ?? 0)
                            ),

                            backgroundColor: clusterColors,
                            borderColor: "#101722",
                            borderWidth: 4,
                            hoverOffset: 9
                        }]
                    },

                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        cutout: "65%",

                        plugins: {
                            legend: {
                                position: "bottom",
                                labels: {
                                    color: "#dce6f1",
                                    padding: 20,
                                    usePointStyle: true
                                }
                            }
                        }
                    }
                }
            );

            console.log("Armour clustering dashboard loaded.");

        } catch (error) {

            rows.innerHTML = "";

            const tr = document.createElement("tr");
            const td = document.createElement("td");

            td.colSpan = 6;
            td.className = "loading";
            td.textContent =
                "Could not load clustering data: " + error.message;

            tr.appendChild(td);
            rows.appendChild(tr);

            console.error("Clustering error:", error);
        }
    }

    loadClustering();
});