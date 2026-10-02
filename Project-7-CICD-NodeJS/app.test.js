const request = require("supertest");
const app = require("./index");

describe("CI/CD Node.js Application", () => {

    test("GET /health should return healthy status", async () => {

        const response = await request(app)
            .get("/health");

        expect(response.statusCode).toBe(200);
        expect(response.body.status).toBe("healthy");
    });

});