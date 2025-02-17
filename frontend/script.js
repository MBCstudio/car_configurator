document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("fetch-btn").addEventListener("click", async function () {
        let data = await fetchCarConfig();
        if (data) {
            document.getElementById("car-info").innerHTML = `
                <p>Model: <strong>${data.name}</strong></p>
                <p>Price: <strong>$${data.price}</strong></p>
            `;
        } else {
            document.getElementById("car-info").innerHTML = `<p>Could not load car data.</p>`;
        }
    });
});
