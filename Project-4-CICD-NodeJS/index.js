const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
   res.send("🚀 CI/CD Pipeline Deployed Successfully!");
});

app.get("/health", (req, res) => {
    res.json({
        status: "healthy",
        application: "Project 7 CI/CD Node.js"
    });
});

if (require.main === module) {
    app.listen(PORT, () => {
        console.log(`Server running on port ${PORT}`);
    });
}

module.exports = app;