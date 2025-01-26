def send_query_to_gemini(s_query, api_key):
    # Endpoint URL
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # Headers
    headers = {
        "Content-Type": "application/json",
    }
    
    # Payload
    payload = {
        "contents": [
            {
                "parts": [{"text": s_query}]
            }
        ]
    }
    
    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Handle the response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status {response.status_code}"}
