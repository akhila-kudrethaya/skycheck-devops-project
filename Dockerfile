# Step 1: Use an official Python image as the base (The "Plate")
FROM python:3.9-slim

# Step 2: Set the "Home" folder inside the container
WORKDIR /app

# Step 3: Copy our requirements file first (Efficiency trick!)
COPY requirements.txt .

# Step 4: Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of our code into the container
COPY . .

# Step 6: Tell the container to open Port 5000
EXPOSE 5000

# Step 7: The command to start the app
CMD ["python", "app.py"]