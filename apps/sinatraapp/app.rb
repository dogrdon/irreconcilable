require 'sinatra/base'
require 'mongo'
require 'json/ext'

class RecApp < Sinatra::Base
    set :bind, '0.0.0.0'

    configure do
    	db = Mongo::Client.new(['localhost:27017'], :database => 'test')
    	set :mongo_db, db[:test]
    end

    helpers do
    	def object_by_id val
    		begin
    			BSON::ObjectId.from_string(val)
    		rescue BSON::ObjectId::Invalid
    			nil
    		end
    	end

    	def document_by_id id
    		#id = object_by_id(id) #if String === id
    		id = id.to_i
    		if id.nil?
    			{}.to_json
    		else
    			document = settings.mongo_db.find(:docid => id).to_a.first
    			(document || {}).to_json
    		end
    	end
    end

    get '/' do
        "Welcome #{request.user_agent}! The time is: #{Time.now}. Pizza, Pizza in #{settings.bind}!"
    end

    get '/things/?' do
    	content_type :json
    	settings.mongo_db.find.to_a.to_json
    end

    get '/thing/:id/?' do
    	content_type :json
    	document_by_id(params[:id])
    end	

    post '/new/?' do
    	content_type :json
    	db = settings.mongo_db
    	params = JSON.parse(request.body.read)
    	result = db.insert_one params
    	db.find(:_id => result.inserted_id).to_a.first.to_json
    end



    run! if app_file == $0

    

end
