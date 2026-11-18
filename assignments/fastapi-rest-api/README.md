# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that exposes and manages resources while practicing routes, HTTP methods, request validation, and JSON responses.

## 📝 Tasks

### 🛠️ Create the API Application

#### Description

Set up a FastAPI application and define an in-memory collection of items.

#### Requirements

Completed program should:

- Create a FastAPI application instance
- Use an in-memory list or dictionary to store resources
- Define a root route that returns a welcome JSON response
- Run the application with `uvicorn`

### 🛠️ Implement Read and Create Routes

#### Description

Add routes that allow students to retrieve items and create new items.

#### Requirements

Completed program should:

- Provide a `GET /items` route that returns all items
- Provide a `GET /items/{item_id}` route that returns one item
- Return a `404` response when an item does not exist
- Provide a `POST /items` route that validates and creates an item

### 🛠️ Implement Update and Delete Routes

#### Description

Complete the API with operations that update and remove resources.

#### Requirements

Completed program should:

- Provide a `PUT /items/{item_id}` route that updates an existing item
- Provide a `DELETE /items/{item_id}` route that removes an item
- Return appropriate success or `404` responses
- Test the endpoints using the FastAPI automatic documentation page
