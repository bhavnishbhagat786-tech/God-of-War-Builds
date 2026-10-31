const berserkerSelect = document.getElementById("berserker");
const recommendBtn = document.getElementById("recommendBtn");

recommendBtn.addEventListener("click", async () => {
    const berserker = berserkerSelect.value;

    if (!berserker) {
        alert("Select a Berserker first.");
        return;
    }

    recommendBtn.disabled = true;
    recommendBtn.textContent = "Generating Build...";

    try {
        const playstyle = document.getElementById("playstyle").value;

        const response = await fetch(
        `/api/build?berserker=${encodeURIComponent(berserker)}&playstyle=${encodeURIComponent(playstyle)}`
        );

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || "Build generation failed.");
            return;
        }

        const result = document.getElementById("result");

        result.classList.add("has-recommendation");
        result.style.display = "block";

        // Existing frontend fields
        document.getElementById("resultTitle").textContent =
            data.Berserker || berserker;

        document.getElementById("buildScore").textContent =
            `Equipment Score: ${data.Equipment_Score ?? data.Build_Score} | Final Score: ${data.Final_Score}`;

        document.getElementById("chest").textContent =
            `Chest: ${data.Chest || "Not available"}`;

        document.getElementById("wrist").textContent =
            `Wrist: ${data.Wrist || "Not available"}`;

        document.getElementById("waist").textContent =
            `Waist: ${data.Waist || "Not available"}`;

        document.getElementById("axe").textContent =
            `Axe: ${data.Axe || "Not available"}`;

        document.getElementById("blades").textContent =
            `Blades: ${data.Blades || "Not available"}`;

        document.getElementById("spear").textContent =
            `Spear: ${data.Spear || "Not available"}`;

        document.getElementById("shield").textContent =
            `Shield: ${data.Shield || "Not available"}`;

        document.getElementById("rond").textContent =
            `Rönd: ${data.Rond || "Not available"}`;

        document.getElementById("relic").textContent =
            `Relic: ${data.Relic || "Not available"}`;

        // New recommendation engine details
        const equipment = data.Equipment_Details || {};

        // Create an extra results section dynamically
        let detailsPanel = document.getElementById("engineDetails");

        if (!detailsPanel) {
            detailsPanel = document.createElement("div");
            detailsPanel.id = "engineDetails";
            detailsPanel.className = "equipment-group";
            result.appendChild(detailsPanel);
        }

        detailsPanel.replaceChildren();

        const heading = document.createElement("h3");
        heading.textContent = "Advanced Build Analysis";
        detailsPanel.appendChild(heading);

        // Display scores
        const scoreItems = [
            ["Equipment Score", data.Equipment_Score],
            ["Relic Score", data.Relic_Score],
            ["Synergy Score", data.Synergy_Score],
            ["Final Build Score", data.Final_Score]
        ];

        scoreItems.forEach(([label, value]) => {
            const p = document.createElement("p");
            p.textContent = `${label}: ${value ?? "N/A"}`;
            detailsPanel.appendChild(p);
        });

        // Display individual weapon components
        const weaponHeading = document.createElement("h3");
        weaponHeading.textContent = "Individual Weapon Components";
        detailsPanel.appendChild(weaponHeading);

        const weaponSlots = [
            "Grip", "Knob", "Maul",
            "Handles", "Pommels",
            "Hind", "Sauroter"
        ];

        weaponSlots.forEach(slot => {
            const item = equipment[slot];

            const p = document.createElement("p");
            p.textContent = `${slot}: ${
                item?.Title || "Not available"
            }`;

            detailsPanel.appendChild(p);
        });
        
        
// Display equipment explanations
const explanationHeading = document.createElement("h3");
explanationHeading.textContent = "Why These Items Were Recommended";
detailsPanel.appendChild(explanationHeading);

const explanations = equipment.explanations || {};

Object.entries(explanations).forEach(([slot, reasons]) => {

    if (!Array.isArray(reasons) || reasons.length === 0) {
        return;
    }

    const section = document.createElement("div");
    section.className = "equipment-explanation";

    const title = document.createElement("h4");
    title.textContent = slot;
    section.appendChild(title);

    reasons.forEach(reason => {

        const p = document.createElement("p");

        p.textContent =
            `${reason.stat}: ${reason.value} | Contribution: ${reason.contribution}`;

        section.appendChild(p);
    });

    detailsPanel.appendChild(section);
});

// Display relic explanation
        const relicExplanation = equipment.relic_explanation;

        const relicHeading = document.createElement("h3");
        relicHeading.textContent = "Why This Relic?";
        detailsPanel.appendChild(relicHeading);

    const relicReason = document.createElement("p");
    relicReason.textContent = relicExplanation?.reason || "No explanation available.";
    detailsPanel.appendChild(relicReason);

    const relicEffect = document.createElement("p");
    relicEffect.textContent = `Relic Effect: ${relicExplanation?.effect || "Not available"}`;
    detailsPanel.appendChild(relicEffect);

    // Display build strategy
    const strategyHeading = document.createElement("h3");
    strategyHeading.textContent = "Recommended Combat Strategy";
    detailsPanel.appendChild(strategyHeading);

    const strategyText = document.createElement("p");
    strategyText.textContent =
    equipment.build_strategy || "No strategy available.";

    detailsPanel.appendChild(strategyText);


        // Display synergy analysis
        const synergyHeading = document.createElement("h3");
        synergyHeading.textContent = "Equipment Synergy";
        detailsPanel.appendChild(synergyHeading);

        const synergies = data.Synergies || {};

        if (Object.keys(synergies).length > 0) {
            Object.entries(synergies).forEach(([category, items]) => {
                const p = document.createElement("p");

                const names = Array.isArray(items)
                    ? items.map(item =>
                        typeof item === "string"
                            ? item
                            : item.Title || item.title || item.slot || "Equipment"
                    ).join(", ")
                    : "";

                p.textContent = `${category}: ${names || "Detected"}`;
                detailsPanel.appendChild(p);
            });
        } else {
            const p = document.createElement("p");
            p.textContent = "No matching equipment synergy detected.";
            detailsPanel.appendChild(p);
        }
/*save build histoy and deletre  */

// Save Generated Build Feature
const saveGeneratedButton = document.createElement("button");

saveGeneratedButton.type = "button";
saveGeneratedButton.id = "saveGeneratedBuildBtn";
saveGeneratedButton.className = "copy-build-btn";
saveGeneratedButton.textContent = "💾 Save Generated Build";

saveGeneratedButton.addEventListener("click", async () => {
    saveGeneratedButton.disabled = true;
    saveGeneratedButton.textContent = "Saving Build...";

    const saveData = {
        Berserker: data.Berserker || berserker,
        Build_Score: data.Final_Score ?? data.Build_Score,
        Chest: data.Chest,
        Wrist: data.Wrist,
        Waist: data.Waist,
        Axe: data.Axe,
        Blades: data.Blades,
        Spear: data.Spear,
        Shield: data.Shield,
        Rond: data.Rond,
        Relic: data.Relic
    };

    try {
        const saveResponse = await fetch("/api/save-build", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(saveData)
        });

        const saveResult = await saveResponse.json();

        if (!saveResponse.ok || !saveResult.success) {
            throw new Error(saveResult.error || "Could not save build.");
        }

        saveGeneratedButton.textContent = "✅ Build Saved!";

    } catch (error) {
        console.error("Save Generated Build Error:", error);
        saveGeneratedButton.textContent = "❌ Save Failed";
        alert(error.message);

    } finally {
        saveGeneratedButton.disabled = false;
    }
});

const oldSaveButton = document.getElementById("saveGeneratedBuildBtn");
if (oldSaveButton) oldSaveButton.remove();

result.appendChild(saveGeneratedButton);

        console.log("Dynamic Build:", data);

        result.scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });

    } catch (error) {
        console.error("Build API Error:", error);
        alert("Backend connection failed. Check Flask server.");

    } finally {
        recommendBtn.disabled = false;
        recommendBtn.textContent = "⚔ Generate My Build →";
    }
});

/* AI Chatbox open and close */
const aiChatToggle = document.getElementById("aiChatToggle");
const aiChatWindow = document.getElementById("aiChatWindow");
const aiChatClose = document.getElementById("aiChatClose");

aiChatToggle.addEventListener("click", () => {
    aiChatWindow.hidden = false;
    aiChatToggle.style.display = "none";
});

aiChatClose.addEventListener("click", () => {
    aiChatWindow.hidden = true;
    aiChatToggle.style.display = "block";
});


/* AI Chat Functionality */
const aiChatForm = document.getElementById("aiChatForm");
const aiChatInput = document.getElementById("aiChatInput");
const aiChatMessages = document.getElementById("aiChatMessages");

aiChatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = aiChatInput.value.trim();

    if (!message) return;

    // Show user's message
    const userMessage = document.createElement("p");
    userMessage.textContent = message;
    userMessage.className = "ai-user-message";
    aiChatMessages.appendChild(userMessage);

    aiChatInput.value = "";

    // Show loading status
    const loading = document.createElement("p");
    loading.textContent = "Kratos is thinking...";
    loading.className = "ai-message";
    aiChatMessages.appendChild(loading);
    aiChatMessages.scrollTop = aiChatMessages.scrollHeight;

    try {
        const response = await fetch("/api/ai-chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        console.log("API response:", data);


        console.log("Recommendation result:", document.getElementById("result"));
        loading.remove();

        const reply = document.createElement("p");
        reply.className = "ai-message";
        reply.textContent = response.ok
            ? data.reply
            : (data.error || "AI request failed.");

        aiChatMessages.appendChild(reply);

    } catch (error) {
        loading.textContent =
            "Connection failed. Please check the Flask server.";
        console.error(error);
    }

    aiChatMessages.scrollTop = aiChatMessages.scrollHeight;
});


/* Featured Berserker Cards */
document.addEventListener("click", (event) => {
    const button = event.target.closest(".view-build");

    if (!button) return;

    const berserkerName = button.dataset.berserker;
    const dropdown = document.getElementById("berserker");
    const recommendButton = document.getElementById("recommendBtn");

    if (!dropdown || !recommendButton || !berserkerName) {
        console.error("Featured Berserker setup is incomplete.");
        return;
    }

    dropdown.value = berserkerName;

    if (dropdown.value !== berserkerName) {
        console.error("Berserker not found in dropdown:", berserkerName);
        return;
    }

    console.log("Featured Berserker selected:", berserkerName);

    document.getElementById("builds")?.scrollIntoView({
        behavior: "smooth"
    });

    recommendButton.click();
});

console.log("FEATURED HANDLER LOADED");

/* ==================================================
   SECTION 3: BERSERKER CARD INTERACTIONS
================================================== */

// Expand or collapse Berserker details
document.addEventListener("click", (event) => {
    const detailsButton = event.target.closest(".guide-details-btn");

    if (!detailsButton) return;

    const card = detailsButton.closest(".berserker-guide-card");
    const details = card.querySelector(".guide-details");
    const isOpening = details.hidden;

    details.hidden = !isOpening;
    detailsButton.textContent = isOpening ? "Hide Details" : "View Details";
    detailsButton.setAttribute("aria-expanded", String(isOpening));
});

// Connect each card to the existing build recommendation feature
document.addEventListener("click", (event) => {
    const buildButton = event.target.closest(".guide-build-btn");

    if (!buildButton) return;

    const berserkerName = buildButton.dataset.berserker;
    const dropdown = document.getElementById("berserker");
    const recommendButton = document.getElementById("recommendBtn");

    if (!dropdown || !recommendButton) {
        console.error("Build recommendation controls were not found.");
        return;
    }

    dropdown.value = berserkerName;

    if (dropdown.value !== berserkerName) {
        console.error("Berserker name not found in dropdown:", berserkerName);
        return;
    }

    document.getElementById("builds")?.scrollIntoView({
        behavior: "smooth"
    });

    recommendButton.click();
});

// END SECTION 3: BERSERKER CARD INTERACTIONS


// berserker comparison
const compareBuildsBtn = document.getElementById("compareBuildsBtn");

compareBuildsBtn.addEventListener("click", async () => {
    const resultsContainer = document.getElementById("comparisonResults");

    compareBuildsBtn.disabled = true;
    compareBuildsBtn.textContent = "Comparing Builds...";
    resultsContainer.textContent = "Loading all Berserker builds...";

    try {
        const selectedStyle = document.getElementById("playstyle").value;

        const response = await fetch(
            `/api/compare-builds?playstyle=${encodeURIComponent(selectedStyle)}`
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Comparison failed.");
        }

        resultsContainer.replaceChildren();

        // Best build
        if (data.best_build) {
            const best = document.createElement("div");
            best.className = "best-build";

            const title = document.createElement("h3");
            title.textContent = "🏆 Best Ranked Build";

            const name = document.createElement("p");
            name.textContent = data.best_build.Berserker;

            const score = document.createElement("p");
            score.textContent = `Final Score: ${data.best_build.Final_Score}`;

            best.append(title, name, score);
            resultsContainer.appendChild(best);
        }

        // Build details container
        const detailsContainer = document.createElement("div");
        detailsContainer.id = "selectedBuildDetails";
        detailsContainer.className = "selected-build-details";

        // Ranking table
        const table = document.createElement("table");
        table.className = "comparison-table";

        const header = document.createElement("tr");

        ["Rank", "Berserker", "Final Score", "Equipment Score", "Relic", "Synergy"]
            .forEach(label => {
                const th = document.createElement("th");
                th.textContent = label;
                header.appendChild(th);
            });

        table.appendChild(header);

        data.comparisons.forEach((boss, index) => {
            const row = document.createElement("tr");

            const rankCell = document.createElement("td");
            rankCell.textContent = index + 1;

            const nameCell = document.createElement("td");
            const nameButton = document.createElement("button");

            nameButton.type = "button";
            nameButton.textContent = boss.Berserker;
            nameButton.className = "berserker-detail-btn";

            nameButton.addEventListener("click", async () => {
                detailsContainer.textContent = "Loading build details...";

                try {
                    const style = document.getElementById("playstyle").value;

                    const buildResponse = await fetch(
                        `/api/build?berserker=${encodeURIComponent(boss.Berserker)}&playstyle=${encodeURIComponent(style)}`
                    );

                    const buildData = await buildResponse.json();

                    if (!buildResponse.ok) {
                        throw new Error(buildData.error || "Could not load build.");
                    }

                    const details = buildData.Equipment_Details || {};

                    detailsContainer.replaceChildren();

                    const heading = document.createElement("h2");
                    heading.textContent = `⚔ ${boss.Berserker} — Recommended Build`;
                    detailsContainer.appendChild(heading);

                    const score = document.createElement("p");
                    score.textContent = `Final Score: ${buildData.Final_Score ?? "N/A"}`;
                    detailsContainer.appendChild(score);
                    
            const scoreBreakdown = document.createElement("div");
                scoreBreakdown.className = "score-breakdown";

            const breakdownTitle = document.createElement("h3");
                breakdownTitle.textContent = "Build Score Breakdown";
                scoreBreakdown.appendChild(breakdownTitle);

            const scoreItems = [
                ["Equipment Score", buildData.Equipment_Score],
                ["Relic Score", buildData.Relic_Score],
                ["Synergy Score", buildData.Synergy_Score]
];


scoreItems.forEach(([label, value]) => {
    const scoreValue = Number(value);

    const scoreCard = document.createElement("div");
    scoreCard.className = "score-card";

    const scoreLabel = document.createElement("p");
    scoreLabel.textContent = `${label}: ${
        Number.isFinite(scoreValue) ? scoreValue.toFixed(4) : "N/A"
    }`;

    const progress = document.createElement("div");
    progress.className = "score-progress";

    const fill = document.createElement("div");
    fill.className = "score-progress-fill";

    if (Number.isFinite(scoreValue)) {
        fill.style.width = `${Math.max(0, Math.min(100, scoreValue * 100))}%`;
    }

    progress.appendChild(fill);
    scoreCard.append(scoreLabel, progress);
    scoreBreakdown.appendChild(scoreCard);
});


detailsContainer.appendChild(scoreBreakdown);

                    const slots = [
                        ["Chest", "Chest"],
                        ["Waist", "Waist"],
                        ["Wrist", "Wrist"],
                        ["Grip", "Grip"],
                        ["Knob", "Knob"],
                        ["Maul", "Maul"],
                        ["Handles", "Handles"],
                        ["Pommels", "Pommels"],
                        ["Hind", "Hind"],
                        ["Sauroter", "Sauroter"],
                        ["shield", "Shield"],
                        ["rond", "Rönd"],
                        ["relic", "Relic"]
                    ];

                    const equipmentHeading = document.createElement("h3");
                    equipmentHeading.textContent = "Recommended Equipment";
                    detailsContainer.appendChild(equipmentHeading);

                    slots.forEach(([key, label]) => {
                        const item = details[key];

                        if (!item) return;

                        const section = document.createElement("div");
                        section.className = "build-detail-item";

                        const itemTitle = document.createElement("h4");
                        itemTitle.textContent = `${label}: ${item.Title || item.Name || "Selected"}`;

                        section.appendChild(itemTitle);
                        
                        const stats = ["Strength", "Defence", "Runic", "Vitality", "Cooldown", "Luck"];

                        const statsBox = document.createElement("p");
                            statsBox.className = "equipment-stats";

                        const availableStats = stats
                            .filter(stat => item[stat] !== undefined && item[stat] !== null)
                            .map(stat => `${stat}: ${item[stat]}`);

                    statsBox.textContent = availableStats.length
                    ? availableStats.join("  |  ")
                    : "No stat information available.";

                    section.appendChild(statsBox);

                        const explanation = details.explanations?.[key];

                        if (explanation?.length) {
                            const reason = document.createElement("p");
                            reason.textContent = "Top contributing stats: " +
                                explanation.map(stat =>
                                    `${stat.stat} (${stat.contribution})`
                                ).join(", ");

                            section.appendChild(reason);
                        }

                        detailsContainer.appendChild(section);
                    });

                    // Relic explanation
                    if (details.relic_explanation) {
                        const relicHeading = document.createElement("h3");
                        relicHeading.textContent = "Relic Explanation";
                        detailsContainer.appendChild(relicHeading);

                        const relicReason = document.createElement("p");
                        relicReason.textContent = details.relic_explanation.reason || "";
                        detailsContainer.appendChild(relicReason);

                        const relicEffect = document.createElement("p");
                        relicEffect.textContent = details.relic_explanation.effect || "";
                        detailsContainer.appendChild(relicEffect);
                    }

                    // Build strategy
                    if (details.build_strategy) {
                        const strategyHeading = document.createElement("h3");
                        strategyHeading.textContent = "Build Strategy";
                        detailsContainer.appendChild(strategyHeading);

                        const strategy = document.createElement("p");
                        strategy.textContent = details.build_strategy;
                        detailsContainer.appendChild(strategy);
                    }

// Synergy Explanation
const synergyHeading = document.createElement("h3");
synergyHeading.textContent = "⚡ Equipment Synergy Analysis";
detailsContainer.appendChild(synergyHeading);

const synergyBox = document.createElement("div");
synergyBox.className = "synergy-details";


if (details.synergy && Object.keys(details.synergy).length > 0) {

    Object.entries(details.synergy).forEach(([type, items]) => {

        const group = document.createElement("div");
        group.className = "synergy-group";

        const heading = document.createElement("h4");
        heading.textContent =
            type.charAt(0).toUpperCase() + type.slice(1);

        group.appendChild(heading);

        items.forEach(item => {
            const line = document.createElement("p");
            line.textContent = `${item.item} — ${item.slot}`;
            group.appendChild(line);
        });

        synergyBox.appendChild(group);
    });

} else {
    synergyBox.textContent = "No synergy details available.";
}



detailsContainer.appendChild(synergyBox);

// Copy Build Feature
const copyButton = document.createElement("button");
copyButton.type = "button";
copyButton.className = "copy-build-btn";
copyButton.textContent = "📋 Copy Complete Build";

copyButton.addEventListener("click", async () => {
    const buildText = [
        `BERSERKER: ${boss.Berserker}`,
        `PLAYSTYLE: ${buildData.Playstyle}`,
        `FINAL SCORE: ${buildData.Final_Score}`,
        "",
        "RECOMMENDED EQUIPMENT:",
        ...slots.map(([key, label]) => {
            const item = details[key];
            return item
                ? `${label}: ${item.Title || item.Name || "Selected"}`
                : null;
        }).filter(Boolean),
        "",
        `RELIC: ${details.relic?.Title || "Not available"}`,
        `STRATEGY: ${details.build_strategy || "Not available"}`
    ].join("\n");

    try {
        await navigator.clipboard.writeText(buildText);
        copyButton.textContent = "✅ Build Copied!";
    } catch (error) {
        console.error("Copy Error:", error);
        copyButton.textContent = "❌ Copy Failed";
    }
});

detailsContainer.appendChild(copyButton);
console.log("Copy button added:", copyButton);


// Save Build Feature
const saveButton = document.createElement("button");
saveButton.type = "button";
saveButton.className = "copy-build-btn";
saveButton.textContent = "💾 Save Recommended Build";

saveButton.addEventListener("click", async () => {
    saveButton.disabled = true;
    saveButton.textContent = "Saving Build...";

    const saveData = {
        Berserker: buildData.Berserker,
        Build_Score: buildData.Build_Score,
        Chest: buildData.Chest,
        Wrist: buildData.Wrist,
        Waist: buildData.Waist,
        Axe: buildData.Axe,
        Blades: buildData.Blades,
        Spear: buildData.Spear,
        Shield: buildData.Shield,
        Rond: buildData.Rond,
        Relic: buildData.Relic
    };

    try {
        const saveResponse = await fetch("/api/save-build", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(saveData)
        });

        const result = await saveResponse.json();

        if (!saveResponse.ok) {
            throw new Error(result.error || "Could not save build.");
        }

        saveButton.textContent = "✅ Build Saved!";

    } catch (error) {
        console.error("Save Build Error:", error);
        saveButton.textContent = "❌ Save Failed";
        alert(error.message);

    } finally {
        saveButton.disabled = false;
    }
});

detailsContainer.appendChild(saveButton);


detailsContainer.scrollIntoView({
    behavior: "smooth",
    block: "start"
});

} catch (error) {
    detailsContainer.textContent = error.message;
    console.error("Build Details Error:", error);
}

});


            nameCell.appendChild(nameButton);

            const values = [
                boss.Final_Score,
                boss.Equipment_Score,
                boss.Relic,
                boss.Synergy_Score
            ];

            row.append(rankCell, nameCell);

            values.forEach(value => {
                const cell = document.createElement("td");
                cell.textContent = value ?? "N/A";
                row.appendChild(cell);
            });

            table.appendChild(row);
        });

        resultsContainer.append(table, detailsContainer);

        console.log("Comparison Results:", data);

            } catch (error) {
            console.error("Comparison Error:", error);
            resultsContainer.textContent = error.message;

        } finally {
            compareBuildsBtn.disabled = false;
            compareBuildsBtn.textContent = "Compare All Berserkers";
        }
} );

// Saved Builds History
const loadSavedBuildsBtn = document.getElementById("loadSavedBuildsBtn");
const savedBuildsResults = document.getElementById("savedBuildsResults");

if (loadSavedBuildsBtn && savedBuildsResults) {

    loadSavedBuildsBtn.addEventListener("click", async () => {

        loadSavedBuildsBtn.disabled = true;
        loadSavedBuildsBtn.textContent = "Loading Saved Builds...";

        try {
            const response = await fetch("/api/saved-builds");
            const result = await response.json();

            if (!response.ok || !result.success) {
                throw new Error(result.error || "Unable to load saved builds.");
            }

            if (result.builds.length === 0) {
                savedBuildsResults.textContent = "No saved builds found.";
                return;
            }

const columns = [
    "ID", "Berserker", "Saved_At", "Build_Score",
    "Chest", "Wrist", "Waist",
    "Axe", "Blades", "Spear",
    "Shield", "Rond", "Relic"
];

            let tableHTML = `
                <div class="saved-build-stats">
    <div class="stat-card">
        <h4>Total Builds</h4>
        <p>${result.total_builds}</p>
    </div>

    <div class="stat-card">
        <h4>Average Score</h4>
        <p>${Number(result.average_score).toFixed(4)}</p>
    </div>

    <div class="stat-card">
        <h4>Highest Score</h4>
        <p>${Number(result.highest_score).toFixed(4)}</p>
    </div>

    <div class="stat-card">
        <h4>Lowest Score</h4>
        <p>${Number(result.lowest_score).toFixed(4)}</p>
    </div>
</div>
                <div class="saved-builds-table">
                <table>
                    <thead>
                        <th>Action</th><tr>
                            ${columns.map(column => `<th>${column}</th>`).join("")}
                        </tr>
                    </thead>
                    <tbody>
            `;

            result.builds.forEach(build => {
                tableHTML += "<tr>";

                columns.forEach(column => {
                    // date and time format
                    let value = build[column] ?? "-";

if (column === "Saved_At" && value !== "-") {
  
/*set date and accuarate to sql */
    const date = new Date(value + "+05:30");
    value = isNaN(date.getTime())
        ? value
        : date.toLocaleString("en-IN", {
            timeZone: "Asia/Kolkata",
            day: "2-digit",
            month: "short",
            year: "numeric",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
            hour12: true
    });
}
                    const safeValue = String(value).replace(/[&<>"']/g, char => ({
                        "&": "&amp;",
                        "<": "&lt;",
                        ">": "&gt;",
                        '"': "&quot;",
                        "'": "&#39;"
                    })[char]);

                    tableHTML += `<td>${safeValue}</td>`;
                });
tableHTML += `
    <td>
        <button
            type="button"
            class="delete-saved-build"
            data-id="${Number(build.ID)}">
            🗑 Delete
        </button>
    </td>
`;
                tableHTML += "</tr>";
            });

            tableHTML += `
                    </tbody>
                </table>
                </div>
            `;

            savedBuildsResults.innerHTML = tableHTML;
            /**sql delete data  */
savedBuildsResults.querySelectorAll(".delete-saved-build")
    .forEach(button => {

        button.addEventListener("click", async () => {

            const buildId = button.dataset.id;

            if (!confirm("Are you sure you want to delete this saved build?")) {
                return;
            }

            try {
                const response = await fetch(
                    `/api/delete-build/${buildId}`,
                    { method: "DELETE" }
                );

                const result = await response.json();

                if (!response.ok || !result.success) {
                    throw new Error(result.error || "Delete failed.");
                }

                alert("Build deleted successfully!");

                loadSavedBuildsBtn.click();

            } catch (error) {
                alert(error.message);
                console.error("Delete Build Error:", error);
            }
        });
    });
        } catch (error) {
            console.error("Saved Builds Error:", error);
            savedBuildsResults.textContent = error.message;

        } finally {
            loadSavedBuildsBtn.disabled = false;
            loadSavedBuildsBtn.textContent = "View Saved Builds";
        }
    });
}


// Export Saved Builds to CSV

const exportSavedBuildsBtn = document.getElementById("exportSavedBuildsBtn");

if (exportSavedBuildsBtn) {

    exportSavedBuildsBtn.addEventListener("click", async () => {

        exportSavedBuildsBtn.disabled = true;
        exportSavedBuildsBtn.textContent = "Exporting...";

        try {
            const response = await fetch("/api/saved-builds");
            const result = await response.json();

            if (!response.ok || !result.success) {
                throw new Error(result.error || "Unable to export builds.");
            }

            if (!result.builds || result.builds.length === 0) {
                alert("No saved builds available!");
                return;
            }

            const columns = [
                "ID", "Berserker", "Saved_At", "Build_Score",
                "Chest", "Wrist", "Waist",
                "Axe", "Blades", "Spear",
                "Shield", "Rond", "Relic"
            ];

            const escapeCSV = (value) => {
                const text = String(value ?? "");
                return `"${text.replace(/"/g, '""')}"`;
            };

            const csvRows = [
                columns.map(escapeCSV).join(",")
            ];

            result.builds.forEach(build => {
                const row = columns.map(column =>
                    escapeCSV(build[column])
                );

                csvRows.push(row.join(","));
            });

            const csvContent = "\uFEFF" + csvRows.join("\r\n");

            const blob = new Blob(
                [csvContent],
                { type: "text/csv;charset=utf-8;" }
            );

            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");

            link.href = url;
            link.download = "God_of_War_Saved_Builds.csv";

            document.body.appendChild(link);
            link.click();
            link.remove();

            URL.revokeObjectURL(url);

        } catch (error) {
            console.error("CSV Export Error:", error);
            alert(error.message);

        } finally {
            exportSavedBuildsBtn.disabled = false;
            exportSavedBuildsBtn.textContent = "📥 Export to CSV";
        }
    });
}

/* God of War website snow effect */
