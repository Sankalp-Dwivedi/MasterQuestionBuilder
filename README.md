# Master Question Builder

Master Question Builder is a Ruby on Rails application designed to generate questions based on input paragraphs. This tool creates multiple-choice questions, including one correct answer and several distractor options, to provide an engaging and effective way to test comprehension of content. The project uses MySQL as the database to manage questions, options, and related data.

## Features

- **Automated Question Generation**: Takes a paragraph as input and generates multiple-choice questions.
- **Options with Distractors**: Provides one correct answer and several distractor options for each question.
- **Ruby on Rails Backend**: Built with Rails for scalability, maintainability, and ease of development.
- **MySQL Database**: Utilizes MySQL for data storage, making it suitable for handling complex queries and large datasets.
- **Customizable Question Logic**: Enables customization of question generation, such as adjusting difficulty and relevance.

## Getting Started

### Prerequisites

- Ruby (version 3.1 or higher)
- Rails (version 7.2 or higher)
- MySQL
- Bundler

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/master-question-builder.git
   cd master-question-builder

2. Install Gems:

   ```bash
   bundle install

3. Database Configuration:

- Create a MySQL database and configure your config/database.yml file with your database credentials.

- Run the database migrations:
   ```bash
   rails db:create db:migrate

- Environment Setup: Set up any necessary environment variables, such as those used for API keys or third-party services.

### Usage
1. Starting the Server:

   ```bash
   rails server

2. Generating Questions:

- Navigate to the application’s designated endpoint where you can input a paragraph.
- The application will process the input and generate questions along with correct answers and distractors.
- View, edit, or save the generated questions in the admin panel.

3. Admin Panel:

Manage questions, view the generated options, and customize question details via the Rails Admin interface if configured.

### Example
Given the paragraph input:

     ```bash
     Ruby on Rails, often simply called Rails, is a server-side web application framework written in Ruby under the MIT License. Rails is a model-view-controller (MVC) framework, provides default structures for a database, a web service, and web pages.

Generated Question:

- Question: What type of framework is Ruby on Rails?
   - Options:
      - Correct Answer: MVC
      - Distractor 1: ORM
      - Distractor 2: API
      - Distractor 3: CMS

## Technologies Used
- Ruby on Rails: Backend framework for handling business logic and routing.
- MySQL: Database for efficient data management and storage.
- NLP & AI Libraries: Optional use of NLP libraries (e.g., Hugging Face or OpenAI for integration) for generating more accurate questions and distractors.
- JavaScript: For frontend interactivity, if applicable.

## Future Enhancements
- Improved Distractor Generation: Use NLP techniques to generate more contextually appropriate distractors.
- Advanced Question Types: Expand to support various question types like true/false, fill-in-the-blank, etc.
- Difficulty Levels: Customize question difficulty based on paragraph complexity and keywords.
- Admin Panel Enhancements: Enable batch question creation, export, and analytics for questions and answers.

## Contributing
Contributions are welcome! Fork the repository and submit a pull request for any improvements, features, or bug fixes.

## License
This project is licensed under the MIT License.
