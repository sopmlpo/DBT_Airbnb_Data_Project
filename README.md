# Airbnb Analytics Project with dbt

This project showcases the use of dbt (Data Build Tool) to transform raw Airbnb data into analytics-ready datasets. It highlights dbt's capabilities for modular, testable, and maintainable SQL transformations within a modern data stack.

## Features
- **Data Sources:** Connects to a data warehouse to retrieve Airbnb data.
- **Data Transformation:** Implements dbt models for cleaning and transforming data.
- **Testing:** Ensures data quality and integrity using singular, generic, and source tests.
- **Documentation:** Auto-generates documentation for dbt models, dependencies, and metadata.
- **Deployment:** Demonstrates scheduled transformations and error handling.
- **Advanced Concepts:** Utilizes macros, packages, and Jinja templates for code reusability and efficiency.

## Tools and Technologies
- **dbt** for transformation and modeling
- **SQL** for defining business logic
- **Integration with** Snowflake
- **Version control** with Git
- **Dashboard with** Preset*

## Key Learning Outcomes
- Understand the dbt workflow: sources, models, tests, and documentation.
- Build reusable and scalable data pipelines with SQL.
- Leverage dbt for analytics engineering in a modern data stack.

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/sopmlpo/DBT_Airbnb_Data_Project.git
cd DBT_Airbnb_Data_Project
```

### 2. Install dbt Locally and Configure Connection
Follow the official [dbt installation guide](https://docs.getdbt.com/docs/introduction) for your operating system.
 
### 3. Run Initial dbt Setup Commands
```bash
dbt deps  # Install dependencies
dbt seed  # Load seed data
dbt run   # Execute transformations
dbt test  # Run data tests
```

### 4. View Auto-Generated Documentation
```bash
dbt docs generate  # Generate documentation
dbt docs serve     # Start a local web server for documentation
```

## Project Structure
```
├── models/       # Contains SQL files for dbt models
├── tests/        # Includes configurations for data validation
├── macros/       # Reusable SQL code snippets
├── analyses/     # Analyses based on the datamart
├── seeds/        # Local file with dates of full moon
├── assets/       # Schema of raw data
├── snapshots/    # History of updates and changes of the raw data
```

*Note: Loading the Preset dashboard link might show error!



