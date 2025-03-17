import google.generativeai as genai

# Configure the API key
genai.configure(api_key="YOUR_API_KEY")

# Load the Gemini model (text-only version)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Send a prompt
response = model.generate_content("What is the capital of Japan?")
print(response.text)
