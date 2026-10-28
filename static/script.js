const berserkerSelect = document.getElementById("berserker");
const recommendBtn = document.getElementById("recommendBtn");

recommendBtn.addEventListener("click", async () => {
    console.log("Generate Build button clicked!");
    const berserker = berserkerSelect.value;

    if (!berserker) {
        alert("Select a Berserker first.");
        return;
    }

    try {
        const response = await fetch(
            `/api/build?berserker=${encodeURIComponent(berserker)}`
        );

        const data = await response.json();

        if (!response.ok) {
            alert(data.error);
            return;
        }

        const result = document.getElementById("result");
        result.classList.add("has-recommendation");
        result.style.display = "block";
        console.log("Build API response:", data);
        console.log("Result container:", result);

        document.getElementById("resultTitle").textContent = data.Berserker;
        document.getElementById("buildScore").textContent =
            `Build Score: ${data.Build_Score}`;

        document.getElementById("chest").textContent =
            `Chest: ${data.Chest}`;

        document.getElementById("wrist").textContent =
            `Wrist: ${data.Wrist}`;

        document.getElementById("waist").textContent =
            `Waist: ${data.Waist}`;

        document.getElementById("axe").textContent =
            `Axe: ${data.Axe}`;

        document.getElementById("blades").textContent =
            `Blades: ${data.Blades}`;

        document.getElementById("spear").textContent =
            `Spear: ${data.Spear}`;

        document.getElementById("shield").textContent =
            `Shield: ${data.Shield}`;

        document.getElementById("rond").textContent =
            `Rönd: ${data.Rond}`;

        document.getElementById("relic").textContent =
            `Relic: ${data.Relic}`;

    } catch (error) {
        console.error("ERROR:", error);
        alert("Backend connection failed.");
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

/* God of War website snow effect */
