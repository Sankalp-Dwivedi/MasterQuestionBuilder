Rails.application.routes.draw do
  mount RailsAdmin::Engine => '/admin', as: 'rails_admin'
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Render dynamic PWA files from app/views/pwa/*
  get "service-worker" => "rails/pwa#service_worker", as: :pwa_service_worker
  get "manifest" => "rails/pwa#manifest", as: :pwa_manifest

  # Defines the root path route ("/")
  # root "posts#index"
  root 'questions#index'
  get 'questions/new', to: 'questions#new', as: 'new_question'
  post 'questions/create', to: 'questions#create', as: 'create_question'
  post 'questions/generate_questions', to: 'questions#generate_questions', as: 'generate_questions'
  get 'questions/result', to: 'questions#result', as: 'result_question'
  post 'questions/save', to: 'questions#save_to_database', as: 'save_questions'

end
