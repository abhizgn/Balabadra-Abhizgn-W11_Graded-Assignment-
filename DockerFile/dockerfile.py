WORKDIR /app

COPY . /app

RUN python -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
