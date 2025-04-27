# test_endpoints.ps1
# Secure API endpoint tests for Health Info System

# 1) List all clients (should be empty or show existing)
Invoke-RestMethod 
  -Uri "http://127.0.0.1:5001/clients" 
  -Method Get 
  -Headers @{ Authorization = "Bearer SECRET123" }

# 2) Register a new client
Invoke-RestMethod 
  -Uri "http://127.0.0.1:5001/clients" 
  -Method Post 
  -Headers @{
    Authorization  = "Bearer SECRET123"
    "Content-Type" = "application/json"
  } 
  -Body (@{ name = "Alice" } | ConvertTo-Json)

# 3) Search for a client by name
Invoke-RestMethod 
  -Uri "http://127.0.0.1:5001/clients/search?name=Ali" 
  -Method Get 
  -Headers @{ Authorization = "Bearer SECRET123" }

# 4) Register a new program
Invoke-RestMethod 
  -Uri "http://127.0.0.1:5001/programs" 
  -Method Post 
  -Headers @{
    Authorization  = "Bearer SECRET123"
    "Content-Type" = "application/json"
  } 
  -Body (@{ name = "Malaria" } | ConvertTo-Json)

# 5) List all programs
Invoke-RestMethod 
  -Uri "http://127.0.0.1:5001/programs" 
  -Method Get 
  -Headers @{ Authorization = "Bearer SECRET123" }

# 6) Enroll the client in the program
Invoke-RestMethod 
  -Uri "http://127.0.0.1:5001/enrollments" 
  -Method Post 
  -Headers @{
    Authorization  = "Bearer SECRET123"
    "Content-Type" = "application/json"
  } 
  -Body (@{ client_id = 1; program_id = 1 } | ConvertTo-Json)
