class QuestionsController < ApplicationController
  require 'httparty'
  require 'open3'
  $question = ''
  def index
    # This will render the project details and a button to go to the form page.
  end

  def new
    # This will display the form for paragraph input.
  end

  # def create
  #   # This will handle the form submission and process the input paragraph.
  #   paragraph = params[:paragraph]
  #   # Logic for question generation goes here
  #   result = Subprocess.check_output(["python3", "app/python_models/msq.py", paragraph])
  #   @questions = JSON.parse(result)

  #   # @questions = generate_random_questions
  #   # redirect_to result_question_path
  # end


  def create
    paragraph = params[:paragraph]

    # Execute Python script with paragraph as an argument
    stdout, stderr, status = Open3.capture3("python3", "app/python_models/msq.py", paragraph)

    if status.success?
      @questions = JSON.parse(stdout)
      temp_record = TempQuestion.create(data: @questions.to_json)
      redirect_to result_question_path(temp_id: temp_record.id)
    else
      Rails.logger.error("Python script error: #{stderr}")
      flash[:error] = "There was an error generating questions. Please try again."
      @questions = []  # Show an empty state or handle appropriately
      redirect_to new_question_path
    end
    

    # Redirect to result page
    # $question = @questions
    # redirect_to result_question_path
  end



  def generate_questions
    paragraph = params[:paragraph]

    response = HTTParty.post("https://ad71-34-125-16-192.ngrok-free.app/generate_questions", 
      body: { paragraph: paragraph }.to_json,
      headers: { 'Content-Type' => 'application/json' }
    )

    if response.success?
      @questions = response.parsed_response
    else
      @error = "Error generating questions"
    end
  end



  def result
    # Retrieve questions for display from the session or instance variable
    # byebug
    # @questions = $question
    temp_record = TempQuestion.find_by(id: params[:temp_id])
    @questions = JSON.parse(temp_record.data) if temp_record
  end

  def save_to_database
    begin
      temp_record = TempQuestion.find_by(id: params[:temp_id])
      @questions = JSON.parse(temp_record.data) if temp_record
      @questions.each do |q|
        question = Question.create(
          question_text: q['question'],
          correct_answer: q['correct_answer']
        )

        # Save each option related to the question
        q['options'].each do |option|
          Option.create(
            option_text: option,
            correct: option == q['correct_answer'], # Mark the correct answer
            question: question
          )
        end
      end
    rescue StandardError => e
      redirect_to new_question_path, notice: 'Something went Wrong!'
      puts "=============>"
      puts e
      byebug
    else
      TempQuestion.find_by(id: params[:temp_id])&.destroy
      redirect_to new_question_path, notice: 'Questions and options have been saved to the database.'
    end
    
  end

 private

  def generate_random_questions
    # Generating 4 random questions with options (answers).
    [
      { question: "What is the main purpose of machine learning?", 
        options: ["Data analysis", "Pattern recognition", "Game development", "Data storage"], correct: "Pattern recognition" },
      
      { question: "Which algorithm is used for supervised learning?", 
        options: ["Linear regression", "K-means", "DBSCAN", "Apriori"], correct: "Linear regression" },
      
      { question: "What does NLP stand for in AI?", 
        options: ["Natural Language Processing", "Neural Language Processing", "Natural Linear Programming", "Neural Logical Process"], correct: "Natural Language Processing" },
      
      { question: "Which type of neural network is best for sequential data?", 
        options: ["Convolutional Neural Network", "Recurrent Neural Network", "Feedforward Network", "Decision Tree"], correct: "Recurrent Neural Network" }
    ]
  end
end
