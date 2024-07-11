require('dotenv').config();
const express = require('express');
const rateLimit = require('express-rate-limit');
const app = express();

app.use(express.json());

const kitRoutes = require('./routes/get_kit');
app.use('/api', kitRoutes);

const limiter = rateLimit({
    windowMs:  60 * 1000, // 1 minute
    max: 10,
    message: "Too many requests from this IP, please try again after a minute"
});

app.use(limiter);

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
