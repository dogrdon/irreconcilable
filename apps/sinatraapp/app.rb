require 'sinatra/base'
require 'mongo'
require 'json/ext'

class RecApp < Sinatra::Base
    set :bind, '0.0.0.0'

    configure do
    	db = Mongo::Client.new(['localhost:27017'], :database => 'test')
    	set :mongo_db, db[:test]
    end

    get '/' do
        "Welcome #{request.user_agent}! The time is: #{Time.now}. Pizza, Pizza in #{settings.bind}!"
    end

    get ''


    run! if app_file == $0

end
