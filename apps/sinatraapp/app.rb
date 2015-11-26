require 'sinatra/base'

class RecApp < Sinatra::Base
    set :bind, '0.0.0.0'

    get '/' do
        "Welcome #{request.user_agent}! The time is: #{Time.now}. Pizza, Pizza!"
    end

    run! if app_file == $0

end
