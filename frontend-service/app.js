const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send(`
    <h1>Travel Booking application</h1>
    <ul>
      <li><a href="/users">Users</a></li>
      <li><a href="/bookings">Bookings</a></li>
    </ul>
  `);
});

app.get("/users", async (req, res) => {
  res.send("User service is running");
});

app.get("/bookings", async (req, res) => {
  res.send("Booking service is running");
});

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});

