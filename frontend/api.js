class CarConfiguratorAPI {
    constructor(baseURL = "http://127.0.0.1:5000/api") {
        this.baseURL = baseURL;
    }

    async fetchData(endpoint) {
        try {
            let response = await fetch(`${this.baseURL}/${endpoint}`);
            if (!response.ok) throw new Error(`Failed to fetch ${endpoint}`);
            return await response.json();
        } catch (error) {
            console.error(`Error fetching ${endpoint}:`, error);
            return null;
        }
    }

    async getBrands() {
        return await this.fetchData("brands");
    }

    async getCabins() {
        return await this.fetchData("cabins");
    }

    async getAxleSpacings() {
        return await this.fetchData("axle_spacings");
    }

    async getEngines() {
        return await this.fetchData("engines");
    }

    async getBodyTypes() {
        return await this.fetchData("body_types");
    }

    async getDimensions() {
        return await this.fetchData("dimensions");
    }

    async getExtras() {
        return await this.fetchData("extras");
    }
}

// Tworzymy instancję klasy i eksportujemy ją globalnie
const carConfiguratorAPI = new CarConfiguratorAPI();
window.carConfiguratorAPI = carConfiguratorAPI;
