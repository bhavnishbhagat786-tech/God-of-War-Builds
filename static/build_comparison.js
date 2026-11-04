const statNames = [
    "Strength",
    "Defence",
    "Runic",
    "Vitality",
    "Cooldown",
    "Luck"
];

let armours = [];
let chart = null;

const buildASelect = document.getElementById("buildA");
const buildBSelect = document.getElementById("buildB");
const compareButton = document.getElementById("compareButton");
const message = document.getElementById("message");

async function loadArmours() {
    try {
        message.textContent = "Loading armour data...";

        const response = await fetch("/api/armours");

        if (!response.ok) {
            throw new Error(`Server returned HTTP ${response.status}`);
        }

        armours = await response.json();

        if (!Array.isArray(armours) || armours.length === 0) {
            throw new Error("No armour records found.");
        }

        populateSelectors();

        compareButton.disabled = false;
        message.textContent =
            `${armours.length} armour records loaded successfully.`;

        compareBuilds();

    } catch (error) {
        console.error("Armour loading error:", error);

        message.textContent =
            "Could not load armour data: " + error.message;

        compareButton.disabled = true;
    }
}

function populateSelectors() {
    [buildASelect, buildBSelect].forEach(select => {
        select.innerHTML = "";

        armours.forEach((armour, index) => {
            const option = document.createElement("option");

            option.value = index;
            option.textContent = armour.Title || `Armour ${index + 1}`;

            select.appendChild(option);
        });
    });

    if (armours.length > 1) {
        buildBSelect.selectedIndex = 1;
    }
}

function getStatValue(armour, stat) {
    const value = Number(armour[stat]);
    return Number.isFinite(value) ? value : 0;
}

function compareBuilds() {
    if (armours.length === 0) return;

    const a = armours[Number(buildASelect.value)];
    const b = armours[Number(buildBSelect.value)];

    if (!a || !b) return;

    document.getElementById("headingA").textContent = a.Title;
    document.getElementById("headingB").textContent = b.Title;

    renderComparisonTable(a, b);
    renderComparisonChart(a, b);
}

function renderComparisonTable(a, b) {
    const rows = document.getElementById("comparisonRows");
    rows.innerHTML = "";

    statNames.forEach(stat => {
        const valueA = getStatValue(a, stat);
        const valueB = getStatValue(b, stat);
        const difference = valueA - valueB;

        const row = document.createElement("tr");

        const values = [
            stat,
            valueA,
            valueB,
            difference > 0 ? `+${difference}` : difference
        ];

        values.forEach((value, index) => {
            const cell = document.createElement("td");
            cell.textContent = value;

            if (index === 3) {
                if (difference > 0) {
                    cell.className = "difference-positive";
                } else if (difference < 0) {
                    cell.className = "difference-negative";
                } else {
                    cell.className = "difference-neutral";
                }
            }

            row.appendChild(cell);
        });

        rows.appendChild(row);
    });
}

function renderComparisonChart(a, b) {
    const canvas = document.getElementById("comparisonChart");

    if (chart) {
        chart.destroy();
    }

    chart = new Chart(canvas, {
        type: "radar",

        data: {
            labels: statNames,

            datasets: [
                {
                    label: a.Title,
                    data: statNames.map(stat => getStatValue(a, stat)),
                    borderColor: "#d67e6a",
                    backgroundColor: "rgba(214, 126, 106, 0.16)",
                    pointBackgroundColor: "#d67e6a",
                    pointRadius: 4,
                    borderWidth: 2
                },
                {
                    label: b.Title,
                    data: statNames.map(stat => getStatValue(b, stat)),
                    borderColor: "#65a9df",
                    backgroundColor: "rgba(101, 169, 223, 0.16)",
                    pointBackgroundColor: "#65a9df",
                    pointRadius: 4,
                    borderWidth: 2
                }
            ]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            scales: {
                r: {
                    beginAtZero: true,

                    ticks: {
                        color: "#aeb8c5",
                        backdropColor: "transparent"
                    },

                    pointLabels: {
                        color: "#f1f0ec",
                        font: {
                            size: 12,
                            family: "Inter"
                        }
                    },

                    grid: {
                        color: "#253249"
                    },

                    angleLines: {
                        color: "#253249"
                    }
                }
            },

            plugins: {
                legend: {
                    position: "bottom",

                    labels: {
                        color: "#f1f0ec",
                        padding: 22,
                        usePointStyle: true
                    }
                }
            }
        }
    });
}

compareButton.addEventListener("click", compareBuilds);

loadArmours();