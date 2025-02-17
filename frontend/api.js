// Fetch data from the backend
async function fetchCarConfig() {
    try {
        let response = await fetch("http://127.0.0.1:5000/api/config"); // Correct URL
        if (!response.ok) throw new Error("Failed to fetch data");
        return await response.json();
    } catch (error) {
        console.error("Error fetching config:", error);
        return null;
    }
}

window.fetchCarConfig = fetchCarConfig;