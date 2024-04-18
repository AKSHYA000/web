const express = require('express');
const mongoose = require('mongoose');

const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/users', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// Define a user schema
const userSchema = new mongoose.Schema({
  username: String,
  password: String,
  email: String
});

// Create a user model
const User = mongoose.model('User', userSchema);

// Middleware to parse JSON
app.use(express.json());

// Route to handle user registration
app.post('/signup', async (req, res) => {
  const { username, password, email } = req.body;

  try {
    // Create a new user instance
    const user = new User({
      username,
      password,
      email
    });

    // Save the user to the database
    await user.save();

    res.status(201).json({ message: 'User created successfully' });
  } catch (error) {
    console.error('Error creating user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
