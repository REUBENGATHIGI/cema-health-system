# 🚀 CEMA Health Information System

This project is a secured, modular, and innovative health information system built with Flask, SQLAlchemy, and Marshmallow, designed for CEMA.  
It allows management of Clients, Programs, and Enrollments with strong security protections and modern innovations.

 Features

- ✅ Client Registration and Management
- ✅ Program Creation and Listing
- ✅ Client Enrollment into Programs
- ✅ Dynamic Search for Clients by Name
- ✅ API Key Authorization for all Endpoints
- ✅ Automatic Database Setup (SQLite)
- ✅ Blueprint Modular Structure (Clean code)
- ✅ Marshmallow Schema Validation
- ✅ Full support for Python 3.13 + SQLite 3.13
- ✅ Easily extensible and scalable system

---

 Innovations Added

Dynamic Client Search API
  Search any client by partial name using `/clients/search?name`

Auto SQLite3 Database and Folder Creation
  No need to manually create the `instance/health.db`. It's auto-generated if missing.

Blueprint Modularization
  Clear separation of concerns: `clients`, `programs`, and `enrollments` each in their own file.

Presentation + Evidence Screenshots  
  Included a full PowerPoint prototype demonstration with screenshots showing API usage and success outputs.

- Release Packaging
  Published a full GitHub Release with all materials: presentation, screenshots, full codebase.


 Security Features

Bearer Token Authorization
  All API endpoints require a valid API Key (`Authorization: Bearer SECRET123`).

SQL Injection Protection 
  All database operations are done via SQLAlchemy ORM, preventing injection attacks.

Input Validation with Marshmallow  
  Every data received via API is validated against Marshmallow schemas, ensuring clean and secure data.

Safe Dependencies
  Locked `marshmallow` version to `<4.0.0` for maximum compatibility and security with Python 3.13.


Technologies Used

Flask 3.0
Flask-SQLAlchemy
Flask-Marshmallow
Marshmallow 3.26
SQLite 3.13
Python 3.13
