class CreateTempQuestions < ActiveRecord::Migration[7.2]
  def change
    create_table :temp_questions do |t|
      t.text :data

      t.timestamps
    end
  end
end
