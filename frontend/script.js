document.addEventListener("DOMContentLoaded", async function () {
    const brandSelect = document.getElementById("brand-select");
    const cabinSelect = document.getElementById("cabin-select");
    const wheelbaseSelect = document.getElementById("wheelbase-select");
    const engineSelect = document.getElementById("engine-select");
    const bodyTypeSelect = document.getElementById("bodyType-select");
    const dimensionsSelect = document.getElementById("dimensions-select");
    const extrasContainer = document.getElementById("extras-container");
    const confirmBtn = document.getElementById("confirm-btn");

    async function fetchData(endpoint) {
        try {
            let response = await fetch(`http://127.0.0.1:5000/api/${endpoint}`);
            return await response.json();
        } catch (error) {
            console.error(`Błąd pobierania ${endpoint}:`, error);
            return [];
        }
    }

    function populateSelect(selectElement, data, textKey = "name", valueKey = "id") {
        selectElement.innerHTML = `<option value="">-- Wybierz --</option>`;
        data.forEach(item => {
            let option = document.createElement("option");
            option.value = item[valueKey];
            option.textContent = item[textKey];
            selectElement.appendChild(option);
        });
    }

    function populateCheckboxList(container, data, textKey = "name", valueKey = "id") {
        container.innerHTML = "";
        data.forEach(item => {
            let label = document.createElement("label");
            label.style.display = "block";
            label.style.fontWeight = "normal"; // Usunięcie pogrubienia

            let checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.value = item[valueKey];
            checkbox.name = "extras";

            label.appendChild(checkbox);
            label.appendChild(document.createTextNode(" " + item[textKey]));
            container.appendChild(label);
        });
    }

    function checkFormCompletion() {
        if (
            brandSelect.value &&
            cabinSelect.value &&
            wheelbaseSelect.value &&
            engineSelect.value &&
            bodyTypeSelect.value &&
            dimensionsSelect.value
        ) {
            confirmBtn.disabled = false;
        } else {
            confirmBtn.disabled = true;
        }
    }

    let brands = await fetchData("brands");
    populateSelect(brandSelect, brands);

    brandSelect.addEventListener("change", async function () {
        if (!this.value) return;
        cabinSelect.disabled = false;
        let cabins = await fetchData(`cabins?id_brand=${this.value}`);
        populateSelect(cabinSelect, cabins);
        checkFormCompletion();
    });

    cabinSelect.addEventListener("change", async function () {
        if (!this.value) return;
        wheelbaseSelect.disabled = false;
        let wheelbases = await fetchData(`axle_spacings?id_cabin=${this.value}`);
        populateSelect(wheelbaseSelect, wheelbases);
        checkFormCompletion();
    });

    wheelbaseSelect.addEventListener("change", async function () {
        if (!this.value) return;
        engineSelect.disabled = false;
        let engines = await fetchData(`engines?id_axle_spacing=${this.value}`);
        populateSelect(engineSelect, engines);
        checkFormCompletion();
    });

    engineSelect.addEventListener("change", async function () {
        if (!this.value) return;
        bodyTypeSelect.disabled = false;
        let bodyTypes = await fetchData("body_types");
        populateSelect(bodyTypeSelect, bodyTypes);
        checkFormCompletion();
    });

    bodyTypeSelect.addEventListener("change", async function () {
        if (!this.value) return;
        dimensionsSelect.disabled = false;
        let dimensions = await fetchData(`dimensions?id_body_type=${this.value}`);
        populateSelect(dimensionsSelect, dimensions);
        checkFormCompletion();
    });

    dimensionsSelect.addEventListener("change", checkFormCompletion);

    // Pobranie dodatków od razu po załadowaniu strony
    let extras = await fetchData("extras");
    populateCheckboxList(extrasContainer, extras);

    confirmBtn.addEventListener("click", () => {
        alert("Konfiguracja zapisana!");
    });
});
