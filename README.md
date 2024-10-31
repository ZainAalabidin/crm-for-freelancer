# Freelancer CRM and Project Management System

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project is a custom CRM and Project Management System built on the Odoo 17 framework, specifically tailored for freelancers. It provides tools to manage clients, track interactions, create and manage projects and tasks, and issue invoices for completed work. The system is designed to streamline the client relationship and project tracking processes, making it easier to handle freelance work efficiently.

## Features
1. **Client Management**:
   - Store client details including contact information, company, and social media links.
   - Categorize clients with tags for easy filtering.
   - Track all interactions with clients.

2. **Project and Task Management**:
   - Create and manage projects with milestones, linked to specific clients.
   - Track task completion and hours spent per task.
   - Set and monitor project states (draft, in-progress, on-hold, completed, or canceled).

3. **Invoice Management**:
   - Generate invoices for projects.
   - Track payment status and flag overdue invoices.
   - Auto-generate invoice references for unique identification.

## Getting Started

### Prerequisites
- **ubunto 20.04**
- **Odoo 17**: This project requires Odoo 17 installed on your system.
- **Python 3.10** or higher.
- **PostgreSQL** (or another compatible database for Odoo).

### Installation
1. Clone the repository:
   ```bash
   git clone https://www.github.com/odoo/odoo --depth --branch 17.0 --single-branch odoo17
   
- **1** install odoo 17 to use the application:
   "git clone https://www.github.com/odoo/odoo --depth --branch 17.0 --single-branch odoo17"

- **2** go to odoo17 file and install the requirement:
   cd oddo17
   pip install -r requirements.txt

- **3** Go to this path:
   cd odoo17/odoo

- **4** Create new directory:
   mkdir custom_addons

- **5** Now clone the the application in the new folder:
   git clone https://github.com/yourusername/freelancer-crm.git
   cd freelancer-crm

- **5** start odoo:
    /odoo17/odoo-bin -c odoo.conf


## Models

1. Client
Manages client details including:

Contact information
Interaction history
Tags for categorization
Follow-up email functionality

2. Project
Tracks project details, including:

Project name, start and end dates, description
Associated tasks
Milestone tracking through project state
Client linkage

3. Task
Represents individual tasks associated with projects, including:

Task name, description, and completion status
Hours spent on the task
Linked to a specific project


4. Invoice
Handles invoicing for projects:

Payment status and due dates
Overdue status tracking
Linked to specific projects and clients


5. Tag
Used to categorize clients for easy filtering. Includes color-coding for enhanced UI experience.

## Contributing

Feel free to submit issues, fork the repository, and make pull requests. Contributions are welcome to help improve the system’s functionality and efficiency.

## License

This `README.md` provides a structured overview of CRM and project management system, guiding users through setup, core functionality, and usage. Let me know if you’d like more details on any section!
