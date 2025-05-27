from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv() # Load your .env file
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("Error: GOOGLE_API_KEY not found in .env file or environment variables.")
    exit()

try:
    genai.configure(api_key=API_KEY)

    # --- Option 1: Try the original model from your app (gemini-1.5-pro) ---
    # model = genai.GenerativeModel('gemini-1.5-pro')

    # --- Option 2: Try gemini-1.5-flash (often faster and widely available) ---
    model = genai.GenerativeModel('gemini-1.5-flash')

    # --- Option 3: List available models to see what works ---
    # print("Listing available models...")
    # for m in genai.list_models():
    #     if "generateContent" in m.supported_generation_methods:
    #         print(f"  - {m.name} (Supports generateContent)")
    # print("\nAttempting to generate content with selected model...")


    response = model.generate_content("Hello Gemini, how are you today? Please respond concisely.")
    print("\nAPI Response:")
    print(response.text)

except Exception as e:
    print(f"An error occurred during API call: {e}")
    # You might still get a 429 if the quota for the *new* model is also hit very quickly,
    # but the 404 is now gone.
    if "429" in str(e):
        print("\nThis might still be a quota issue, but for the specific model you tried.")
        print("Please check your Google Cloud Project quotas again.")
    elif "404" in str(e) and "models" in str(e):
        print("\nModel not found or not supported. You might need to try a different model name.")
        print("Uncomment 'Option 3' in the script to list available models.")