# Physiotherapy Equipment Rental and Selling Software

A desktop application developed as a mini-project by me **Jignesh Rana** for managing rental and sales services of physiotherapy equipment. The software supports user registration, login authentication, product browsing, purchasing, and rental features with integrated billing functionality.

## 🧾 Features

- **User Authentication**: Register new users and authenticate existing users via login credentials.
- **Product Management**: Browse physiotherapy equipment across different categories.
- **Purchase and Rental Options**: Users can either purchase equipment or lease them temporarily.
- **Billing System**: Automatically generate and display bills for purchases or rentals.
- **Database Integration**: Stores user and product data in a MySQL database via phpMyAdmin.

## 🗂 Project Structure

All functionality is implemented in a single main file named: `MiniProject`.

The application includes the following key frames:
- **HomeFrame**: Entry point of the application with navigation options.
- **LoginFrame**: Secure login form integrated with a MySQL database.
- **RegisterFrame**: New user registration with data validation and database storage.
- **PhysiotherapyFrame & ExerciseFrame**: Navigate product categories and available equipment.
- **DisplayBillFrame**: Displays a detailed bill for purchased or rented equipment.

## 🛠 Technology Stack

- **Language**: Python (Tkinter based GUI)
- **Database**: MySQL (phpMyAdmin interface)
- **Database Name**: `physio-equip_surgical`

## 💾 Database

Ensure that a MySQL database named `physio-equip_surgical` is created, and that it includes a `users` table for authentication purposes. Product and transaction data should also be modeled appropriately.

## ▶ How to Run

1. Open the project in your preferred texteditor (e.g., notepad, sublime text, vs-code).
2. Set up the MySQL database `physio-equip_surgical` using phpMyAdmin.
3. Populate the `users` table and add initial product data if necessary.
4. Compile and run the `MiniProject` Python file.

## 📌 Usage Instructions

- **Login/Register**: Access via the HomeFrame.
- **Explore Products**: Click on a category to view 6 predefined equipment options.
- **Purchase/Lease**: Choose quantity, then click “Buy Product” or “Product on Leased”.
- **Generate Bill**: Bill will appear in `DisplayBillFrame`, finish to return to Home.

## 📧 Author

**Jignesh Rana**  
---

> Note: This project is designed for educational purposes. Please ensure all environment setups (Python runtime, MySQL server, ODBC connection) are correctly configured before use.
